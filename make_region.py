"""
This is a module that creates openmc.Cell
"""

from zx_openmc import config 
inside_number = config.inside_number
outside_number = config.outside_number
upside_Z_coordinate_number = config.upside_Z_coordinate_number
downside_Z_coordinate_number = config.downside_Z_coordinate_number

def make_region(
    radius_list,
    Z_coordinate_list,
    inside_number= inside_number,
    outside_number= outside_number,
    upside_Z_coordinate_number= upside_Z_coordinate_number,
    downside_Z_coordinate_number= downside_Z_coordinate_number,
):
    region_list = [i for i in range(len(inside_number))]
    for i in region_list:
        region_list[i] = (
            +radius_list[inside_number[i]]
            & -radius_list[outside_number[i]]
            & +Z_coordinate_list[downside_Z_coordinate_number[i]]
            & -Z_coordinate_list[upside_Z_coordinate_number[i]]
        )
    return region_list