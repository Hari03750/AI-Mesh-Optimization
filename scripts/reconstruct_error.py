"""
AI-Based Error Evaluation & Visualization
-----------------------------------------
Compares original vs reconstructed meshes,
computes error metrics, and plots visual results.
"""

import numpy as np
import matplotlib.pyplot as plt
import trimesh
from pathlib import Path
from datetime import datetime


# ---------- Metrics ---------- #
def mse(a, b):
    return np.mean((a - b) ** 2, axis=0)

def mae(a, b):
    return np.mean(np.abs(a - b), axis=0)

def overall_mse(a, b):
    return np.mean(np.sum((a - b) ** 2, axis=1))


# ---------- Main Pipeline ---------- #
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python scripts/reconstruct_error.py data/cube.obj outputs/reconstructed_min_max.ply")
        sys.exit()

    orig_path = Path(sys.argv[1])
    recon_path = Path(sys.argv[2])

    mesh_orig = trimesh.load(orig_path, force='mesh')
    mesh_recon = trimesh.load(recon_path, force='mesh')

    v1, v2 = np.asarray(mesh_orig.vertices), np.asarray(mesh_recon.vertices)
    if v1.shape != v2.shape:
        print("⚠️ Warning: vertex counts differ, resizing to smallest set")
        n = min(len(v1), len(v2))
        v1, v2 = v1[:n], v2[:n]

    mse_axis = mse(v1, v2)
    mae_axis = mae(v1, v2)
    overall = overall_mse(v1, v2)

    print("\n📊 AI Error Analysis Report")
    print("──────────────────────────────────────────────")
    print(f"Original Mesh    : {orig_path.name}")
    print(f"Reconstructed    : {recon_path.name}")
    print(f"MSE per axis     : X={mse_axis[0]:.6f}, Y={mse_axis[1]:.6f}, Z={mse_axis[2]:.6f}")
    print(f"MAE per axis     : X={mae_axis[0]:.6f}, Y={mae_axis[1]:.6f}, Z={mae_axis[2]:.6f}")
    print(f"Overall MSE      : {overall:.8f}")
    print(f"Timestamp        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("──────────────────────────────────────────────")

    dominant_axis = ['X', 'Y', 'Z'][np.argmax(mse_axis)]
    print("🤖 AI Interpretation:")
    if overall < 1e-5:
        print(" - Excellent reconstruction fidelity, minimal quantization loss.")
    elif overall < 1e-3:
        print(" - Good reconstruction quality with minor quantization error.")
    else:
        print(" - Notable geometric error detected; consider higher bin count or alternate normalization.")
    print(f" - Highest variance observed along {dominant_axis}-axis.\n")

    # ---------- Visualization ---------- #
    Path("figures").mkdir(exist_ok=True)
    plt.figure(figsize=(6, 4))
    plt.bar(["X", "Y", "Z"], mse_axis)
    plt.title("MSE per Axis")
    plt.xlabel("Axis")
    plt.ylabel("MSE")
    plt.tight_layout()
    plt.savefig("figures/mse_per_axis.png")
    plt.close()

    # Per-vertex Euclidean error histogram
    errors = np.linalg.norm(v1 - v2, axis=1)
    plt.figure(figsize=(6, 4))
    plt.hist(errors, bins=50)
    plt.title("Per-Vertex Euclidean Error")
    plt.xlabel("Error magnitude")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("figures/error_histogram.png")
    plt.close()

    print("📁 Figures saved in 'figures/' (mse_per_axis.png, error_histogram.png)\n")
