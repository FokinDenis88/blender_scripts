import bpy

def replace_char_by_index(text_object, index, new_str):
    result_text = text_object[:index] + new_str + text_object[index + 1:]
    return result_text

def to_upper_camel_case(text_object):
    if text_object is not None and len(text_object) > 0:
        is_previous_space_or_underscore = False
        for i in range(len(text_object)):
            if is_previous_space_or_underscore:
                text_object = replace_char_by_index(text_object, i, text_object[i].upper())
                is_previous_space_or_underscore = False
            if text_object[i] == ' ' or text_object[i] == '_':
                is_previous_space_or_underscore = True

        return text_object
    else:
        return ''

def white_space_to_underscore(text_object):
    if text_object is not None and len(text_object) > 0:
        for i in range(len(text_object)):
            if text_object[i] == ' ':
                text_object = replace_char_by_index(text_object, i, '_')

        return text_object
    else:
        return ''

def delete_space_or_underscore(text_object):
    if text_object is not None and len(text_object) > 0:
        text_object = text_object.replace(' ', '')
        text_object = text_object.replace('_', '')

        return text_object
    else:
        return ''

## Capitalize, upper_camel_case, delete_space in names of selected objects
def standardize_selected_names(to_delete_space = True):
    for object in bpy.context.selected_objects:
        standard_name = object.name.capitalize()
        standard_name = to_upper_camel_case(standard_name)
        if to_delete_space:
           standard_name = delete_space_or_underscore(standard_name)

        object.name = standard_name


standardize_selected_names(False)