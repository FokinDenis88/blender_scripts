import os

import bpy


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
            image.unpack()
        except:
            print(unpack_all_images.__name__+ '(): ' + image.name + ' did not unpacked')

def set_image_properties():
    a = 0
    # packed textures filepath: //textures\ammo_1_baseColor.jpeg
    #node.image.filepath = os.path.join(os.path.dirname(node.image.filepath), new_texture_name)
    #node.image.name = new_texture_name
    #node.image.filepath = '//textures\\' + new_texture_name

def get_packed_image_absolute_path(image):
    if image is not None:
        return os.path.join(os.getcwd(), image.filepath[2:])
    else:
        print(get_packed_image_absolute_path.__name__ + '(): image must not be None')
        return