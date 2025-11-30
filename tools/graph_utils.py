import matplotlib.pyplot as plt
from io import BytesIO
import base64

def create_graph_base64(x, y, xlabel, ylabel, topic):
    plt.style.use("seaborn-v0_8-whitegrid")

    fig, ax = plt.subplots(figsize=(7, 4), dpi=120)
    fig.patch.set_facecolor("#f7f7f7")
    ax.set_facecolor("white")

    ax.plot(
        x, y,
        color="#4A90E2",
        linewidth=3,
        marker="o",
        markersize=7,
        markerfacecolor="white",
        markeredgewidth=2
    )

    ax.set_title(topic, fontsize=18, pad=15)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.grid(True, linestyle="--", alpha=0.6)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    buffer = BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    encoded = base64.b64encode(buffer.read()).decode()

    plt.close()
    return encoded
