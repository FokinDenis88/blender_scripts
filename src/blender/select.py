import bpy


def make_object_active(object):
    bpy.context.view_layer.objects.active = object

def select_all():
    for object in bpy.data.objects:
        object.select_set(True)

def un_select_all():
    for object in bpy.data.objects:
        object.select_set(False)

def select_object(object):
    object.select_set(True)

def select_object_list(object_list):
    for object in object_list:
        object.select_set(True)

def select_object_name(object_name):
    if object_name != '':
        bpy.data.objects[object_name].select_set(True)

def select_only_one_object(object):
    un_select_all()
    select_object(object)

def select_only_one_object_by_name(object_name):
    un_select_all()
    select_object(object_name)