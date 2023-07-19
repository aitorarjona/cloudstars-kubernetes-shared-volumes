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

procA = [
    2424832,
    2363392,
    2359296,
    3026944,
    73207808,
    141705216,
    236212224,
    310038528,
    401874944,
    503767040,
    542228480,
    542257152,
    542232576,
    542240768,
    542236672,
    542232576,
    542236672,
    542236672,
    542236672,
    542187520,
    542228480,
    542228480,
    542134272,
    542105600,
    542236672,
    542015488,
    542232576,
    542232576,
    542130176,
    542232576,
    542138368,
    542150656,
    542244864,
    542240768,
    542232576,
    542228480,
    542236672,
    542228480,
    542232576,
    540475392,
    540479488,
    540479488,
    540475392,
    540483584,
    540491776,
    540471296,
]

procB = [
    2441216,
    2387968,
    2383872,
    2310144,
    2379776,
    2383872,
    2387968,
    2383872,
    2396160,
    2383872,
    2379776,
    2392064,
    3117056,
    3112960,
    3112960,
    3104768,
    3112960,
    3108864,
    3121152,
    3268608,
    3174400,
    3375104,
    3387392,
    3297280,
    3375104,
    3411968,
    3452928,
    3293184,
    3555328,
    3715072,
    3670016,
    3842048,
    3866624,
    3903488,
    3796992,
    3825664,
    4059136,
    3809280,
    4206592,
    3559424,
    2396160,
    2408448,
    2396160,
    2404352,
    2281472,
    2396160,
]


if __name__ == "__main__":
    # sns.set_theme()

    fig, ax = plt.subplots()

    ax.plot(np.arange(0, len(procA)), np.asarray(procA) * 1e-6, label="Writer process")
    ax.plot(np.arange(0, len(procB)), np.asarray(procB) * 1e-6, label="Reader process")

    ax.grid(ls=":", alpha=0.5)

    ax.set_xlabel("Wallclock time (s)")
    ax.set_ylabel("cgroups memory usage (MB)")

    ax.set_yscale("log")

    ax.legend()
    fig.set_size_inches(4, 3)
    fig.tight_layout()

    plt.savefig("mem_usage_writer_reader.pdf")
