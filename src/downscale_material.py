import os

import bpy

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

## Get nodes by type ShaderNodeTexImage
def get_shader_nodes_texture_image(material):
    texture_nodes = []
    if material.node_tree is not None:
        nodes = material.node_tree.nodes
        for node in nodes:
            if type(node) == bpy.types.ShaderNodeTexImage:
                texture_nodes.append(node)
    else:
        print(get_shader_nodes_texture_image.__name__ + '(): There is no node_tree in material')

    return texture_nodes

def downscale_material(material, downscale_resolution, new_textures_dir_path):
    #os.path.basename
    os.mkdir(new_textures_dir_path)
