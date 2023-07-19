import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams.update(
    {
        "text.usetex": True,
        # "font.family": "serif",
        "pgf.texsystem": "pdflatex",
        "font.size": 9,
        # "font.size": 10,
        # "pgf.preamble": "\n".join(
        #     [
        #         r"\usepackage{libertine}",
        #         # r"\usepackage{lmodern}",
        #     ]
        # ),
        # "lines.linewidth": 0.8,
        "lines.markersize": 3,
        # "axes.linewidth": 0.5,
        # "grid.linewidth": 0.3,
        "grid.linestyle": ":",
        # "axes.edgecolor": matplotlib.rcParams["grid.color"],
        # "ytick.color": matplotlib.rcParams["grid.color"],
        # "ytick.direction": "in",
        # "xtick.color": matplotlib.rcParams["grid.color"],
        # "xtick.direction": "in",
        # "axes.titlesize": "medium",
        # "axes.titlepad": 2,
        # "axes.labelpad": 1,
        # "axes.spines.top": False,
        # "axes.spines.right": False,
        # "axes.spines.bottom": False,
        # "axes.spines.left": False,
        # "legend.labelspacing": 0,
        # "legend.handlelength": 1,
        # "legend.handletextpad": 0.2,
        # "legend.columnspacing": 1,
        # "legend.borderpad": 0,
    }
)

proc = [
    2334720,
    2244608,
    2379776,
    2387968,
    2392064,
    2387968,
    25665536,
    115929088,
    244097024,
    267161600,
    267177984,
    267177984,
    267210752,
    267190272,
    267182080,
]

killed_T = 9

if __name__ == "__main__":
    # sns.set_theme()

    fig, ax = plt.subplots()

    ax.plot(np.arange(0, len(proc)), np.asarray(proc) * 1e-6)
    ax.axvline(x=killed_T, c="red", ls="--", label="Process OOM killed")

    ax.grid(ls=":", alpha=0.5)

    ax.set_xlabel("Wallclock time (s)")
    ax.set_ylabel("cgroups memory usage (MB)")

    ax.legend()
    fig.set_size_inches(4, 3)
    fig.tight_layout()

    plt.savefig("oom.pdf")
