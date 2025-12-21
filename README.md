# The Foundry

> A shared narrative universe for **Ironsworn**, **Starforged**, and **Sundered Isles** players

## What is The Foundry?

**The Foundry** is a collaborative storytelling repository where players using **Obsidian + Iron Vault** can:
- **Publish their entire campaign vault** - share your adventures with the community
- **Explore other campaigns** - read and discover the stories of fellow players
- **Build shared worlds** - contribute to campaigns and create interconnected narratives
- **Collaborate organically** - add characters, journals, and content to any campaign

The Foundry uses automatic governance through GitHub Actions to manage permissions and ownership, making collaboration effortless and invisible.
## How It Works

### The Magic: Automatic Ownership

Every file in The Foundry has exactly one owner. When you create a file, you own it. When someone else creates a file, they own it. Simple.

**What you can do:**
- ✅ Create new files anywhere in the repository
- ✅ Edit, rename, move, or delete your own files
- ✅ Read everyone's files
- ❌ Edit or delete files owned by others

**What happens if you try to edit someone else's file?**

The Foundry automatically detects unauthorized edits and silently restores the file to its correct state. Your next sync will pull the corrected version. No errors, no drama, just clean content.

### File Ownership Tracking

Ownership is tracked in a centralized registry `registry.yml` file at [The-Foundry-Guardian](https://github.com/nickarrow/the-foundry-guardian/blob/main/registry.yml) repo:

```yaml
files:
  "My-Campaign/Characters/My-Hero.md":
    owner: yourusername
    created: 2025-12-15T10:30:00Z
    modified: 2025-12-15T14:22:00Z
    checksum: abc123def456...
```

**Don't worry about this!** The system manages the registry automatically. Your markdown files stay clean - no automated frontmatter injection. The registry tracks ownership, timestamps, and file integrity using SHA-256 checksums.

## Getting Started

### Prerequisites

- **Obsidian** - [Download here](https://obsidian.md/)
- **Iron Vault plugin** - Install from Obsidian Community Plugins
- **FIT plugin** - Install from Obsidian Community Plugins
- **GitHub account** - [Sign up here](https://github.com/)

### Setup Instructions

#### 1. Create an Empty Obsidian Vault

1. Open Obsidian
2. Click "Create new vault", give it a name `The Foundry` is a good one, but any name will work. 
3. Pick a location to save it locally

#### 2. Get GitHub Repository Access
1. Contact the repository admin (nickarrow) to be added as a collaborator with **Write** permissions.
2. If you do not have a GitHub account, get one for free and then contact me (nickarrow)
#### 3. Configure the FIT Plugin (Minimalist File giT)

1. In Obsidian, open Settings → Community Plugins
2. Install the FIT plugin
3. Configure it to sync with this repository
4. Enable automatic syncing

**Important:** Make sure FIT is configured to use your GitHub credentials that match your GitHub username. This ensures proper ownership tracking.

#### 5. Start Creating!

Create your campaign folder and start adding content:

```
My-IronSwornGame/
├── Characters/
│   └── My-Hero.md
├── Journals/
│   └── Session-1.md
└── Campaign Index.md
```

FIT will automatically sync your changes to GitHub, and The Foundry will inject ownership frontmatter.

## Collaborative Campaigns

The real magic happens when players contribute to each other's worlds.

### Example: Joining Another Player's Campaign

1. Browse the repository and find a campaign you like (e.g., `The Starforged/`)
2. Create your character file: `The Starforged/Characters/YourCharacter.md`
3. Write your journal entries: `The Starforged/Journals/YourJournal.md`
4. Sync in Obsidian with FIT

Now both you and the campaign creator can see each other's content, but neither can edit the other's files. The world grows organically!

## Technical Details

### The Enforcement Pipeline

Every time you push changes to GitHub, an automated workflow:

1. **Scans changed files** - only processes what you modified
2. **Calculates checksums** - uses SHA-256 to detect which files actually changed
3. **Updates registry** - adds new files or updates existing entries
4. **Validates ownership** - checks if you're authorized to make the edit
5. **Restores unauthorized edits** - reverts files you don't own
6. **Commits corrections** - pushes the corrected registry and files back to the repository

This all happens in seconds, completely automatically.

### File Types

**All non-hidden files:**
- Ownership tracked in `.foundry/registry.yml`
- Includes markdown, images, PDFs, and any other file type
- SHA-256 checksums ensure file integrity
- Automatically added to registry on first commit

**Hidden files and folders:**
- `.obsidian/`, `.git/`, etc. are excluded from enforcement
- `.github/` folder is protected by the Guardian system (see below)
- `.foundry/registry.yml` is admin-only (ownership hardcoded in enforcement script)

### Admin Privileges

The repository admin (`nickarrow`) follows the same ownership rules as all other players. However, for moderation purposes, the admin can use an **admin override** flag.

**How Admin Override Works:**

To edit another player's file, the admin must explicitly add this to the registry entry:

```yaml
files:
  "Other-Campaign/Characters/Their-Hero.md":
    owner: otherplayer
    created: 2025-12-15T10:30:00Z
    modified: 2025-12-15T14:22:00Z
    checksum: abc123def456...
    admin_override: true  # Add this line
```

**Steps:**
1. Edit `.foundry/registry.yml` and add `admin_override: true` to the file entry
2. Make your changes to the file
3. Commit both the registry and file changes together
4. The enforcement workflow automatically removes the flag after use (one-time override)

**Benefits:**
- Prevents accidental edits (admin must explicitly set the flag)
- One-time use (flag is automatically removed)
- All admin overrides are logged in the GitHub Actions output for transparency
- Works for edit, rename, move, or delete operations

## Best Practices

### Naming Conventions

- Use descriptive folder and file names
- Avoid special characters that might cause issues across platforms
- Use hyphens or underscores instead of spaces (though spaces work fine)

## Troubleshooting

### My edits disappeared!

This means you tried to edit a file you don't own. The Foundry automatically restored it. Create your own file instead!

### Sync conflicts with registry.yml

The registry file updates automatically on every commit. If you get a sync conflict:
1. Pull the latest changes first
2. Make your file edits
3. Push your changes
4. The enforcement workflow will update the registry automatically

**Important:** Never manually edit the registry unless you're the admin using the override feature.

### FIT isn't syncing

Check your FIT configuration and GitHub credentials. Make sure you have Write access to the repository.

## Community Guidelines

- **Be respectful** - this is a shared creative space
- **No spam** - don't create excessive empty files or folders
- **Report issues** - if you see problems, contact the admin

## Guardian Protection System

The Foundry uses a two-tier protection system to ensure both player content and the enforcement infrastructure remain secure:

### Tier 1: Enforcement Pipeline (Player Content)
- Runs on every push to `main` in this repository
- Validates file ownership for player content
- Reverts unauthorized edits to player files
- Excludes `.github/` folder (protected by external Guardian)

### Tier 2: External Guardian (Infrastructure Protection)
- Runs every 15 minutes from a separate private repository: [`the-foundry-guardian`](https://github.com/nickarrow/the-foundry-guardian)
- Monitors this repository for compromised workflows
- Cannot be disabled by attackers (they don't have access to the guardian repo)
- If workflows are compromised, searches git history to find last known good state
- Restores entire repository to that state (maximum 15-minute vulnerability window)

**Why external Guardian is needed:** Without it, an attacker could delete the enforcement workflows from this repository, then delete/modify any content they want. The external Guardian ensures that even if all workflows are deleted here, everything gets restored automatically from the external monitoring system.

**How it works:**
1. Guardian runs from separate private repository (only admin has access)
2. Every 15 minutes, clones this repository and checks if `.github/` files are intact
3. Compares workflows against canonical versions stored in guardian repo
4. If compromised, finds the last commit where workflows were correct
5. Restores workflow files from canonical versions
6. Restores all other files from last known good commit
7. Pushes restoration to this repository
8. Logs attack details in guardian repo workflow output

**Attack scenario protection:**
- 2:00 PM - Attacker deletes enforcement workflows
- 2:01 PM - Attacker deletes player content
- 2:15 PM - External Guardian detects compromise and restores everything
- 2:16 PM - Repository fully restored, attacker's changes reverted

For complete Guardian documentation, see the [`the-foundry-guardian`](https://github.com/nickarrow/the-foundry-guardian) repository.

## Technical Architecture

For developers and the technically curious:

- **Version Control:** Git/GitHub
- **Automation:** GitHub Actions (two workflows: enforcement + guardian)
- **Enforcement Script:** Python with PyYAML and hashlib (SHA-256)
- **Ownership Registry:** `.foundry/registry.yml` (centralized tracking)
- **Integrity Checking:** SHA-256 checksums for all tracked files
- **Sync Tool:** FIT plugin for Obsidian
- **Game System:** Iron Vault plugin for Obsidian
- **Protection:** Two-tier system (enforcement pipeline + guardian workflow)

### Why Registry-Based?

The Foundry previously used frontmatter injection but switched to a registry-based system to:
- **Eliminate merge conflicts** - Registry updates separately from file content
- **Keep files clean** - No automated frontmatter injection
- **Improve performance** - Checksums quickly identify changed files
- **Centralize tracking** - All ownership data in one place
- **Enhance security** - Registry ownership hardcoded in protected enforcement script

## Contributing

Want to improve The Foundry itself (not just add campaign content)?

1. Fork the repository
2. Create a feature branch
3. Make your changes to the enforcement scripts or documentation
4. Submit a pull request

Changes to the core system require admin approval.

## License

See [LICENSE](.LICENSE) for details.

## Questions?

Contact the repository admin: [@nickarrow](https://github.com/nickarrow)

---

**Welcome to The Foundry.**
