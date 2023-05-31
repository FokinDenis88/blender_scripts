import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy


import blender_scripts.src.blender.object_name as object_name

import importlib
importlib.reload(object_name)

#set_prefix_to_selected_materials()
#set_prefix_to_all_materials()

object_name.delete_selected_objects_suffix('_low')