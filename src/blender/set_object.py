import bpy

def duplicate_materials(materials):
    duplicated_materials = []
    if materials is not None:
        for material in materials:
            duplicated_materials.append(material.copy())
    return duplicated_materials

def duplicate_objects_with_mesh_n_materials(input_objects):
    duplicated_objects = []
    if input_objects is not None:
        # Old materials, that are already copied
        already_copied_old_materials = []
        new_materials = []
        for object in input_objects:
            object_mesh = object.data
            duplicated_object = bpy.data.objects.new(object.name, object_mesh.copy())
            if duplicated_object.material_slots is not None:
                for material_slot in duplicated_object.material_slots:
                    material = material_slot.material
                    if already_copied_old_materials.count(material) == 0:
                        already_copied_old_materials.append(material_slot.material)
                        material_slot.material = material_slot.material.copy()
                        new_materials.append(material_slot.material)
                    else:
                        index_of_material = already_copied_old_materials.index(material)
                        material_slot.material = new_materials[index_of_material]
            bpy.context.scene.collection.objects.link(duplicated_object)
            duplicated_objects.append(duplicated_object)
    return duplicated_objects

## Duplicate selected objects
# @param linked Duplicate object but not object data, linking to the original data
# @param mode  (enum in Transform Mode Types, (optional)) – Mode
# https://docs.blender.org/api/current/bpy.ops.object.html
def duplicate_selected_objects(linked = False, mode = 'TRANSLATION'):
    bpy.ops.object.duplicate(linked, mode)