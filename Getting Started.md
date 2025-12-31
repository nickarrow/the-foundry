# Getting Started

Let's get you set up and playing.

## Prerequisites

- **Obsidian** — [Download here](https://obsidian.md/)
- **GitHub account** — [Sign up here](https://github.com/) (free)
- **Repository access** — contact **@nickarrow** on the [Ironsworn Discord](https://discord.gg/8bRuZwK) to be added as a collaborator

## Setup Instructions
### Step 1: Create an Empty Vault

1. Open Obsidian
2. Click "Create new vault"
3. Name it whatever you like ("The Foundry" works)
4. Pick a location to save it

**Important:** Keep this vault empty for now. Don't add files or install other plugins yet.

### Step 2: Create a GitHub Personal Access Token

1. Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token" → "Generate new token (classic)"
3. Name it something like "The Foundry - FIT Plugin"
4. Set expiration (90 days or 1 year recommended)
5. Select the `repo` scope (Full control of private repositories)
6. Click "Generate token"
7. **Copy the token immediately** — you won't see it again

### Step 3: Install and Configure FIT Plugin

FIT (Minimalist File giT) handles syncing your vault with GitHub.

1. Go to Settings → Community Plugins
2. Browse and install **FIT**
3. Enable the plugin
4. Open FIT settings
5. Paste your personal access token
6. Click "Authenticate" — your username and repositories will auto-populate
7. Select **"the-foundry"** from the repository dropdown
8. Select **"main"** from the branch dropdown
9. Set Auto sync to "Remind Only" <-- IMPORTANT to avoid syncing conflicts

### Step 4: Initial Sync

Once FIT is configured, trigger the initial sync. FIT will automatically pull everyone's campaigns, characters, journals, and other content into your vault. This is normal - you're now part of a shared storytelling universe!

### Step 5: Install Iron Vault Plugin

1. Go to Settings → Community Plugins
2. Browse and install **Iron Vault**
3. Enable the plugin
4. Configure for your preferred game system (Ironsworn, Starforged, or Sundered Isles)

## Start Playing

You have two paths:

### Option A: Start Your Own Campaign

Use Iron Vault to create a new campaign. You'll end up with something like:

```
My-Campaign/
├── Characters/
│   └── My-Hero.md
├── Journals/
│   └── Session-1.md
└── Campaign-Index.md
```

FIT syncs your files to GitHub, and The Foundry marks you as the owner.

### Option B: Join an Existing Campaign

This is where The Foundry shines:

1. Browse the the existing campaigns of others in your vault
2. Create a character in their folder, for example: `The Starforged/Characters/YourCharacter.md`
3. Write journal entries: `The Starforged/Journals/YourJournal.md`
4. Start playing

You own your files. They own theirs. The world grows organically.

## What Happens Behind the Scenes

When you sync:
- New files get added to The Foundry's ownership registry with you as the owner
- You can freely edit your own files
- If you accidentally edit or delete someone else's file, it gets silently restored on your next sync

You don't need to think about any of this — it just works.

## Next Steps

- Check out [[Tips and Best Practices]]
- Explore existing campaigns to see what others are creating
- Visit [Ironvault.Quest](https://ironvault.quest/player's-guide/getting-started/04-create-your-character.html) for Iron Vault tutorials

## Troubleshooting

**My edits disappeared!**
You edited a file you don't own. The Foundry restored it. Create your own file instead.

**FIT isn't syncing**
Check your FIT configuration and GitHub credentials. Make sure you have Write access to the repository.

**Sync conflicts**
Pull the latest changes first, then make your edits and push. The enforcement system handles the rest.

