import bpy

#==============Ini Section===========

BASE_OBJECTS_NAME = 'Mesh'

#========================================

SEPARATOR = '_'

## Rename objects to standard: base_name + separator + index
def rename_to_named_list(base_name):
    i = 1
    for object in bpy.context.selected_objects:
        object.name = base_name + SEPARATOR + str(i)
        i += 1


def main():
    rename_to_named_list(BASE_OBJECTS_NAME)

main()