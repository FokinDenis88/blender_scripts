import bpy
import mathutils


DECIMATE_TYPE_COLLAPSE = 'COLLAPSE'
ERROR_MODEL_EMPTY_NAME = 'Error: Model must has name'


def get_selected_objects():
    return bpy.context.selected_objects

def get_active_object():
    return bpy.context.active_node

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

def select_only_one(object):
    un_select_all()
    select_object(object)

def select_only_one_name(object_name):
    un_select_all()
    select_object(object_name)


def is_model_name_valid(name):
    if name != '':
        return True
    else:
        print(ERROR_MODEL_EMPTY_NAME)
        return False

def get_modifier(model, modifier_name):
    if modifier_name != '':
        if modifier_name in model.modifiers:
            return model.modifiers[modifier_name]
        else:
            print('Error: There is no decimate modifier with name: ', modifier_name)
    else:
        print('Error: GetModifier must has modifier_name not empty')

def get_object_size_on_axis(object, axis_index):
    world_mtx = object.matrix_world
    object_axis_glob_co = ((world_mtx @ vertice.co)[axis_index] for vertice in object.data.vertices)
    max_axis = max(object_axis_glob_co)
    min_axis = min(object_axis_glob_co)
    return max_axis - min_axis

def get_object_size(object):
    size = mathutils.Vector(( 0.0, 0.0, 0.0 ))
    for i in range(3):
         size[i] = get_object_size_on_axis(i)
    return size

def translate(value):
    bpy.ops.transform.translate(value)

def set_object_location(object, location):
    object.location = location