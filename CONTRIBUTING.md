# Contributing to PySeas
Thank you for taking the time to contribute! All types of contributions are encouraged and valued. This project started from a passion for Sea of Thieves, inspired by its seafearing spirit.

> If you like the project, but just don't have time to contribute, that's fine. You could help us out to show support and appreciation of the project by:
> - Star the project
> - Share about it on your socials
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/collagues

## Table of Contents
- [Code of Conduct]([#code-of-conduct](https://github.com/ultimateownsz/PySeas?tab=coc-ov-file#readme))
- [I Want To Contribute](#i-want-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Your First Code Contribution](#your-first-code-contribution)
- [Improving The Documentation](#improving-the-documentation)
- [Pull Request Process](#pull-request-process)
- [Pull Request Template](#pull-request-template)

## Code of Conduct
Please note we have a code of conduct, please follow it in all your interactions with the project.
[Go to code of conduct](https://github.com/ultimateownsz/PySeas/blob/main/CODE_OF_CONDUCT.md)

## I Want To Contribute

> ### Legal Notice 
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project [license](https://github.com/ultimateownsz/PySeas?tab=AGPL-3.0-1-ov-file#readme).
> Tip: If you use assets with a [creative commons license](https://creativecommons.org/licenses/by/4.0/deed.en) you can use it without any legal issues.
> We keep a list of all the assets, software etc in this [file](./CREDITS.md).

### Reporting Bugs

#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
<!-- - Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](). If you are looking for support, you might want to check [this section](#i-have-a-question)). -->
<!-- - To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](issues?q=label%3Abug). -->
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older versions?

#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <>.

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/ultimateownsz/PySeas/issues). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for CONTRIBUTING.md, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://open.codecks.io/pyseas) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/ultimateownsz/PySeas/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.


#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/ultimateownsz/PySeas/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux. 
- **Explain why this enhancement would be useful** to most CONTRIBUTING.md users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

### Your First Code Contribution


### Improving The Documentation
You can find our Game Design Document (GGD) [here](./docs/Pyseas%20Game%20Design%20Document.pdf).

For improvements you can create a *New issue* on [Issues](https://github.com/ultimateownsz/PySeas/issues) or via our [Discord](https://discord.gg/MZ5MHqDnGW), if you have ideas to improve our documentation!

### Pull Request Process
**Working on your first Pull Request?** You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://www.freecodecamp.org/news/how-to-contribute-to-open-source-projects-beginners-guide/)


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


1. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
2. If you find issues in the code you can make a *New issue* on [Issues](https://github.com/ultimateownsz/PySeas/issues)
3. When making a Pull Request you may have to wait for the sign-off of a reviewer that approves your changes.

### Pull Request Template
- Title: Short one line title describing your idea/bug/feature.
- Description: Write a longer description of what the change does (if the title isn't enough).
- Explain: Give an explanation of why the change is being made.
- Discuss: Perhaps a discussion of context nd/or alternatives that were considered.
