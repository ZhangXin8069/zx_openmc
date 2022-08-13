'''
This is a module for drawing
'''

import openmc
import openmc.deplete
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import re



def Energy_Probability():
    sp = openmc.StatePoint("statepoint.200.h5")
    energy_bins = np.logspace(3, 9)
    probability, bin_edges = np.histogram(sp.source["E"], energy_bins, density=True)
    sp.close()
    print(sum(probability * np.diff(energy_bins)))
    plt.semilogx(energy_bins[:-1], probability * np.diff(energy_bins), drawstyle="steps")
    plt.xlabel("Energy (eV)")
    plt.ylabel("Probability/eV")

def Energy_colorbar():
    sp = openmc.StatePoint("statepoint.200.h5")
    plt.quiver(
    sp.source["r"]["x"],
    sp.source["r"]["y"],
    sp.source["u"]["x"],
    sp.source["u"]["y"],
    np.log(sp.source["E"]),
    cmap="jet",
    scale=20.0,)
    sp.close()
    plt.colorbar()

def deplete_errorbar():
    results = openmc.deplete.Results("depletion_results.h5")
    time, k = results.get_keff()
    time /= 24 * 60 * 60
    pyplot.errorbar(time, k[:, 0], yerr=k[:, 1])
    pyplot.xlabel("Time [d]")
    pyplot.ylabel("$k_{eff}\pm \sigma$")


def keff_plot():
    file = open("keff.txt")
    file_list = file.read().split(sep="\n")
    file.close()
    P_u = []
    keff = []
    for i in file_list[:-1]:
        P_u.append(float(re.findall(pattern=r"P\(u\):([0-9]*?\.[0-9]*).*", string=i)[0]))
        keff.append(float(re.findall(pattern=r"keff:([0-9]*?\.[0-9]*).*", string=i)[0]))
    plt.figure(dpi=160)
    plt.plot(P_u, keff)
    plt.grid()
    plt.xlabel("$P_{(U_{233})}$")
    plt.ylabel("$keff$")
    plt.title("$P_{(U_{233})}$-$keff$")