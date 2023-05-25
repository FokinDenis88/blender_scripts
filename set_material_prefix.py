import bpy

def add_material_prefix_to_name(material):
    if material is not None:
        MATERIAL_PREFIX = 'M_'
        if not material.name.startswith(MATERIAL_PREFIX):
            material.name = MATERIAL_PREFIX + material.name
    else:
        print(add_material_prefix_to_name.__name__ + '(): material must not be None')

def set_prefix_to_selected_materials():
    for object in bpy.context.selected_objects:
        for material_slot in object.material_slots:
            add_material_prefix_to_name(material_slot.material)

def set_prefix_to_all_materials():
    for material in bpy.data.materials:
        add_material_prefix_to_name(material)

def capitalize_all_material_names():
    for material in bpy.data.materials:
        material.name = material.name.capitalize()


#set_prefix_to_selected_materials()
capitalize_all_material_names()
set_prefix_to_all_materials()