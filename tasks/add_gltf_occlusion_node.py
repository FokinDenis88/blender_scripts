import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import blender_scripts.src.blender.get_object as get_object
import blender_scripts.src.blender.gltf_occlusion_node as gltf_occlusion_node

import importlib
importlib.reload(get_object)
importlib.reload(gltf_occlusion_node)


gltf_occlusion_node.add_occlusion_gltf_Settings_group_in_materials_selected(materials)