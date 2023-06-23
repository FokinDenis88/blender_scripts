import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import re

#import bpy


import blender_scripts.external.python_library.src.general as general
import blender_scripts.src.blender.get_object as get_object
import blender_scripts.src.blender.base.shader_node as shader_node
import blender_scripts.external.python_library.src.prefix_suffix as prefix_suffix
import blender_scripts.src.unreal.texture as texture
import blender_scripts.src.blender.base.image as image
import blender_scripts.src.unreal.naming_convention as convention

import importlib
importlib.reload(general)
importlib.reload(get_object)
importlib.reload(shader_node)
importlib.reload(prefix_suffix)
importlib.reload(texture)
importlib.reload(image)
importlib.reload(convention)


PREFIX_SUFFIX_SEPARATOR = '_'
TEXTURE_PREFIX = 'T_'
MATERIAL_PREFIX = 'M_'
NO_TEXTURE_TYPE = 'None'


## Finds if texture name with/without extension has texture prefix T_
def has_texture_name_correct_prefix(texture_file_name):
    if (general.is_not_none_or_empty(texture_file_name) and len(texture_file_name) > len(TEXTURE_PREFIX) and
        texture_file_name.startswith(TEXTURE_PREFIX)):
        return True
    else:
        return False

def add_material_prefix_to_materials(materials):
    if general.is_not_none_or_empty(materials):
        for material in materials:
            if not material.name.startswith(MATERIAL_PREFIX):
                material.name = MATERIAL_PREFIX + material.name

    else:
        print(add_material_prefix_to_materials.__name__ + '() Error: material must not be None')

def add_material_prefix_to_material(material):
    add_material_prefix_to_materials([material])

def add_material_prefix_to_selected():
    materials = get_object.get_selected_objects()
    add_material_prefix_to_materials(materials)

## Add M_ prefix to all materials in data
def add_material_prefix_to_all():
    materials = get_object.get_all_materials()
    add_material_prefix_to_materials(materials)


def get_texture_prefix_no_extension(texture_name_without_extension):
    if general.is_not_none_or_empty(texture_name_without_extension):
        prefix = prefix_suffix.get_prefix(texture_name_without_extension)
        if len(texture_name_without_extension) > len(prefix):
            return prefix
    else:
        print(get_texture_prefix_no_extension.__name__ + '() Error: texture_name_n_extension must not be Empty or None')
    return ''

def get_texture_prefix(texture_name_n_extension):
    if general.is_not_none_or_empty(texture_name_n_extension):
        return get_texture_prefix_no_extension(os.path.splitext()[0])
    else:
        print(get_texture_prefix.__name__ + '() Error: texture_name_n_extension must not be Empty or None')
    return ''


def get_texture_suffix_no_extension(texture_name_without_extension):
    if general.is_not_none_or_empty(texture_name_without_extension):
        prefix = get_texture_prefix_no_extension(texture_name_without_extension)
        suffix = prefix_suffix.get_suffix(texture_name_without_extension)
        if len(texture_name_without_extension) > (len(prefix) + len(suffix)):
            return suffix
    else:
        print(get_texture_suffix_no_extension.__name__ + '() Error: texture_name_without_extension must not be Empty or None')
    return ''

def get_texture_suffix(texture_name_n_extension):
    if general.is_not_none_or_empty(texture_name_n_extension):
        return get_texture_suffix_no_extension(os.path.splitext()[0])
    else:
        print(get_texture_suffix.__name__ + '() Error: texture_name_n_extension must not be Empty or None')
    return ''

def get_texture_name_without_prefix_suffix(texture_name_without_extension):
    if general.is_not_none_or_empty(texture_name_without_extension):
        prefix = get_texture_prefix_no_extension(texture_name_without_extension)
        suffix = prefix_suffix.get_suffix(texture_name_without_extension)
        if len(texture_name_without_extension) > (len(prefix) + len(suffix)):
            return texture_name_without_extension[len(prefix):-len(suffix)]
    else:
        print(get_texture_name_without_prefix_suffix.__name__ + '() Error: texture_name_without_extension must not be Empty or None')
    return ''


## @param texture_fullname Prefix_BaseName_Suffix.FileExtension
def get_prefixed_texture_name(texture_name_n_extension):
    if has_texture_name_correct_prefix(texture_name_n_extension):
        return texture_name_n_extension
    else:
        return TEXTURE_PREFIX + texture_name_n_extension

## @param texture_short_name (str) texture file name without extension
# @return (str) shortname_with_replaced_suffix + extension
def get_texture_shortname_with_replaced_suffix(texture_short_name, new_suffix):
    if general.is_not_none_or_empty_lists([texture_short_name, new_suffix]):
        suffix = get_texture_suffix_no_extension(texture_short_name)
        return texture_short_name[:-len(suffix)] + new_suffix
    else:
        print(get_texture_shortname_with_replaced_suffix.__name__ + '() Error: texture_name_n_extension, new_suffix must not be Empty or None')
        return texture_short_name

## @return (str) shortname_with_replaced_suffix + extension
def get_texture_fullname_with_replaced_suffix(texture_name_n_extension, new_suffix):
    if general.is_not_none_or_empty_lists([texture_name_n_extension, new_suffix]):
        texture_short_name, texture_extension = os.path.splitext(texture_name_n_extension)
        return get_texture_shortname_with_replaced_suffix(texture_short_name, new_suffix) + texture_extension
    else:
        print(get_texture_fullname_with_replaced_suffix.__name__ + '() Error: texture_name_n_extension, new_suffix must not be Empty or None')
        return texture_name_n_extension


