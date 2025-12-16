#!/usr/bin/env python3
"""
The Foundry - Ownership Enforcement Script

This script enforces file ownership rules for The Foundry shared narrative repository.
It runs automatically on every push to main and:
1. Scans changed files
2. Injects Foundry frontmatter for markdown files
3. Validates ownership
4. Restores unauthorized edits
5. Commits corrections if needed
"""

import os
import sys
import subprocess
import yaml
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# Constants
REPO_ADMIN = "nickarrow"
FOUNDRY_NAMESPACE = "foundry"


class FoundryEnforcer:
    def __init__(self):
        self.commit_author = os.environ.get("COMMIT_AUTHOR", "unknown").lower()
        self.commit_sha = os.environ.get("COMMIT_SHA", "HEAD")
        self.corrections_made = False
        self.files_corrected = []
        
    def run(self):
        """Main enforcement pipeline"""
        print(f"🔨 Foundry Enforcer starting...")
        print(f"   Commit author: {self.commit_author}")
        print(f"   Commit SHA: {self.commit_sha}")
        
        # Check if this is a guardian restoration commit
        if self.is_guardian_commit():
            print("🛡️  Guardian restoration commit detected - skipping enforcement")
            return
        
        # Step 1: Get changed files
        changed_files = self.get_changed_files()
        if not changed_files:
            print("✅ No files to process")
            return
        
        print(f"\n📋 Processing {len(changed_files)} changed file(s)")
        
        # Step 2-6: Process each file
        for file_info in changed_files:
            self.process_file(file_info)
        
        # Step 7: Commit corrections if needed
        if self.corrections_made:
            self.commit_corrections()
        else:
            print("\n✅ No corrections needed - all edits were valid")
    
    def is_guardian_commit(self) -> bool:
        """Check if the current commit is from the guardian restoration workflow"""
        # Get commit author and message
        result = subprocess.run(
            ["git", "log", "-1", "--format=%an|%ae|%s", self.commit_sha],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            return False
        
        output = result.stdout.strip()
        parts = output.split('|')
        
        if len(parts) < 3:
            return False
        
        author_name = parts[0]
        author_email = parts[1]
        commit_message = parts[2]
        
        # Check if commit is from Guardian Bot
        is_guardian_author = (
            author_name == "Guardian Bot" and 
            author_email == "guardian@the-foundry.bot"
        )
        
        # Check if message starts with "Guardian:"
        is_guardian_message = commit_message.startswith("Guardian:")
        
        return is_guardian_author and is_guardian_message
    
    def get_changed_files(self) -> List[Dict]:
        """Get list of changed files from git diff"""
        # Get the previous commit (parent of current)
        result = subprocess.run(
            ["git", "rev-parse", f"{self.commit_sha}^"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            # First commit in repo, compare against empty tree
            prev_commit = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
        else:
            prev_commit = result.stdout.strip()
        
        # Get diff with rename detection
        result = subprocess.run(
            ["git", "diff", "--name-status", "-M", prev_commit, self.commit_sha],
            capture_output=True,
            text=True,
            check=True
        )
        
        changed_files = []
        for line in result.stdout.strip().split('\n'):
            if not line:
                continue
            
            parts = line.split('\t')
            status = parts[0]
            
            # Skip hidden files/folders (including .github - protected by Guardian)
            path_parts = parts[1].split('/')
            if any(p.startswith('.') for p in path_parts):
                continue
            
            if status.startswith('R'):  # Rename
                old_path = parts[1]
                new_path = parts[2]
                changed_files.append({
                    'status': 'renamed',
                    'old_path': old_path,
                    'path': new_path
                })
            elif status == 'D':  # Deleted
                changed_files.append({
                    'status': 'deleted',
                    'path': parts[1]
                })
            elif status in ['A', 'M']:  # Added or Modified
                changed_files.append({
                    'status': 'added' if status == 'A' else 'modified',
                    'path': parts[1]
                })
        
        return changed_files
    
    def process_file(self, file_info: Dict):
        """Process a single file through the enforcement pipeline"""
        path = file_info['path']
        status = file_info['status']
        
        print(f"\n📄 {path} ({status})")
        
        # Handle deletions
        if status == 'deleted':
            self.handle_deletion(file_info)
            return
        
        # Check if file exists (might have been deleted)
        if not os.path.exists(path):
            return
        
        # Determine file type
        is_markdown = path.endswith('.md')
        is_root_level = '/' not in path
        
        if is_markdown:
            self.process_markdown_file(file_info)
        else:
            self.process_non_markdown_file(file_info, is_root_level)
    
    def process_markdown_file(self, file_info: Dict):
        """Process markdown file: inject frontmatter and validate ownership"""
        path = file_info['path']
        status = file_info['status']
        
        # Check if file is in .github folder
        is_github_folder = path.startswith('.github/')
        
        # Read file content
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse frontmatter
        frontmatter, body = self.parse_frontmatter(content)
        
        # Handle renames - preserve owner from old file
        if status == 'renamed':
            old_owner = self.get_owner_from_history(file_info['old_path'])
            if old_owner and FOUNDRY_NAMESPACE in frontmatter:
                frontmatter[FOUNDRY_NAMESPACE]['file_owner'] = old_owner
                print(f"   🔄 Preserved owner from rename: {old_owner}")
        
        # Inject or validate Foundry frontmatter
        needs_injection = FOUNDRY_NAMESPACE not in frontmatter
        needs_update = False
        
        if needs_injection:
            # New file or missing Foundry data
            if FOUNDRY_NAMESPACE not in frontmatter:
                frontmatter[FOUNDRY_NAMESPACE] = {}
            
            # Files in .github folder are always admin-owned
            if is_github_folder:
                frontmatter[FOUNDRY_NAMESPACE]['file_owner'] = REPO_ADMIN
            else:
                frontmatter[FOUNDRY_NAMESPACE]['file_owner'] = self.commit_author
            
            frontmatter[FOUNDRY_NAMESPACE]['created_date'] = self.get_iso_timestamp()
            frontmatter[FOUNDRY_NAMESPACE]['last_modified'] = self.get_iso_timestamp()
            needs_update = True
            owner = frontmatter[FOUNDRY_NAMESPACE]['file_owner']
            print(f"   ➕ Injecting frontmatter (owner: {owner})")
        
        # Validate ownership
        file_owner = frontmatter.get(FOUNDRY_NAMESPACE, {}).get('file_owner')
        
        if not file_owner:
            # Missing owner, inject it
            if FOUNDRY_NAMESPACE not in frontmatter:
                frontmatter[FOUNDRY_NAMESPACE] = {}
            frontmatter[FOUNDRY_NAMESPACE]['file_owner'] = self.commit_author
            file_owner = self.commit_author
            needs_update = True
        
        # Check for admin override (case-insensitive comparison)
        admin_override = frontmatter.get(FOUNDRY_NAMESPACE, {}).get('admin_override', False)
        has_admin_override = (self.commit_author.lower() == REPO_ADMIN.lower() and admin_override is True)
        
        is_authorized = (self.commit_author.lower() == file_owner.lower() or has_admin_override)
        
        if not is_authorized:
            # Unauthorized edit - restore from history
            print(f"   ❌ Unauthorized edit (owner: {file_owner}, editor: {self.commit_author})")
            is_new_file = (status == 'added')
            self.restore_file_from_history(path, is_new_file)
            self.files_corrected.append(path)
            self.corrections_made = True
        else:
            # Authorized edit
            if has_admin_override:
                print(f"   🔑 Admin override used (owner: {file_owner}, admin: {self.commit_author})")
                # Remove the admin_override flag after use
                if FOUNDRY_NAMESPACE in frontmatter and 'admin_override' in frontmatter[FOUNDRY_NAMESPACE]:
                    del frontmatter[FOUNDRY_NAMESPACE]['admin_override']
                    needs_update = True
            
            if status == 'modified' and not needs_injection:
                # Update last_modified for valid edits
                frontmatter[FOUNDRY_NAMESPACE]['last_modified'] = self.get_iso_timestamp()
                needs_update = True
            
            if needs_update:
                # Write updated frontmatter
                new_content = self.serialize_frontmatter(frontmatter, body)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                # Stage the change
                subprocess.run(['git', 'add', path], check=True)
                self.corrections_made = True
                print(f"   ✅ Valid edit - frontmatter updated")
            else:
                print(f"   ✅ Valid edit - no changes needed")
    
    def process_non_markdown_file(self, file_info: Dict, is_root_level: bool):
        """Process non-markdown file: validate ownership via git history"""
        path = file_info['path']
        status = file_info['status']
        
        # Check if file is in .github folder
        is_github_folder = path.startswith('.github/')
        
        # Determine owner
        if is_root_level or is_github_folder:
            # Root-level files and .github folder files are admin-only
            file_owner = REPO_ADMIN
        else:
            # Get original committer from history
            if status == 'added':
                file_owner = self.commit_author
            else:
                file_owner = self.get_owner_from_history(path)
        
        is_authorized = (self.commit_author.lower() == file_owner.lower() or self.commit_author.lower() == REPO_ADMIN.lower())
        
        if not is_authorized:
            print(f"   ❌ Unauthorized edit (owner: {file_owner}, editor: {self.commit_author})")
            self.restore_file_from_history(path)
            self.files_corrected.append(path)
            self.corrections_made = True
        else:
            print(f"   ✅ Valid edit")
    
    def handle_deletion(self, file_info: Dict):
        """Handle file deletion - restore if unauthorized"""
        path = file_info['path']
        
        # Determine owner from history
        file_owner = self.get_owner_from_history(path)
        
        if not file_owner:
            # Can't determine owner, allow deletion
            print(f"   ⚠️  Cannot determine owner, allowing deletion")
            return
        
        # Check for admin override in the file before it was deleted
        has_admin_override = False
        if self.commit_author.lower() == REPO_ADMIN.lower():
            # Check if the deleted file had admin_override flag
            result = subprocess.run(
                ["git", "show", f"{self.commit_sha}^:{path}"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0 and path.endswith('.md'):
                frontmatter, _ = self.parse_frontmatter(result.stdout)
                admin_override = frontmatter.get(FOUNDRY_NAMESPACE, {}).get('admin_override', False)
                has_admin_override = (admin_override is True)
        
        is_authorized = (self.commit_author.lower() == file_owner.lower() or has_admin_override)
        
        if not is_authorized:
            print(f"   ❌ Unauthorized deletion (owner: {file_owner}, editor: {self.commit_author})")
            self.restore_file_from_history(path)
            self.files_corrected.append(path)
            self.corrections_made = True
        else:
            if has_admin_override:
                print(f"   🔑 Admin override used for deletion (owner: {file_owner}, admin: {self.commit_author})")
            else:
                print(f"   ✅ Valid deletion")
    
    def get_owner_from_history(self, path: str) -> Optional[str]:
        """Get file owner from git history (first committer or frontmatter)"""
        # Try to get frontmatter owner from previous commit
        result = subprocess.run(
            ["git", "show", f"{self.commit_sha}^:{path}"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0 and path.endswith('.md'):
            # Parse frontmatter from previous version
            frontmatter, _ = self.parse_frontmatter(result.stdout)
            owner = frontmatter.get(FOUNDRY_NAMESPACE, {}).get('file_owner')
            if owner:
                return owner
        
        # Fall back to first committer
        result = subprocess.run(
            ["git", "log", "--follow", "--format=%an", "--", path],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0 and result.stdout.strip():
            # Get last line (first commit)
            lines = result.stdout.strip().split('\n')
            return lines[-1] if lines else None
        
        return None
    
    def restore_file_from_history(self, path: str, is_new_file: bool = False):
        """Restore file to its state in the previous commit, or delete if new"""
        if is_new_file:
            # New file with unauthorized ownership - delete it
            if os.path.exists(path):
                os.remove(path)
                subprocess.run(['git', 'add', path], check=True)
                print(f"   🗑️  Deleted unauthorized new file")
            return
        
        result = subprocess.run(
            ["git", "checkout", f"{self.commit_sha}^", "--", path],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            subprocess.run(['git', 'add', path], check=True)
            print(f"   🔄 Restored from previous commit")
        else:
            # File doesn't exist in history - must be new, delete it
            if os.path.exists(path):
                os.remove(path)
                subprocess.run(['git', 'add', path], check=True)
                print(f"   🗑️  Deleted unauthorized new file (no history found)")
            else:
                print(f"   ⚠️  Could not restore file: {result.stderr}")
    
    def parse_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """Parse YAML frontmatter from markdown content"""
        # Match frontmatter between --- delimiters
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
        
        if match:
            yaml_content = match.group(1)
            body = match.group(2)
            
            try:
                frontmatter = yaml.safe_load(yaml_content) or {}
            except yaml.YAMLError:
                frontmatter = {}
            
            return frontmatter, body
        else:
            # No frontmatter
            return {}, content
    
    def serialize_frontmatter(self, frontmatter: Dict, body: str) -> str:
        """Serialize frontmatter and body back to markdown"""
        if not frontmatter:
            return body
        
        yaml_str = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
        return f"---\n{yaml_str}---\n{body}"
    
    def get_iso_timestamp(self) -> str:
        """Get current timestamp in ISO 8601 format"""
        return datetime.now(timezone.utc).isoformat()
    
    def commit_corrections(self):
        """Commit any corrections made during enforcement"""
        print(f"\n📝 Committing corrections for {len(self.files_corrected)} file(s)")
        
        subprocess.run(
            ['git', 'commit', '-m', 'Enforced ownership rules'],
            check=True
        )
        
        subprocess.run(['git', 'push'], check=True)
        
        print("✅ Corrections committed and pushed")


if __name__ == "__main__":
    try:
        enforcer = FoundryEnforcer()
        enforcer.run()
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
