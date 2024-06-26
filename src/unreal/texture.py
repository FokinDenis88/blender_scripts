import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.external.python_library.src.general as general
import blender_scripts.src.blender.get_object as get_object
import blender_scripts.external.python_library.src.prefix_suffix as prefix_suffix
import blender_scripts.src.unreal.prefix_suffix_unreal as prefix_suffix_unreal
import blender_scripts.src.blender.base.image as image
import blender_scripts.src.blender.base.shader_node as shader_node

import importlib
importlib.reload(general)
importlib.reload(get_object)
importlib.reload(prefix_suffix)
importlib.reload(prefix_suffix_unreal)
importlib.reload(image)
importlib.reload(shader_node)

## Get texture suffix from linked bsdf principled node socket
# Use, when you find to what socket texture node is connected
def get_texture_suffix_from_socket_name(socket_name):
    if general.is_not_none_or_empty(socket_name):
        if socket_name == 'Base Color':
            return '_Diff'
        elif socket_name == 'Subsurface':
            return ''
        elif socket_name == 'Subsurface Radius':
            return ''
        elif socket_name == 'Subsurface Color':
            return ''
        elif socket_name == 'Subsurface IOR':
            return ''
        elif socket_name == 'Subsurface Anisotropy':
            return ''
        elif socket_name == 'Metallic':
            return '_Metallic'
        elif socket_name == 'Specular':
            return '_Specular'
        elif socket_name == 'Specular Tint':
            return ''
        elif socket_name == 'Roughness':
            return '_Rough'
        elif socket_name == 'Anisotropic':
            return ''
        elif socket_name == 'Anisotropic Rotation':
            return ''
        elif socket_name == 'Sheen':
            return ''
        elif socket_name == 'Sheen Tint':
            return ''
        elif socket_name == 'Clearcoat':
            return ''
        elif socket_name == 'Clearcoat Roughness':
            return ''
        elif socket_name == 'IOR':
            return ''
        elif socket_name == 'Transmission':
            return ''
        elif socket_name == 'Transmission Roughness':
            return ''
        elif socket_name == 'Emission':
            return '_Emissive'
        elif socket_name == 'Emission Strength':
            return ''
        elif socket_name == 'Alpha':
            return '_Opacity'
        elif socket_name == 'Normal':
            return '_Normal'
        elif socket_name == 'Clearcoat Normal':
            return ''
        elif socket_name == 'Tangent':
            return ''
        # Additional sockets in material output and gltf Settings
        elif socket_name == 'Occlusion':
            return '_AO'
        elif socket_name == 'Displacement':
            return '_Disp'

    else:
        print(get_texture_suffix_from_socket_name.__name__ + '(): socket_name must not be None or Empty')

## If it is gltf model, texture shader nodes have specific suffixes
def get_suffix_in_gltf_texture(fullname_no_extension):
    suffix = prefix_suffix.get_suffix(fullname_no_extension)
    #old_image_prefix_n_basename = old_image_fullname_no_extension[:-len(suffix)]
    suffix = prefix_suffix_unreal.correct_suffix(suffix)
    return suffix


def get_suffix_for_texture_from_target_node(material, texture_node, target_node_type, material_links = None):
    suffix = ''
    target_node = shader_node.get_shader_nodes_by_type_in_material(material, target_node_type)[0]

    if (target_node_type is bpy.types.ShaderNodeGroup):
        group_input_sockets = shader_node.find_sockets_by_name_in_node_inputs(target_node, 'Occlusion')
        # Is group glTF Settings Occlusion Node?
        if not general.is_not_none_or_empty(group_input_sockets):
            return suffix
    if material_links is None:
       material_links = shader_node.get_links_of_material(material)

    check_results = shader_node.are_nodes_linked_by_chain_sockets(material_links, texture_node, target_node)
    is_linked_to_target_node = check_results[0]
    if is_linked_to_target_node:
        input_socket_of_target_node = check_results[2]
        target_node_input_socket_name = input_socket_of_target_node.name
        suffix = get_texture_suffix_from_socket_name(target_node_input_socket_name)
    return suffix

def get_suffix_from_bsdf_linked_socket(material, texture_node, material_links = None):
    return get_suffix_for_texture_from_target_node(material, texture_node, bpy.types.ShaderNodeBsdfPrincipled, material_links)

