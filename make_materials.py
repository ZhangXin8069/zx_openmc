"""
This is a module that produces openmc.Materials
"""

from openmc import Material
from zx_openmc import config 

U_enrichment = config.U_enrichment
temperature = config.temperature
composition_list = config.composition_list
max_position = config.max_position
correspond_density = config.correspond_density

def composition_name(name="O", number=4):
    return [name + "_" + str(i) for i in range(1, number + 1)]


def make_materials(
    U_enrichment= U_enrichment,
    temperature= temperature,
    composition_list= composition_list,
    max_position= max_position,
    correspond_density= correspond_density,
):
    correspond_density[0] += correspond_density[3] * (1 - U_enrichment)
    correspond_density[1] += correspond_density[4] * (1 - U_enrichment)
    correspond_density[3] *= U_enrichment
    correspond_density[4] *= U_enrichment

    composition_name_list0 = [
        composition_name(name=i, number=j)
        for i, j in zip(composition_list, max_position)
    ]
    composition_name_list = []
    for i in composition_name_list0:
        for j in i:
            composition_name_list.append(j)
    composition_set = {i: j for i, j in zip(composition_name_list, correspond_density)}
    material_list = [i for i in range(max(max_position))]
    for i in material_list:
        material_list[i] = Material(temperature=temperature)
        lis = []
        for j in composition_name_list:
            if j.split(sep="_")[-1] == str(i + 1):
                lis.append(j)
        atom_sum = sum([composition_set[eva] for eva in lis])
        for k in lis:
            if len(k.split(sep="_")) == 2:
                material_list[i].add_element(
                    element=str(k.split(sep="_")[0]),
                    percent=composition_set[k] / atom_sum,
                    percent_type="ao",
                )
            if len(k.split(sep="_")) == 3:
                material_list[i].add_nuclide(
                    nuclide=str(k.split(sep="_")[0]) + str(k.split(sep="_")[1]),
                    percent=composition_set[k] / atom_sum,
                    percent_type="ao",
                )
        material_list[i].set_density(units="atom/cm3", density=atom_sum * 1e24)
    return material_list