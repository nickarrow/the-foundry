# The Foundry

> A shared narrative universe for **Ironsworn**, **Starforged**, and **Sundered Isles** players

## What is The Foundry?

**The Foundry** is a collaborative storytelling repository where players using **Obsidian + Iron Vault** can:

- 📖 **Publish your campaigns** — Share your adventures with the community
- 🔍 **Explore others' stories** — Read the campaigns, characters, and journals around you
- 🤝 **Collaborate organically** — Add your character to someone else's campaign, write journal entries that interweave with theirs
- 🌍 **Build shared worlds** — Watch the universe grow as players contribute to each other's stories

All governance happens automatically through GitHub Actions — no manual permission management, no drama.

## How Ownership Works

Every file has exactly one owner — whoever created it. Simple.

**What you can do:**
- ✅ Create new files anywhere in the repository
- ✅ Edit, rename, move, or delete your own files
- ✅ Read everyone's files
- ❌ Edit or delete files owned by others

**What happens if you try to edit someone else's file?**

The Foundry silently restores it. Your next sync pulls the corrected version. No errors, no drama, just clean content.

## Getting Started

### Prerequisites
- [Obsidian](https://obsidian.md/)
- [GitHub account](https://github.com/)
- Repository access — contact [@nickarrow](https://github.com/nickarrow) or find me on the [Ironsworn Discord](https://discord.gg/8bRuZwK)

### Quick Setup
1. Create an empty Obsidian vault
2. Install the **FIT** plugin and configure it to sync with this repository
3. Install the **Iron Vault** plugin
4. Start creating!

For the full setup walkthrough, see [[2. Getting Started]].

## Start Playing

Once you're synced, you have two paths:

### Start Your Own Campaign
Use Iron Vault to create a new campaign in your own folder. You own everything you create.

### Join an Existing Campaign
Browse the campaigns in your vault. Create your character in someone else's folder. Write journal entries. You own your files, they own theirs, and the world grows organically.

## Community & Guidelines

The Foundry follows the community rules from the [Ironsworn Discord](https://discord.gg/8bRuZwK) and embraces the **"Yes, and..."** philosophy of collaborative storytelling.

For community guidelines and the collaborative philosophy, see [[1. Welcome to The Foundry]].

## Documentation

- [[1. Welcome to The Foundry]] — Community guidelines and collaborative philosophy
- [[2. Getting Started]] — Detailed setup walkthrough
- [[3. Tips and Best Practices]] — Helpful advice for playing
- [[4. Iron Vault Feature Wishlist and Bugs]] — Community feedback on Iron Vault

---

## For the Technically Curious

*Playing in The Foundry? You can stop here — everything above is all you need. The rest is for contributors and those curious about how the system works.*

### Technical Specification

For full technical details, see **[SPECIFICATION.md](.foundry/SPECIFICATION.md)**, which covers:
- Ownership model and registry system
- Enforcement pipeline
- Guardian protection system
- Edge cases and implementation details

### Architecture Overview
- **Version Control:** Git/GitHub
- **Automation:** GitHub Actions (enforcement pipeline + external Guardian)
- **Ownership Registry:** Centralized YAML with SHA-256 checksums
- **Sync Tool:** FIT plugin for Obsidian
- **Game System:** Iron Vault plugin for Obsidian

### Guardian Protection System

The Foundry uses a two-tier protection system:

1. **Enforcement Pipeline** — Runs on every push, validates ownership, reverts unauthorized edits
2. **External Guardian** — Runs every 15 minutes from a [separate private repository](https://github.com/nickarrow/the-foundry-guardian), protecting the enforcement infrastructure itself

Even if an attacker deletes all workflows, the Guardian restores everything within 15 minutes. Maximum vulnerability window: 15 minutes.

### Contributing

Want to improve The Foundry itself (not just add campaign content)?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Changes to the core system require admin approval.

### License

See [LICENSE](.foundry/.LICENSE) for details.

---

**Welcome to The Foundry. Forge your story.**
