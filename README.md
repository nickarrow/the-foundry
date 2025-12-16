---
foundry:
  file_owner: nickarrow
  created_date: '2025-12-15T20:25:33.504586+00:00'
  last_modified: '2025-12-16T04:01:14.864852+00:00'
---
# The Foundry

> A shared narrative universe for **Ironsworn**, **Starforged**, and **Sundered Isles** players

## What is The Foundry?

**The Foundry** is a collaborative storytelling repository where players using **Obsidian + Iron Vault** can:
- 📖 **Publish their entire campaign vault** - share your adventures with the community
- 🔍 **Explore other campaigns** - read and discover the stories of fellow players
- 🌍 **Build shared worlds** - contribute to campaigns and create interconnected narratives
- 🤝 **Collaborate organically** - add characters, journals, and content to any campaign

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

Ownership is tracked through YAML frontmatter that's automatically added to your markdown files:

```yaml
---
foundry:
  file_owner: "yourusername"
  created_date: "2025-12-15T10:30:00Z"
  last_modified: "2025-12-15T14:22:00Z"
---
```

**Don't worry about this!** The system injects and manages this frontmatter automatically. Your existing Iron Vault and Obsidian frontmatter is always preserved.

## Getting Started

### Prerequisites

- **Obsidian** - [Download here](https://obsidian.md/)
- **Iron Vault plugin** - Install from Obsidian Community Plugins
- **FIT plugin** - [Install from here](https://github.com/joshuakto/fit)
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
2. **Injects frontmatter** - adds ownership metadata if missing
3. **Validates ownership** - checks if you're authorized to make the edit
4. **Restores unauthorized edits** - reverts files you don't own
5. **Commits corrections** - pushes the corrected state back to the repository

This all happens in seconds, completely automatically.

### File Types

**Markdown files (`.md`):**
- Ownership tracked via frontmatter
- Automatically injected on first commit

**Non-markdown files (images, PDFs, etc.):**
- Root-level files owned by repository admin
- Files owned by whoever added them
- Ownership tracked via git history

**Hidden files:**
- `.obsidian/`, `.git/`, etc. are excluded from enforcement
- `.github/` folder is protected by the Guardian system (see below)

### Admin Privileges

The repository admin (`nickarrow`) follows the same ownership rules as all other players. However, for moderation purposes, the admin can use an **admin override** flag.

**How Admin Override Works:**

To edit another player's file, the admin must explicitly add this to the frontmatter:

```yaml
---
foundry:
  file_owner: "otherplayer"
  created_date: "2025-12-15T10:30:00Z"
  last_modified: "2025-12-15T14:22:00Z"
  admin_override: true
---
```

- The `admin_override: true` flag only works for the admin account
- After the edit is accepted, the flag is automatically removed
- This prevents accidental edits while providing an intentional escape hatch
- All admin overrides are logged in the GitHub Actions output for transparency

## Best Practices

### Naming Conventions

- Use descriptive folder and file names
- Avoid special characters that might cause issues across platforms
- Use hyphens or underscores instead of spaces (though spaces work fine)

## Troubleshooting

### My edits disappeared!

This means you tried to edit a file you don't own. The Foundry automatically restored it. Create your own file instead!

### Frontmatter looks weird

The Foundry uses namespaced frontmatter (`foundry:`) to avoid conflicts. Your Iron Vault and Obsidian frontmatter is preserved above or below it. Frontmatter can be hidden in Obsidian settings.

### Sync conflicts

If you get a sync conflict, wait a moment and then try again. The enforcement pipeline prevents most conflicts from happening.

### FIT isn't syncing

Check your FIT configuration and GitHub credentials. Make sure you have Write access to the repository.

## Community Guidelines

- **Be respectful** - this is a shared creative space
- **No spam** - don't create excessive empty files or folders
- **Report issues** - if you see problems, contact the admin

## Guardian Protection System

The Foundry uses a two-tier protection system to ensure both player content and the enforcement infrastructure remain secure:

### Tier 1: Enforcement Pipeline (Player Content)
- Runs on every push to `main`
- Validates file ownership for player content
- Reverts unauthorized edits to player files
- Excludes `.github/` folder (protected by Guardian)

### Tier 2: Guardian Workflow (Infrastructure Protection)
- Runs every 15 minutes from a protected branch (`protected-workflows`)
- Protects the enforcement system itself from tampering
- If workflows are compromised, searches git history to find last known good state
- Restores entire repository to that state (maximum 15-minute vulnerability window)

**Why Guardian is needed:** Without it, an attacker could delete the enforcement workflows, then delete/modify any content they want. Guardian ensures that even if workflows are compromised, everything gets restored automatically.

**How it works:**
1. Guardian runs from `protected-workflows` branch (players cannot modify this branch)
2. Every 15 minutes, checks if `.github/` files are intact
3. If compromised, finds the last commit where workflows were correct
4. Restores all files (except `.github/`) from that commit
5. Commits restoration and pushes to main

For complete Guardian documentation, see the `protected-workflows` branch README.

## Technical Architecture

For developers and the technically curious:

- **Version Control:** Git/GitHub
- **Automation:** GitHub Actions (two workflows: enforcement + guardian)
- **Enforcement Script:** Python with PyYAML
- **Sync Tool:** FIT plugin for Obsidian
- **Game System:** Iron Vault plugin for Obsidian
- **Protection:** Two-tier system (enforcement pipeline + guardian workflow)

## Contributing

Want to improve The Foundry itself (not just add campaign content)?

1. Fork the repository
2. Create a feature branch
3. Make your changes to the enforcement scripts or documentation
4. Submit a pull request

Changes to the core system require admin approval.

## License

See [LICENSE](LICENSE) for details.

## Questions?

Contact the repository admin: [@nickarrow](https://github.com/nickarrow)

---

**Welcome to The Foundry. Your story awaits.**
