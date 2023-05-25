import os
import sys
import re

import bpy

sys.path.append(r'C:\Development\Projects\IT\Programming\!it-projects\!best-projects')

#import blender_scripts.backface_culling as backface_culling

import importlib
#importlib.reload(backface_culling)

PREFIX_REGEX = '^[^_]+_'
SUFFIX_REGEX = '_[^_]+\\Z'

def get_prefix(text):
    match_object = re.search(PREFIX_REGEX, text)
    if match_object is not None:
        return match_object[0]
    else:
        return ''

def get_suffix(text):
    match_object = re.search(SUFFIX_REGEX, text)
    if match_object is not None:
        return match_object[0]
    else:
        return ''

def correct_suffix(suffix):
    if suffix == '_baseColor':
        return '_Diff'
    elif suffix == '_normal':
        return '_Normal'
    elif suffix == '_metallicRoughness':
        return '_MetalRough'
    elif suffix == '_emissive':
        return '_Emissive'
    else:
        return suffix

def pack_all_images():
    for image in bpy.data.images:
        try:
            image.pack()
        except:
            print(pack_all_images.__name__+ '(): ' + image.name + ' did not packed')

def unpack_all_images():
    for image in bpy.data.images:
        try:
            image.unpack()
        except:
            print(unpack_all_images.__name__+ '(): ' + image.name + ' did not unpacked')

# Corrects color space for node
def setup_node_color_space(node, suffix):
    if suffix == '_Diff':
        node.image.colorspace_settings.name = 'sRGB'
    elif suffix == '_Normal':
        node.image.colorspace_settings.name = 'Non-Color'
    elif suffix == '_MetalRough':
        node.image.colorspace_settings.name = 'Non-Color'
    elif suffix == '_Emissive':
        node.image.colorspace_settings.name = 'sRGB'


def resave_textures():
    for material in bpy.data.materials:
        textures_name_with_prefix = 'T_' + material.name.removeprefix('M_')
        #node_tree = material.node_tree
        if material.node_tree is not None:
            unpack_all_images()
            nodes = material.node_tree.nodes
            for node in nodes:
                if type(node) == bpy.types.ShaderNodeTexImage:
                    old_image_name_n_extension = node.image.name
                    texture_path_old = os.path.join(os.getcwd(), node.image.filepath[2:])
                    image_name_no_extension, image_extension = os.path.splitext(node.image.name)
                    suffix = get_suffix(image_name_no_extension)
                    suffix = correct_suffix(suffix)
                    new_texture_name = textures_name_with_prefix + suffix + image_extension
                    node.name = new_texture_name
                    node.label = new_texture_name

                    #texture_path_old = node.image.packed_files[0].filepath
                    textures_dir = os.path.dirname(texture_path_old)
                    texture_path_new = os.path.join(textures_dir, new_texture_name)
                    if os.path.exists(texture_path_old):    # Same OcclusionMetallicRoughness map can be renamed 2 times
                       os.rename(texture_path_old, texture_path_new)
                    new_image = bpy.data.images.load(texture_path_new)
                    node.image = new_image
                    setup_node_color_space(node, suffix)

                    # packed textures filepath: //textures\ammo_1_baseColor.jpeg
                    #node.image.filepath = os.path.join(os.path.dirname(node.image.filepath), new_texture_name)
                    #node.image.name = new_texture_name
                    #node.image.filepath = '//textures\\' + new_texture_name


#unpack_all_images()
#pack_all_images()
resave_textures()