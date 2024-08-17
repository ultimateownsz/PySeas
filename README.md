# PySeas - Open Source Pirate (Adventure) Board Game

[![Discord](https://discord.com/api/guilds/1272287320934056066/widget.png)](https://discord.gg/s2P9fZbeZs)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://www.freecodecamp.org/news/how-to-make-your-first-pull-request-on-github-3/)
[![License](https://img.shields.io/github/license/ultimateownsz/pyseas)](https://github.com/ultimateownsz/PySeas/blob/main/LICENSE)

## Project Description

Welcome to PySeas, an open-source project to create an exciting and engaging board game in Python, inspired by the popular game Sea of Thieves! This project is perfect for anyone interested in game development, Python programming, and creative collaboration.

## About the Project

PySeas {working title} a tiled based adventure game Python/Pygame-CE project. It is based on a former school project, a board game made in Python.

## Get notified about project updates
For organising the project we mainly use [Codecks](https://open.codecks.io/pyseas). Codecks is a management tool made for indie game developers, it is based on a card game and has a lot of similarities like Trello. The main thing what we liked about this is, we can show you how we make the game via open decks. Decks make it possible to share contens of any projects we are working on publicly on the web. You can create a account to get notified for updates or you can vote on cards.

### Discord server
We also made a dedicated [Discord](https://discord.gg/MZ5MHqDnGW) server where you can engage in conversations about how to improve, add or give feedback to the developers. It also has the option to construct a message to send to Codecks to directly see it on the deck what is being worked on or being fixed.

## Project Goals
- **Pygame version:** We aim to create a pygame version, everything we wanted to do in Python wasn't possible so we decided to remake the game in Pygame: bringing enhanced graphics and more dynamic interactions.

For all new goals we refer to see [Codecks](https://open.codecks.io/pyseas) to vote on cards with implementing features/goals. We also made improvements to give feedback within the [Discord](https://discord.gg/MZ5MHqDnGW) directly to Codecks..

### Goals for later
- **Refactor the Python version:** The project started out as an Python boardgame inspired by Sea of Thieves and is now changed to a bigger project and scope. We intend to first remake the game in Pygame first and later on refactor the game to Python's version too but with an ASCII look.
- **Unified Launcher:** Our final goal is to provide a Pygame-based launcher that offers players the option to choose between the Python version and the Pygame version of the game, making it easy to play either version from a single interface.
<img src="https://img.itch.zone/aW1nLzE1MDEzOTMwLmdpZg==/347x500/A%2BBsU5.gif" style="width: 150px; height: 150px;" />

## Why Join PySeas?

- Learn and improve your Python and Pygame skills through practical, hands-on development.
- Collaborate with a community of like-minded enthusiasts and contribute to a shared goal.
- Create something fun and engaging that others can enjoy and build upon.
- Explore the world of game development and design, gaining valuable experience along the way.
- Contributing to an open-source project can be a great addition to your resume or portfolio, showcasing your skills to potential employers or collaborators.
- As an open-source contributor, you have the opportunity to influence the development and future features of the game. Your ideas and feedback are valued and can directly impact the project.

Whether you're a seasoned developer or just starting, your contributions are valuable. Let's create an amazing board game together!

## How to Get Involved

This project requires Python 3.12 or above. Luckily you can set up a virtual machine to run the project with.

1. **Clone the Repository:** Start by cloning the PySeas repository from GitHub.
```
  git clone https://github.com/ultimateownsz/pyseas.git
```
2. **Set up a virtual machine:** 

   **Linux/MacOS**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
   **Windows**
    ```
    python -m venv venv
    venv\Scripts\activate
    ```

4. **Install dependencies:**
```
pip install -r requirements.txt # For running the game (runtime dependencies)
pip install -r requirements_dev.txt # For local development
```
4. **Run this project:**
```
python main.py
```

## Local Development
**See how to contribute:** [contribute](./CONTRIBUTING.md)

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