## Change gltf Standard texture suffix to Custom Standard
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


## Reads prefix and suffix of texture asset and returns type of texture by convention
# Converts all text to lower case
def get_texture_type_by_prefix_suffix_in_shortname(texture_short_name):
    prefix = get_texture_prefix_no_extension(texture_short_name)
    suffix = get_texture_suffix_no_extension(texture_short_name)

    texture_types = convention.TextureTypesCustom
    texture_types_keys = list(convention.TextureTypesCustom.keys())
    is_type_found = False
    type_indx = 0
    key = ''
    while (not is_type_found) and type_indx < len(texture_types_keys):
        key = texture_types_keys[type_indx]
        if texture_types[key][0].casefold() == prefix.casefold():     # check prefix
            is_suffix_found = False
            suffix_indx = 0
            while (not is_suffix_found) and suffix_indx < len(texture_types[key][1]):
                if texture_types[key][1][suffix_indx].casefold() == suffix.casefold():    # check suffix in suffix list
                    is_type_found = True
                    is_suffix_found = True
                else:
                    suffix_indx +=1
        type_indx += 1

    if not is_type_found:
        key = NO_TEXTURE_TYPE
    return key

## Rename texture file name suffix to default variation.
# Default variation is zero in list of TextureTypesCustom suffixes
# F.e. From _BaseColor to _Diff
# @return texture_name_n_extension (str) full name with extension with standard suffix
def get_texture_name_with_standard_suffix(texture_name_n_extension):
    if general.is_not_none_or_empty(texture_name_n_extension):
        texture_short_name = os.path.splitext(texture_name_n_extension)[0]
        texture_type = get_texture_type_by_prefix_suffix_in_shortname(texture_short_name)
        if texture_type != NO_TEXTURE_TYPE:
            suffix = get_texture_suffix_no_extension(texture_short_name)
            standard_suffix = convention.get_TextureTypesCustom_standard_suffix(texture_type)
            if suffix != standard_suffix:
                return get_texture_fullname_with_replaced_suffix(texture_name_n_extension, standard_suffix)
        else:
            print(get_texture_name_with_standard_suffix.__name__ + '() Error: did not find texture type')
    else:
        print(get_texture_name_with_standard_suffix.__name__ + '() Error: texture_name_n_extension must not be Empty or None')

    return texture_name_n_extension

## If texture node has no prefix, add prefix T_.
# Standardize texture suffix to default 0 element in TextureTypesCustom suffixes
# Rename and Reload texture image file in node.
# Each texture_nodes list in texture_nodes_packs is associated with material in materials
# @texture_nodes_packs (shader_node) list of lists of shader nodes with texture image
def correct_n_standardize_texture_nodes_prefix_suffix_in_materials(materials, texture_nodes_packs):
    if general.is_not_none_or_empty_lists([materials, texture_nodes_packs]):
        if general.are_lists_equal_length([materials, texture_nodes_packs]):
            for i in range(len(materials)):
                material = materials[i]
                for texture_node in texture_nodes_packs[i]:
                    original_texture_name_n_extension = image.get_texture_node_file_name_n_extension(texture_node)
                    correct_texture_name_n_extension = get_prefixed_texture_name(original_texture_name_n_extension)
                    correct_texture_name_n_extension = get_texture_name_with_standard_suffix(correct_texture_name_n_extension)

                    texture.rename_n_reload_texture_in_node_in_same_dir(material, texture_node, correct_texture_name_n_extension)
                    print (original_texture_name_n_extension + ' -> ' + correct_texture_name_n_extension)

        else:
            print(correct_n_standardize_texture_nodes_prefix_suffix_in_materials.__name__ +
              '() Error: materials and texture_nodes_packs must be equal length')
    else:
        print(correct_n_standardize_texture_nodes_prefix_suffix_in_materials.__name__ +
              '() Error: materials and texture_nodes_packs must not be None or Empty')

## If texture node has no prefix, add prefix T_.
# Standardize texture suffix to default 0 element in TextureTypesCustom suffixes
# Rename and Reload texture image file in node.
# Each texture_nodes list in texture_nodes_packs is associated with material in materials
# @texture_nodes_pack (shader_node) list of shader nodes with texture image
def correct_n_standardize_texture_nodes_prefix_suffix_in_material(material, texture_nodes_pack):
    correct_n_standardize_texture_nodes_prefix_suffix_in_materials([material], [texture_nodes_pack])

## If texture node has no prefix, add prefix T_.
# Standardize texture suffix to default 0 element in TextureTypesCustom suffixes
# Rename and Reload texture image file in node.
# Each texture_nodes list in texture_nodes_packs is associated with material in materials
# @texture_nodes_pack (shader_node) list of shader nodes with texture image
# TODO: Needs to be tested
def correct_n_standardize_texture_nodes_prefix_suffix_in_selected_materials():
    selected_materials = get_object.get_selected_materials()
    if general.is_not_none_or_empty(selected_materials):
        texture_nodes_packs = []
        for material in selected_materials:
            texture_nodes_packs.append(shader_node.get_shader_nodes_texture_image_in_material(material))

        correct_n_standardize_texture_nodes_prefix_suffix_in_materials(selected_materials, texture_nodes_packs)
    else:
        print(correct_n_standardize_texture_nodes_prefix_suffix_in_selected_materials.__name__ + '() Info: no materials are selected')