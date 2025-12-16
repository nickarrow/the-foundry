---
foundry:
  file_owner: nickarrow
  created_date: '2025-12-15T20:55:23.390124+00:00'
  last_modified: '2025-12-16T17:16:51.017758+00:00'
---
# The Foundry - Technical Specification

## Project Overview

**The Foundry** is a shared narrative repository that allows *Ironsworn*, *Starforged*, and *Sundered Isles* players using **Obsidian + Iron Vault** to:
- Publish their **entire campaign vault**
- Read and explore the campaigns of others
- Contribute to a larger, living narrative universe

Players sync their Obsidian vaults using [FIT](https://github.com/joshuakto/fit). All governance, moderation, and permissions are enforced **automatically** within GitHub through GitHub Actions.

### Design Philosophy

The Foundry is designed to feel:
- **Effortless for players** - no manual permission management
- **Invisible in its enforcement** - self-healing corrections happen automatically
- **Fiction-first in presentation** - focus on storytelling, not technical barriers
- **Technically boring and reliable** - proven tools, simple architecture

---

## Core Problem Statement

In a shared repository where multiple players contribute to interconnected campaigns, we need:
1. **File ownership** - every file has exactly one owner
2. **Automatic enforcement** - unauthorized edits are corrected without manual intervention
3. **Collaborative world-building** - players can add content to each other's campaigns
4. **Protection** - players cannot modify or delete files they don't own

---

## Ownership Model

### Frontmatter Schema

All markdown files use **namespaced YAML frontmatter** to track ownership:

```yaml
---
foundry:
  file_owner: "nickarrow"
  created_date: "2025-12-15T10:30:00Z"
  last_modified: "2025-12-15T14:22:00Z"
  admin_override: true  # Optional: only for admin moderation
---
```

**Field Definitions:**
- `file_owner` (string): GitHub username of the file owner
- `created_date` (ISO 8601): Timestamp when file was first committed
- `last_modified` (ISO 8601): Timestamp of last valid edit by owner
- `admin_override` (boolean, optional): Allows repository admin to edit files they don't own

**Key Principles:**
- Frontmatter injection must **preserve existing YAML** from Obsidian/Iron Vault
- Only add missing Foundry fields, never overwrite or delete existing keys
- Use namespacing (`foundry:`) to avoid conflicts with other plugins

### Ownership Rules by File Type

#### Markdown Files (`.md`)
- Ownership determined by `foundry.file_owner` in frontmatter
- If frontmatter is missing, GitHub Action injects it using commit author
- Owner can freely edit, rename, move, or delete their files

#### Non-Markdown Files (images, PDFs, etc.)
- **Root-level files**: Owned by `nickarrow` (repository admin)
- **Non-Markdown files**: Owned by the commit author who first added them
- Ownership tracked via git history (no frontmatter possible)

#### Hidden Files & Folders
- `.obsidian/`, `.git/`, `.gitignore`, etc. are **excluded** from enforcement
- `.github/` folder is **excluded** from enforcement (protected by Guardian system instead)

---

## Enforcement Pipeline

### Trigger
- Runs on **every push to `main` branch**
- FIT syncs directly to main (no pull requests)

### Concurrency Control
- Uses GitHub Actions concurrency groups to prevent conflicts
- Only one enforcement action runs at a time
- Additional pushes are queued (not cancelled)
- Each action processes the latest state including previous corrections
- Ensures no race conditions or merge conflicts when multiple players sync simultaneously

### Pipeline Steps

#### 1. Scan Changed Files
- Use `git diff` to identify modified, added, renamed, or deleted files
- Only process changed files for performance
- **Exclude `.github/` folder** - protected by Guardian system (see Guardian Protection System section)

#### 2. Inject Foundry Frontmatter
For markdown files without Foundry frontmatter:
- Parse existing YAML (preserve all existing keys)
- Add `foundry.file_owner` = commit author's GitHub username
- Add `foundry.created_date` = current timestamp (ISO 8601)
- Add `foundry.last_modified` = current timestamp (ISO 8601)
- Write back to file with formatting preserved

#### 3. Validate Ownership
For each changed file:
- **Markdown files**: Check if commit author matches `foundry.file_owner`, OR if admin override is active
- **Root-level non-markdown**: Check if commit author is `nickarrow`
- **Other non-markdown**: Check if commit author matches original committer (via git history)

**Admin Override:**
- If `foundry.admin_override: true` is present AND commit author is `nickarrow` (admin), allow the edit
- After successful override, automatically remove the `admin_override` flag
- Log the override clearly in the Actions output for transparency
- This provides an intentional escape hatch while preventing accidental edits

#### 4. Restore Unauthorized Edits
If validation fails:
- Revert file to last valid version from git history
- Do not update `foundry.last_modified`
- Track which files were reverted for commit message

#### 5. Handle Special Cases

**File Renames/Moves:**
- Git tracks renames as delete + add
- Detect renames using git rename detection
- Preserve `foundry.file_owner` from original file
- Do not treat as new file (prevents ownership theft)

**File Deletions:**
- If user deletes a file they don't own: restore from previous commit
- If user deletes their own file: allow deletion

**Frontmatter Tampering:**
- If user modifies/deletes Foundry frontmatter in file they don't own: restore entire file
- If owner modifies their own frontmatter: allow, but re-inject if removed

#### 6. Update Metadata
For valid edits by file owner:
- Update `foundry.last_modified` to current timestamp
- Keep `foundry.created_date` unchanged
- Keep `foundry.file_owner` unchanged

#### 7. Commit Corrections
- If any files were corrected, create a new commit
- Commit message: `"Enforced ownership rules"`
- If no corrections needed (all edits were unauthorized): skip correction commit
- Push corrected state back to `main`

---

## Collaborative World-Building

### Folder Structure Freedom
- Players can create files and folders **anywhere** in the repository
- No path-based restrictions (except root-level non-markdown files)
- Example: Player B can create `NickArrow/The Starforged/PlayerB-Character.md`

### Cross-Campaign Contributions
**Scenario:** Player B wants to join Player A's campaign
1. Player B creates a character file in Player A's campaign folder
2. Player B writes journal entries in that folder
3. Player A can read Player B's contributions but cannot edit them
4. Player B cannot edit Player A's original campaign files
5. Both players see a shared, evolving world

**Result:** Organic, emergent world-building without permission management

---

## Edge Cases & Nuances

### Merge Conflicts
- **Low risk** due to self-healing enforcement
- Most conflicts occur when multiple users edit the same file
- Enforcement pipeline catches unauthorized edits before they propagate
- If conflict occurs: unauthorized edits are reverted, owner's changes win

### Manual GitHub Edits
- **Low risk** - players use FIT, not GitHub web interface
- Admin (`nickarrow`) follows same ownership rules as all players
- Admin can use `admin_override: true` flag for intentional moderation
- If other user makes manual edits: same enforcement rules apply

### Empty Commits
- If a push contains only unauthorized edits (everything reverted): skip correction commit
- Player's local vault will sync and receive the reverted state
- No noise in commit history for "nothing happened"

### Performance at Scale
- Scanning only changed files keeps pipeline fast
- Even with hundreds of files, git diff is efficient
- Concurrency control ensures actions run sequentially (queued, not parallel)
- Multiple simultaneous pushes will queue but process quickly (typically seconds per action)
- If performance becomes an issue: add caching or incremental processing

---

## Player Experience

### What Players See
- **Seamless syncing** via FIT plugin in Obsidian
- **Silent corrections** - unauthorized edits disappear on next sync
- **No error messages** - just clean, corrected content
- **Clear boundaries** - documentation explains ownership model upfront

### What Players Can Do
- ✅ Create new files anywhere
- ✅ Edit their own files freely
- ✅ Delete their own files
- ✅ Rename/move their own files
- ✅ Read everyone's files
- ❌ Edit files owned by others
- ❌ Delete files owned by others
- ❌ Steal ownership via rename/frontmatter tampering

### Onboarding & Documentation
- Root-level documentation files explain The Foundry rules
- Owned by `nickarrow` (protected from edits unless admin override used)
- Clear disclaimers about automatic corrections
- Examples of collaborative workflows

### Admin Experience
- Repository admin (`nickarrow`) follows same ownership rules as all players
- Cannot accidentally edit other players' files
- Can use `admin_override: true` flag for intentional moderation/fixes
- Override flag is automatically removed after use (one-time)
- All overrides logged in GitHub Actions for audit trail

---

## Technical Architecture

### Technology Stack
- **Git/GitHub**: Version control and hosting
- **GitHub Actions**: Enforcement pipeline automation
- **Obsidian**: Player-facing vault interface
- **FIT Plugin**: Automatic git sync from Obsidian
- **Iron Vault Plugin**: Ironsworn/Starforged game mechanics

### GitHub Action Implementation

**Workflow File:** `.github/workflows/enforce-ownership.yml`

**Required Capabilities:**
- YAML parsing and manipulation (preserve existing keys)
- Git history inspection (for renames and non-markdown ownership)
- File system operations (read, write, revert)
- Commit and push with GitHub token
- Concurrency control to prevent race conditions

**Language/Tools:**
- Python 3.11+ with PyYAML for frontmatter handling
- Git CLI commands for history inspection
- GitHub Actions native features for triggers, auth, and concurrency groups

**Concurrency Configuration:**
```yaml
concurrency:
  group: foundry-enforcement
  cancel-in-progress: false
```
This ensures enforcement actions run sequentially, preventing merge conflicts when multiple players push simultaneously.

### Repository Structure
```
the-foundry/
├── .github/
│   ├── scripts/
│   │   └── enforce_ownership.py    # Enforcement script
│   └── workflows/
│       ├── enforce-ownership.yml   # Main enforcement workflow
│       └── guardian.yml            # Guardian protection (on protected-workflows branch)
├── .obsidian/                      # Excluded from enforcement
├── The Starforged/                 # Game folders (any structure)
│   ├── Characters/
│   ├── Journals/
│   └── ...
├── LICENSE                         # Root file (owned by nickarrow)
├── README.md                       # Root file (owned by nickarrow)
└── SPECIFICATION.md                # This file
```

### Branch Structure
- **`main`** - Active repository with all player content and workflows
- **`protected-workflows`** - Protected branch containing only canonical `.github/` files
  - Only admin can push to this branch
  - Guardian workflow runs from here
  - Contains "source of truth" for enforcement infrastructure

---

## Guardian Protection System

### Problem Statement

The enforcement pipeline protects player content, but what protects the enforcement pipeline itself? 

**Attack scenario without Guardian:**
1. Attacker deletes `.github/workflows/enforce-ownership.yml`
2. Enforcement pipeline stops running
3. Attacker can now delete/modify any content without restriction
4. Manual intervention required to restore

**Solution:** Guardian workflow runs from a separate protected branch that players cannot modify.

### Architecture

#### Two-Tier Protection

**Tier 1: Enforcement Pipeline** (runs on `main`)
- Protects player content from unauthorized edits
- Validates file ownership
- Reverts unauthorized changes
- **Excludes `.github/` folder** (protected by Tier 2)

**Tier 2: Guardian Workflow** (runs on `protected-workflows`)
- Protects the enforcement infrastructure
- Runs every 15 minutes from protected branch
- Detects compromised workflows
- Restores entire repository to last known good state

#### Protected Branch: `protected-workflows`

**Purpose:**
- Contains canonical versions of `.github/` files
- Guardian workflow runs from here (cannot be disabled by players)
- Minimal branch (only `.github/` folder + README)

**Branch Protection Rules:**
- ✅ Restrict updates - Only admin can push
- ✅ Restrict deletions - Branch cannot be deleted
- ✅ Require pull request before merging - All changes need approval
- ✅ Block force pushes - History cannot be rewritten
- ✅ Required approvals: 1 - Admin must approve any PRs

**Critical:** `main` and `protected-workflows` should NEVER be merged. They serve different purposes and merging would cause file deletions.

### Guardian Workflow Logic

**Runs every 15 minutes:**

1. **Check Workflow Integrity**
   ```
   For each protected file (.github/workflows/enforce-ownership.yml, etc.):
     - Check if file exists on main
     - Compare with canonical version from protected-workflows
     - If missing or different: mark as TAMPERED
   ```

2. **Find Last Known Good State**
   ```
   If TAMPERED:
     Search git history backwards:
       For each commit:
         Check if all workflow files exist and match canonical versions
         If yes: this is LAST_GOOD_COMMIT
         Break
     
     Safety limit: Check up to 100 commits
   ```

3. **Restore Repository**
   ```
   If LAST_GOOD_COMMIT found:
     Get all files changed since LAST_GOOD_COMMIT
     For each changed file (excluding .github/):
       - Deleted files: restore from LAST_GOOD_COMMIT
       - Modified files: restore from LAST_GOOD_COMMIT
       - Added files: delete them
       - Renamed files: revert to original name
     
     Restore workflow files from protected-workflows branch
     Commit all restorations
     Push to main
   ```

### Attack Scenario Protection

**Example sustained attack:**

```
1:59 PM - Repository in good state
2:00 PM - Attacker deletes enforce-ownership.yml (commit 1)
2:01 PM - Attacker deletes 50 player files (commit 2)
2:03 PM - Attacker modifies 20 more files (commit 3)
2:05 PM - Attacker renames folders (commit 4)
2:10 PM - Attacker makes more malicious commits (commits 5-10)

2:15 PM - Guardian runs:
  - Detects workflows are missing
  - Searches backwards through commits 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
  - Finds commit at 1:59 PM has intact workflows
  - Restores ALL files (except .github/) from 1:59 PM
  - Restores workflow files from protected-workflows
  - Commits restoration
  - Pushes to main

2:16 PM - Repository fully restored to 1:59 PM state
```

**Maximum vulnerability window:** 15 minutes

### Protected Files

Guardian monitors these critical files:
- `.github/workflows/enforce-ownership.yml` - Main enforcement workflow
- `.github/scripts/enforce_ownership.py` - Enforcement script
- `.github/workflows/guardian.yml` - Guardian itself (self-protecting)

### Performance Considerations

- Guardian searches up to 100 commits to find last good state
- Typically finds it in 1-5 commits (recent attacks)
- Safety limit prevents infinite loops
- 15-minute interval balances protection vs. resource usage

### Updating Workflows (Admin Only)

**Process:**
1. Update files on `protected-workflows` branch first
2. Manually copy changes to `main` (DO NOT MERGE)
3. Guardian will see files match and allow them

**Why not merge?**
- `protected-workflows` is a minimal branch (only `.github/` + README)
- `main` has all player content
- Merging would delete all player content from main
- Branches serve different purposes and must remain separate

### Limitations

- 15-minute vulnerability window (attacker can cause damage before Guardian runs)
- Guardian only activates when workflows are compromised
- If workflows are intact, Guardian assumes Enforcement Pipeline is handling content
- Requires admin to have branch protection properly configured

### Monitoring

**GitHub Actions Tab:**
- Guardian runs show up as "Guardian - Protect Workflows"
- Logs show:
  - Workflow integrity check results
  - Number of commits searched
  - Files restored (if any)
  - Timestamp of last known good state

**Manual Trigger:**
- Admin can manually trigger Guardian from Actions tab
- Useful for immediate checking after suspected attack

---

## Future Considerations

### Not in Scope
- Pull request workflows (FIT doesn't use them)
- Collaborative editing permissions (one owner per file only)
- Content moderation beyond ownership (no profanity filters, etc.)
- Notification system for corrections (silent only)

### Potential Future Enhancements
- Analytics dashboard (most active campaigns, etc.)
- Web interface for browsing (GitHub is the interface)
- Community Discord

---

## Success Criteria

The Foundry ownership model is successful when:
1. ✅ Players can sync their vaults without thinking about permissions
2. ✅ Unauthorized edits are corrected within seconds of push
3. ✅ No manual moderation required for ownership enforcement
4. ✅ Players naturally collaborate across campaign boundaries
5. ✅ Zero data loss (all valid edits preserved, invalid edits reverted)
6. ✅ Repository remains stable and usable as it grows
7. ✅ Enforcement infrastructure is protected from tampering (Guardian)
8. ✅ Repository can self-heal from attacks within 15 minutes (Guardian)

---

## Implementation Roadmap

### Phase 1: Foundation ✅ Complete
1. ✅ Add namespaced frontmatter to existing markdown files
2. ✅ Create GitHub Action workflow skeleton
3. ✅ Implement frontmatter injection logic
4. ✅ Test with manual commits

### Phase 2: Enforcement ✅ Complete
1. ✅ Implement ownership validation
2. ✅ Implement file restoration for unauthorized edits
3. ✅ Handle renames and deletions
4. ✅ Test with multiple simulated users

### Phase 3: Guardian Protection ✅ Complete
1. ✅ Create protected-workflows branch
2. ✅ Implement Guardian workflow
3. ✅ Add workflow integrity checking
4. ✅ Add last-known-good-state restoration
5. ✅ Configure branch protection rules
6. ✅ Test attack scenarios

### Phase 4: Polish 🚧 In Progress
1. ✅ Optimize performance (changed files only)
2. ✅ Add comprehensive logging
3. ✅ Update root-level documentation
4. ⏳ Invite beta testers

### Phase 5: Launch
1. Announce to Ironsworn/Starforged community
2. Monitor for edge cases
3. Iterate based on real-world usage

---

## Appendix: Example Scenarios

### Scenario A: New Player Joins
1. Player C clones the repository
2. Player C creates `PlayerC/My-Campaign/` folder
3. Player C adds character and journal files
4. FIT syncs to GitHub
5. GitHub Action injects frontmatter with `file_owner: "playerc"`
6. Files are now protected - only Player C can edit them

### Scenario B: Unauthorized Edit Attempt
1. Player B edits `NickArrow/The Starforged/Truths.md`
2. FIT syncs the change to GitHub
3. GitHub Action detects commit author (playerb) ≠ file_owner (nickarrow)
4. Action reverts file to previous version
5. Action commits correction
6. Player B's next sync pulls the corrected version
7. Player B's unauthorized edit is gone

### Scenario C: Collaborative Campaign
1. Player A creates `PlayerA/Shared-World/` campaign
2. Player B creates `PlayerA/Shared-World/PlayerB-Character.md`
3. Player C creates `PlayerA/Shared-World/PlayerC-Journal.md`
4. All three players can read all files
5. Each player can only edit their own files
6. The campaign grows organically with multiple contributors

### Scenario D: Admin Moderation
1. Admin needs to fix a typo in Player A's file
2. Admin opens `PlayerA/Campaign/Character.md`
3. Admin adds `admin_override: true` to the frontmatter
4. Admin makes the correction and syncs
5. GitHub Action detects admin override flag
6. Action allows the edit and removes the override flag
7. Action logs the override in the workflow output
8. File is corrected, audit trail preserved

---

**Last Updated:** 2025-12-16  
**Author:** nickarrow  
**Status:** Implemented and Active (with Guardian Protection)
