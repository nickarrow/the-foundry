#!/usr/bin/env python3
"""
The Foundry - Ownership Enforcement Script

This script enforces file ownership rules for The Foundry shared narrative repository.
It runs automatically on every push to main and:
1. Scans changed files
2. Updates the ownership registry
3. Validates ownership via checksum comparison
4. Restores unauthorized edits
5. Commits corrections if needed
"""

import os
import sys
import subprocess
import yaml
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# Constants
REPO_ADMIN = "nickarrow"
GUARDIAN_REPO_PATH = os.environ.get("GUARDIAN_REPO_PATH", "guardian-repo")
REGISTRY_PATH = f"{GUARDIAN_REPO_PATH}/registry.yml"
GUARDIAN_PAT = os.environ.get("GUARDIAN_PAT", "")


class FoundryEnforcer:
    def __init__(self):
        self.commit_author = os.environ.get("COMMIT_AUTHOR", "unknown").lower()
        self.commit_sha = os.environ.get("COMMIT_SHA", "HEAD")
        self.corrections_made = False
        self.files_corrected = []
        self.registry = self.load_registry()
        self.registry_updated = False
        
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
        
        # Step 7: Clean up empty folders
        self.cleanup_empty_folders()
        
        # Step 8: Save registry if updated
        if self.registry_updated:
            self.save_registry()
        
        # Step 9: Commit corrections if needed (only if there were actual corrections)
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
    
    def is_enforcement_commit(self) -> bool:
        """Check if the current commit is from the enforcement workflow"""
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
        
        # Check if commit is from Foundry Enforcer
        is_enforcer_author = (
            author_name == "Foundry Enforcer" and 
            author_email == "actions@github.com"
        )
        
        # Check if message is "Enforced ownership rules"
        is_enforcer_message = commit_message == "Enforced ownership rules"
        
        return is_enforcer_author and is_enforcer_message
    
    def load_registry(self) -> Dict:
        """Load the ownership registry from file"""
        if not os.path.exists(REGISTRY_PATH):
            return {'files': {}}
        
        try:
            with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
                registry = yaml.safe_load(f) or {}
                if 'files' not in registry:
                    registry['files'] = {}
                return registry
        except Exception as e:
            print(f"⚠️  Warning: Could not load registry: {e}")
            return {'files': {}}
    
    def save_registry(self):
        """Save the ownership registry to file in guardian repo"""
        try:
            # Ensure guardian repo directory exists
            os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)
            
            with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
                f.write("# The Foundry - File Ownership Registry\n")
                f.write("# This file tracks ownership and integrity of all non-hidden files in the repository.\n")
                f.write("# DO NOT EDIT MANUALLY - Managed automatically by the Foundry enforcement system.\n\n")
                yaml.dump(self.registry, f, default_flow_style=False, sort_keys=True)
            
            # Commit and push to guardian repo
            subprocess.run(['git', '-C', GUARDIAN_REPO_PATH, 'add', 'registry.yml'], check=True)
            subprocess.run(
                ['git', '-C', GUARDIAN_REPO_PATH, 'commit', '-m', 'Update registry from enforcement'],
                check=True
            )
            subprocess.run(['git', '-C', GUARDIAN_REPO_PATH, 'push'], check=True)
            
            print(f"💾 Registry updated in guardian repo")
        except Exception as e:
            print(f"❌ Error saving registry: {e}")
            raise
    
    def calculate_checksum(self, file_path: str) -> str:
        """Calculate SHA-256 checksum of a file"""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            print(f"⚠️  Warning: Could not calculate checksum for {file_path}: {e}")
            return ""
    
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
            
            # Skip hidden files/folders (including .github and .foundry - protected by Guardian)
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
        
        # Handle renames
        if status == 'renamed':
            self.handle_rename(file_info)
            return
        
        # Check if file exists (might have been deleted)
        if not os.path.exists(path):
            return
        
        # Process based on status
        if status == 'added':
            self.handle_new_file(file_info)
        elif status == 'modified':
            self.handle_modified_file(file_info)
    
    def handle_new_file(self, file_info: Dict):
        """Handle a newly added file"""
        path = file_info['path']
        
        # Calculate checksum
        checksum = self.calculate_checksum(path)
        
        # Determine owner (creator is the owner)
        owner = self.commit_author
        
        # Add to registry
        timestamp = self.get_iso_timestamp()
        self.registry['files'][path] = {
            'owner': owner,
            'created': timestamp,
            'modified': timestamp,
            'checksum': checksum
        }
        self.registry_updated = True
        
        print(f"   ➕ Added to registry (owner: {owner})")
    
    def handle_modified_file(self, file_info: Dict):
        """Handle a modified file"""
        path = file_info['path']
        
        # Calculate current checksum
        current_checksum = self.calculate_checksum(path)
        
        # Check if file is in registry
        if path not in self.registry['files']:
            # File not in registry - treat as new file
            print(f"   ⚠️  File not in registry, treating as new")
            self.handle_new_file(file_info)
            return
        
        file_entry = self.registry['files'][path]
        registry_checksum = file_entry.get('checksum', '')
        
        # Check if file actually changed
        if current_checksum == registry_checksum:
            print(f"   ℹ️  No changes detected (checksum match)")
            return
        
        # File changed - validate ownership
        file_owner = file_entry.get('owner', '')
        
        # Check for admin override
        admin_override = file_entry.get('admin_override', False)
        has_admin_override = (self.commit_author.lower() == REPO_ADMIN.lower() and admin_override is True)
        
        is_authorized = (self.commit_author.lower() == file_owner.lower() or has_admin_override)
        
        if not is_authorized:
            print(f"   ❌ Unauthorized edit (owner: {file_owner}, editor: {self.commit_author})")
            self.restore_file_from_history(path)
            self.files_corrected.append(path)
            self.corrections_made = True
        else:
            # Authorized edit - update registry
            if has_admin_override:
                print(f"   🔑 Admin override used (owner: {file_owner}, admin: {self.commit_author})")
                # Remove the admin_override flag after use (one-time use)
                del file_entry['admin_override']
            
            file_entry['modified'] = self.get_iso_timestamp()
            file_entry['checksum'] = current_checksum
            self.registry_updated = True
            print(f"   ✅ Valid edit - registry updated")
    
    def handle_rename(self, file_info: Dict):
        """Handle a renamed/moved file"""
        old_path = file_info['old_path']
        new_path = file_info['path']
        
        # Check if old file is in registry
        if old_path not in self.registry['files']:
            print(f"   ⚠️  Original file not in registry, treating as new")
            self.handle_new_file(file_info)
            return
        
        file_entry = self.registry['files'][old_path]
        file_owner = file_entry.get('owner', '')
        
        # Check for admin override
        admin_override = file_entry.get('admin_override', False)
        has_admin_override = (self.commit_author.lower() == REPO_ADMIN.lower() and admin_override is True)
        
        is_authorized = (self.commit_author.lower() == file_owner.lower() or has_admin_override)
        
        if not is_authorized:
            print(f"   ❌ Unauthorized rename (owner: {file_owner}, editor: {self.commit_author})")
            # Restore old file and remove new file
            self.restore_file_from_history(old_path)
            if os.path.exists(new_path):
                os.remove(new_path)
                subprocess.run(['git', 'add', new_path], check=True)
            self.files_corrected.append(old_path)
            self.corrections_made = True
        else:
            # Authorized rename - update registry
            if has_admin_override:
                print(f"   🔑 Admin override used for rename (owner: {file_owner}, admin: {self.commit_author})")
            
            # Calculate new checksum
            checksum = self.calculate_checksum(new_path)
            
            # Move entry to new path (without admin_override flag)
            self.registry['files'][new_path] = {
                'owner': file_owner,
                'created': file_entry.get('created', self.get_iso_timestamp()),
                'modified': self.get_iso_timestamp(),
                'checksum': checksum
            }
            
            # Remove old entry
            del self.registry['files'][old_path]
            self.registry_updated = True
            
            print(f"   ✅ Valid rename - registry updated")
    
    def handle_deletion(self, file_info: Dict):
        """Handle file deletion - restore if unauthorized"""
        path = file_info['path']
        
        # Check if file is in registry
        if path not in self.registry['files']:
            print(f"   ⚠️  File not in registry, allowing deletion")
            return
        
        file_entry = self.registry['files'][path]
        file_owner = file_entry.get('owner', '')
        
        # Check for admin override
        admin_override = file_entry.get('admin_override', False)
        has_admin_override = (self.commit_author.lower() == REPO_ADMIN.lower() and admin_override is True)
        
        is_authorized = (self.commit_author.lower() == file_owner.lower() or has_admin_override)
        
        if not is_authorized:
            print(f"   ❌ Unauthorized deletion (owner: {file_owner}, editor: {self.commit_author})")
            self.restore_file_from_history(path)
            self.files_corrected.append(path)
            self.corrections_made = True
        else:
            # Authorized deletion - remove from registry
            if has_admin_override:
                print(f"   🔑 Admin override used for deletion (owner: {file_owner}, admin: {self.commit_author})")
            
            del self.registry['files'][path]
            self.registry_updated = True
            print(f"   ✅ Valid deletion - removed from registry")
    

    
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
    

    
    def get_iso_timestamp(self) -> str:
        """Get current timestamp in ISO 8601 format"""
        return datetime.now(timezone.utc).isoformat()
    
    def cleanup_empty_folders(self):
        """Remove empty folders from the repository (excluding hidden folders)"""
        empty_folders = []
        
        # Walk the directory tree bottom-up
        for root, dirs, files in os.walk('.', topdown=False):
            # Skip hidden folders
            if any(part.startswith('.') for part in Path(root).parts):
                continue
            
            # Check if directory is empty (no files and no non-hidden subdirs)
            try:
                contents = list(os.listdir(root))
                # Filter out hidden items
                visible_contents = [item for item in contents if not item.startswith('.')]
                
                if not visible_contents and root != '.':
                    empty_folders.append(root)
                    os.rmdir(root)
            except OSError:
                # Directory not empty or permission issue, skip
                continue
        
        if empty_folders:
            print(f"\n🧹 Cleaned up {len(empty_folders)} empty folder(s):")
            for folder in empty_folders:
                print(f"   🗑️  {folder}")
            self.corrections_made = True
        else:
            print("\n🧹 No empty folders to clean up")
    
    def commit_corrections(self):
        """Commit any corrections made during enforcement"""
        if self.files_corrected:
            print(f"\n📝 Committing corrections for {len(self.files_corrected)} file(s)")
        else:
            print(f"\n📝 Committing registry updates")
        
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
