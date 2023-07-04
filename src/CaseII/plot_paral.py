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
case_path = "/home/saeunn/Numerical-modelling-of-convection-driven-cooling-deformation-and-fracturing-of-thermo-poroelastic-m/src/CaseI_update3/"
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

 #   fig, (ax1, ax2) = plt.subplots(1, 2)
 #   fig.suptitle('Horizontally stacked subplots')
    #ax1.plot(x, y)
    #ax2.plot(x, -y)

    fig, axs = plt.subplots(2, 2)
#axs[0, 0].plot(x, y)
#axs[0, 0].set_title('Axis [0, 0]')
#axs[0, 1].plot(x, y, 'tab:orange')
#axs[0, 1].set_title('Axis [0, 1]')
#axs[1, 0].plot(x, -y, 'tab:green')
#axs[1, 0].set_title('Axis [1, 0]')
#axs[1, 1].plot(x, -y, 'tab:red')
#axs[1, 1].set_title('Axis [1, 1]')

# top left
    in_name = "CaseII_sh_40p/fracture_sizes"
    data = read_pickle(in_name)
    fracture_sizes = data["fracture_sizes"]
    time_steps = np.array(data["time_steps"]) / pp.YEAR
    #fig, gs = prepare_plotting(figsize=(6, 5), widths=[2], heights=[1, 5])  # , 3, 3, 3
    #ax_label = fig.add_subplot(gs[0, 0])
    #ax = fig.add_subplot(gs[1, 0])
    #linestyles = ["-", "-", "-", "-", "--"]
    n_frac = fracture_sizes.shape[1]
    for frac in range(n_frac):
        
        label = "$\Omega_{}$".format(frac + 2)
        axs[0, 0].plot(
                time_steps,
                fracture_sizes[:, frac],
                color=colors[frac],
     #           ls=linestyles[frac],
                )
     #   ax_label.plot([], label=label, color=colors[frac])
    
    #ax_label.legend(loc="center", frameon=False, ncol=n_frac)
    #ax_label.axis("off")
    # xs = [0, 1200, 2400, 3600]
    # ax.set_xticks(xs)
    # ax.set_xticklabels(xs)
    axs[0, 0].set_xlabel("$t$ [yr]")
    axs[0, 0].set_ylabel(r"$\|\Omega_i|$ [m$^2$]")
    axs[0, 0].set_title('(SH, Sh) = Sv(1.2, 0.4)')

# top right 
    in_name = "CaseII_sh_40p_normal/fracture_sizes"
    data = read_pickle(in_name)
    fracture_sizes = data["fracture_sizes"]
    time_steps = np.array(data["time_steps"]) / pp.YEAR
    #fig, gs = prepare_plotting(figsize=(6, 5), widths=[2], heights=[1, 5])  # , 3, 3, 3
    #ax_label = fig.add_subplot(gs[0, 0])
    #ax = fig.add_subplot(gs[1, 0])
    #linestyles = ["-", "-", "-", "-", "--"]
    n_frac = fracture_sizes.shape[1]
    for frac in range(n_frac):
        
        label = "$\Omega_{}$".format(frac + 2)
        axs[0, 1].plot(
                time_steps,
                fracture_sizes[:, frac],
                color=colors[frac],
     #           ls=linestyles[frac],
                )
     #   ax_label.plot([], label=label, color=colors[frac])
    
    #ax_label.legend(loc="center", frameon=False, ncol=n_frac)
    #ax_label.axis("off")
    # xs = [0, 1200, 2400, 3600]
    # ax.set_xticks(xs)
    # ax.set_xticklabels(xs)

    axs[0, 1].set_xlabel("$t$ [yr]")
    axs[0, 1].set_ylabel(r"$\|\Omega_i|$ [m$^2$]")    
    axs[0, 1].set_title('(SH, Sh) = Sv(0.8, 0.4)')
# bottom left

    in_name = case_path + "CaseI_sh_60p/fracture_sizes"
    data = read_pickle(in_name)
    fracture_sizes = data["fracture_sizes"]
    time_steps = np.array(data["time_steps"]) / pp.YEAR
    #fig, gs = prepare_plotting(figsize=(6, 5), widths=[2], heights=[1, 5])  # , 3, 3, 3
    #ax_label = fig.add_subplot(gs[0, 0])
    #ax = fig.add_subplot(gs[1, 0])
    #linestyles = ["-", "-", "-", "-", "--"]
    n_frac = fracture_sizes.shape[1]
    for frac in range(n_frac):
        
        label = "$\Omega_{}$".format(frac + 2)
        axs[1, 0].plot(
                time_steps,
                fracture_sizes[:, frac],
                color=colors[frac],
     #           ls=linestyles[frac],
                )
     #   ax_label.plot([], label=label, color=colors[frac])
    
    #ax_label.legend(loc="center", frameon=False, ncol=n_frac)
    #ax_label.axis("off")
    # xs = [0, 1200, 2400, 3600]
    # ax.set_xticks(xs)
    # ax.set_xticklabels(xs)
    axs[1, 0].set_xlabel("$t$ [yr]")
    axs[1, 0].set_ylabel(r"$\|\Omega_i|$ [m$^2$]")
    axs[1, 0].set_title('(SH, Sh) = Sv(1.2, 0.6)')
# bottom right 
    in_name = case_path + "CaseI_sh_60p_normal/fracture_sizes"
    data = read_pickle(in_name)
    fracture_sizes = data["fracture_sizes"]
    time_steps = np.array(data["time_steps"]) / pp.YEAR
    #fig, gs = prepare_plotting(figsize=(6, 5), widths=[2], heights=[1, 5])  # , 3, 3, 3
    #ax_label = fig.add_subplot(gs[0, 0])
    #ax = fig.add_subplot(gs[1, 0])
    #linestyles = ["-", "-", "-", "-", "--"]
    n_frac = fracture_sizes.shape[1]
    for frac in range(n_frac):
        
        label = "$\Omega_{}$".format(frac + 2)
        axs[1, 1].plot(
                time_steps,
                fracture_sizes[:, frac],
                color=colors[frac],
     #           ls=linestyles[frac],
                )
     #   ax_label.plot([], label=label, color=colors[frac])
    
    #ax_label.legend(loc="center", frameon=False, ncol=n_frac)
    #ax_label.axis("off")
    # xs = [0, 1200, 2400, 3600]
    # ax.set_xticks(xs)
    # ax.set_xticklabels(xs)

    axs[1, 1].set_xlabel("$t$ [yr]")
    axs[1, 1].set_ylabel(r"$\|\Omega_i|$ [m$^2$]")        
    axs[1, 1].set_title('(SH, Sh) = Sv(0.8, 0.6)')    
    
    fig.tight_layout()
    plt.savefig(save_path + "Case_compare.pdf")
    plt.show()




#plot_applications("exIV")
plot_ex_IV()

# plot_ex_I()
# plot_ex_II()
