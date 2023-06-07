import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

#import blender_scripts.src.general as general
#import blender_scripts.src.blender.get_object as get_object
import blender_scripts.src.blender.base.shader_node as shader_node

import importlib
#importlib.reload(general)
#importlib.reload(get_object)
importlib.reload(shader_node)


## gltf Settings group is used for importing gltf texture Ambient Occlusion to Game Engines
def add_occlusion_gltf_Settings_group(material):
    if material is not None:
        node_group = shader_node.new_shader_node_in_material(material, bpy.types.ShaderNodeGroup)

    else:
        print(add_occlusion_gltf_Settings_group.__name__ + '() Error: material must not be None')
