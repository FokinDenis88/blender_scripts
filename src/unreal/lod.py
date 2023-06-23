import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

#import blender_scripts.external.python_library.src.general as general
import blender_scripts.src.blender.select as select
import blender_scripts.src.blender.base.modifier as modifier
import blender_scripts.src.blender.object_name as object_name

import importlib
#importlib.reload(general)
importlib.reload(select)
importlib.reload(modifier)
importlib.reload(object_name)


# Constants
MAXIMUM_LODS_COUNT = 8

## Decimate Modifier Name, from which all other lods will calc there modifiers
DECIMATE_MODIFIER_NAME_UNIQUE = 'Script_Decimate'
## Default Name of Decimate Modifier
DEFAULT_DECIMATE_MODIFIER_NAME = 'Decimate'
LOD_TEXT = 'LOD'


LOD_GROUP_PROPERTY_NAME = 'fbx_type'
LOD_GROUP_PROPERTY_VALUE = 'LodGroup'
CONTEXT = bpy.context
## Default Screen size of lods in Unreal Engine. Screen size is distance between view camera and model
UNREAL_SCREEN_SIZE = [1.0, 0.75, 0.5625, 0.421875, 0.316406, 0.237305, 0.177979, 0.133484]
## Customizable Distance from View camera and Model in Unreal Engine
CUSTOM_SCREEN_SIZE = UNREAL_SCREEN_SIZE

ERROR_LOD_INDEX_INAVLID = 'Error: Lod index must be > 0'

def is_lod_index_valid(lod_index):
    if lod_index >= 0:
        return True
    else:
        print(ERROR_LOD_INDEX_INAVLID)
        return False

def is_name_and_lod_index_valid(name, lod_index):
    return object_name.is_model_name_valid(name) and is_lod_index_valid(lod_index)


def get_model_lod_name(model_origin_name, lod_index):
    if is_name_and_lod_index_valid(model_origin_name, lod_index):
        return model_origin_name + '_' + LOD_TEXT + str(lod_index)
    else:
        print(object_name.ERROR_MODEL_EMPTY_NAME, ' or ', ERROR_LOD_INDEX_INAVLID)
        return ''

def rename_to_lod(model, model_origin_name, lod_index):
    if is_name_and_lod_index_valid(model_origin_name, lod_index):
        model.name = get_model_lod_name(model_origin_name, lod_index)

def get_lod_group_name(model_origin_name):
    if object_name.is_model_name_valid(model_origin_name):
        return LOD_TEXT + '_' + model_origin_name
    else:
        return ''

## Calculate proper decimate modifier for lod of model. More Proccessing
def calc_lod_decimate_ratio(lod_zero_decimate, lod_index, percent_triangles_reduction):
    if is_lod_index_valid(lod_index):
        ratio = lod_zero_decimate.ratio
        # There is no reduction on lod level 0
        for i in range(1, lod_index + 1):
            ratio *= percent_triangles_reduction[i] / 100.0
        return ratio
    else:
        return 0

## Set proper decimate modifier for lod model. More Space.
def calc_lod_decimate_ratio_prev_v(lod_decimates_list, lod_index, percent_triangles_reduction):
    if is_lod_index_valid(lod_index):
        return lod_decimates_list[lod_index - 1] * (percent_triangles_reduction[lod_index] / 100.0)
    else:
        return 0

## Setting proper modifier for lod zero. If there is no such modifier, create new.
def setup_modifier_for_lods(model, decimate_modifier_name):
    if decimate_modifier_name not in model.modifiers or (
        decimate_modifier_name in model.modifiers and model.modifiers[decimate_modifier_name].decimate_type != modifier.DECIMATE_TYPE_COLLAPSE):

        print('There is no decimate_modifier_name in Modifiers of Model. Script Decimate Modifier will be added.')
        model.modifiers.new(name = decimate_modifier_name, type = modifier.DECIMATE_MODIFIER_TYPE)
        decimate_modifier_name = decimate_modifier_name
        model.modifiers[decimate_modifier_name].ratio = 1.0
    model.modifiers[decimate_modifier_name].use_collapse_triangulate = True

## Setting up Lod group for importing lod to Unreal Engine
def get_empty_lod_group(lod_zero):
    empty_lod_group = bpy.data.objects.new(get_lod_group_name(lod_zero.name), None)
    lod_zero_collection = lod_zero.users_collection[0]
    lod_zero_collection.objects.link(empty_lod_group)

    # Add Custom Property to Empty Lod Group
    CONTEXT.view_layer.objects.active = empty_lod_group
    select.make_object_active(empty_lod_group)
    CONTEXT.object[LOD_GROUP_PROPERTY_NAME] = LOD_GROUP_PROPERTY_VALUE
    print('empty_lod_group.name: ', empty_lod_group.name)
    return empty_lod_group


## Create ready for export to Unreal Engine Lods from Model
# Main Function
def create_lods(lods_count_p, decimate_modifier_name, percent_triangles_reduction, is_mesh_data_linked):
    print('Script started.')
    selected_models = CONTEXT.selected_objects
    lods = []
    for lod_zero in selected_models:
        lods.append(lod_zero)
        setup_modifier_for_lods(lod_zero, decimate_modifier_name)
        lod_zero_decimate = modifier.get_modifier(lod_zero, decimate_modifier_name)
        model_origin_name = lod_zero.name

        rename_to_lod(lod_zero, model_origin_name, 0)
        empty_lod_group = get_empty_lod_group(lod_zero)

        # Calculation variable for storing previous lod layer decimate value
        lod_decimates_list = [lod_zero_decimate.ratio, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        for lod_index in range(1, lods_count_p):
            select.select_only_one(lod_zero)
            bpy.ops.object.duplicate(linked = is_mesh_data_linked)
            new_lod_model = CONTEXT.selected_objects[0]
            lods.append(new_lod_model)
            rename_to_lod(new_lod_model, model_origin_name, lod_index)
            new_lod_model.parent = empty_lod_group
            print('new_lod_model.name: ', new_lod_model.name)

            decimate_modifier_new_lod = modifier.get_modifier(new_lod_model, decimate_modifier_name)
            decimate_modifier_new_lod.ratio = calc_lod_decimate_ratio_prev_v(lod_decimates_list, lod_index, percent_triangles_reduction)
            lod_decimates_list[lod_index] = decimate_modifier_new_lod.ratio
            print('decimate_modifier_new_lod.ratio: ', decimate_modifier_new_lod.ratio)

        lod_zero.parent = empty_lod_group
        print('Lod has been created: ', lod_zero.name); print()
    print('Script finished.')