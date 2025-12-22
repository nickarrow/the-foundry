# 3. Tips and Best Practices

## Organizing Your Content

**Use folders to keep things organized.** Since this vault contains multiple players' campaigns, a clear folder structure helps everyone navigate. Iron Vault helps by providing a folder scaffold, but you can create files and folders anywhere in the repository - there are no path restrictions. Feel free to organize your content however makes sense for your story.

## Collaborative Campaigns

**Join existing campaigns!** The Foundry shines when players contribute to each other's worlds:
- Create your character in someone else's campaign folder
- Write journal entries from your character's perspective
- Add locations, NPCs, or other content that enriches the shared world
- Remember: you can only edit files you create, but you can read everything

**Example:** If you want to join "The Starforged" campaign, create `The Starforged/Characters/YourCharacter.md` and start playing. The campaign creator can read your content but can't edit it, and vice versa.

**Practice "Yes, and..." in your writing.** The Foundry protects files technically, but collaborative storytelling requires narrative respect too:
- Write about others' creations as living, ongoing stories - not concluded ones
- Use rumors, observations, and your character's perspective rather than definitive statements about others' content
- If your story *needs* something dramatic to happen to shared content, reach out to the creator first
- Remember: your files are yours, other's files are theirs, but the universe is everyone's

## Naming Conventions
- Use descriptive folder and file names
- Avoid special characters that might cause issues across platforms
- Hyphens or underscaces work great (e.g., `My-Character.md` or `My_Character.md`)
- Spaces are fine too, but some players prefer hyphens for consistency

## Recommended Plugins

Beyond the required plugins (Iron Vault and FIT), consider installing these optional plugins to enhance your experience:

**Required:**
- `Iron Vault` - For playing Ironsworn, Starforged, or Sundered Isles (you need this!)
- `FIT` - For syncing with GitHub (you need this too!)

**Optional but useful:**
- `Dataview` - Create fancy character sheets and dynamic queries
- `Excalidraw` - Draw maps, diagrams, and visual content

## Syncing Best Practices

**Use "remind" mode for the safest experience.** FIT can sync automatically, but there's a catch: if you're actively writing when a sync triggers, you might get a conflict. This happens because FIT reads your files, syncs them, then updates its cache - but if you edited a file during that 1-2 second window, the timing can get confused.

**Recommended FIT settings for writers:**
- Set `Auto sync` to `Remind` instead of `On`
- Set `Check every X minutes` to 5-10 minutes
- When you see "Remote update detected", finish your current thought, then click the GitHub icon to sync manually

This way you're always in control of when syncs happen, and you won't lose work mid-sentence.

**If you prefer auto-sync anyway:**
- Watch for the spinning GitHub icon - that means a sync is running
- If you do get a conflict, don't panic - your local work is always preserved

**Understanding the `_fit/` folder:** When FIT detects a conflict (same file changed both locally and remotely), it saves the remote version to `_fit/your-file.md` and keeps your local version in place. You can then manually compare and merge if needed. Feel free to delete files from `_fit/` once you've resolved them.

**If your edits disappear:** This means you tried to edit a file you don't own. The Foundry automatically restored it. Create your own file instead!

## Getting Help
- Check the README.md for detailed technical information
- Visit [Ironvault.Quest](https://ironvault.quest/) for Iron Vault tutorials
- Contact nickarrow if you have questions or issues
- Join the [Ironsworn Discord](https://discord.gg/8bRuZwK) for community support

## Common Questions

**Can I rename or move my files?**
Yes! You own your files, so you can rename, move, or delete them freely.

**Can I delete someone else's file?**
No. The Foundry will automatically restore it.

**What if I accidentally edit someone else's file?**
No worries! The Foundry will silently restore it on the next sync. No harm done.

**Can multiple people edit the same file?**
No. Each file has exactly one owner. For collaborative content, create separate files that reference each other.

**How do I know who owns a file?**
If you created the file, you own it. If you didn't create it, you don't. But if you really want to see the whole file registry, you can view it here [registry.yml](https://github.com/nickarrow/the-foundry-guardian/blob/main/registry.yml)
