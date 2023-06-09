import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import math

import bpy
import mathutils

import blender_scripts.src.blender.transform as transform

import importlib
importlib.reload(transform)


#====================================Ini Section================================
ROWS_COUNT = 5

# Horizontal additional interval between columns. SizeOfMaxObject + Indent. In meters.
HORIZONTAL_INDENT = 0.0
# Vertical additional interval between rows. SizeOfMaxObject + Indent. In meters.
VERTICAL_INDENT = 0.0

# The Point, from which all object will be relocated
START_POINT = mathutils.Vector(( 0.0, 0.0, 0.0 ))

IS_HORIZONTAL_PLANE = False

# Models will form Square after replacement
IS_SQUARE = True

USE_MINIMAL_INDENT = True

#===============================================================================


transform.translate_to_interval_selected(START_POINT, ROWS_COUNT, HORIZONTAL_INDENT, VERTICAL_INDENT,
                                         IS_HORIZONTAL_PLANE, IS_SQUARE, USE_MINIMAL_INDENT)