# Blender Scripts for Game Development Unreal Engine
Use scripts for preparing asset for import to Unreal Engine

## Installation
1) git clone --branch develop --recurse-submodules https://gitlab.com/furious-dragon/blender_scripts.git
2) BLENDER_SCRIPTS_DIR_PATH change path to absolute path to folder on computer. F.e. 'C:/blender_scripts'

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
### Bitcoin and other cryptocurrency:  
***Bitcoin (Zengo)***:	3E18A9tKarZSCUUCPiBympih7iy9LFvkG5  
	![3E18A9tKarZSCUUCPiBympih7iy9LFvkG5](https://drive.google.com/uc?export=view&id=1W-j3C0oI7UvUr-KsCdG--dqCyM2hZTNY)  
***Ethereum (Zengo)***: 0xa0B86C071A52A14C01f53c0D1E887D0fe08c6C0f  
	![0xa0B86C071A52A14C01f53c0D1E887D0fe08c6C0f](https://drive.google.com/uc?export=view&id=14g0dtqEhl92-tQgBcVXmNJnH61DtM7K2)  
#### Telegram cryptocurrency:  
***Toncoin (TON)***:	UQA5lQeCGaWC04Fqv_OF5WggsxCevdYqopqUTPBtYeERYJwg  
	![UQA5lQeCGaWC04Fqv_OF5WggsxCevdYqopqUTPBtYeERYJwg](https://drive.google.com/uc?export=view&id=1A12KEmxyDmfba3aTRILMEk1vwLoICyUH)  
***Dollar (USDT)***:	TJa9G18po9WM6y6vqgGU2CagM4oqdWfcgN  
	![TJa9G18po9WM6y6vqgGU2CagM4oqdWfcgN](https://drive.google.com/uc?export=view&id=1ctJvfwq_hkXLFMxY_JCHpvSDsG3Px-_V)  
***Bitcoin (BTC)***:	17jSk2fvfGwQ9vKje4jyEMekrHHSJDL9Y1  
	![17jSk2fvfGwQ9vKje4jyEMekrHHSJDL9Y1](https://drive.google.com/uc?export=view&id=1Z2hMVApFkxHYQx7JnePpzDcrS0FdUBf2)  

### World:  
***PayPal***:              -  
***Visa***:                -  
***Stripe***:              -  
***Payeer***:         P1113895997  
***Volet***:       U 1138 0788 4280, E 8013 3382 9320  
***Profee***:              -  
***Patreon***:             -  
***Buy Me a Coffee***:     -  
***Ko-Fi***:               -  

### China:  
***UnionPay***:   -

### Japan:  
***JCB (Japan Credit Bureau)***:   -

### Russia:  
***Карта Мир (ВТБ)***:  2200 2459 3616 1947  
***ЮMoney***:           5599002065385959  
***Ozon Card***:        2204240208423477  
***VK Pay***:           [https://vk.com/furious__dragon](https://vk.com/furious__dragon)  
***Boosty***:           [https://boosty.to/furious_dragon](https://boosty.to/furious_dragon)  
***YandexPay***:                -

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