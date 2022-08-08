"""
This is a module that creates openmc.Cell
"""


def make_region(
    radius_list,
    Z_coordinate_list,
    inside_number=[0, 0, 0, 1, 2, 2, 2, 3, 4, 2, 2, 5],
    outside_number=[1, 1, 1, 2, 5, 5, 3, 4, 5, 5, 5, 6],
    upside_Z_coordinate_number=[7, 4, 3, 7, 7, 6, 5, 5, 5, 2, 1, 7],
    downside_Z_coordinate_number=[4, 3, 0, 0, 6, 5, 2, 2, 2, 1, 0, 0],
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