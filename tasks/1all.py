import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

## Setting backface_culling and M_ prefix to material on all selected objects

import blender_scripts.tasks.backface_culling as backface_culling
import blender_scripts.tasks.set_material_prefix as set_material_prefix
#import blender_scripts.standardize_names as standardize_names

import importlib
importlib.reload(backface_culling)
importlib.reload(set_material_prefix)
#importlib.reload(standardize_names)