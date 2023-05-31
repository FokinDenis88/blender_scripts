import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

#import bpy

import blender_scripts.src.general as general
import blender_scripts.src.blender.get_object as get_object

import importlib
importlib.reload(general)
importlib.reload(get_object)


PREFIX_SUFFIX_SEPARATOR = '_'
TEXTURE_PREFIX = 'T_'
MATERIAL_PREFIX = 'M_'

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


## @param texture_fullname Prefix_BaseName_Suffix.FileExtension
def correct_texture_prefix(texture_fullname):
    if general.is_not_none_or_empty(texture_fullname):
        if not texture_fullname.startswith(TEXTURE_PREFIX):
            texture_fullname = TEXTURE_PREFIX + texture_fullname
        return texture_fullname

    else:
        print(correct_texture_prefix.__name__ + '(): texture_fullname must not be None or Empty')
        return texture_fullname

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