"""
This is a module that creates openmc.Cell
"""

from openmc import Cell


def make_cell(
    region_list,
    material_list,
    correspond_cell_material_number=[4, 4, 4, 4, 4, 3, 0, 1, 2, 3, 4, 4],
):
    cell_list = [i for i in range(len(region_list))]
    for i in cell_list:
        cell_list[i] = Cell(
            fill=material_list[correspond_cell_material_number[i]],
            region=region_list[i],
        )
    
    return cell_list