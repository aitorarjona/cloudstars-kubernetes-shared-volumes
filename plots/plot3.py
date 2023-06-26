import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

if __name__ == "__main__":
    sns.set_theme()

    df = pd.read_csv("results/proc3.out")
    print(df)

    fig, ax = plt.subplots()

    ax.plot(np.arange(df["free"][0:100].shape[0]), df["free"][0:100] * 1e-6, label="free")
    ax.plot(np.arange(df["cache"][0:100].shape[0]), df["cache"][0:100] * 1e-6, label="cache")

    ax.set_xlabel("Wallclock time (s)")
    ax.set_ylabel("Memory (GB)")

    ax.legend()
    fig.tight_layout()

    plt.savefig("plot3.png", dpi=500)
