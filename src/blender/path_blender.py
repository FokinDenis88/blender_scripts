import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

#import blender_scripts.src.general as general
import blender_scripts.external.python_library.src.path_ext as path_ext

import importlib
#importlib.reload(general)
importlib.reload(path_ext)

##  // prefix is Blender specific to denote relative paths used within Blender
def abspath(path):
    return bpy.path.abspath(path)

## // prefix is Blender specific to denote relative paths used within Blender
def relpath(path):
    return bpy.path.relpath(path)

def basename_abspath(path):
    return path_ext.basename_abspath(bpy.path.abspath(path))