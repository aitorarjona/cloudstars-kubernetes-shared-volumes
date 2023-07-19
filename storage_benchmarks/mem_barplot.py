import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
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


if __name__ == "__main__":
    df = pd.read_csv("storage_benchmarks/write-mem.csv")
    # df = pd.read_csv("storage_benchmarks/read-mem.csv")

    print(df)

    fig, ax = plt.subplots()
    sns.barplot(
        ax=ax,
        data=df,
        x="mb",
        y="gb/s",
        hue="storage",
        estimator=np.mean,
        errorbar=("ci", 95),
        capsize=0.2,
    )
    ax.legend_.remove()

    ax.legend(
        bbox_to_anchor=(0, 1.02, 1, 0.2),
        loc="lower center",
        ncol=2,
    )
    ax.set_xlabel("File Size (MB)")
    ax.set_ylabel("Throughput (GB/s)")
    fig.set_size_inches(4, 3)
    fig.tight_layout()

    fig.savefig("write_benchmark_mem.pdf")
    # fig.savefig("read_benchmark_mem.pdf")
