import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.src.general as general
#import blender_scripts.src.python.prefix_suffix as prefix_suffix

import importlib
importlib.reload(general)
#importlib.reload(prefix_suffix)

## Corrects color space for node
def setup_node_color_space(node, suffix):
    if suffix == '_Diff':
        node.image.colorspace_settings.name = 'sRGB'
    elif suffix == '_Normal':
        node.image.colorspace_settings.name = 'Non-Color'
    elif suffix == '_MetalRough':
        node.image.colorspace_settings.name = 'Non-Color'
    elif suffix == '_Emissive':
        node.image.colorspace_settings.name = 'sRGB'
    else:   # Default
        node.image.colorspace_settings.name = 'sRGB'

## Loads new image to ShaderNodeTexImage node. Saves properties of node
def load_shader_node_tex_image_same_settings(node, new_texture_path):
    if node is not None:
        if general.is_not_none_or_empty(new_texture_path):
            if os.path.exists(new_texture_path):
                new_texture_name = os.path.basename(new_texture_path)
                node.name = new_texture_name
                node.label = new_texture_name
                old_colorspace_settings = node.image.colorspace_settings.name
                new_image = bpy.data.images.load(new_texture_path)
                node.image = new_image
                #suffix = prefix_suffix.get_suffix(os.path.splitext(new_texture_name)[0])
                node.image.colorspace_settings.name = old_colorspace_settings

            else:
                print(load_shader_node_tex_image_same_settings.__name__ + '(): there is no texture file with path ' + new_texture_path)
        else:
            print(load_shader_node_tex_image_same_settings.__name__ + '(): new_texture_path must not be None or Empty')
    else:
        print(load_shader_node_tex_image_same_settings.__name__ + '(): node must not be None')