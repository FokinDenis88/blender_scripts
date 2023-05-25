import os
import sys
'''WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(WORKING_DIR, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))'''

sys.path.append(r'C:\Development\Projects\IT\Programming\!it-projects\!best-projects')

import blender_scripts.backface_culling as backface_culling
import blender_scripts.set_material_prefix as set_material_prefix
#import blender_scripts.standardize_names as standardize_names


import importlib
importlib.reload(backface_culling)
importlib.reload(set_material_prefix)
#importlib.reload(standardize_names)
