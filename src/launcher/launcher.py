"""THIS HAS A LOW PRIORITY"""

# import pygame
# import sys
# import os
# import subprocess

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# # from pygame_version import


# def start():
#     pygame.init()
#     screen = pygame.display.set_mode((640, 480))
#     pygame.display.set_caption('Game Launcher')
#     font = pygame.font.Font(None, 36)

#     option_python = font.render('1: Start the Python version', True, (255, 255, 255))
#     option_pygame = font.render('2: Start the Pygame version', True, (255, 255, 255))

#     running = True
#     while running:
#         screen.fill((0, 0, 0))
#         screen.blit(option_python, (50, 100))
#         screen.blit(option_pygame, (50, 200))
#         pygame.display.flip()

#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_1:
#                         # print("Key '1' is pressed")
#                         run_py_version()
#                     elif event.key == pygame.K_2:
#                         # print("Key '2' is pressed")
#                         run_pygame_version()
#                     elif event.key == pygame.K_ESCAPE:
#                         running = False
#     pygame.quit()

#     def run_py_version():
#         py_executable = sys.executable
#         script_path = os.path.join(os.path.dirname(__file__), '..', 'py_version')
#         subprocess.run[py_executable, script_path]

#     def run_pygame_version():
#         from pygame_version import game as pygame_game
#         pygame_game.run()
