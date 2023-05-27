# blender_scripts

## Description
Use scripts for preparing asset for import to Unreal Engine

## Functions of Project
**2delete_suffix_prefix:**
* delete_object_prefix() - Delete selected object name prefix.
* delete_object_suffix() - Delete selected object name suffix.

**3resave_textures:**
* pack_all_images ()		- Packs all images in data.
* unpack_all_images()		- Unpacks all images in data.
* resave_textures()		    - Resaves textures with conventional names. Base name depends on material name
* setup_node_color_space() - Corrects color space for node. 

**admin_tasks:**
* rename_to_named_list() - Rename objects to standard: base_name + separator + index. 

**backface_culling:**
* set_backface_culling() - Set backface_culling value to materials of selected objects.

**create_lods:**
* create_lods() - Create ready for export to Unreal Engine Lods from Model Main Function

**inline:**
* relocate_to_interval() - Move multiple objects by rows and columns in form of table or line. 

**set_material_prefix:**
* capitalize_all_material_names() - Make first char in name of material upper case to all materials in data. 
* set_prefix_to_all_materials()	- Add M_ prefix to all materials in data. 

**standardize_names:**
* standardize_selected_names() - Capitalize, upper_camel_case, delete_space in names of selected objects. 

**to_floor:**
* to_floor_plane_selected() - Move all selected objects to xy floor plane. 

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
MIT License. Open source code.

## Project status
Active
