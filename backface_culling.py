import bpy

def set_backface_culling(use_backface_culling_p):
    for object in bpy.context.selected_objects:
        for material_slot in object.material_slots:
            material_slot.material.use_backface_culling = use_backface_culling_p


set_backface_culling(True)