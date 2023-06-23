import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import math

import bpy
import mathutils

import blender_scripts.external.python_library.src.general as general
import blender_scripts.src.blender.select as select
import blender_scripts.src.blender.get_object as get_object
import blender_scripts.src.blender.base.mesh as mesh

import importlib
importlib.reload(general)
importlib.reload(select)
importlib.reload(get_object)
importlib.reload(mesh)


# Types of Transform: Translation, · Scaling, · Rotation

#==============================Translation========================================

# Multiply world matrix and vector with vertice coordinates
#def GetGlobalCoordinates(world_mtx, ):
    #return

## Move multiple objects by rows and columns in form of table or line
# @param horizontal_indent Horizontal additional interval between columns. SizeOfMaxObject + Indent. In meters.
# @param vertical_indent Vertical additional interval between rows. SizeOfMaxObject + Indent. In meters.
# @param start_point The Point, from which all object will be relocated
# @param is_square Models will form Square after replacement
def translate_to_interval(objects, start_point, rows_count, horizontal_indent, vertical_indent,
                          is_horizontal_plane = True, is_square = False, use_minimal_indent = False):
    if general.is_not_none_or_empty(objects):
        objects_count = len(objects)
        if is_square:
            rows_count = math.ceil(objects_count / rows_count)
        columns_count = objects_count // rows_count
        #min_indent = mathutils.Vector((0.0, 0.0, 0.0))
        horizontal_min_indent = 0
        vertical_min_indent = 0
        if use_minimal_indent:
            objects_max_size = mesh.get_max_size_of_objects(objects)
            print('objects_max_size');    print(objects_max_size)
            if is_horizontal_plane:
                #min_indent = mathutils.Vector((objects_max_size[0], objects_max_size[1], 0.0))
                horizontal_min_indent = objects_max_size[0]
                vertical_min_indent = objects_max_size[1]
            else:
                #min_indent = mathutils.Vector((objects_max_size[0], 0.0, objects_max_size[2]))
                horizontal_min_indent = objects_max_size[0]
                vertical_min_indent = objects_max_size[2]

        row = 0
        column = 0
        # The point to that object will be placed
        carriage_pos = start_point.copy()
        for object in objects:
            #select.select_only_one_object(object)
            object.location = carriage_pos
            # Horizontal Shift. Table Column
            carriage_pos += mathutils.Vector((horizontal_indent + horizontal_min_indent, 0.0, 0.0))

            column += 1
            if column >= columns_count:     # Next Row
                row += 1
                column = 0
                # Vertical Shift. Table Row
                if is_horizontal_plane:
                    carriage_pos += mathutils.Vector((0.0, vertical_indent + vertical_min_indent, 0.0))
                else:
                    carriage_pos += mathutils.Vector((0.0, 0.0, vertical_indent + vertical_min_indent))
                carriage_pos[0] = start_point[0]
    else:
        print(translate_to_interval.__name__ + '() Error: objects must not be None or Empty')

def translate_to_interval_selected(start_point, rows_count, horizontal_indent, vertical_indent,
                                   is_horizontal_plane = True, is_square = False, use_minimal_indent = False):
    selected_objects = get_object.get_selected_objects()
    translate_to_interval(selected_objects, start_point, rows_count, horizontal_indent, vertical_indent,
                          is_horizontal_plane, is_square, use_minimal_indent)


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