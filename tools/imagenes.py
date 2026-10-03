"""Generate social-preview images (1280x640) and the LinkedIn banner (1584x396).

Same visual identity as ``assets/banner.svg``: wine gradient, dot grid, a faint
normal density and mathematical symbols. Run from the repo root::

    python tools/imagenes.py

Outputs go to ``assets/social/``. Upload each ``preview_<repo>.png`` in the
repo's Settings > General > Social preview, and ``linkedin_banner.png`` as the
LinkedIn background photo.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

OUT = Path("assets/social")
SANS = ["Segoe UI", "Arial", "DejaVu Sans"]
MATH = ["Cambria", "DejaVu Serif"]
WHITE, PINK = "#FFFFFF", "#F3D9DC"
WINE = LinearSegmentedColormap.from_list("wine", ["#4A0F17", "#7A1F2B", "#9C3341"])

PROJECTS = {
    "muestreo-complejo-ser-estudiante": dict(
        title="Complex survey sampling",
        question="How wrong is an analysis that ignores the sampling design?",
        stats=["Standard errors understated 1.8 to 3.8 times",
               "98 / 98 survey estimates verified by hand"],
        tags="R · survey · tidyverse · 50,578 students"),
    "eda-limpieza-defunciones-ecuador-pandas-sql": dict(
        title="Messy-data EDA",
        question="What must be fixed before trusting an official registry?",
        stats=["369,685 disguised missing values found",
               "Cleaning pipeline reproduces 58 / 58 columns"],
        tags="Python · pandas · SQL · Ecuador deaths 2021"),
    "regresion-lineal-numpy-desde-cero": dict(
        title="Linear regression from scratch",
        question="Can a plane predict how deep Ecuador's earthquakes are?",
        stats=["Existence and uniqueness of the minimizer proved",
               "Matches scikit-learn to 2.84e-13"],
        tags="Python · NumPy · optimization · USGS 2010–2025"),
    "algebra-lineal-visual-numpy": dict(
        title="Visual linear algebra",
        question="What does a matrix do, geometrically?",
        stats=["98.86 % of image energy kept with k = 2",
               "PCA = SVD of centered data, proved and checked"],
        tags="Python · NumPy · SVD · eigenvalues"),
}


def background(w: int, h: int, curve_x: float, curve_w: float):
    """Draw the shared background on a figure of w x h pixels."""
    fig = plt.figure(figsize=(w / 100, h / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w)
    ax.set_ylim(h, 0)
    ax.axis("off")
    yy, xx = np.mgrid[0:1:200j, 0:1:200j]
    ax.imshow((xx + yy) / 2, cmap=WINE, extent=(0, w, h, 0), aspect="auto")
    gx, gy = np.meshgrid(np.arange(2, w, 24), np.arange(2, h, 24))
    ax.scatter(gx, gy, s=1.4, c=WHITE, alpha=0.07, linewidths=0)
    base = h * 0.87
    x = np.linspace(curve_x - curve_w, curve_x + curve_w, 400)
    y = base - h * 0.55 * np.exp(-0.5 * ((x - curve_x) / (curve_w / 3.2)) ** 2)
    ax.plot(x, y, color=PINK, alpha=0.45, lw=3)
    ax.fill_between(x, y, base, where=np.abs(x - curve_x) <= curve_w / 3.2,
                    color=PINK, alpha=0.08, lw=0)
    ax.plot([curve_x - curve_w, curve_x + curve_w], [base, base], color=PINK, alpha=0.25, lw=1.5)
    return fig, ax


def symbols(ax, items):
    for x, y, s, size in items:
        ax.text(x, y, s, fontsize=size, color=WHITE, alpha=0.13, family=MATH, va="baseline")


def preview(repo: str, p: dict) -> None:
    w, h = 1280, 640
    fig, ax = background(w, h, curve_x=1020, curve_w=330)
    symbols(ax, [(1150, 110, "∑", 54), (760, 150, "∫", 46), (1190, 300, "∂", 34), (900, 95, "λ", 26)])
    t = dict(family=SANS, va="baseline")
    ax.text(80, 120, "EDUARDO ARAQUE · PORTFOLIO", fontsize=15, color=PINK, alpha=0.85, weight="bold", **t)
    ax.text(78, 215, p["title"], fontsize=46 if len(p["title"]) <= 24 else 40,
            color=WHITE, weight="bold", **t)
    ax.text(80, 280, p["question"], fontsize=21, color=WHITE, style="italic", alpha=0.92, **t)
    for i, s in enumerate(p["stats"]):
        ax.text(80, 380 + 52 * i, "▸  " + s, fontsize=21, color=PINK, **t)
    ax.text(80, 545, p["tags"], fontsize=16, color=PINK, alpha=0.85, **t)
    ax.text(80, 590, f"github.com/Eduardo0602/{repo}", fontsize=14, color=WHITE, alpha=0.6, **t)
    fig.savefig(OUT / f"preview_{repo}.png", dpi=100)
    plt.close(fig)


def linkedin_banner() -> None:
    # The profile photo covers the lower-left corner on desktop: text goes right.
    w, h = 1584, 396
    fig, ax = background(w, h, curve_x=560, curve_w=300)
    symbols(ax, [(330, 120, "∑", 50), (150, 150, "∫", 42), (250, 300, "∀ε>0", 26), (820, 290, "λ", 26)])
    t = dict(family=SANS, va="baseline", ha="right")
    ax.text(1520, 140, "Mathematician · Statistics · Data Science", fontsize=30, color=WHITE, weight="bold", **t)
    ax.text(1520, 195, "Survey sampling · Forecasting · Predictive models with honest validation",
            fontsize=17, color=PINK, **t)
    ax.text(1520, 245, "I prove why a method works, then I make it work on real data.",
            fontsize=17, color=WHITE, style="italic", alpha=0.92, **t)
    ax.text(1520, 320, "R · Python · SQL · LaTeX   |   github.com/Eduardo0602", fontsize=15,
            color=PINK, alpha=0.85, **t)
    fig.savefig(OUT / "linkedin_banner.png", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for repo, p in PROJECTS.items():
        preview(repo, p)
    linkedin_banner()
    print("\n".join(sorted(str(f) for f in OUT.glob("*.png"))))
