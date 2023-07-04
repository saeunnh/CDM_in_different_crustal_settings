# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:46:54 2020

@author: Ivar
"""
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from utils import read_pickle
import numpy as np
import porepy as pp

#save_path = "../figures/"
#save_path = "figures/"
save_path = "/home/saeunn/Numerical-modelling-of-convection-driven-cooling-deformation-and-fracturing-of-thermo-poroelastic-m/src/CaseII_update3/"
#save_path = "C:/Users/Ivar/Documents/GitHub/Thermal_fracturing/figures/"

sns.set_style("ticks")

colors = ["b", "r", "g", "c", "y"]


def prepare_plotting(**kwargs):
    plt.close("all")
    matplotlib.use("agg", warn=False, force=True)  # force non-GUI backend.

    # Number of floating points
    mf = matplotlib.ticker.ScalarFormatter(useMathText=True)
    mf.set_powerlimits((-4, 4))

    # Plotting

    # Preparing plot
    sns.set_context("paper")  # set scale and size of figures
    sns.set_palette("tab10", 10)
    # itertools.cycle(sns.color_palette())  # iterate if > 10 colors are needed
    figsize = kwargs.get("figsize", (6, 8))
    fig = plt.figure(8, constrained_layout=True, figsize=figsize)
    widths = kwargs.get("widths", [5, 5, 1])
    heights = kwargs.get("heights", [1, 3, 3, 3, 3, 3, 3])
    gs = fig.add_gridspec(
        nrows=len(heights),
        ncols=len(widths),
        width_ratios=widths,
        height_ratios=heights,
    )
    return fig, gs


def plot_ex_IV():
    plt.figure()
    in_name = "CaseII_sh_45p_normal/fracture_sizes"
    data = read_pickle(in_name)
    fracture_sizes = data["fracture_sizes"]
    time_steps = np.array(data["time_steps"]) / pp.YEAR

    fig, gs = prepare_plotting(figsize=(6, 5), widths=[2], heights=[1, 5])  # , 3, 3, 3
    ax_label = fig.add_subplot(gs[0, 0])
    ax = fig.add_subplot(gs[1, 0])
    linestyles = ["-", "-", "-", "-", "--"]
    n_frac = fracture_sizes.shape[1]
    for frac in range(n_frac):
        
        label = "$\Omega_{}$".format(frac + 2)
        ax.plot(
                time_steps,
                fracture_sizes[:, frac],
                color=colors[frac],
                ls=linestyles[frac],
                )
        ax_label.plot([], label=label, color=colors[frac])
    

    
    
    ax_label.legend(loc="center", frameon=False, ncol=n_frac)
    ax_label.axis("off")
    # xs = [0, 1200, 2400, 3600]
    # ax.set_xticks(xs)
    # ax.set_xticklabels(xs)

    ax.set_xlabel("$t$ [yr]")
    ax.set_ylabel(r"$\|\Omega_i|$ [m$^2$]")
    fig.tight_layout()
    plt.savefig(save_path + "CaseII_45p_normal.pdf")
    plt.show()




#plot_applications("exIV")
plot_ex_IV()

# plot_ex_I()
# plot_ex_II()
