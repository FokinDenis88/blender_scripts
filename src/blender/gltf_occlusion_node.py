import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import bpy

import blender_scripts.external.python_library.src.general as general
import blender_scripts.src.blender.get_object as get_object
import blender_scripts.src.blender.base.shader_node as shader_node

import importlib
importlib.reload(general)
importlib.reload(get_object)
importlib.reload(shader_node)


## gltf Settings group is used for importing gltf texture Ambient Occlusion to Game Engines
def add_occlusion_gltf_Settings_group_in_materials(materials):
    node_groups = []
    if general.is_not_none_or_empty(materials):
        for material in materials:
            node_group = shader_node.new_shader_node_group(material)
            node_group.name = 'Group'
            node_tree_group_key = 'glTF Settings'
            if node_tree_group_key not in bpy.data.node_groups:
                bpy.data.node_groups.new('glTF Settings', 'ShaderNodeTree')
            node_tree_group = bpy.data.node_groups[node_tree_group_key]
            node_group.node_tree = node_tree_group

            #node_input = shader_node.new_shader_node_in_tree(node_tree_group, 'ShaderNode', 'Group Input')
            #node_output = shader_node.new_shader_node_in_tree(node_tree_group, 'ShaderNode', 'Group Output')

            #if node_tree_group is not None:
            if 'Occlusion' not in node_tree_group.inputs:
                node_tree_group.inputs.clear()
                node_tree_group.outputs.clear()
                node_tree_group.inputs.new('NodeSocketFloat', 'Occlusion')
            node_groups.append(node_group)
            #else:
                #print(add_occlusion_gltf_Settings_group_in_materials.__name__ + '() Info: node_group.node_tree must not be None')
    else:
        print(add_occlusion_gltf_Settings_group_in_materials.__name__ + '() Error: material must not be None')
    return node_groups

def add_occlusion_gltf_Settings_group_in_material(material):
    return add_occlusion_gltf_Settings_group_in_materials([material])[0]

def add_occlusion_gltf_Settings_group_in_materials_selected():
    selected_materials = get_object.get_selected_materials()
    add_occlusion_gltf_Settings_group_in_materials(selected_materials)

'''
https://blender.stackexchange.com/questions/5387/how-to-handle-creating-a-node-group-in-a-script

import bpy

# create a group
test_group = bpy.data.node_groups.new('testGroup', 'ShaderNodeTree')

# create group inputs
group_inputs = test_group.nodes.new('NodeGroupInput')
group_inputs.location = (-350,0)
test_group.inputs.new('NodeSocketFloat','in_to_greater')
test_group.inputs.new('NodeSocketFloat','in_to_less')

# create group outputs
group_outputs = test_group.nodes.new('NodeGroupOutput')
group_outputs.location = (300,0)
test_group.outputs.new('NodeSocketFloat','out_result')

# create three math nodes in a group
node_add = test_group.nodes.new('ShaderNodeMath')
node_add.operation = 'ADD'
node_add.location = (100,0)

node_greater = test_group.nodes.new('ShaderNodeMath')
node_greater.operation = 'GREATER_THAN'
node_greater.label = 'greater'
node_greater.location = (-100,100)

node_less = test_group.nodes.new('ShaderNodeMath')
node_less.operation = 'LESS_THAN'
node_less.label = 'less'
node_less.location = (-100,-100)

# link nodes together
test_group.links.new(node_add.inputs[0], node_greater.outputs[0])
test_group.links.new(node_add.inputs[1], node_less.outputs[0])

# link inputs
test_group.links.new(group_inputs.outputs['in_to_greater'], node_greater.inputs[0])
test_group.links.new(group_inputs.outputs['in_to_less'], node_less.inputs[0])

#link output
test_group.links.new(node_add.outputs[0], group_outputs.inputs['out_result'])

'''