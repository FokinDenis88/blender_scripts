import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.external.python_library.src.general as general
import blender_scripts.src.blender.get_object as get_object

import importlib
importlib.reload(general)
importlib.reload(get_object)


def get_materials_from_material_slots(material_slots):
    materials = []
    if material_slots is not None:
        for material_slot in material_slots:
            materials.append(material_slot.material)
    return materials

def get_materials_from_object(object):
    return get_materials_from_material_slots(object.material_slots)

def get_materials_from_objects(objects):
    materials = []
    if general.is_not_none_or_empty(objects):
        for object in objects:
            materials.extend(get_materials_from_object(object))
    else:
        print(get_materials_from_objects.__name__ + '(): objects must not be None or Empty')
    return materials

def get_materials_from_selected():
    selected_objects = get_object.get_selected_objects()
    return get_materials_from_object(selected_objects)


## Set backface_culling value to materials of selected objects
def set_backface_culling_for_materials(materials, to_use_backface_culling = False):
    if general.is_not_none_or_empty(materials):
        for material in materials:
            material.use_backface_culling = to_use_backface_culling
    else:
        print(set_backface_culling_for_materials.__name__ + '(): materials must not be None or Empty')

def set_backface_culling_objects(objects, to_use_backface_culling = False):
    if general.is_not_none_or_empty(objects):
        materials = get_materials_from_objects(objects)
        if general.is_not_none_or_empty(materials):
            set_backface_culling_for_materials(materials, to_use_backface_culling)

        else:
            print(set_backface_culling_objects.__name__ + '() Info: materials are None or Empty')
    else:
        print(set_backface_culling_objects.__name__ + '() Error: objects must not be None or Empty')

def set_backface_culling_for_selected(to_use_backface_culling = False):
    selected_objects = get_object.get_selected_objects()
    if general.is_not_none_or_empty(selected_objects):
        set_backface_culling_objects(selected_objects, to_use_backface_culling)
    else:
        print(set_backface_culling_for_selected.__name__ + '() Info: selected_objects are None or Empty')

def set_backface_culling_for_all(to_use_backface_culling = False):
    objects = get_object.get_all_objects()
    if general.is_not_none_or_empty(objects):
        set_backface_culling_objects(objects, to_use_backface_culling)

    else:
        print(set_backface_culling_for_selected.__name__ + '() Info: objects are None or Empty')