def get_suffix_from_material_output(material, texture_node, material_links = None):
    return get_suffix_for_texture_from_target_node(material, texture_node, bpy.types.ShaderNodeOutputMaterial, material_links)

def get_suffix_from_occlusion_gltf_settings(material, texture_node, material_links = None):
    return get_suffix_for_texture_from_target_node(material, texture_node, bpy.types.ShaderNodeGroup, material_links)

## Get suffix for texture in texture_node from linked chain of nodes.
def get_suffix_from_shader_nodes(material, texture_node):
    material_links = shader_node.get_links_of_material(material)
    # find suffix in bsdf principled
    suffix = get_suffix_from_bsdf_linked_socket(material, texture_node, material_links)
    if suffix == '':
        # find suffix in material output
        suffix = get_suffix_from_material_output(material, texture_node, material_links)
        if suffix == '':
            # find suffix in occlusion gltf settings
            suffix = get_suffix_from_occlusion_gltf_settings(material, texture_node, material_links)
    return suffix

## Change basename of Texture in node. Basename = name of texture without suffix
# @param old_texture_fullname_n_extension T_BaseName_Suffix + file_extension(f.e. .png)
# Fullname = prefix + basename + suffix + file_extension
def change_texture_basename_in_fullname(material, texture_node, old_texture_fullname_n_extension,
                                        new_texture_basename, is_gltf_suffix = True):
    new_texture_fullname_n_extension = ''
    if general.is_not_none_or_empty(old_texture_fullname_n_extension):
        # old_image_name_no_extension = prefix + basename + suffix
        old_image_fullname_no_extension, old_image_extension = os.path.splitext(old_texture_fullname_n_extension)
        old_image_fullname_no_extension = prefix_suffix_unreal.get_prefixed_texture_name(old_image_fullname_no_extension)

        suffix = ''
        if is_gltf_suffix:
            suffix = get_suffix_in_gltf_texture(old_image_fullname_no_extension)
        else:
            suffix = get_suffix_from_shader_nodes(material, texture_node)

        new_texture_fullname_n_extension = prefix_suffix_unreal.TEXTURE_PREFIX + new_texture_basename + suffix + old_image_extension

    else:
        print(change_texture_basename_in_fullname.__name__ + '() Info: old_image_name_n_extension must not be None or Empty')

    return new_texture_fullname_n_extension

## Rename texture file contained in shader texture node
def rename_n_reload_texture_in_node(material, texture_node, texture_path_new):
    if general.are_list_objects_not_None([material, texture_node]) and general.is_not_none_or_empty(texture_path_new):
        texture_path_old = image.get_image_in_node_abs_path(texture_node)
        if os.path.exists(texture_path_old) and not os.path.exists(texture_path_new):    # Same OcclusionMetallicRoughness map can be renamed 2 times
            os.rename(texture_path_old, texture_path_new)

        shader_node.load_shader_node_tex_image_same_settings(texture_node, texture_path_new)
    else:
        print(rename_n_reload_texture_in_node.__name__ + '() Info: texture_node must not be None or Empty')

## Rename texture file contained in the same directory in shader texture node
def rename_n_reload_texture_in_node_in_same_dir(material, texture_node, new_texture_name_n_extension):
    if general.is_not_none_or_empty(new_texture_name_n_extension):
        texture_abs_path_old = image.get_packed_image_absolute_path(texture_node.image)
        texture_dir = os.path.dirname(texture_abs_path_old)
        texture_path_new = os.path.join(texture_dir, new_texture_name_n_extension)

        rename_n_reload_texture_in_node(material, texture_node, texture_path_new)
    else:
        print(rename_n_reload_texture_in_node.__name__ + '() Error: new_texture_name_n_extension must not be None or Empty')

## Resaves textures with conventional names. Base name depends on material name
def resave_all_textures(is_gltf_suffix = True):
    image.unpack_all_images()
    for material in bpy.data.materials:
        new_texture_basename = material.name.removeprefix('M_')
        if material.node_tree is not None:
            texture_nodes = shader_node.get_shader_nodes_texture_image_in_material(material)
            for texture_node in texture_nodes:
                old_texture_name_n_extension = image.get_image_file_name_n_extension(texture_node.image)
                new_texture_name_n_extension = change_texture_basename_in_fullname(material, texture_node, old_texture_name_n_extension,
                                                                                   new_texture_basename, is_gltf_suffix)

                rename_n_reload_texture_in_node_in_same_dir(material, texture_node, new_texture_name_n_extension)