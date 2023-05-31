import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.src.general as general
#import blender_scripts.src.blender.get_object as get_object
import blender_scripts.src.python.prefix_suffix as prefix_suffix
import blender_scripts.src.unreal.prefix_suffix_unreal as prefix_suffix_unreal
import blender_scripts.src.blender.base.image as image
import blender_scripts.src.blender.base.shader_node as shader_node

import importlib
importlib.reload(general)
#importlib.reload(get_object)
importlib.reload(prefix_suffix)
importlib.reload(prefix_suffix_unreal)
importlib.reload(image)
importlib.reload(shader_node)


## Change basename of Texture. Basename = name of texture without suffix
# @param old_texture_fullname_n_extension T_BaseName_Suffix + file_extension(f.e. .png)
# Fullname = prefix + basename + suffix + file_extension
def change_texture_basename_in_fullname(old_texture_fullname_n_extension, new_texture_basename):
    new_texture_fullname_n_extension = ''
    if general.is_not_none_or_empty(old_texture_fullname_n_extension):
        # old_image_name_no_extension = prefix + basename + suffix
        old_image_fullname_no_extension, old_image_extension = os.path.splitext(old_texture_fullname_n_extension)
        old_image_fullname_no_extension = prefix_suffix_unreal.correct_texture_prefix(old_image_fullname_no_extension)
        suffix = prefix_suffix.get_suffix(old_image_fullname_no_extension)
        #old_image_prefix_n_basename = old_image_fullname_no_extension[:-len(suffix)]
        suffix = prefix_suffix_unreal.correct_suffix(suffix)

        new_texture_fullname_n_extension = prefix_suffix_unreal.TEXTURE_PREFIX + new_texture_basename + suffix + old_image_extension

    else:
        print(change_texture_basename_in_fullname.__name__ + '(): old_image_name_n_extension must not be None or Empty')

    return new_texture_fullname_n_extension

## Resaves textures with conventional names. Base name depends on material name
def resave_textures():
    for material in bpy.data.materials:
        new_texture_basename = material.name.removeprefix('M_')
        if material.node_tree is not None:
            image.unpack_all_images()
            nodes = material.node_tree.nodes
            for node in nodes:
                if type(node) == bpy.types.ShaderNodeTexImage:
                    old_texture_name_n_extension = node.image.name
                    new_texture_name_n_extension = change_texture_basename_in_fullname(old_texture_name_n_extension, new_texture_basename)

                    texture_path_old = image.get_packed_image_absolute_path(node.image)
                    textures_dir = os.path.dirname(texture_path_old)
                    texture_path_new = os.path.join(textures_dir, new_texture_name_n_extension)
                    if os.path.exists(texture_path_old):    # Same OcclusionMetallicRoughness map can be renamed 2 times
                       os.rename(texture_path_old, texture_path_new)

                    shader_node.load_shader_node_tex_image_same_settings(node, texture_path_new)