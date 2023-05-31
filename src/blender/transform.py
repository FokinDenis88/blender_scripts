import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import math

import bpy
import mathutils

#import blender_scripts.src.general as general
import blender_scripts.src.blender.select as select
import blender_scripts.src.blender.get_object as get_object

import importlib
#importlib.reload(general)
importlib.reload(select)
importlib.reload(get_object)


# Types of Transform: Translation, · Scaling, · Rotation

#==============================Translation========================================

# Multiply world matrix and vector with vertice coordinates
#def GetGlobalCoordinates(world_mtx, ):
    #return

## Move multiple objects by rows and columns in form of table or line
def translate_to_interval(axis_index, start_point, rows_count, horizontal_indent, vertical_indent, is_square):
    selected_objects = get_object.get_selected_objects()
    objects_count = len(selected_objects)
    if is_square:
        rows_count = math.ceil(objects_count / rows_count)
    columns_count = objects_count // rows_count

    row = 0
    column = 0
    # The point to that object will be placed
    carriage_pos = start_point.copy()
    for object in selected_objects:
        select.select_only_one(object)
        object.location = carriage_pos
        carriage_pos += mathutils.Vector((0.0, horizontal_indent, 0.0))
        column += 1
        if column >= columns_count:
            row += 1
            column = 0
            carriage_pos += mathutils.Vector((vertical_indent, 0.0, 0.0))
            carriage_pos[1] = start_point[1]


def translate_to_floor_plane(object):
    if object is not None:
        mtx = object.matrix_world
        min_z = min((mtx @ vertice.co)[2] for vertice in object.data.vertices)
        mtx.translation.z -= min_z

    else:
        print(translate_to_floor_plane.__name__ + '() Error: object must not be None')

## Move all selected objects to xy floor plane
def translate_to_floor_plane_selected():
    selected_objects = get_object.get_selected_objects()
    for object in selected_objects:
        translate_to_floor_plane(object)

def translate(value):
    bpy.ops.transform.translate(value)

def set_object_location(object, location):
    object.location = location

#===================================Scaling=====================================




#===================================Rotation=====================================