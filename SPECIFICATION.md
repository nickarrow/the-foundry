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

### Registry-Based Tracking

All file ownership is tracked in a centralized registry at `.foundry/registry.yml`:

```yaml
files:
  "My-Campaign/Characters/My-Hero.md":
    owner: nickarrow
    created: 2025-12-15T10:30:00Z
    modified: 2025-12-15T14:22:00Z
    checksum: abc123def456789...
  "Other-Campaign/Characters/Their-Hero.md":
    owner: otherplayer
    created: 2025-12-16T09:15:00Z
    modified: 2025-12-18T11:45:00Z
    checksum: def789ghi012345...
    admin_override: true  # Optional: Allows admin to edit this file once
```

**Field Definitions:**
- `owner` (string): GitHub username of the file owner
- `created` (ISO 8601): Timestamp when file was first committed
- `modified` (ISO 8601): Timestamp of last valid edit by owner
- `checksum` (string): SHA-256 hash of file content for integrity checking
- `admin_override` (boolean, optional): Allows repository admin to edit files they don't own (one-time use)

**Key Principles:**
- Registry is the single source of truth for ownership
- No frontmatter injection into user files (keeps files clean)
- SHA-256 checksums detect unauthorized modifications
- Registry itself is admin-only (ownership hardcoded in enforcement script)

### Why Registry-Based?

The Foundry switched from frontmatter injection to registry-based tracking to:
- **Eliminate merge conflicts** - Registry updates separately from file content
- **Keep files clean** - No automated frontmatter injection
- **Improve performance** - Checksums quickly identify changed files
- **Centralize tracking** - All ownership data in one place
- **Enhance security** - Registry ownership hardcoded in protected enforcement script

### Ownership Rules by File Type

#### All Non-Hidden Files
- Ownership tracked in `.foundry/registry.yml`
- Includes markdown, images, PDFs, and any other file type
- SHA-256 checksums ensure file integrity
- Owner can freely edit, rename, move, or delete their files

#### Hidden Files & Folders
- `.obsidian/`, `.git/`, `.gitignore`, etc. are **excluded** from enforcement
- `.github/` folder is **excluded** from enforcement (protected by Guardian system instead)
- `.foundry/registry.yml` is **admin-only** (ownership hardcoded in enforcement script, protected by Guardian)

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

#### 1. Load Registry
- Load `.foundry/registry.yml` from repository
- Parse YAML structure
- If registry doesn't exist, initialize empty registry

#### 2. Scan Changed Files
- Use `git diff` to identify modified, added, renamed, or deleted files
- Only process changed files for performance
- **Include `.foundry/registry.yml`** for validation (special case)
- **Exclude other `.github/` and `.foundry/` files** - protected by Guardian system

#### 3. Calculate Checksums
For each changed file:
- Calculate SHA-256 hash of file content
- Compare with checksum in registry (if file exists in registry)
- If checksums match, file hasn't actually changed (skip)
- If checksums differ, file was modified (validate ownership)

#### 4. Validate Ownership
For each changed file:
- **Registry file (`.foundry/registry.yml`)**: 
  - Check if commit is from enforcement workflow (allow)
  - Check if commit author is `nickarrow` (admin, allow)
  - Otherwise: restore from previous commit
- **New files**: Add to registry with commit author as owner
- **Modified files**: Check if commit author matches registry owner OR admin override is active
- **Renamed files**: Check if commit author matches registry owner, update registry path
- **Deleted files**: Check if commit author matches registry owner, remove from registry

**Admin Override:**
- If `admin_override: true` is present in registry entry AND commit author is `nickarrow` (admin), allow the edit
- After successful override, automatically remove the `admin_override` flag from registry
- Log the override clearly in the Actions output for transparency
- This provides an intentional escape hatch while preventing accidental edits

#### 5. Restore Unauthorized Edits
If validation fails:
- Revert file to last valid version from git history
- Do not update registry entry
- Track which files were reverted for commit message

#### 6. Handle Special Cases

**File Renames/Moves:**
- Git tracks renames as delete + add
- Detect renames using git rename detection
- Preserve owner from original registry entry
- Update registry: remove old path, add new path with same owner
- Do not treat as new file (prevents ownership theft)

**File Deletions:**
- If user deletes a file they don't own: restore from previous commit
- If user deletes their own file: allow deletion, remove from registry

**Registry Tampering:**
- If user modifies registry without authorization: restore registry from previous commit
- Only admin and enforcement workflow can modify registry

