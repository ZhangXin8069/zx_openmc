"""
This is a module that gives the default openmc.setting

"""

from openmc import Source, Settings
from openmc.stats import Box


def default_setting():
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
    return settings