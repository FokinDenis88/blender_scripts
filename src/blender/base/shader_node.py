import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.src.general as general
import blender_scripts.src.blender.get_object as get_object
#import blender_scripts.external.python_library.src.prefix_suffix as prefix_suffix

import importlib
importlib.reload(general)
importlib.reload(get_object)
#importlib.reload(prefix_suffix)


def use_shader_nodes(material):
    return material.use_nodes and material.node_tree is not None

def get_shader_nodes_in_materials(materials):
    nodes = []
    if general.is_not_none_or_empty(materials):
        for material in materials:
            if use_shader_nodes(material):
                nodes.extend(material.node_tree.nodes)
            else:
                print(get_shader_nodes_in_materials.__name__ + '() Info: material doesnt use nodes')
    else:
        print(get_shader_nodes_in_materials.__name__ + '() Error: materials must not be None or Empty')
    return nodes

def get_shader_nodes_in_material(material):
    return get_shader_nodes_in_materials([material])


def get_links_of_material(material):
    if material is not None:
        if material.node_tree is not None:
            return material.node_tree.links
    else:
        print(get_links_of_node.__name__ + '() Error: material must not be None')
    return

## Checks are nodes the same. F.e. checks to_node, from_node in link with simple node
#def are_nodes_same(first_node, second_node):

def get_links_of_node(all_node_tree_links, target_node):
    # links, that connects to input of target_node
    input_links_to_node = []
    # links, that connects to output of target_node
    output_links_from_node = []
    if general.is_not_none_or_empty(all_node_tree_links) and target_node is not None:
        for link in all_node_tree_links:
            if link.to_node == target_node:
                input_links_to_node.append(link)
            if link.from_node == target_node:
                output_links_from_node.append(link)
    else:
        print(get_links_of_node.__name__ + '() Error: all_node_tree_links, target_node must not be None or Empty')

    return input_links_to_node, output_links_from_node

def get_input_links_of_node(all_node_tree_links, target_node):
    return get_links_of_node(all_node_tree_links, target_node)[0]
def get_output_links_of_node(all_node_tree_links, target_node):
    return get_links_of_node(all_node_tree_links, target_node)[1]

## Finish End Output nodes.
# @return to_node() to all input links
def get_to_nodes(links):
    to_nodes = []
    if general.is_not_none_or_empty(links):
        for link in links:
            to_nodes.append(link.to_node)
    else:
        print(get_to_nodes.__name__ + '() Error: links must not be None or Empty')
    return to_nodes

## Start Input nodes
# @return from_node() to all input links
def get_from_nodes(links):
    from_nodes = []
    if general.is_not_none_or_empty(links):
        for link in links:
            from_nodes.append(link.from_node)
    else:
        print(get_from_nodes.__name__ + '() Error: links must not be None or Empty')
    return from_nodes


## Checks if two nodes are linked to each other by chain of other nodes
## @return check_results (bool), output_of_start_node, input_of_end_node
def are_nodes_linked_by_chain_sockets(all_links_in_material, start_node, end_node):
    output_links_of_node = get_output_links_of_node(all_links_in_material, start_node)
    if general.is_not_none_or_empty(output_links_of_node):
        for output_link in output_links_of_node:
            if (output_link is not None) and output_link.to_node == end_node:
                return (True, output_link.from_socket, output_link.to_socket )

        # Nodes, connected with start_node output sockets
        external_nodes = get_to_nodes(output_links_of_node)
        if general.is_not_none_or_empty(external_nodes):
            for node in external_nodes:
                search_results = are_nodes_linked_by_chain_sockets(all_links_in_material, node, end_node)
                if search_results[0]:
                    return search_results

    return (False, None, None)

def are_nodes_linked_by_chain_sockets_in_material(material, start_node, end_node):
    if use_shader_nodes(material):
        return are_nodes_linked_by_chain_sockets(material.node_tree.links, start_node, end_node)
    else:
        print(are_nodes_linked_by_chain_sockets_in_material.__name__ + '() Error: material must use shader nodes')
        return

## Checks if two nodes are linked to each other by chain of other nodes
def are_nodes_linked_by_chain(links, start_node, end_node):
    return are_nodes_linked_by_chain_sockets(links, start_node, end_node)[0]


def find_sockets_by_name(sockets, socket_name):
    if general.is_not_none_or_empty(sockets):
        found_sockets = []
        for socket in sockets:
            if socket.name == socket_name:
                found_sockets.append(socket)
        return found_sockets

    else:
        print(find_sockets_by_name.__name__ + '() Error: sockets must not be None or Empty')
        return

def find_sockets_by_name_in_node_inputs(node, socket_name):
    return find_sockets_by_name(node.inputs, socket_name)
def find_sockets_by_name_in_node_outputs(node, socket_name):
    return find_sockets_by_name(node.outputs, socket_name)
