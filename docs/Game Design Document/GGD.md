# Game Design Document

<div style="text-align: center;">
  <img src="Assets/Pygame%20CE%20logo.png" alt="PySeas" width="600">
</div>

## Game Summary Pitch

Pyseas is an opensource project that aims to create a 2D, top down, turn based board game in Pygame. Where players become pirates and control their own ship. Using a card-based dice system, players explore a dynamic map, complete quests, and battle rival pirates

---

## Table of Contents
- [Game Design Document](#game-design-document)
  - [Game Summary Pitch](#game-summary-pitch)
  - [Table of Contents](#table-of-contents)
  - [Inspiration](#inspiration)
    - [Sea of Thieves](#sea-of-thieves)
    - [Pillars of Eternity 2: Dead Fire](#pillars-of-eternity-2-dead-fire)
    - [Slay the Spire](#slay-the-spire)
  - [Player Experience](#player-experience)
    - [Platform](#platform)
    - [Development Software](#development-software)
      - [Optional Development Software](#optional-development-software)
    - [Genre](#genre)
    - [Target Audience](#target-audience)
  - [Concept](#concept)
    - [Gameplay Overview](#gameplay-overview)
    - [Theme Interpretation (Curse is Strenth)](#theme-interpretation-curse-is-strenth)
    - [Primary Mechanics](#primary-mechanics)
    - [Secondary Mechanics](#secondary-mechanics)
  - [Art](#art)
    - [Theme Interpretation](#theme-interpretation)
    - [Design](#design)
    - [Map Design](#map-design)
  - [Audio](#audio)
    - [Music](#music)
    - [Sound Effects](#sound-effects)
  - [Game Experience](#game-experience)
    - [User Interface (UI)](#user-interface-ui)
    - [Controls](#controls)
  - [Developent Timeline](#developent-timeline)
    - [GitHub Projects](#github-projects)
  - [Communication](#communication)
    - [Discord](#discord)

---

## Inspiration

### Sea of Thieves
Sea of Thieves is the main inspiration towards **immersion** and **exploration**. The game also focusses on competitive aspects in player versus player interactions.

### Pillars of Eternity 2: Dead Fire

As big fans of role-playing games, we enjoy how the **choices** you make can alter the **outcomes** of the game.

### Slay the Spire

In Slay the Spire we looked at **deck building** and how we could integrate this with a **dice system**. This can affect how much your range of possible rolls can be.

---

## Player Experience

In board game setting, **time** is a valuable resource. We aim to provide players with multiple options during their turn, allowing them to choose how they spend their time. Players can **explore** the map, encounter **world events**, complete **quests** or **board other player's ships**.

### Platform

The game will be developed in **Pygame-CE**. Our initial focus is on creating a working game loop, with plans to add **multiplayer** functionality, accessibility via **browser** and **local** connections, in future updates.

### Development Software

- Pygame-CE
- Tiled (map editor) for map creations

#### Optional Development Software
- Aseprite for graphics and UI
- LibreSprite

### Genre
- Singeplayer
- Multiplayer
- Tabletop boardgame
- Pirate adventure
- Role-playing-game

### Target Audience
- This game is designed for tabletop enthusiasts 
- It appeals to casual gamers 
- Suitable for ages 12 to 70 
- Ideal for players who enjoy adventure, role-playing and tabletop 
board games

---

## Concept

### Gameplay Overview

| ![Gameplay Overview](Assets/UI.png) | The player controls a **customizable ship** and rolls dice to move across the board. We aim to create a seamless **User Interface (UI)** that integrates the board with the player’s **own map/book**, similar to how the old Pokémon games used the ‘Pokédex’ to manage items, Pokémon, and view the map. |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Theme Interpretation (Curse is Strenth)

<div style="text-align: center;">
  <img src="Assets/Curses.png" alt="PySeas" width="1000">
</div>

Unlike in Sea of Thieves, where curses are purely cosmetic, we aim to 
use **curses** more like **status effects** found in role-playing games such 
as Pillars of Eternity 2. 

At the start of the game, the player must choose one of the available 
curses. Each curse influences how the player interacts with non-
playable characters, undertake quests, or uses the dice system.

---

### Primary Mechanics

| Mechanic              | Description                                                                | Animated mock-up<br>(Art not necessarily final)                 |
|-----------------------|----------------------------------------------------------------------------|----------------------------------|
| **Dice Roll**         | Players move based on the number rolled on the dice.                       | ![Dice Roll](Assets/dice_roll.gif) |
| **Virtual Book**      | A virtual book serves as inventory, quest log, and more.                   | ![Virtual book](Assets/Virtual%20book.gif)|
| **Free Movement**     | Players can move freely across the board during their turn.                | ![Free movement](Assets/Free%20movement.gif)|
| **Ship Upgrading**    | Each player begins the game with a starter ship, which can be upgraded to larger and more powerful vessels as the game progresses.<br><br>Upgraded ships offer various advantages, particularly withing the dice system, such as increased movement, better combat options, allowing players to tailor their ships to their preferred playstyle. | ![Ship upgrading 1](Assets/Ship%20upgrading%201.png) ![Ship upgrading 2](Assets/Ship%20upgrading%202.png) |


### Secondary Mechanics

| Mechanic              | Description                                                                | Animated mock-up<br>(Art not necessarily final)                                             |
|-----------------------|----------------------------------------------------------------------------|--------------------------------------------------------------|
| **Fog of War**        | Limits the player’s visibility on the map, adding an element of exploration and uncertainty, forcing players to strategically uncover new areas as they progress.                     | ![Fog of War](Assets/Fog%20of%20war.gif) |
| **Procedural Generation** | Ensures that the map layout changes with each playthrough, offering unique challenges and environments every time, which enhances replay-ability.                       | ![Procedural generation](Assets/Procedural%20generation.gif) |
| **World Events**      | World events can be triggered similarly to how encounters occur in the old Pokémon games when players interact with ‘tall grass’ or water areas. These events are dynamic and can happen as players explore certain areas of the map. exploration.                                | ![World events](Assets/World%20event.gif) |

---

## Art

---

### Theme Interpretation

The game will utilize **pixel art**, with assets from **Creative Commons** 
licenses. The art style will be vibrant and colorful, but certain gameplay 
elements can alter the color tones to reflect changes in the world map. 

As players interact with the **environment**, the colors may shift to 
indicate different moods, states, or reactions, enhancing the 
immersion and atmosphere

### Design

As an opensource project we adopt a **minimalistic** design approach, 
allowing the community to have significant input in shaping the overall 
design of the game.

This approach ensures **flexibility** and encourages 
**collaboration**, giving contributors the freedom to influence the game’s 
development and aesthetics.

### Map Design

For the project we’ve created a simple 100x100 tile-based map using 
Tiled, utilizing 16x16 pixel assets. This serves as the initial **starting point** for the game, providing a foundational layout for exploration and gameplay. As development progresses, this map can be expanded or modified based on gameplay needs and **community feedback**.

![Map starting point](Assets/Map.png)

---

## Audio

### Music

A dynamic and adaptive soundtrack will accompany players as they explore the map. The music will shift in tone and intensify depending on the player’s actions and the environment, from calm and mysterious melodies while exploring uncharted waters, to intense rhythms during 
combat.

### Sound Effects

To enhance the experience and add polish, a variety of environmental sound effects will provide feedback and depth to the player’s actions. These sounds will be integrated throughout the game, including when using the inventory, world map, menus, settings, and more.

---

## Game Experience

### User Interface (UI)

The User Interface (UI) is a central mechanic in the game, designed to track all aspects of the player’s progress, including the quest log, items storage, and other key elements. The UI will be easy to use and accessible, providing players with a clear view of their in-game 
activities and resources.

### Controls

**Mouse:**
- Left click: primary interaction method for navigating the UI and 
interacting with game elements.

**Keyboard:**
- Special keys: for interacting with the map, accessing the inventory 
or instantly focusing on the player. 

---

## Developent Timeline

### GitHub Projects

We aim to use Github projects to manage the development timeline and roadmap for the game future features, updates, and milestones. It will be organized and tracked through our [Project Task List](https://github.com/users/ultimateownsz/projects/15), with new features and tasks being created via issues. This approach allows for transparent progress tracking, collaborative development, and ensures that the  community can easily follow and contribute to the project.

---

## Communication

### Discord

For communication among contributors, we use our [Discord Server](https://discord.gg/MZ5MHqDnGW). This helps us to stay transparent with progress tracking, reporting on feedback and actively involve the community in the project.
