"""
AI-Smart Mesh Inspector
-----------------------
Loads a 3D OBJ mesh, analyzes its geometry, and prints a human-style summary.
Author : Your Name
Date   : 2025-11-08
"""

import numpy as np
import trimesh
from datetime import datetime


def load_mesh(file_path: str):
    """Loads a mesh file and returns both the mesh object and its vertices."""
    mesh = trimesh.load(file_path, force='mesh')

    if not hasattr(mesh, 'vertices'):
        raise TypeError("❌ The loaded file is not a valid 3D mesh.")

    vertices = np.asarray(mesh.vertices)
    faces = np.asarray(mesh.faces) if hasattr(mesh, 'faces') else None
    return mesh, vertices, faces


def compute_statistics(vertices: np.ndarray):
    """Compute geometric statistics: min, max, mean, std, and bounding box size."""
    mins = vertices.min(axis=0)
    maxs = vertices.max(axis=0)
    means = vertices.mean(axis=0)
    stds = vertices.std(axis=0)
    bbox_size = maxs - mins
    return mins, maxs, means, stds, bbox_size


def generate_ai_report(name: str, mins, maxs, means, stds, bbox_size, vertex_count):
    """Generates a natural-language summary that sounds like an AI analysis."""
    print("\n🧠 AI-Generated Mesh Analysis Report")
    print("──────────────────────────────────────────────")
    print(f"Mesh Name       : {name}")
    print(f"Timestamp       : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Vertex Count    : {vertex_count:,}")
    print(f"Bounding Box    : {bbox_size.round(4)} (x, y, z)")
    print(f"Centroid (mean) : {means.round(4)}")
    print(f"Spread (std dev): {stds.round(4)}\n")

    # Simple interpretation
    dominant_axis = ['X', 'Y', 'Z'][np.argmax(bbox_size)]
    print(f"🔍 Interpretation:")
    print(f" - The model spans roughly {bbox_size.max():.3f} units, "
          f"with its largest dimension along the {dominant_axis}-axis.")
    if np.allclose(stds, stds.mean(), rtol=0.2):
        print(" - The shape appears roughly symmetric across axes.")
    else:
        print(" - The geometry seems elongated or irregular along "
              f"the {dominant_axis}-axis.")
    print("──────────────────────────────────────────────\n")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python scripts/load_inspect.py data/your_model.obj")
        sys.exit()

    file_path = sys.argv[1]
    mesh, verts, faces = load_mesh(file_path)
    mins, maxs, means, stds, bbox_size = compute_statistics(verts)

    generate_ai_report(file_path, mins, maxs, means, stds, bbox_size, len(verts))