def find_sockets_by_name_in_node_inputs_n_outputs(node, socket_name):
    input_output_sockets = []
    input_output_sockets.extend(find_sockets_by_name_in_node_inputs(node, socket_name))
    input_output_sockets.extend(find_sockets_by_name_in_node_outputs(node, socket_name))
    return input_output_sockets


def get_sockets_names(sockets):
    if general.is_not_none_or_empty(sockets):
        names = []
        for socket in sockets:
            names.append(socket.name)
        return names
    else:
        print(get_sockets_names.__name__ + '() Error: sockets must not be None or Empty')
        return

def get_inputs_sockets_names(node):
    if node is not None:
        names = []
        for socket in node.inputs:
            names.append(socket.name)
        return names
    else:
        print(get_inputs_sockets_names.__name__ + '() Error: node must not be None')
        return []
def get_outputs_sockets_names(node):
    if node is not None:
        names = []
        for socket in node.outputs:
            names.append(socket.name)
        return names
    else:
        print(get_outputs_sockets_names.__name__ + '() Error: node must not be None')
        return []
def get_all_sockets_names(node):
    names = []
    names.extend(get_inputs_sockets_names(node))
    names.extend(get_outputs_sockets_names(node))
    return names


## @return list of shader nodes
def get_shader_nodes_by_types_in_materials(materials, shader_nodes_types):
    found_nodes = []
    if general.is_not_none_or_empty(materials):
        for material in materials:
            if use_shader_nodes(material):
                    nodes = material.node_tree.nodes
                    for node in nodes:
                        if general.is_in_types(node, shader_nodes_types):
                            found_nodes.append(node)
            else:
                print(get_shader_nodes_by_types_in_materials.__name__ + '() Info: material is not using shader nodes: ' + str(material))

        else:
            print(get_shader_nodes_by_types_in_materials.__name__ + '() Info: There is no node_tree in material')
    else:
        print(get_shader_nodes_by_types_in_materials.__name__ + '() Error: materials must not be None or Empty')

    return found_nodes

def get_shader_nodes_by_type_in_materials(materials, shader_nodes_type):
    return get_shader_nodes_by_types_in_materials(materials, [shader_nodes_type])
def get_shader_nodes_by_types_in_material(material, shader_nodes_types):
    return get_shader_nodes_by_types_in_materials([material], shader_nodes_types)
def get_shader_nodes_by_type_in_material(material, shader_nodes_type):
    return get_shader_nodes_by_types_in_materials([material], [shader_nodes_type])

## Get nodes by type ShaderNodeTexImage
def get_shader_nodes_texture_image_in_material(material):
    return get_shader_nodes_by_type_in_material(material, bpy.types.ShaderNodeTexImage)
def get_shader_nodes_texture_image_in_materials(materials):
    return get_shader_nodes_by_type_in_materials(materials, bpy.types.ShaderNodeTexImage)

## Gets list of bsdf principled nodes
def get_all_shader_nodes_bsdf_principled_in_material(material):
    return get_shader_nodes_by_type_in_material(material, bpy.types.ShaderNodeBsdfPrincipled)
def get_all_shader_nodes_bsdf_principled_in_materials(materials):
    return get_shader_nodes_by_type_in_materials(materials, bpy.types.ShaderNodeBsdfPrincipled)
def get_shader_node_bsdf_principled_in_material(material):
    return get_all_shader_nodes_bsdf_principled_in_material(material)[0]
def get_shader_node_bsdf_principled_in_materials(materials):
    return get_all_shader_nodes_bsdf_principled_in_materials(materials)

def get_all_shader_node_material_output_in_material(material):
    return get_shader_nodes_by_type_in_material(material, bpy.types.ShaderNodeOutputMaterial)
def get_all_shader_node_material_output_in_materials(materials):
    return get_shader_nodes_by_type_in_materials(materials, bpy.types.ShaderNodeOutputMaterial)
def get_shader_node_material_output_in_material(material):
    return get_shader_nodes_by_type_in_material(material, bpy.types.ShaderNodeOutputMaterial)[0]

def get_all_shader_node_material_output_in_material(material):
    return get_shader_nodes_by_type_in_material(material, bpy.types.ShaderNodeGroup)
def get_all_shader_node_material_output_in_materials(materials):
    return get_shader_nodes_by_type_in_materials(materials, bpy.types.ShaderNodeGroup)


def get_images_in_nodes_of_materials(materials):
    images = []
    if general.is_not_none_or_empty(materials):
        for material in materials:
            nodes_with_image = get_shader_nodes_texture_image_in_material(material)     # Type = ShaderNodeTexImage
            if general.is_not_none_or_empty(nodes_with_image):
                for node in nodes_with_image:
                    if images.count(node.image) == 0:
                        images.append(node.image)
            else:
                print(get_images_in_nodes_of_material.__name__ + '() Info: material has no nodes with images')

    else:
        print(get_images_in_nodes_of_material.__name__ + '() Error: material must not be None')

    return images

