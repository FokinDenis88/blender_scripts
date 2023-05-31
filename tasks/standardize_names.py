import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.src.blender.object_name as object_name

import importlib
importlib.reload(object_name)


object_name.standardize_selected_names(to_delete_space = False)