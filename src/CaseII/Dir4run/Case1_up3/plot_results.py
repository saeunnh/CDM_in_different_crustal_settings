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
save_path = "/home/saeunn/Numerical-modelling-of-convection-driven-cooling-deformation-and-fracturing-of-thermo-poroelastic-m/src/CaseI_update3/"
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


def plot_ex_I():
    in_name = "exI/all_errors"
    # Axes for the error array are poisson ratios, mesh sizes and the three
    # errors computed (for apertures, SIF_I, SIF_II).
    data = read_pickle(in_name)
    errors = data["all_errors"]
    poisson_ratios = data["poisson_ratios"]
    mesh_sizes = data["mesh_sizes"]

    # ax_label = fig.add_subplot(gs[0, :])
    error_labels = ["$E_{I}$", "$E_{II}$"]
    file_names = ["exI/errors_I.pdf", "exI/errors_II.pdf"]
    for mode in range(2):

        fig = plt.figure()
        ax = fig.add_subplot(111)
        sif_errors = errors[:, :, mode]
        w = 0.02
        for i in range(mesh_sizes.size):
            ax.bar(
                poisson_ratios + (i - 1.5) * w,
                sif_errors[:, i],
                color=colors[i],
                width=w,
                label=mesh_sizes[i],
            )

        ax.set_xlabel(r"$\nu$")
        ax.set_ylabel(error_labels[mode])

        ax.set_xticks(poisson_ratios)
        if mode == 1:
            ax.legend(title="$h$")
        fig.tight_layout()
        plt.savefig(save_path + file_names[mode])
        plt.show()


def plot_ex_II():
    plt.figure()

    in_name = "exII/fracture_sizes"
    data = read_pickle(in_name)
    fracture_sizes = data["fracture_sizes"]
    export_times = data["export_times"]
    time_steps = data["time_steps"][:]
    n_cells = data["n_cells"][:]
    fig, gs = prepare_plotting(figsize=(6, 5), widths=[5], heights=[0.2, 0.1, 4])
    ax_label = fig.add_subplot(gs[0, 0])
    ax_label_ref = fig.add_subplot(gs[1, 0])
    ax = fig.add_subplot(gs[2, 0])
    linestyles = ["-", "dashed", "dotted", "dashdot", (0, (3, 10, 1, 10)), "dotted"]
    for i, dt in enumerate(time_steps):
        for j, nx in enumerate(n_cells):
            times = np.array(export_times[(dt, nx)]) / pp.HOUR
            length = fracture_sizes[(dt, nx)][:, 0]
            label = "$dt$: ${},\ 1/h$: ${}$".format(dt, nx)
            ax.plot(
                times,
                length,
                color=colors[i],
                linestyle=linestyles[j],
                label=label,
            )
            ax_label.plot([], linestyle=linestyles[j], label=label, color=colors[i])
    # Add reference
    in_name = "exII_ref/fracture_sizes"
    data = read_pickle(in_name)
    fracture_sizes = data["fracture_sizes"]
    times = np.linspace(0, 14400, 577) / pp.HOUR
    dt = data["time_steps"][0]
    nx = data["n_cells"][-1]
    length = fracture_sizes[(dt, nx)][:, 0]
    label = "Reference: $dt$: ${},\ 1/h$: ${}$".format(dt, nx)
    ls = "-"  # linestyles[-1]
    ax.plot(
        times,
        length,
        color="black",
        linestyle=ls,
        label=label,
        linewidth=0.7,
    )
    ax_label_ref.plot([], linestyle=ls, label=label, color="black")

    ax_label.legend(loc="center", frameon=False, ncol=time_steps.size)
    ax_label.axis("off")
    ax_label_ref.legend(loc="center", frameon=False, ncol=1)
    ax_label_ref.axis("off")
    xs = np.arange(0, 5)  # [0, 1200, 2400, ]
    ax.set_xticks(xs)
    ax.set_xticklabels(xs)

    ax.set_xlabel("$t$ [h]")
    ax.set_ylabel(r"$\|\Omega_2|$ [m]")
    fig.tight_layout()
    plt.savefig(save_path + "exII/fracture_size.pdf")
    plt.show()


def plot_ex_IV():
    plt.figure()
    in_name = "CaseI_sh_60p_normal/fracture_sizes"
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
    plt.savefig(save_path + "CaseI_60p_normal.pdf")
    plt.show()


def plot_applications(folder):
    plt.figure()
    in_name = folder + "/fracture_sizes"
    data = read_pickle(in_name)
    fracture_sizes = data["fracture_sizes"]
    time_steps = np.array(data["time_steps"]) / pp.YEAR

    fig, gs = prepare_plotting(figsize=(6, 5), widths=[2], heights=[1, 5])  # , 3, 3, 3
    ax_label = fig.add_subplot(gs[0, 0])
    ax = fig.add_subplot(gs[1, 0])
    linestyles = ["-", "-", "-", "--", "--"]
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
    ax_label.legend(loc="center", frameon=False, ncol=n_frac, fontsize=12)
    ax_label.axis("off")
    # xs = [0, 1200, 2400, 3600]
    # ax.set_xticks(xs)
    # ax.set_xticklabels(xs)

    ax.set_xlabel("$t$ [yr]")
    ax.set_ylabel(r"$\|\Omega_i|$ [m$^2$]")
    fig.tight_layout()
    plt.savefig(save_path + "/" + folder + "/fracture_size.pdf")
    plt.show()


def plot_ex_III():
    plt.figure()
    in_name = "exIII/fracture_sizes"
    data = read_pickle(in_name)
    fracture_sizes = data["fracture_sizes"]
    pressures = data["pressures"]
    temperatures = data["temperatures"]
    time_steps = np.array(data["time_steps"]) / pp.YEAR

    fig, gs = prepare_plotting(figsize=(6, 5), widths=[2], heights=[1, 5])  # , 3, 3, 3
    ax_label = fig.add_subplot(gs[0, 0])
    ax = fig.add_subplot(gs[1, 0])
    ax_T = ax.twinx()
    linestyles = ["-", "-", "-", "--", "--"]
    n_frac = fracture_sizes.shape[1]
    for frac in range(n_frac):

        label = "$\Omega_{}$".format(frac + 2)
        ax.plot(
            time_steps,
            pressures[:, frac],
            color=colors[frac],
            ls="-",
        )
        ax_T.plot(
            time_steps,
            temperatures[:, frac],
            color=colors[frac],
            ls="--",
        )
        ax_label.plot([], label="$p_{}$".format(frac + 2), ls="-", color=colors[frac])
        ax_label.plot([], label="$T_{}$".format(frac + 2), ls="--", color=colors[frac])

    ax_label.legend(loc="center", frameon=False, ncol=4, fontsize=12)
    ax_label.axis("off")
    # xs = [0, 1200, 2400, 3600]
    # ax.set_xticks(xs)
    # ax.set_xticklabels(xs)

    ax.set_xlabel("$t$ [yr]")
    ax.set_ylabel(r"$p$ [Pa]")
    ax_T.set_ylabel(r"$T$ [K]")
    fig.tight_layout()
    plt.savefig(save_path + "/exIII/pressure_and_temperature.pdf")
    plt.show()


#plot_applications("exIV")
plot_ex_IV()

# plot_ex_I()
# plot_ex_II()
