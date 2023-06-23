import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.external.python_library.src.general as general
import blender_scripts.src.blender.path_blender as path_blender

import importlib
importlib.reload(general)
importlib.reload(path_blender)


TEXTURES_DEFAULT_DIR_NAME = 'textures'

##
# https://docs.blender.org/manual/en/latest/files/media/image_formats.html
SUPPORTED_IMAGE_FORMATS_EXTENSIONS = {
    'BMP': ['.bmp'],
    'Iris': ['.sgi', '.rgb', '.bw'],
    'PNG': ['.png'],
    'JPEG': ['.jpg', '.jpeg'],
    'JPEG 2000': ['.jp2', '.j2c'],
    'Targa': ['.tga'],
    'Cineon & DPX': ['.cin', '.dpx'],
    'OpenEXR': ['.exr'],
    'Radiance HDR': ['.hdr'],
    'TIFF': ['.tif', '.tiff'],
    'WebP': ['.webp']
}


## @return file name stored on disk in filepath of image
def get_image_file_name(image):
    return path_blender.basename_abspath(image.filepath)

def has_packed_files(image):
    if image is not None:
        if general.is_not_none_or_empty(image.packed_files):
            return True
        else:
            return False
    else:
        print(has_packed_files.__name__ + '(): image must not be None')
        return False

## Packs all images in data
def pack_all_images():
    for image in bpy.data.images:
        try:
            image.pack()
        except:
            print(pack_all_images.__name__+ '(): ' + image.name + ' did not packed')

## Unpacks all images in data
def unpack_all_images():
    for image in bpy.data.images:
        try:
            if has_packed_files(image):
                image.unpack()
            else:
                print(unpack_all_images.__name__+ '() Info: ' + image.name + ' there is no packed files')
        except:
            print(unpack_all_images.__name__+ '() Exception: ' + image.name + ' did not unpacked')

def set_image_properties():
    a = 0
    # packed textures filepath: //textures\ammo_1_baseColor.jpeg
    #node.image.filepath = os.path.join(os.path.dirname(node.image.filepath), new_texture_name)
    #node.image.name = new_texture_name
    #node.image.filepath = '//textures\\' + new_texture_name

# [Deprecated]
def get_packed_image_absolute_path_d(image):
    if image is not None:
        return os.path.join(os.getcwd(), image.filepath[2:])
    else:
        print(get_packed_image_absolute_path_d.__name__ + '(): image must not be None')
        return

def get_packed_image_absolute_path(image):
    if image is not None:
        return bpy.path.abspath(image.filepath)
    else:
        print(get_packed_image_absolute_path.__name__ + '(): image must not be None')
        return

## @return file_name (str) file name and extension without path. F.e. image_name.png
def get_image_file_name_n_extension(image):
    if image is not None:
        path = get_packed_image_absolute_path(image)
        return os.path.basename(os.path.abspath(path))
    else:
        return ''

def get_texture_node_file_name_n_extension(texture_node):
    if texture_node is not None:
        return get_image_file_name_n_extension(texture_node.image)
    else:
        return ''

## @return (str) absolute path of image of shader node
def get_image_in_node_abs_path(texture_node):
    if texture_node is not None:
        return get_packed_image_absolute_path(texture_node.image)
    else:
        return ''


## Loads image to all blender data
def load_image(image_file_path):
    if general.is_not_none_or_empty(image_file_path):
        return bpy.data.images.load(image_file_path)
    else:
        print(load_image.__name__ + '() Error: image_file_path must not be None or Empty')
        return

def load_images_in_paths(image_files_paths):
    if general.is_not_none_or_empty_lists(image_files_paths):
        images = []
        for image_file_path in image_files_paths:
            images.append(load_image(image_file_path))
        return images
    else:
        print(load_images_in_paths.__name__ + '() Error: image_files_paths must not be None or Empty')
        return

def load_images_in_dir(dir_path):
    if general.is_not_none_or_empty(dir_path):
        file_names_in_dir = os.listdir(dir_path)
        if general.is_not_none_or_empty(file_names_in_dir):
            images = []
            for image_file_name in file_names_in_dir:
                image_file_path = os.path.join(dir_path, image_file_name)
                images.append(load_image(image_file_path))
            return images

        else:
            print(load_images_in_dir.__name__ + '() Info: there is no image files in directory')
    else:
        print(load_images_in_dir.__name__ + '() Error: dirs_paths must not be None or Empty')
    return

## Scale the buffer of the image, in pixels
def scale_images(images, width, height):
    if general.is_not_none_or_empty(images):
        for image in images:
            image.scale(width, height)
    else:
        print(scale_images.__name__ + '() Error: images must not be None or Empty')

def save_images(images):
    if general.is_not_none_or_empty(images):
        for image in images:
            image.save()
    else:
        print(save_images.__name__ + '() Error: images must not be None or Empty')

def scale_images_n_save(images, width, height):
    scale_images(images, width, height)
    save_images(images)

## Searches first image by loaded image name in list of images. Not file name on disk.
# @param database_image_name loaded image name in project database
def find_first_image_by_image_name(images, database_image_name):
    if images is not None:
        for image in images:
            if image.name == database_image_name:
                return image
    else:
        print(find_first_image_by_image_name.__name__ + '() Error: images must not be None')
    return

## Searches first image by file name on disk in list of images.
def find_first_image_by_file_name(images, searching_file_name):
    if images is not None:
        for image in images:
            image_file_name = path_blender.basename_abspath(image.filepath)
            if image_file_name == searching_file_name:
                return image
    else:
        print(find_first_image_by_image_name.__name__ + '() Error: images must not be None')
    return

## Searches first image by file name on disk in list of images.
def find_first_image_by_file_path(images, searching_file_path):
    if images is not None:
        for image in images:
            if bpy.path.abspath(image.filepath) == searching_file_path:
                return image
    else:
        print(find_first_image_by_image_name.__name__ + '() Error: images must not be None')
    return