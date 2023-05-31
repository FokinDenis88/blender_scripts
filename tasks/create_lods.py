import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.src.unreal.lod as lod

import importlib
importlib.reload(lod)


#============================Customizable Setup INI Parameters. Can be changed.==========================================

# Lods count in the model, after script finished
LODS_COUNT = lod.MAXIMUM_LODS_COUNT

# Target Start Modifier of LOD0, from which all following lods decimate modifier will be calculated
#decimate_modifier_name_ini = kDecimateModifierNameUnique
DECIMATE_MODIFIER_NAME_INI = DEFAULT_DECIMATE_MODIFIER_NAME

# How much percents of lod triangles count of previous lod level will stored in next level. next_lvl_count = previous_lvl_count * percents / 100
#                             [  0,    1,    2,    3,    4,    5,    6,    7]
PERCENT_TRIANGLES_REDUCTION = [0.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]

# If Mesh Data is Linked, all lods are not unique, but blend project file will be smaller
# There is no impact on space of asset in Unreal Engine or exported fbx file.
# There is impact only on size of .blend project
IS_MESH_DATA_LINKED = True

#========================================================================================================================

# Lods Number start From LOD0 end to LOD7
# Decimate Modifier name must be default: 'Decimate'

lod.create_lods(LODS_COUNT, DECIMATE_MODIFIER_NAME_INI, PERCENT_TRIANGLES_REDUCTION, IS_MESH_DATA_LINKED)