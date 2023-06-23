import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

#import bpy
import mathutils

import blender_scripts.external.python_library.src.general as general
#import blender_scripts.src.blender.get_object as get_object

import importlib
importlib.reload(general)
#importlib.reload(get_object)


def get_one_axis_values(list_vectors, axis_index):
    one_axis_values = []
    if general.is_not_none_or_empty(list_vectors) and axis_index in range(3):
        for vec in list_vectors:
            one_axis_values.append(vec[axis_index])
    else:
        print(get_one_axis_values.__name__ + '() Error: list_vectors must not be None or Empty')
    return one_axis_values

def get_object_size_on_axis(object, axis_index):
    if (object is not None) and axis_index in range(3):
        world_mtx = object.matrix_world
        max_axis = max(((world_mtx @ vertice.co)[axis_index] for vertice in object.data.vertices))
        min_axis = min(((world_mtx @ vertice.co)[axis_index] for vertice in object.data.vertices))
        return max_axis - min_axis

    else:
        print(get_object_size_on_axis.__name__ + '() Error: object must not be None')
        return 0

def get_object_size(object):
    size = mathutils.Vector(( 0.0, 0.0, 0.0 ))
    if object is not None:
        for i in range(3):
             size[i] = get_object_size_on_axis(i)
    else:
        print(get_object_size.__name__ + '() Error: object must not be None')
    return size

def get_objects_size(objects):
    objects_size = []
    for object in objects:
        objects_size.append(mathutils.Vector(( 0.0, 0.0, 0.0 )))

    if general.is_not_none_or_empty(objects):
        for object in objects:
            if object is not None:
                size = mathutils.Vector(( 0.0, 0.0, 0.0 ))
                for i in range(3):
                    size[i] = get_object_size_on_axis(object, i)
                objects_size[i] = size.copy()
            else:
                print(get_objects_size.__name__ + '() Error: object must not be None')
    else:
        print(get_objects_size.__name__ + '() Error: objects must not be None or Empty')
    return objects_size

def get_max_size_of_objects(objects):
    max_objects_size = mathutils.Vector((0.0, 0.0, 0.0))
    if general.is_not_none_or_empty(objects):
        objects_size = get_objects_size(objects)
        max_x = max(get_one_axis_values(objects_size, 0))
        max_y = max(get_one_axis_values(objects_size, 1))
        max_z = max(get_one_axis_values(objects_size, 2))
        max_objects_size = mathutils.Vector((max_x, max_y, max_z))
    else:
        print(get_max_size_of_objects.__name__ + '() Error: objects must not be None or Empty')
    return max_objects_size

#def get_min_size_of_objects():