def get_images_in_nodes_of_material(material):
    get_images_in_nodes_of_materials([material])


# Gets all images from 3D Object
def get_images_in_nodes_of_objects(objects):
    if general.is_not_none_or_empty(objects):
        materials = get_object.get_materials_from_objects(objects)
        return get_images_in_nodes_of_materials(materials)
    else:
        print(get_images_in_nodes_of_object.__name__ + '() Error: object must not be None')
        return

def get_images_in_nodes_of_object(object):
    return get_images_in_nodes_of_objects([object])


## Corrects color space for node
def setup_node_color_space(node, suffix):
    if suffix == '_Diff':
        node.image.colorspace_settings.name = 'sRGB'
    elif suffix == '_Normal':
        node.image.colorspace_settings.name = 'Non-Color'
    elif suffix == '_MetalRough':
        node.image.colorspace_settings.name = 'Non-Color'
    elif suffix == '_Emissive':
        node.image.colorspace_settings.name = 'sRGB'
    else:   # Default
        node.image.colorspace_settings.name = 'sRGB'

## Set new image to ShaderNodeTexImage node. Save properties and settings of node
def attach_image_n_save_settings(node, new_image):
    if general.is_not_none_lists([node, new_image]):
        old_colorspace_settings_name = node.image.colorspace_settings.name
        node.image = new_image
        node.image.colorspace_settings.name = old_colorspace_settings_name
    else:
        print(attach_image_n_save_settings.__name__ + '(): node and new_image must not be None or Empty')

## Loads new image to ShaderNodeTexImage node. Saves properties of node
def load_shader_node_tex_image_same_settings(node, new_texture_path):
    if node is not None:
        if general.is_not_none_or_empty(new_texture_path):
            if os.path.exists(new_texture_path):
                new_texture_name = os.path.basename(new_texture_path)
                node.name = new_texture_name
                node.label = new_texture_name
                new_image = bpy.data.images.load(new_texture_path)
                attach_image_n_save_settings(node, new_image)

            else:
                print(load_shader_node_tex_image_same_settings.__name__ + '(): there is no texture file with path ' + new_texture_path)
        else:
            print(load_shader_node_tex_image_same_settings.__name__ + '(): new_texture_path must not be None or Empty')
    else:
        print(load_shader_node_tex_image_same_settings.__name__ + '(): node must not be None')

def load_shader_node_tex_image_same_settings_i(node, image):
    load_shader_node_tex_image_same_settings(node, os.path.abspath(image.filepath))

## Add node to nodes (Nodes bpy_prop_collection of Node)
# @param node_tree material.node_tree.nodes
# @param node_type (string) not bpy.types!!! Type of node to add (Warning: should be same as node.bl_idname)
def new_shader_node_in_tree(node_tree, node_type, name = ''):
    new_node = None
    if node_tree is not None and node_type is not None:
        new_node = node_tree.nodes.new(node_type)
        if general.is_not_none_or_empty(name):
            new_node.name = name
    else:
        print(new_shader_node_in_tree.__name__ + '() Info: material doesnt use nodes')
    return new_node

## Add node to nodes (Nodes bpy_prop_collection of Node) material.node_tree.nodes
# @param node_type (string) not bpy.types!!! Type of node to add (Warning: should be same as node.bl_idname)
def new_shader_node_in_material(material, node_type, name = '', location = None):
    new_node = None
    if material is not None and node_type is not None:
        if use_shader_nodes(material):
            new_node = material.node_tree.nodes.new(node_type)
            if general.is_not_none_or_empty(name):
                new_node.name = name
        else:
            print(new_shader_node_in_material.__name__ + '() Info: material doesnt use nodes')
    else:
        print(new_shader_node_in_material.__name__ + '() Error: material, node_type must not be None')
    return new_node

## Creates new node group in material
# @param nodes_inside_group nodes, that must be placed inside of group between nodes group input, output
def new_shader_node_group(material, nodes_inside_group = None, location = None):
    node_group = None
    if material is not None:
        node_group = new_shader_node_in_material(material, 'ShaderNodeGroup')
        node_tree_group = node_group.node_tree
        if node_tree_group is not None:
            #node_tree_group.inputs.clear()
            #node_tree_group.outputs.clear()

            # TODO: add target nodes_inside_group to group and link them
            if nodes_inside_group is not None:
                for node in nodes_inside_group:
                    a = 0
        else:
            print(new_shader_node_group.__name__ + '() Info: node_group.node_tree must not be None')
    else:
        print(new_shader_node_group.__name__ + '() Error: material must not be None')
    return node_group