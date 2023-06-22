import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import re

#import bpy


import blender_scripts.src.general as general
import blender_scripts.src.blender.get_object as get_object

import importlib
importlib.reload(general)
importlib.reload(get_object)


PREFIX_SUFFIX_SEPARATOR = '_'
TEXTURE_PREFIX = 'T_'
MATERIAL_PREFIX = 'M_'

def add_material_prefix_to_materials(materials):
    if general.is_not_none_or_empty(materials):
        for material in materials:
            if not material.name.startswith(MATERIAL_PREFIX):
                material.name = MATERIAL_PREFIX + material.name

    else:
        print(add_material_prefix_to_materials.__name__ + '() Error: material must not be None')

def add_material_prefix_to_material(material):
    add_material_prefix_to_materials([material])

def add_material_prefix_to_selected():
    materials = get_object.get_selected_objects()
    add_material_prefix_to_materials(materials)

## Add M_ prefix to all materials in data
def add_material_prefix_to_all():
    materials = get_object.get_all_materials()
    add_material_prefix_to_materials(materials)


## @param texture_fullname Prefix_BaseName_Suffix.FileExtension
def correct_texture_prefix(texture_fullname):
    if general.is_not_none_or_empty(texture_fullname):
        if not texture_fullname.startswith(TEXTURE_PREFIX):
            texture_fullname = TEXTURE_PREFIX + texture_fullname
        return texture_fullname

    else:
        print(correct_texture_prefix.__name__ + '(): texture_fullname must not be None or Empty')
        return texture_fullname

## Change gltf Standard texture suffix to Custom Standard
def correct_suffix(suffix):
    if suffix == '_baseColor':
        return '_Diff'
    elif suffix == '_normal':
        return '_Normal'
    elif suffix == '_metallicRoughness':
        return '_MetalRough'
    elif suffix == '_emissive':
        return '_Emissive'
    else:
        return suffix




def get_prefix(text):
    match_object = re.search(PREFIX_REGEX, text)
    if match_object is not None:
        return match_object[0]
    else:
        return ''

def get_suffix(text):
    match_object = re.search(SUFFIX_REGEX, text)
    if match_object is not None:
        return match_object[0]
    else:
        return ''

