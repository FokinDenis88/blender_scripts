import math

import bpy
import mathutils

import os
import sys
sys.path.append( os.path.dirname(os.path.abspath(__file__)) )

import service_functions as service

import importlib
importlib.reload(service)


#====================================Ini Section================================
ROWS_COUNT = 1
#kColumnCount = 0

# Horizontal additional interval between columns. SizeOfMaxObject + Indent. In meters.
HORIZONTAL_INDENT = 12
# Vertical additional interval between rows. SizeOfMaxObject + Indent. In meters.
VERTICAL_INDENT = 10

# The Point, from which all object will be relocated
START_POINT = mathutils.Vector(( 0.0, 0.0, 0.0 ))

# Models will form Square after replacement
IS_SQUARE = False


# Choose axis along which models will be placed
# 0 = x; 1 = y; 2 = z
AXIS_INDEX_PLACEMENT = 1
#===============================================================================



# Multiply world matrix and vector with vertice coordinates
#def GetGlobalCoordinates(world_mtx, ):
    #return

def relocate_to_interval(axis_index, start_point, rows_count, horizontal_indent, vertical_indent, is_square):
    print('Script starts')
    selected_objects = bpy.context.selected_objects
    objects_count = len(selected_objects)
    if is_square:
        rows_count = math.ceil(objects_count / rows_count)
    columns_count = objects_count // rows_count

    row = 0
    column = 0
    # The point to that object will be placed
    carriage_pos = start_point.copy()
    for object in selected_objects:
        service.select_only_one(object)
        object.location = carriage_pos
        carriage_pos += mathutils.Vector((0.0, horizontal_indent, 0.0))
        column += 1
        if column >= columns_count:
            row += 1
            column = 0
            carriage_pos += mathutils.Vector((vertical_indent, 0.0, 0.0))
            carriage_pos[1] = start_point[1]
    print('Script finished')


relocate_to_interval(AXIS_INDEX_PLACEMENT, START_POINT, ROWS_COUNT, HORIZONTAL_INDENT, VERTICAL_INDENT, IS_SQUARE)