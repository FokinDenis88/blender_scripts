import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import blender_scripts.src.blender.get_object as get_object
import blender_scripts.src.blender.object_name as object_name

import importlib
importlib.reload(get_object)
importlib.reload(object_name)


object_name.rename_material_by_object_names_selected()