"""
This is a module that creates openmc.Cell
"""

from openmc import Cell
from zx_openmc import config 
correspond_cell_material_number = config.correspond_cell_material_number

def make_cell(
    region_list,
    material_list,
    correspond_cell_material_number= correspond_cell_material_number,
):
    cell_list = [i for i in range(len(region_list))]
    for i in cell_list:
        if i == None:
            cell_list[i] = Cell(fill=None, region=region_list[i])
            continue

        cell_list[i] = Cell(
            fill=material_list[correspond_cell_material_number[i]],
            region=region_list[i],
        )

    return cell_list