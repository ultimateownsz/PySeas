<!--
REMINDER:
- Complete all sections labeled as (MUST).
- Use the checkboxes to ensure all necessary tasks are completed before submitting.
- (FOR REVIEWERS) ~ Review the "Code Review Checklist" to confirm everything is ready for merging.
-->

# Pull Request Template

---

## Types of Changes (MUST)
<!--
INSTRUCTIONS:
- Select all the types of changes that apply to this pull request.
- Use "Breaking change" for changes that modify or remove existing functionality.
-->
**Tip**: Check all applicable types of changes:

### Code Changes
- [ ] 🛠️ Code optimization/refactoring
- [ ] 🐛 Bug fix (fixes an existing issue)
- [ ] ✨ New feature (adds functionality)

### Visual/Gameplay Changes
- [ ] 🎨 Visual improvement (e.g., sprites, UI updates)
- [ ] 🎮 Gameplay improvement (e.g., mechanics, level design)
- [ ] 🎵 Music/audio update (e.g., new background music, sound effects)
- [ ] 🎨 Asset addition or update (e.g., sprites, textures, models)

### Other Changes
- [ ] 📝 Documentation update
- [ ] ⚠️ Breaking change (modifies existing functionality)

---

## Summary of Changes (MUST)
<!-- 
INSTRUCTIONS:
- Briefly describe the purpose of this pull request. 
- Mention any related issue numbers (e.g., "Fixes #123").
- Explain what the PR implements, enhances, or fixes.
-->

**Summary**: _(e.g., "This PR adds a new level to the game with dynamic enemies.")_

**Related Issues**: _(e.g., Fixes #123, Closes #456)_

---

## Pull Request Checklist [FOR PULL REQUESTER]
<!-- 
INSTRUCTIONS (FOR PULL REQUESTER):
- Check each box to confirm you have completed these steps before submitting your pull request.
- This checklist ensures the quality and readiness of the pull request for review.
-->
**Tip**: Use this checklist to confirm you’ve completed all essential steps before submission:

### General
- [ ] ✅ I have tested my code, and it works as expected (e.g., game runs without errors).
- [ ] 📝 The description clearly explains the changes made.
- [ ] 🔗 Any related issues are linked in the summary above. (optional)

### Code Quality
- [ ] 🔍 Code is reviewed for clarity and quality.
- [ ] 📖 Variables, functions, and methods are named clearly
- [ ] 🛡️ Error handling is implemented where applicable.

### Gameplay Testing
- [ ] 🎮 Gameplay features are tested for functionality.
- [ ] 🧪 Edge cases and player inputs have been verified.

### Assets (Visual & Audio)
- [ ] 🎨 Visual assets are properly integrated (e.g., sprite alignment, texture quality).
- [ ] 🎵 Audio/music assets are tested (e.g., volume levels, correct triggers).

### Conventional Commits
- [ ] 📝 All commits follow the [Conventional Commits format](https://www.conventionalcommits.org/):
  - `<type>(<scope>): <description>`
  - Example:
    ```plaintext
    feat(level): add new enemy AI
    fix(sprite): resolve texture alignment issue
    docs(readme): update contributing guidelines
    ```

---

## Code Reviewer Checklist [FOR REVIEWERS ONLY]
<!-- 
INSTRUCTIONS FOR REVIEWERS:
- Use this checklist to ensure the pull request meets quality standards.
-->
**Tip**: Use this checklist to confirm the code is ready to merge:

### Code Quality
- [ ] 📖 Code is easy to read and understand.
- [ ] 🧹 No unused or commented-out code remains.
- [ ] 💬 Relevant comments are added for clarity.
- [ ] 🔤 Variables and functions are named clearly and consistently.

### Gameplay and Visuals
- [ ] 🎮 Gameplay is smooth, functional, and free of major bugs.
- [ ] 🎨 Visuals (e.g., sprites, UI) are consistent and fit the game's style.
- [ ] 🎵 Music/audio is functional, and volume levels are appropriate.
- [ ] 🎨 Visual assets are aligned and of high quality.

### Functionality
- [ ] 🧪 Tests (manual or automated) are included for key features. (optional)
- [ ] 🛡️ Errors are handled appropriately (e.g., player input validation). (optional)

### Commit Messages
- [ ] ✅ All commits follow the Conventional Commits format.

### Review Comments [IF APPLICABLE]
<!-- INSTRUCTIONS: - Use this section to provide feedback if any checklist items are not met. - Suggest alternatives or solutions where applicable. -->

**Explanation for any unchecked items:** _(e.g., "Tests for the new AI feature are missing. Please add them before merging.")_

---

## Final Review Checklist
<!--
INSTRUCTIONS:
- Use this checklist to confirm all necessary testing, documentation, and preparation for merging is complete.
-->

**Tip**: Confirm everything is complete and ready for merge:

### Gameplay Testing
- [ ] 🎮 All features have been tested in gameplay.

### Code Quality
- [ ] 📖 Code is reviewed and maintainable.
- [ ] 📝 Required documentation is updated.

### Commit Messages
- [ ] ✅ Commit messages follow the Conventional Commits format.

### Merge Readiness
- [ ] 🚀 This pull request is ready for merge.

