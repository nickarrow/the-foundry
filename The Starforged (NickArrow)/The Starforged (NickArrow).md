---
name: The Starforged (NickArrow)
ironvault:
  playset:
    type: globs
    lines:
      - "@include(starforged)"
      - asset:sundered_isles/** [starforged.recommended=true]
      - oracle_rollable:sundered_isles/misc**
      - oracle_rollable:sundered_isles/overland**
      - oracle_rollable:sundered_isles/weather**
      - oracle_rollable:sundered_isles/treasure**
      - "!oracle_rollable:sundered_isles/misc/local**"
  customContentFolder: Custom Content
iron-vault-kind: campaign

---

Welcome to your new campaign! This is a campaign index file, which marks its folder as a campaign. Any journals or game entities inside this folder will use this campaign for any mechanics or commands. You can replace all this text with any details or notes you have about your campaign. As long as the file properties remain the same, you don't have to worry about the contents of this file.
