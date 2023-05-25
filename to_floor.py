import bpy

CONTEXT = bpy.context

def to_floor_plane(object):
    mtx = object.matrix_world
    min_z = min((mtx @ vertice.co)[2] for vertice in object.data.vertices)
    mtx.translation.z -= min_z


for object in CONTEXT.selected_objects:
    to_floor_plane(object)