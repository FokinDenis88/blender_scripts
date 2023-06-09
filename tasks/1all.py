import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))


import blender_scripts.src.blender.base.material as material
import blender_scripts.src.blender.object_name as object_name
import blender_scripts.src.unreal.prefix_suffix_unreal as prefix_suffix_unreal
#import blender_scripts.standardize_names as standardize_names

import importlib
importlib.reload(material)
importlib.reload(object_name)
importlib.reload(prefix_suffix_unreal)


material.set_backface_culling_for_all(True)
#object_name.capitalize_all_material_names()
prefix_suffix_unreal.add_material_prefix_to_all()


#importlib.reload(standardize_names)