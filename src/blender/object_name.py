import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.src.general as general
import blender_scripts.src.blender.get_object as get_object

import importlib
importlib.reload(general)
importlib.reload(get_object)


SEPARATOR = '_'
BASE_OBJECTS_NAME = 'Object'
ERROR_MODEL_EMPTY_NAME = 'Error: Model must has name'


def is_model_name_valid(name):
    if name != '':
        return True
    else:
        print(ERROR_MODEL_EMPTY_NAME)
        return False

def replace_char_by_index(text_object, index, new_str):
    result_text = text_object[:index] + new_str + text_object[index + 1:]
    return result_text

def to_upper_camel_case(text_object):
    if general.is_not_none_or_empty(text_object):
        is_previous_space_or_underscore = False
        for i in range(len(text_object)):
            if is_previous_space_or_underscore:
                text_object = replace_char_by_index(text_object, i, text_object[i].upper())
                is_previous_space_or_underscore = False
            if text_object[i] == ' ' or text_object[i] == '_':
                is_previous_space_or_underscore = True

        return text_object
    else:
        return ''

def white_space_to_underscore(text_object):
    if general.is_not_none_or_empty(text_object):
        for i in range(len(text_object)):
            if text_object[i] == ' ':
                text_object = replace_char_by_index(text_object, i, '_')

        return text_object
    else:
        return ''

def delete_space_or_underscore(text_object):
    if general.is_not_none_or_empty(text_object):
        text_object = text_object.replace(' ', '')
        text_object = text_object.replace('_', '')

        return text_object
    else:
        return ''

## Capitalize, upper_camel_case, delete_space in names of selected objects
def standardize_selected_names(to_delete_space = True):
    selected_objects = get_object.get_selected_objects()
    for object in selected_objects:
        standard_name = object.name.capitalize()
        standard_name = to_upper_camel_case(standard_name)
        if to_delete_space:
           standard_name = delete_space_or_underscore(standard_name)

        object.name = standard_name


## Delete selected object name suffix
def delete_selected_objects_suffix(suffix):
    for object in bpy.context.selected_objects:
        if object.name.endswith(suffix):
            object.name = object.name.removesuffix(suffix)

## Delete selected object name prefix
def delete_selected_objects_prefix(prefix):
    for object in bpy.context.selected_objects:
        if object.name.startswith(prefix):
            object.name = object.name.removeprefix(prefix)


## Rename objects to standard: base_name + separator + index
def rename_to_named_list(base_name):
    i = 1
    for object in bpy.context.selected_objects:
        object.name = base_name + SEPARATOR + str(i)
        i += 1


def capitalize_objects_names(objects):
    if general.is_not_none_or_empty(objects):
        for object in objects:
            object.name = object.name.capitalize()
    else:
        print(capitalize_objects_names.__name__ + '(): objects must not be None or Empty')

def capitalize_object_name(object):
    capitalize_objects_names([object])

## Make first char in name of material upper case to all materials in data
def capitalize_all_material_names():
    for material in bpy.data.materials:
        material.name = material.name.capitalize()

def capitalize_all_meshes_names():
    for mesh in bpy.data.meshes:
        mesh.name = mesh.name.capitalize()