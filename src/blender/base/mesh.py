#import bpy
import mathutils


def get_object_size_on_axis(object, axis_index):
    if object is not None:
        world_mtx = object.matrix_world
        object_axis_glob_co = ((world_mtx @ vertice.co)[axis_index] for vertice in object.data.vertices)
        max_axis = max(object_axis_glob_co)
        min_axis = min(object_axis_glob_co)
        return max_axis - min_axis

    else:
        print(get_object_size_on_axis.__name__ + '() Error: object must not be None')
        return 0

def get_object_size(object):
    if object is not None:
        size = mathutils.Vector(( 0.0, 0.0, 0.0 ))
        for i in range(3):
             size[i] = get_object_size_on_axis(i)
        return size

    else:
        print(get_object_size.__name__ + '() Error: object must not be None')
        return 0