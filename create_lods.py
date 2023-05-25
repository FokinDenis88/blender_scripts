import bpy

import os
import sys
#sys.path.append( os.path.dirname(os.path.abspath(__file__)) )
sys.path.append(r'C:\Development\Projects\IT\Programming\!it-projects\!best-projects')

import service_functions as service

import importlib
importlib.reload(service)


# Constants
MAXIMUM_LODS_COUNT = 8
# Default Name of Decimate Modifier
DEFAULT_DECIMATE_MODIFIER_NAME = 'Decimate'
# Decimate Modifier Name, from which all other lods will calc there modifiers
DECIMATE_MODIFIER_NAME_UNIQUE = 'Script_Decimate'

#============================Customizable Setup INI Parameters. Can be changed.==========================================

# Lods count in the model, after script finished
LODS_COUNT = MAXIMUM_LODS_COUNT

# Target Start Modifier of LOD0, from which all following lods decimate modifier will be calculated
#decimate_modifier_name_ini = kDecimateModifierNameUnique
DECIMATE_MODIFIER_NAME_INI = DEFAULT_DECIMATE_MODIFIER_NAME

# How much percents of lod triangles count of previous lod level will stored in next level. next_lvl_count = previous_lvl_count * percents / 100
#                             [  0,    1,    2,    3,    4,    5,    6,    7]
PERCENT_TRIANGLES_REDUCTION = [0.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]

# If Mesh Data is Linked, all lods are not unique, but blend project file will be smaller
# There is no impact on space of asset in Unreal Engine or exported fbx file.
# There is impact only on size of .blend project
IS_MESH_DATA_LINKED = True

#========================================================================================================================


# Constants
LOD_TEXT = 'LOD'
DECIMATE_MODIFIER_TYPE = 'DECIMATE'

LOD_GROUP_PROPERTY_NAME = 'fbx_type'
LOD_GROUP_PROPERTY_VALUE = 'LodGroup'
CONTEXT = bpy.context
# Default Screen size of lods in Unreal Engine. Screen size is distance between view camera and model
UNREAL_SCREEN_SIZE = [1.0, 0.75, 0.5625, 0.421875, 0.316406, 0.237305, 0.177979, 0.133484]
# Customizable Distance from View camera and Model in Unreal Engine
CUSTOM_SCREEN_SIZE = UNREAL_SCREEN_SIZE


ERROR_LOD_INDEX_INAVLID = 'Error: Lod index must be > 0'

def is_lod_index_valid(lod_index):
    if lod_index >= 0:
        return True
    else:
        print(ERROR_LOD_INDEX_INAVLID)
        return False

def is_name_and_lod_index_valid(name, lod_index):
    return service.is_model_name_valid(name) and is_lod_index_valid(lod_index)


def get_model_lod_name(model_origin_name, lod_index):
    if is_name_and_lod_index_valid(model_origin_name, lod_index):
        return model_origin_name + '_' + LOD_TEXT + str(lod_index)
    else:
        print(service.ERROR_MODEL_EMPTY_NAME, ' or ', ERROR_LOD_INDEX_INAVLID)
        return ''

def rename_to_lod(model, model_origin_name, lod_index):
    if is_name_and_lod_index_valid(model_origin_name, lod_index):
        model.name = get_model_lod_name(model_origin_name, lod_index)

def get_lod_group_name(model_origin_name):
    if service.is_model_name_valid(model_origin_name):
        return LOD_TEXT + '_' + model_origin_name
    else:
        return ''

# Calculate proper decimate modifier for lod of model. More Proccessing
def calc_lod_decimate_ratio(lod_zero_decimate, lod_index):
    if is_lod_index_valid(lod_index):
        ratio = lod_zero_decimate.ratio
        # There is no reduction on lod level 0
        for i in range(1, lod_index + 1):
            ratio *= PERCENT_TRIANGLES_REDUCTION[i] / 100.0
        return ratio
    else:
        return 0

# Set proper decimate modifier for lod model. More Space.
def calc_lod_decimate_ratio_prev_v(lod_decimates_list, lod_index):
    if is_lod_index_valid(lod_index):
        return lod_decimates_list[lod_index - 1] * (PERCENT_TRIANGLES_REDUCTION[lod_index] / 100.0)
    else:
        return 0

# Setting proper modifier for lod zero. If there is no such modifier, create new.
def setup_modifier_for_lods(model, decimate_modifier_name):
    if decimate_modifier_name not in model.modifiers or (
        decimate_modifier_name in model.modifiers and model.modifiers[decimate_modifier_name].decimate_type != service.DECIMATE_TYPE_COLLAPSE):

        print('There is no decimate_modifier_name in Modifiers of Model. Script Decimate Modifier will be added.')
        model.modifiers.new(name=decimate_modifier_name, type=DECIMATE_MODIFIER_TYPE)
        decimate_modifier_name = decimate_modifier_name
        model.modifiers[decimate_modifier_name].ratio = 1.0
    model.modifiers[decimate_modifier_name].use_collapse_triangulate = True

# Setting up Lod group for importing lod to Unreal Engine
def get_empty_lod_group(lod_zero):
    empty_lod_group = bpy.data.objects.new(get_lod_group_name(lod_zero.name), None)
    lod_zero_collection = lod_zero.users_collection[0]
    lod_zero_collection.objects.link(empty_lod_group)

    # Add Custom Property to Empty Lod Group
    CONTEXT.view_layer.objects.active = empty_lod_group
    service.make_object_active(empty_lod_group)
    CONTEXT.object[LOD_GROUP_PROPERTY_NAME] = LOD_GROUP_PROPERTY_VALUE
    print('empty_lod_group.name: ', empty_lod_group.name)
    return empty_lod_group


# Create ready for export to Unreal Engine Lods from Model
# Main Function
def create_lods(lods_count_p, decimate_modifier_name):
    print('Script started.')
    selected_models = CONTEXT.selected_objects
    lods = []
    for lod_zero in selected_models:
        lods.append(lod_zero)
        setup_modifier_for_lods(lod_zero, decimate_modifier_name)
        lod_zero_decimate = service.get_modifier(lod_zero, decimate_modifier_name)
        model_origin_name = lod_zero.name

        rename_to_lod(lod_zero, model_origin_name, 0)
        empty_lod_group = get_empty_lod_group(lod_zero)

        # Calculation variable for storing previous lod layer decimate value
        lod_decimates_list = [lod_zero_decimate.ratio, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        for lod_index in range(1, lods_count_p):
            service.select_only_one(lod_zero)
            bpy.ops.object.duplicate(linked=IS_MESH_DATA_LINKED)
            new_lod_model = CONTEXT.selected_objects[0]
            lods.append(new_lod_model)
            rename_to_lod(new_lod_model, model_origin_name, lod_index)
            new_lod_model.parent = empty_lod_group
            print('new_lod_model.name: ', new_lod_model.name)

            decimate_modifier_new_lod = service.get_modifier(new_lod_model, decimate_modifier_name)
            decimate_modifier_new_lod.ratio = calc_lod_decimate_ratio_prev_v(lod_decimates_list, lod_index)
            lod_decimates_list[lod_index] = decimate_modifier_new_lod.ratio
            print('decimate_modifier_new_lod.ratio: ', decimate_modifier_new_lod.ratio)

        lod_zero.parent = empty_lod_group
        print('Lod has been created: ', lod_zero.name); print()
    print('Script finished.')



# Lods Number start From LOD0 end to LOD7
# Decimate Modifier name must be default: 'Decimate'

create_lods(LODS_COUNT, DECIMATE_MODIFIER_NAME_INI)