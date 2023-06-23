import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import shutil

import bpy

import blender_scripts.external.python_library.src.general as general
import blender_scripts.src.blender.get_object as get_object
import blender_scripts.src.blender.set_object as set_object
import blender_scripts.src.blender.base.material as material
import blender_scripts.src.blender.base.image as image
import blender_scripts.src.blender.base.shader_node as shader_node

import importlib
importlib.reload(general)
importlib.reload(get_object)
importlib.reload(set_object)
importlib.reload(material)
importlib.reload(image)
importlib.reload(shader_node)

## @param key = resolution_index; value = tuple(Width, Height)
screen_resolution = {
    '8k': (7680, 4320),
    '4k': (3840, 2160),
    '2k': (2048, 1080),
    '1k': (1024, 768)
}

## Get the short index of screen resolution f.e. 1k
# 7680 x 4320 = 8k
# 3840 x 2160 = 4k
# 2048 x 1080 = 2k
# 1024 x 768 = 1k
def get_screen_resolution_index(width_size):
    if width_size == 7680:
        return '8k'
    elif width_size == 3840:
        return '4k'
    elif width_size == 2048:
        return '2k'
    elif width_size == 1024:
        return '1k'
    else:
        return ''

# Changes images to lower resolution, when scaled materials are created
def switch_object_resolution():
    a = 0

#get_new_scaled_image_path
def attach_scaled_textures(all_texture_nodes, scaled_images):
    for node in all_texture_nodes:
        found_image = image.find_first_image_by_file_name(scaled_images, image.get_image_file_name(node.image))
        if found_image is not None:
            shader_node.attach_image_n_save_settings(node, found_image)
        else:
            print(attach_scaled_textures.__name__ + '() Error: did not find proper associated image')

## Prepare source and destination paths for create_scaled_material
def prepare_source_n_dest_paths(image_path, screen_width):
    textures_dir_path = os.path.dirname(os.path.abspath(image_path))
    textures_parent_dir_path = os.path.abspath(os.path.join(textures_dir_path, os.path.pardir))
    resolution_index = get_screen_resolution_index(screen_width)
    scaled_textures_dir_name = os.path.basename(textures_dir_path) + '_' + resolution_index
    destination_dir_path = os.path.abspath(os.path.join(textures_parent_dir_path, scaled_textures_dir_name))
    return textures_dir_path, destination_dir_path


## Create duplicated material with scaled textures in new folder with scale index in folder name
def create_scaled_materials(objects, screen_width, screen_height):
    if general.is_not_none_or_empty(objects) and screen_width >= 0 and screen_height >= 0:
        materials = get_object.get_materials_from_objects(objects)
        images_of_objects = shader_node.get_images_in_nodes_of_objects(objects)
        if general.is_not_none_or_empty(images_of_objects):
            first_image_abs_file_path = bpy.path.abspath(images_of_objects[0].filepath)
            print(first_image_abs_file_path)
            source_dir_path, destination_dir_path = prepare_source_n_dest_paths(first_image_abs_file_path, screen_width)

            if not os.path.exists(destination_dir_path):
                # TODO: Copy Images of materials to destination_dir_path; !!! Not all dir !!!
                shutil.copytree(source_dir_path, destination_dir_path)
                # TODO: Rename dest dir and files with resolution index
                scaled_images = image.load_images_in_dir(destination_dir_path)
                image.scale_images_n_save(scaled_images, screen_width, screen_height)
                duplicated_objects = set_object.duplicate_objects_with_mesh_n_materials(objects)
                scaled_materials = get_object.get_materials_from_objects(duplicated_objects)
                all_texture_nodes = shader_node.get_shader_nodes_texture_image_in_materials(scaled_materials)
                attach_scaled_textures(all_texture_nodes, scaled_images)
            else:
                print(create_scaled_materials.__name__ + '() Error: destination_dir_path has already exists, please choose another dir_path')

        else:
            print(create_scaled_materials.__name__ + '() Info: there is no texture image in materials of objects')
    else:
        print(create_scaled_materials.__name__ +
              '() Error: materials, downscale_resolution, source_dir_path, destination_dir_path must not be None or Empty')

def create_scaled_materials_selected(screen_width, screen_height):
    selected_objects = get_object.get_selected_objects()
    create_scaled_materials(selected_objects, screen_width, screen_height)