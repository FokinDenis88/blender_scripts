import bpy


def get_selected_objects():
    return bpy.context.selected_objects

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