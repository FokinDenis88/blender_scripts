import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.external.python_library.src.general as general
import blender_scripts.src.blender.get_object as get_object
import blender_scripts.src.blender.scale_material as scale_material

import importlib
importlib.reload(general)
importlib.reload(get_object)
importlib.reload(scale_material)


# '8k': (7680, 4320),
# '4k': (3840, 2160),
# '2k': (2048, 1080),
# '1k': (1024, 768)

#======================================Ini Section==================================================

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = SCREEN_WIDTH

#====================================================================================================


scale_material.create_scaled_materials_selected(SCREEN_WIDTH, SCREEN_HEIGHT)