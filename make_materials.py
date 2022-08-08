"""
This is a module that produces openmc.Materials
"""

from openmc import Material


def composition_name(name="O", number=4):
    return [name + "_" + str(i) for i in range(1, number + 1)]


def make_materials(
    model=None,
    U_enrichment=None,
    temperature=293.15,
    composition_list=["Th_232", "U_233", "O", "Fe", "Cr", "Mn", "W", "Pb"],
    max_position=[3, 2, 3, 4, 4, 4, 4, 5],
    correspond_density=[
        0,
        0,
        7.45e-3,
        6.35e-3,
        7.45e-3,
        1.27e-2,
        1.49e-2,
        1.49e-2,
        8.10e-3,
        8.87e-3,
        8.87e-3,
        6.63e-3,
        1.12e-3,
        1.06e-3,
        1.06e-3,
        8.00e-4,
        4.60e-5,
        5.10e-5,
        5.10e-5,
        3.80e-5,
        4.60e-5,
        5.10e-5,
        5.10e-5,
        3.80e-5,
        1.77e-2,
        1.56e-2,
        1.56e-2,
        2.41e-2,
        3.05e-2,
    ],
):
    if model != None:
        correspond_density[0]+=correspond_density[3]*(1-U_enrichment)
        correspond_density[1]+=correspond_density[4]*(1-U_enrichment)
        correspond_density[3]*=U_enrichment
        correspond_density[4]*=U_enrichment
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