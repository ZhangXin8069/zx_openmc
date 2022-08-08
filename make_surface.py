"""
This is a module that creates openmc.Surface
"""
from openmc import ZCylinder, ZPlane


def make_surface(
    radius=[0, 10, 32.5, 82.5, 147.5, 162.5, 320],
    Z_coordinate=[-320, -165, -75, -25, 25, 75, 165, 320],
):
    radius_list = [i for i in range(len(radius))]
    for i in range(len(radius)):
        radius_list[i] = ZCylinder(r=radius[i])
        if i in [len(radius) - 1]:
            radius_list[i].boundary_type = "vacuum"
            continue
        radius_list[i].boundary_type = "transmission"
    Z_coordinate_list = [i for i in range(len(Z_coordinate))]
    for i in range(len(Z_coordinate)):
        Z_coordinate_list[i] = ZPlane(z0=Z_coordinate[i])
        if i in [0,len(Z_coordinate) - 1]:
            Z_coordinate_list[i].boundary_type = "vacuum"
            continue
        Z_coordinate_list[i].boundary_type = "transmission"
    return radius_list, Z_coordinate_list
