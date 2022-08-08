"""
This is a simple input U_enrichment that gives the results module

"""


import sys
import os

U_enrichment = float(sys.argv[1])


import make_materials
import make_surface
import make_region
import make_cell
import default_setting
import openmc

material_list = make_materials.make_materials(model="zx", U_enrichment=U_enrichment)
radius_list, Z_coordinate_list = make_surface.make_surface()
region_list = make_region.make_region(
    radius_list=radius_list, Z_coordinate_list=Z_coordinate_list
)
cell_list = make_cell.make_cell(region_list=region_list, material_list=material_list)
universe = openmc.Universe(cells=cell_list)
materials = openmc.Materials(material_list)
geometry = openmc.Geometry(universe)
settings = default_setting.default_setting()

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()

openmc.run()

sp = openmc.StatePoint("statepoint.200.h5")
keff = sp.keff
sp.close()
try:
    os.system("rm statepoint.*")
except Exception as e:
    print(e)
os.system('echo "P(u):{} keff:{}" >> keff.txt'.format(U_enrichment, keff))