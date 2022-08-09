from openmc import Source, Settings
from openmc.stats import Box

source = Source()
source.space = Box(
    (50, -10, -10),
    (70, 10, 10),
    only_fissionable=True,
)
settings = Settings()
settings.batches = 200
settings.inactive = 75
settings.particles = 16 * 625
# settings.run_mode = "eigenvalue"
# settings.keff_trigger = {"type": "std_dev", "threshold": 5e-4}
# settings.trigger_active = True
settings.trigger_max_batches = 200
settings.source = source

U_enrichment = 1.0
temperature = 293.15
composition_list = ["Th_232", "U_233", "O", "Fe", "Cr", "Mn", "W", "Pb"]
max_position = [3, 2, 3, 4, 4, 4, 4, 5]
correspond_density = [
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
]
correspond_cell_material_number = [4, 4, 4, 4, 4, 3, 0, 1, 2, 3, 4, 4]
inside_number = [0, 0, 0, 1, 2, 2, 2, 3, 4, 2, 2, 5]
outside_number = [1, 1, 1, 2, 5, 5, 3, 4, 5, 5, 5, 6]
upside_Z_coordinate_number = [7, 4, 3, 7, 7, 6, 5, 5, 5, 2, 1, 7]
downside_Z_coordinate_number = [4, 3, 0, 0, 6, 5, 2, 2, 2, 1, 0, 0]
radius = [0, 10, 32.5, 82.5, 147.5, 162.5, 320]
Z_coordinate = [-320, -165, -75, -25, 25, 75, 165, 320]

empty_list=[]