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


def get_materials_from_material_slots(material_slots):
    materials = []
    if material_slot is not None:
        for material_slot in material_slots:
            materials.append(material_slot.material)
    return materials

def get_materials_from_mesh(mesh):
    return get_materials_from_material_slots(mesh.material_slots)

def get_materials_from_meshes(meshes):
    materials = []
    if general.is_not_none_or_empty(meshes):
        for object in meshes:
            materials.extend(get_materials_from_mesh(object))
    else:
        print(get_materials_from_meshes.__name__ + '(): objects must not be None or Empty')
    return materials

## Set backface_culling value to materials of selected objects
def set_backface_culling_for_materials(materials, to_use_backface_culling = False):
    if general.is_not_none_or_empty(materials):
        for material in materials:
            material.use_backface_culling = to_use_backface_culling
    else:
        print(set_backface_culling_for_materials.__name__ + '(): materials must not be None or Empty')

def set_backface_culling_meshes(meshes, to_use_backface_culling = False):
    if general.is_not_none_or_empty(meshes):
        materials = get_materials_from_meshes(meshes)
        if general.is_not_none_or_empty(materials):
            set_backface_culling_for_materials(materials, to_use_backface_culling)

        else:
            print(set_backface_culling_meshes.__name__ + '() Info: materials are None or Empty')
    else:
        print(set_backface_culling_meshes.__name__ + '() Error: objects must not be None or Empty')

def set_backface_culling_for_selected(to_use_backface_culling = False):
    selected_objects = get_object.get_selected_objects()
    if general.is_not_none_or_empty(selected_objects):
        set_backface_culling_meshes(selected_objects, to_use_backface_culling)
    else:
        print(set_backface_culling_for_selected.__name__ + '() Info: selected_objects are None or Empty')

def set_backface_culling_for_all(to_use_backface_culling = False):
    meshes = get_object.get_all_meshes()
    if general.is_not_none_or_empty(meshes):
        set_backface_culling_meshes(meshes, to_use_backface_culling)

    else:
        print(set_backface_culling_for_selected.__name__ + '() Info: meshes are None or Empty')