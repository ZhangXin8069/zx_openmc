"""
This is a simple module that simulates the Vacuole effect
"""

import sys
import os
from zx_openmc import config 

try:
    os.system("rm statepoint.*")
except Exception as e:
    print(e)

empty_list = config.empty_list
U_enrichment = config.U_enrichment
temperature = config.temperature
settings = config.settings
correspond_density = config.correspond_density
P_u_keff_set = config.P_u_keff_set
argv = sys.argv

try:
    if argv.index("-e"):
        empty_list = eval(argv[argv.index("-e") + 1])
except Exception as e:
    print(e)


try:
    if argv.index("-U"):
        U_enrichment = eval(argv[argv.index("-U") + 1])
except Exception as e:
    print(e)

try:
    if argv.index("-t"):
        temperature = eval(argv[argv.index("-t") + 1])
except Exception as e:
    print(e)

for i in range(5):
    if i in empty_list:
        correspond_density[i - 5] = 0.0

print(
    "U_enrichment:{}\ntemperature:{}\nempty_list:{}".format(
        U_enrichment, temperature, empty_list
    )
)


from zx_openmc import make_materials
from zx_openmc import make_surface
from zx_openmc import make_region
from zx_openmc import make_cell
import openmc

material_list = make_materials(
    U_enrichment=U_enrichment,
    temperature=temperature,
    correspond_density=correspond_density,
)
radius_list, Z_coordinate_list = make_surface()
region_list = make_region(
    radius_list=radius_list, Z_coordinate_list=Z_coordinate_list
)
cell_list = make_cell(region_list=region_list, material_list=material_list)
universe = openmc.Universe(cells=cell_list)
materials = openmc.Materials(material_list)
geometry = openmc.Geometry(universe)

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()

openmc.run()

sp = openmc.StatePoint("statepoint.200.h5")
keff = sp.keff
sp.close()

t = 1.0
keff_bol = None
for i in list(P_u_keff_set):
    if abs(U_enrichment - i) <= 0.0001:
        keff_bol = P_u_keff_set[i]
        if keff < P_u_keff_set[i]:
            t = -1.0
os.system(
    'echo "empty_list:{} keff_bol:{} keff:{} vacuole_effect:{:.0f}" >> vacule_effect.txt'.format(
        empty_list,
        keff_bol,
        keff,
        t * abs((keff.nominal_value - 1) / keff.nominal_value) * 1e5,
    )
)