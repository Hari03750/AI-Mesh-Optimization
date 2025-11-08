"""
AI-Adaptive Normalization & Quantization
----------------------------------------
Chooses optimal normalization automatically and performs quantization.
"""

import numpy as np
import trimesh
from pathlib import Path
from datetime import datetime


# ---------- Normalization Methods ---------- #
def minmax_normalize(verts):
    vmin, vmax = verts.min(axis=0), verts.max(axis=0)
    denom = np.where(vmax - vmin == 0, 1, vmax - vmin)
    normalized = (verts - vmin) / denom
    return normalized, {"method": "Min-Max", "vmin": vmin, "vmax": vmax}


def unit_sphere_normalize(verts):
    centroid = verts.mean(axis=0)
    centered = verts - centroid
    maxd = np.linalg.norm(centered, axis=1).max() or 1.0
    normalized = centered / maxd
    return normalized, {"method": "Unit-Sphere", "centroid": centroid, "scale": maxd}


# ---------- Quantization ---------- #
def quantize(arr, bins=1024):
    arr01 = (arr - arr.min()) / (arr.max() - arr.min())
    return np.floor(arr01 * (bins - 1)).astype(np.int32)


def dequantize(q, bins=1024):
    return q.astype(float) / (bins - 1)


# ---------- Main AI Decision Logic ---------- #
def choose_best_method(verts):
    spread = verts.std(axis=0)
    ratio = spread.max() / (spread.min() + 1e-8)
    # heuristic: if spread very unequal -> sphere normalization
    if ratio > 2.0:
        return "Unit-Sphere"
    else:
        return "Min-Max"


def save_mesh(vertices, faces, path):
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=False)
    mesh.export(path)


# ---------- Pipeline ---------- #
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python scripts/normalize_quantize.py data/your_model.obj")
        sys.exit()

    path = Path(sys.argv[1])
    mesh = trimesh.load(path, force='mesh')
    verts, faces = np.asarray(mesh.vertices), np.asarray(mesh.faces)
    method = choose_best_method(verts)

    if method == "Min-Max":
        normed, meta = minmax_normalize(verts)
    else:
        normed, meta = unit_sphere_normalize(verts)

    q = quantize(normed)
    dq = dequantize(q)

    # reconstruct
    if method == "Min-Max":
        recon = dq * (meta["vmax"] - meta["vmin"]) + meta["vmin"]
    else:
        recon = (dq * 2 - 1) * meta["scale"] + meta["centroid"]

    outdir = Path("outputs")
    outdir.mkdir(exist_ok=True)
    save_mesh(recon, faces, outdir / f"reconstructed_{method.lower().replace('-','_')}.ply")

    print("\n🤖 AI-Adaptive Normalization & Quantization Report")
    print("──────────────────────────────────────────────")
    print(f"Model Path     : {path}")
    print(f"Chosen Method  : {method}")
    print(f"Vertices       : {len(verts):,}")
    print(f"Quantization   : 1024 levels per axis")
    print(f"Output Saved   : outputs/reconstructed_{method.lower().replace('-','_')}.ply")
    print(f"Timestamp      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("──────────────────────────────────────────────\n")