#### 7. Update Registry
For valid operations:
- **New files**: Add entry with owner, created timestamp, modified timestamp, checksum
- **Modified files**: Update modified timestamp and checksum
- **Renamed files**: Move entry to new path, update modified timestamp and checksum
- **Deleted files**: Remove entry from registry
- **Admin override used**: Remove `admin_override` flag from entry

#### 8. Save Registry
- Write updated registry to `.foundry/registry.yml`
- Stage registry file for commit

#### 9. Commit Corrections
- If any files were corrected OR registry was updated, create a new commit
- Commit message: `"Enforced ownership rules"`
- Commit author: "Foundry Enforcer" (enforcement workflow identity)
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
- YAML parsing and manipulation (for registry)
- SHA-256 checksum calculation (for file integrity)
- Git history inspection (for renames and restoration)
- File system operations (read, write, revert)
- Commit and push with GitHub token
- Concurrency control to prevent race conditions

**Language/Tools:**
- Python 3.11+ with PyYAML for registry handling
- Python hashlib for SHA-256 checksums
- Git CLI commands for history inspection and rename detection
- GitHub Actions native features for triggers, auth, and concurrency groups

**Concurrency Configuration:**
```yaml
concurrency:
  group: foundry-enforcement
  cancel-in-progress: false
```
This ensures enforcement actions run sequentially, preventing merge conflicts when multiple players push simultaneously.

### Repository Structure

**Main Repository:** `the-foundry`
```
the-foundry/
├── .github/
│   ├── scripts/
│   │   └── enforce_ownership.py    # Enforcement script
│   └── workflows/
│       └── enforce-ownership.yml   # Main enforcement workflow
├── .foundry/
│   └── registry.yml                # Ownership registry (admin-only)
├── .obsidian/                      # Excluded from enforcement
├── The Starforged/                 # Game folders (any structure)
│   ├── Characters/
│   ├── Journals/
│   └── ...
├── LICENSE                         # Root file (tracked in registry)
├── README.md                       # Root file (tracked in registry)
├── SPECIFICATION.md                # This file (tracked in registry)
└── REGISTRY_MIGRATION.md           # Registry system documentation
```

**Guardian Repository:** `the-foundry-guardian` (private)
```
the-foundry-guardian/
├── .github/
│   └── workflows/
│       └── monitor.yml             # Guardian monitoring workflow
├── canonical-workflows/
│   ├── enforce-ownership.yml       # Canonical enforcement workflow
│   ├── enforce_ownership.py        # Canonical enforcement script
│   └── registry.yml                # Canonical registry structure
└── README.md                       # Guardian documentation
```

### Repository Relationship
- **`the-foundry`** - Main collaborative repository (players have write access)
- **`the-foundry-guardian`** - Private monitoring repository (only admin has access)
- Guardian monitors `the-foundry` every 15 minutes
- Guardian cannot be disabled by players (separate private repo)
- Canonical workflow versions stored in guardian repo

---

## Guardian Protection System

### Problem Statement

The enforcement pipeline protects player content, but what protects the enforcement pipeline itself? 

**Attack scenario without Guardian:**
1. Attacker deletes `.github/workflows/enforce-ownership.yml`
2. Enforcement pipeline stops running
3. Attacker can now delete/modify any content without restriction
4. Manual intervention required to restore

**Solution:** Guardian workflow runs from a separate private repository that attackers cannot access.

### Architecture

#### Two-Tier Protection

**Tier 1: Enforcement Pipeline** (runs on `main` in `the-foundry`)
- Protects player content from unauthorized edits
- Validates file ownership
- Reverts unauthorized changes
- **Excludes `.github/` folder** (protected by Tier 2)

