"""
This is a module that creates openmc.Surface
"""
from openmc import ZCylinder, ZPlane
from zx_openmc import config 

Z_coordinate = config.Z_coordinate
radius = config.radius

def make_surface(
    radius=radius,
    Z_coordinate=Z_coordinate,
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
