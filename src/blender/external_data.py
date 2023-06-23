import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

#import blender_scripts.external.python_library.src.general as general
#import blender_scripts.src.blender.get_object as get_object

import importlib
#importlib.reload(general)
#importlib.reload(get_object)


# https://blender.stackexchange.com/questions/12152/absolute-path-of-files-in-blender-with-python
#bpy.context.user_preferences.filepaths.use_relative_paths = False
#bpy.ops.wm.save_as_mainfile(filepath = YourNewFilePath, relative_remap = False)