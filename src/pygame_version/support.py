# import json
# import math
# import os
# import sys
# import random

# import pygame
# import pygame.gfxdraw
# import pytmx


# from src import settings


# def resource_path(relative_path: str):
#     """Get absolute path to resource, works for dev and for PyInstaller"""
#     relative_path = relative_path.replace("/", os.sep)
#     try:
#         base_path = sys._MEIPASS
#     except AttributeError:
#         base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
#     return os.path.join(base_path, relative_path)


# def tmx_importer(tmx_path: str) -> settings.MapDict:
#     files = {}
#     for folder_path, _, file_names in os.walk(resource_path(tmx_path)):
#         for file_name in file_names:
#             full_path = os.path.join(folder_path, file_name)
#             files[file_name.split('.')[0]] = (
#                 pytmx.util_pygame.load_pygame(full_path)
#             )
#     return files