**Tier 2: External Guardian** (runs in separate repository)
- Protects the enforcement infrastructure
- Runs every 15 minutes from [`the-foundry-guardian`](https://github.com/nickarrow/the-foundry-guardian) repository
- Detects compromised workflows
- Restores entire repository to last known good state
- Cannot be disabled by attackers (separate private repo)

#### External Guardian Repository

**Repository:** [`the-foundry-guardian`](https://github.com/nickarrow/the-foundry-guardian)

**Purpose:**
- Private repository (only admin has access)
- Contains Guardian monitoring workflow
- Stores canonical versions of `.github/` files
- Monitors `the-foundry` repository every 15 minutes
- Cannot be disabled by players (they don't have access)

**How it works:**
1. Scheduled workflow runs every 15 minutes
2. Clones `the-foundry` repository
3. Compares workflow files against canonical versions
4. If compromised, finds last known good commit
5. Restores workflows from canonical versions
6. Restores content from last good commit
7. Pushes restoration to `the-foundry`
8. Logs attack details in workflow output

**Security:**
- Separate repository = cannot be disabled by attackers
- Private repository = only admin can access
- Uses Personal Access Token with minimal permissions
- All Guardian actions logged in GitHub Actions

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
- `.foundry/registry.yml` - Ownership registry (validated by enforcement, protected by Guardian)

### Performance Considerations

- Guardian searches up to 100 commits to find last good state
- Typically finds it in 1-5 commits (recent attacks)
- Safety limit prevents infinite loops
- 15-minute interval balances protection vs. resource usage

### Updating Workflows (Admin Only)

**Process:**
1. Update workflow files in `the-foundry` repository
2. Test that they work correctly
3. Copy updated files to `the-foundry-guardian/canonical-workflows/`
4. Commit and push to guardian repository
5. Guardian will now use the new canonical versions for comparison

**Example:**
```bash
# 1. Update in the-foundry
cd the-foundry
# Edit .github/workflows/enforce-ownership.yml
git add .github/
git commit -m "Update enforcement workflow"
git push

# 2. Update canonical versions in guardian
cd ../the-foundry-guardian
cp ../the-foundry/.github/workflows/enforce-ownership.yml canonical-workflows/
cp ../the-foundry/.github/scripts/enforce_ownership.py canonical-workflows/
git add canonical-workflows/
git commit -m "Update canonical workflows"
git push
```

### Limitations

- 15-minute vulnerability window (attacker can cause damage before Guardian runs)
- Guardian only activates when workflows are compromised
- If workflows are intact, Guardian assumes Enforcement Pipeline is handling content
- Requires admin to have branch protection properly configured

### Monitoring

**Guardian Repository Actions Tab:**
- Go to [`the-foundry-guardian`](https://github.com/nickarrow/the-foundry-guardian) → Actions
- Guardian runs show up as "Guardian - Monitor The Foundry"
- Logs show:
  - Workflow integrity check results
  - Number of commits searched
  - Files restored (if any)
  - Timestamp of last known good state
  - Attack details (attackers, malicious commits, files affected)

**Manual Trigger:**
- Admin can manually trigger Guardian from guardian repo Actions tab
- Useful for immediate checking after suspected attack
- Select "Guardian - Monitor The Foundry" → "Run workflow"

**Attack Detection:**
- When attack is detected, full details logged in workflow output
- Review Actions tab in guardian repo to see attack logs
- Includes attacker usernames, malicious commits, and files affected

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
5. GitHub Action adds files to registry with `owner: "playerc"`
6. Files are now protected - only Player C can edit them

### Scenario B: Unauthorized Edit Attempt
1. Player B edits `NickArrow/The Starforged/Truths.md`
2. FIT syncs the change to GitHub
3. GitHub Action calculates file checksum (detects change)
4. Action checks registry: commit author (playerb) ≠ owner (nickarrow)
5. Action reverts file to previous version
6. Action commits correction
7. Player B's next sync pulls the corrected version
8. Player B's unauthorized edit is gone

### Scenario C: Collaborative Campaign
1. Player A creates `PlayerA/Shared-World/` campaign
2. Player B creates `PlayerA/Shared-World/PlayerB-Character.md`
3. Player C creates `PlayerA/Shared-World/PlayerC-Journal.md`
4. All three players can read all files
5. Each player can only edit their own files
6. The campaign grows organically with multiple contributors

### Scenario D: Admin Moderation
1. Admin needs to fix a typo in Player A's file
2. Admin opens `.foundry/registry.yml`
3. Admin adds `admin_override: true` to the file's registry entry
4. Admin makes the correction to the file and syncs both changes
5. GitHub Action detects admin override flag in registry
6. Action allows the edit and removes the override flag from registry
7. Action updates the file's checksum and modified timestamp
8. Action logs the override in the workflow output
9. File is corrected, audit trail preserved

### Scenario E: Registry Protection
1. Player B tries to edit `.foundry/registry.yml` to grant themselves ownership of Player A's files
2. FIT syncs the registry change to GitHub
3. GitHub Action detects registry was modified
4. Action checks: commit author (playerb) ≠ admin (nickarrow) AND not enforcement workflow
5. Action reverts registry to previous version
6. Action commits correction
7. Player B's next sync pulls the corrected registry
8. Player B's attempted ownership theft is prevented

---

**Last Updated:** 2025-12-17  
**Author:** nickarrow  
**Status:** Implemented and Active (Registry-Based with Guardian Protection)
