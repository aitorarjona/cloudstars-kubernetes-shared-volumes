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
    df = pd.read_csv("storage_benchmarks/write-ephemeral.csv")
    # df = pd.read_csv("storage_benchmarks/read-ephemeral.csv")

    print(df)

    df = df.drop(df[df.mb == 10].index)
    df = df.drop(df[df.mb == "1mb"].index)

    fig, ax = plt.subplots()

    sns.boxplot(ax=ax, data=df, x="mb", y="mb/s", hue="storage")
    ax.legend_.remove()

    ax.legend(
        bbox_to_anchor=(0, 1.02, 1, 0.2),
        loc="lower center",
        ncol=3,
    )
    ax.set_xlabel("File Size (MB)")
    ax.set_ylabel("Throughput (MB/s)")
    fig.set_size_inches(4, 3)
    fig.tight_layout()

    fig.savefig("write_benchmark_ephemeral.pdf")
    # fig.savefig("read_benchmark_ephemeral.pdf")
