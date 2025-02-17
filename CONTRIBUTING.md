# Contributing to PyCeas
Thank you for taking the time to contribute! All types of contributions are encouraged and valued. This project started from a passion for Sea of Thieves, inspired by its seafearing spirit.

> If you like the project, but just don't have time to contribute, that's fine. You could help us out to show support and appreciation of the project by:
> - 🌟 Starring the project
> - 🗣️ Sharing it on social media or at meetups.
> - 📄 Mention the project in your own repositories or documentation.

---

## Table of Contents
- [Contributing to PyCeas](#contributing-to-pyceas)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [I Want To Contribute](#i-want-to-contribute)
  - [How We Handle Issues](#how-we-handle-issues)
    - [User Story-Based Issues](#user-story-based-issues)
  - [Reporting Bugs](#reporting-bugs)
    - [Steps for a Good Bug Report](#steps-for-a-good-bug-report)
    - [Visual Proof](#visual-proof)
    - [Suggesting Enhancements](#suggesting-enhancements)
      - [Before Submitting an Enhancement](#before-submitting-an-enhancement)
    - [Steps for a Good Enhancement Suggestion](#steps-for-a-good-enhancement-suggestion)
    - [Proposing Ideas or Tasks (Contributor Guide)](#proposing-ideas-or-tasks-contributor-guide)
    - [For Your First Code Contribution](#for-your-first-code-contribution)
    - [Improving The Documentation](#improving-the-documentation)
    - [Pull Request Process](#pull-request-process)
    - [Commit Messages with Conventional Commits](#commit-messages-with-conventional-commits)
  - [A commit message example](#a-commit-message-example)
  - [Common Commit Types](#common-commit-types)
  - [Example Workflow](#example-workflow)
    - [Linting and Formatting](#linting-and-formatting)

## Code of Conduct
Please note we have a code of conduct, please follow it in all your interactions with the project.
[Go to code of conduct](https://github.com/PyCeas/Pyceas/blob/main/CODE_OF_CONDUCT.md)

---

## I Want To Contribute

> ### Legal Notice 
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project [license](https://github.com/PyCeas/Pyceas?tab=AGPL-3.0-1-ov-file#readme).
> Tip: If you use assets with a [creative commons license](https://creativecommons.org/licenses/by/4.0/deed.en) you can use it without any legal issues.
> We keep a list of all the assets, software etc in this [file](./CREDITS.md).

---

## How We Handle Issues

We use specific templates to ensure issues and tasks are well-structured and easy to collaborate on.

### User Story-Based Issues

We use **user stories** to break down complex features into manageable tasks. Each issue can include multiple user stories, which may be converted into separate issues for collaboration.

- **What is a User Story?**
  A user story describes the functionality from the user's perspective.  
  Example:  
  > As a player, I want to see seamless transitions between the main menu and the game map so that my experience feels smooth and uninterrupted.

- **How Do We Use User Stories?**
  Each user story includes:
  - A clear description of the user's goal.
  - A list of tasks required to implement the story.
  - Guidance for contributors (e.g., file references, related issues).

Check out our **[User Story-Based Template](https://github.com/PyCeas/.github/blob/main/.github/ISSUE_TEMPLATE/user_story_based_issue.md)** for detailed guidance.

---

## Reporting Bugs

### Steps for a Good Bug Report

1. **Check if you are using the latest version** of PyCeas.
2. Gather the following information:
    - OS, Python version, and project version.
    - Steps to reproduce the bug.
    - Any error messages or screenshots.
3. Submit the bug using our **[Bug Report Template](https://github.com/PyCeas/.github/blob/main/.github/ISSUE_TEMPLATE/bug_report.yml)** 

### Visual Proof

For bugs that are hard to explain, a short GIF or video is incredibly helpful. We recommend using:

- **[LICEcap](https://www.cockos.com/licecap/):** A free tool for Windows and macOS to create GIFs of your screen.
- **[Peek](https://github.com/phw/peek):** A Linux-friendly alternative.

Please attach the GIF or video to your bug report!

> **IMPORTANT:** Do not report security vulnerabilities here.  
> Please email sensitive issues to [PySeasproject@proton.me](mailto:PySeasproject@proton.me).
> We use **ProtonMail**, a secure, privacy-focues email provider, to handle all security communications. Your messages are encryped in transit for added privacy.
> The email may still be seen as PySeas, this is not misspelled, this was made before we changed our project's name, will change in the future!

---

### Suggesting Enhancements

We welcome your ideas to improve PyCeas! Whether it's a completely new feature or minor improvement, your contributions help shape the project. Follow these steps to submit an enhancement suggestion:

Ready to propose an enhancement? Use the **[Enhancement Template](https://github.com/PyCeas/.github/blob/main/.github/ISSUE_TEMPLATE/enhancement.md)**

#### Before Submitting an Enhancement

### Steps for a Good Enhancement Suggestion

1. Check the **[Documentation](https://github.com/PyCeas/Pyceas/tree/main/docs)** to ensure the feature doesn't already exist.
2. Search for similar suggestions in **[Issues](https://github.com/PyCeas/Pyceas/issues)**.

Enhancement suggestions should include:
- A **clear and descriptive title**.
- A **step-by-step description** of the proposed feature or improvement.
- An explanation of **why this enhancement is useful**.
- Screenshots or GIFs if applicable (see the **[Visual Proof](#visual-proof)** section for tools).

---

### Proposing Ideas or Tasks (Contributor Guide)

If you're new or have an idea for the project, use our **[Contributor Guide Template](https://github.com/PyCeas/.github/blob/main/.github/ISSUE_TEMPLATE/contributor_guide.md)** to structure your proposal.

This template helps you:
- Describe your idea or task.
- Get feedback from maintainers.
- Understand next steps to get started.

> **Example:**
> If you're proposing a feature for the map, you can describe how it improves the player experience and outline basic steps to implement it.

---

### For Your First Code Contribution

1. Look for **[Good First Issues](https://github.com/PyCeas/Pyceas/labels/good%20first%20issue)**.
2. Fork the repository and clone it locally.
3. Work on your changes in a new branch.
4. Submit a pull request when you're ready.

---

### Improving The Documentation
You can find our Game Design Document (GGD) [here](./docs/PyCeas%20Game%20Design%20Document.pdf).

For improvements you can:
- Create a *New issue* on [Issues](https://github.com/PyCeas/Pyceas/issues)
- Reach out to us on [Discord](https://discord.gg/MZ5MHqDnGW)

---

### Pull Request Process
**Working on your first Pull Request?** You can learn how from this free series **[How to Contribute to an Open Source Project on GitHub](https://www.freecodecamp.org/news/how-to-contribute-to-open-source-projects-beginners-guide/)**

---

### Commit Messages with Conventional Commits

Using consistent commit messages helps maintainers and contributors quickly understand the purpose of each change, manage the project more effectively, and collaborate better. This guide will show you how to write clear, meaningful commit messages using the **[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)** format.

## A commit message example

A commit message is structured like this:


| Component        | Example                      | Description                                             |
|------------------|------------------------------|---------------------------------------------------------|
| **type**         | `feat`                       | The type of change (feature, bug fix, etc.).            |
| **scope**        | `map`                        | (Optional) The part of the project affected.            |
| **description**  | `add player location markers`| A concise explanation of what the commit does.          |

---

## Common Commit Types

| Type       | Description                               | Example                                    |
|------------|-------------------------------------------|--------------------------------------------|
| `feat`     | A new feature                             | `feat(map): add player location markers`   |
| `fix`      | A bug fix                                 | `fix(api): resolve stats calculation bug`  |
| `docs`     | Documentation-only changes               | `docs(readme): update contributing section`|
| `style`    | Code style changes (e.g., formatting)    | `style(ui): adjust button alignment`       |
| `refactor` | Code changes that neither fix bugs nor add features | `refactor(ui): simplify navigation logic` |
| `test`     | Adding or updating tests                 | `test(map): add unit tests for markers`    |
| `chore`    | Maintenance tasks                        | `chore(deps): update dependency versions`  |

---

## Example Workflow

Suppose you're adding a new feature to the game map. Your workflow might look like this:

1. Make changes to the code.
   - Edit the code to implement your changes
2. Stage your changes:
   - Use the following command to stage all modified files:
   ```sh
   git add .
   ```
3. Write a Commit Message:
   - Use this command to commit your changes:
  ```sh
  git commit -m "<type>(<scope>): <description>"
  ```
  - Example:
  ```sh
  git commit -m "feat(map): add player location markers"
  ```
  - Best Practices:
    - Write the commit as a command:
     ```plaintext
     add player location markers
     ```
     Instead of:
     ```plaintext
     added player location markers
     ```
    - Link issues related to your change:
    ```plaintext
    fix(map) resolve marker alignment issue
    Closes #123
    ```
4. Push your Changes:
  ```sh
  git push
  ```

---

### Linting and Formatting
We chose to use [Ruff](https://docs.astral.sh/ruff/) to automatically lint and format the code. `Run pip install -r requirements_dev.txt` to install Ruff and other relevant dependencies.

> [!IMPORTANT]
> **Before you open a Pull Request, please run this bash commands to format your code properly and doesn't upset our linter:**
>
> 
> ```sh
> ruff format . && ruff check --include I --fix . # this formats code and sort imports
> ruff check . # run linting and perform fixes
> mypy main.py
> ```
>
> **If you use powershell, run these commands:**
>
> ```powershell
> ruff format .;
> ruff check --include I --fix .;
> ruff check .;
> mypy main.py
> ```
