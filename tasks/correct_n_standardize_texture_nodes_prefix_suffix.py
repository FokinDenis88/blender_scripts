import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.src.unreal.prefix_suffix_unreal as prefix_suffix_unreal

import importlib
importlib.reload(prefix_suffix_unreal)

# TODO: Needs to be tested
prefix_suffix_unreal.correct_n_standardize_texture_nodes_prefix_suffix_in_selected_materials()