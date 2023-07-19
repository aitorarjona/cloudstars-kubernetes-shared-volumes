import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

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

alloc_T = [10, 440]
free_T = [340]


if __name__ == "__main__":
    # sns.set_theme()

    df = pd.read_csv("results/proc3-2.out")

    fig, ax = plt.subplots()

    ax.plot(np.arange(df["free"].shape[0]), df["free"] * 1e-6, label="free")
    ax.plot(np.arange(df["cache"].shape[0]), df["cache"] * 1e-6, label="cache")

    first = True
    for x in alloc_T:
        if first:
            ax.axvline(x, color="C2", ls="--", label="Memory alloc")
            first = False
        else:
            ax.axvline(x, color="C2", ls="--")

    first = True
    for x in free_T:
        if first:
            ax.axvline(x, color="C3", ls="--", label="Memory free")
            first = False
        else:
            ax.axvline(x, color="C3", ls="--")

    ax.grid(ls=":", alpha=0.5)

    ax.set_xlabel("Wallclock time (s)")
    ax.set_ylabel("Memory (GB)")

    ax.legend(loc="upper left")
    fig.set_size_inches(4, 3)
    fig.tight_layout()

    plt.savefig("vmstat.pdf")
