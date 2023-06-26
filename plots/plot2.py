import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
    sns.set_theme()

    fig, ax = plt.subplots()

    ax.plot(np.arange(0, len(proc)), np.asarray(proc) * 1e-6)
    ax.axvline(x=killed_T, c="red", ls="--", label="Process OOM killed")

    ax.set_xlabel("Wallclock time (s)")
    ax.set_ylabel("cgroups memory usage (MB)")

    ax.legend()
    fig.tight_layout()

    plt.savefig("plot2.png", dpi=500)
