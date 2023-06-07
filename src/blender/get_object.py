import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.src.general as general

import importlib
importlib.reload(general)


def get_materials_from_slots(material_slots):
    materials = []
    if material_slots is not None:
        for material_slot in material_slots:
            material_of_slot = material_slot.material
            if materials.count(material_of_slot) == 0:
                materials.append(material_of_slot)
    return materials

def get_materials_from_object(object):
    if object is not None:
        return get_materials_from_slots(object.material_slots)
    else:
        return []

def get_materials_from_objects(objects):
    result_materials = []
    if general.is_not_none_or_empty(objects):
        for object in objects:
            object_materials = get_materials_from_object(object)
            if object_materials is not None:
                for material in object_materials:
                    if result_materials.count(material) == 0:
                        result_materials.append(material)
    else:
        print(get_materials_from_objects.__name__ + '() Error: objects must not be None or Empty')
    return result_materials


def get_selected_objects():
    return bpy.context.selected_objects

def get_selected_materials():
    materials = []
    selected_objects = get_selected_objects()
    if selected_objects is not None:
        materials = get_materials_from_objects(selected_objects)
    return materials

def get_active_object():
    return bpy.context.active_node

#====================Get All Data===========================

def get_all_images():
    return bpy.data.images

def get_all_materials():
    return bpy.data.materials

def get_all_meshes():
    return bpy.data.meshes

def get_all_node_groups():
    return bpy.data.node_groups

def get_all_objects():
    return bpy.data.objects

def get_all_scenes():
    return bpy.data.scenes

def get_all_sounds():
    return bpy.data.sounds

def get_all_texts():
    return bpy.data.texts

def get_all_volumes():
    return bpy.data.volumes

def get_all_texts_worlds():
    return bpy.data.texts_worlds

def get_all_workspaces():
    return bpy.data.workspaces

def get_all_window_managers():
    return bpy.data.window_managers

#========================================================