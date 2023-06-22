import os
import sys
BLENDER_SCRIPTS_DIR_PATH = r'C:\Development\Projects\IT\Programming\!git-web\public\blender_scripts'
PARENT_DIR = os.path.join(BLENDER_SCRIPTS_DIR_PATH, os.pardir)
sys.path.append(os.path.abspath(PARENT_DIR))

import blender_scripts.src.unreal.texture as texture

import importlib
importlib.reload(texture)


#unpack_all_images()
#pack_all_images()
texture.resave_all_textures(is_gltf_suffix = True)