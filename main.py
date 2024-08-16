"""Project Name: PySeas
Description: PySeas is an open-source project to create an engaging board game in Python,
inspired by Sea of Thieves. Ideal for game development enthusiasts and Python programmers
Author(s): Danilo Saiu (https://www.github.com/ultimateownsz),
Davit Alsemgeest (https://www.github.com/davidek523)
Date: 2024-09-08

Python Version: 1.0.0
Pygame Version: 0.0.1"""

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


# import Python specific objects, functions and functionality
from src.CLI.gameloop import CLI

# import Pygame specific objects, functions and functionality
from src.GUI.gameloop import GUI


# I moved the two classes CLI and GUi to their own folders. I called them gameloop.py in both of these folders, for naming conventions I think It's better to name them differently.
class Launcher:
    """ I have now created the launcher from the terminal. This is a basic version of the launcher, we could add options """
    print(
        """
          Welcome to Pyseas!
          Please select a version to play:
          1. CLI version
          2. GUI version"""
    )
    choice: str = input("Enter the number of your choice: ")
    while choice not in ['1', '2']:
        choice = input("Enter the number of your choice: ")

    if choice == "1":
        CLI().run()
    elif choice == "2":
        GUI().run()


if __name__ == "__main__":
    start_game = Launcher()