'''## @return (str) name of asset without prefix and suffix, without extension.
def get_asset_name_without_prefix_suffix(object_path):
    if general.is_not_none_or_empty(object_path):
        file_name_no_extension = unreal.Paths.get_base_filename(object_path)
        file_name_no_prefix_suffix = file_name_no_extension
        prefix = get_prefix(file_name_no_extension)
        #unreal.log('prefix'); unreal.log(prefix)
        if prefix in convention.get_AssetsPrefixConventionTable_prefixes():
            file_name_no_prefix_suffix = file_name_no_prefix_suffix[len(prefix):]

        suffix = get_suffix(file_name_no_extension)
        #unreal.log('suffix'); unreal.log(suffix)
        if suffix in convention.get_TextureTypesCustom_suffixes():
            file_name_no_prefix_suffix = file_name_no_prefix_suffix[:-len(suffix)]
        return file_name_no_prefix_suffix
    else:
        unreal.log_error(get_asset_name_without_prefix_suffix.__name__ + ': object_path must not be None or empty')
        return ''

## Correct prefix by unreal engine asset type (Texture, Material, Static Mesh).
# Adds prefix, if there is no prefix
def correct_prefix_by_uclass(object_path, asset_data = None,
                          include_only_on_disk_assets = False):
    if asset_data == None:
        asset_data = get_asset.get_asset_data_by_object_path(object_path, include_only_on_disk_assets)

    if asset_data != None:
        asset_class = general.Name_to_str(asset_data.get_editor_property('asset_class'))
        prefix_for_class = convention.AssetsPrefixConventionTable[asset_class]
        #unreal.log('prefix_for_class');   unreal.log(prefix_for_class)
        if prefix_for_class != None and prefix_for_class != '':
            # If function was called by correct_prefix_by_uclass_dirs, it has one transaction with all assets in folder
            with unreal.ScopedEditorTransaction(correct_prefix_by_uclass.__name__) as ue_transaction:
                add_prefix_suffix(object_path, prefix = prefix_for_class, is_folder_operation = False,
                                    include_only_on_disk_assets = include_only_on_disk_assets)

        else:
            unreal.log_error(correct_prefix_by_uclass.__name__ + '(): Did not find prefix for asset class - ' + asset_class)
    else:
        unreal.log_error(correct_prefix_by_uclass.__name__ + '(): Did not find asset_data from object_path')

## Correct prefix by unreal engine asset type (Texture, Material, Static Mesh).
# Adds prefix, if there is no prefix
def correct_prefix_by_uclass_dirs(dir_paths, recursive = False, include_only_on_disk_assets = False):
    with unreal.ScopedEditorTransaction(correct_prefix_by_uclass_dirs.__name__) as ue_transaction:
        assets_data = get_asset.get_assets_by_dirs(dir_paths, recursive, include_only_on_disk_assets)

        progress_bar_text = correct_prefix_by_uclass_dirs.__name__ + config.IS_WORKING_TEXT
        with unreal.ScopedSlowTask(len(assets_data), progress_bar_text) as slow_task:
            slow_task.make_dialog(True)

            for asset_data in assets_data:
                if slow_task.should_cancel():
                    break
                object_path = asset_data.get_editor_property('object_path')
                correct_prefix_by_uclass(object_path, asset_data, include_only_on_disk_assets)

                slow_task.enter_progress_frame(1)


## Rename texture asset suffix to default variation.
# Default variation is zero in list of TextureTypesCustom suffixes
# F.e. From _BaseColor to _Diff
def standardize_texture_suffix_asset_data(texture_asset_data):
    if texture_asset_data is not None:
        texture_type = get_texture_type_by_prefix_suffix_in_data(texture_asset_data)
        if texture_type != NO_TEXTURE_TYPE:
            texture_name_no_extension = get_asset.get_asset_name_no_extension_in_data_asset(texture_asset_data)
            prefix, suffix = get_asset_prefix_suffix_by_name(texture_name_no_extension)
            standard_suffix = convention.get_TextureTypesCustom_standard_suffix(texture_type)
            if suffix != standard_suffix:
                replace_prefix_suffix_asset_data(texture_asset_data, prefix = '', suffix = suffix,
                                                 new_prefix = '', new_suffix = standard_suffix)
        else:
            unreal.log_error(standardize_texture_suffix_asset_data.__name__ + '(): did not find texture type')
    else:
        unreal.log_error(standardize_texture_suffix_asset_data.__name__ + '(): no asset_data in input')

## Rename texture asset suffix to default variation.
# Default variation is zero in list of TextureTypesCustom suffixes
# F.e. From _BaseColor to _Diff
def standardize_texture_suffix_materials(materials):
    if general.is_not_none_or_empty(textures_assets_data):
        progress_bar_text = standardize_texture_suffix_assets_data.__name__ + config.IS_WORKING_TEXT
        with unreal.ScopedSlowTask(len(textures_assets_data), progress_bar_text) as slow_task:
            slow_task.make_dialog(True)

            for asset_data in textures_assets_data:
                if slow_task.should_cancel():
                    break
                standardize_texture_suffix_asset_data(asset_data)

                slow_task.enter_progress_frame(1)
    else:
        unreal.log(standardize_texture_suffix_assets_data.__name__ + '(): no assets_data in input')

## Rename texture asset suffix to default variation.
# Default variation is zero in list of TextureTypesCustom suffixes
# F.e. From _BaseColor to _Diff
def standardize_texture_suffix_dirs(dir_paths, recursive = False, include_only_on_disk_assets = False):
     with unreal.ScopedEditorTransaction(correct_prefix_by_uclass_dirs.__name__) as ue_transaction:
        assets_data = get_asset.get_textures_data_by_dirs(dir_paths, recursive, include_only_on_disk_assets)
        standardize_texture_suffix_assets_data(assets_data)

def correct_n_standardize_texture_suffix_dirs(dir_paths, recursive = False, include_only_on_disk_assets = False):
    correct_prefix_by_uclass_dirs(dir_paths, recursive, include_only_on_disk_assets)
    standardize_texture_suffix_dirs(dir_paths, recursive, include_only_on_disk_assets)
'''