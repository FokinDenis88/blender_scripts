#import bpy

DECIMATE_MODIFIER_TYPE = 'DECIMATE'
DECIMATE_TYPE_COLLAPSE = 'COLLAPSE'

def get_modifier(model, modifier_name):
    if modifier_name != '':
        if modifier_name in model.modifiers:
            return model.modifiers[modifier_name]
        else:
            print('Error: There is no decimate modifier with name: ', modifier_name)
    else:
        print('Error: GetModifier must has modifier_name not empty')