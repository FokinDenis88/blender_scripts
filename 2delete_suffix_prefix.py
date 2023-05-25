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


#set_prefix_to_selected_materials()
#set_prefix_to_all_materials()

def delete_object_suffix(suffix):
    for object in bpy.context.selected_objects:
        if object.name.endswith(suffix):
            object.name = object.name.removesuffix(suffix)

def delete_object_prefix(prefix):
    for object in bpy.context.selected_objects:
        if object.name.startswith(prefix):
            object.name = object.name.removeprefix(prefix)


delete_object_suffix('_low')