import sys
import os
import config

try:
    os.system("rm statepoint.*")
except Exception as e:
    print(e)

empty_list = config.empty_list
U_enrichment = config.U_enrichment
temperature = config.temperature  
correspond_cell_material_number = config.correspond_cell_material_number
argv = sys.argv

try:
    if argv.index("-U"):
        U_enrichment = eval(argv[argv.index("-U")+1])
except Exception as e:
    print(e)


try:
    if argv.index("-e"):
        empty_list = eval(argv[argv.index("-e")+1])
except Exception as e:
    print(e)

    
    
print('U_enrichment:{}\nempty_list:{}'.format(U_enrichment,empty_list))



import make_materials
import make_surface
import make_region
import make_cell
import default_setting
import openmc

material_list = make_materials.make_materials(U_enrichment=U_enrichment,temperature=temperature)
radius_list, Z_coordinate_list = make_surface.make_surface()
region_list = make_region.make_region(
    radius_list=radius_list, Z_coordinate_list=Z_coordinate_list
)
cell_list = make_cell.make_cell(region_list=region_list, material_list=material_list,
                                correspond_cell_material_number=correspond_cell_material_number)
universe = openmc.Universe(cells=cell_list)
materials = openmc.Materials(material_list)
geometry = openmc.Geometry(universe)
settings = default_setting.default_setting()

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()

openmc.run()

sp = openmc.StatePoint("statepoint.200.h5")
keff_bol = sp.keff
sp.close()
try:
    os.system("rm statepoint.*")
except Exception as e:
    print(e)
    
    
temperature=273.15+150

for i in range(len(correspond_cell_material_number)):
    if i in empty_list:
        correspond_cell_material_number[i]=None
    
material_list = make_materials.make_materials(U_enrichment=U_enrichment,temperature=temperature)
radius_list, Z_coordinate_list = make_surface.make_surface()
region_list = make_region.make_region(
    radius_list=radius_list, Z_coordinate_list=Z_coordinate_list
)
cell_list = make_cell.make_cell(region_list=region_list, material_list=material_list,correspond_cell_material_number=correspond_cell_material_number)
universe = openmc.Universe(cells=cell_list)
materials = openmc.Materials(material_list)
geometry = openmc.Geometry(universe)
settings = default_setting.default_setting()

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()

openmc.run()

sp = openmc.StatePoint("statepoint.200.h5")
keff_t_150 = sp.keff
sp.close()

    
    
    
os.system('echo "P(u):{} empty:{} pa-ef:{}" >> pa-ef.txt'.format(U_enrichment,empty_list, (keff_t_150.nominal_value-keff_bol.nominal_value)/keff_bol.nominal_value))