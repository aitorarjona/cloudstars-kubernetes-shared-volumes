import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

alloc_T = [10, 440]
free_T = [340]


if __name__ == "__main__":
    sns.set_theme()

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

    ax.set_xlabel("Wallclock time (s)")
    ax.set_ylabel("Memory (GB)")

    ax.legend(loc="upper left")
    fig.tight_layout()

    plt.savefig("plot4.png", dpi=500)
