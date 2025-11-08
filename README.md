# AI-Based 3D Mesh Optimization System

## 📌 Project Overview
This project implements an AI-driven 3D mesh optimization pipeline that performs:

- Mesh Structure Inspection  
- Adaptive Normalization (Min–Max and Unit-Sphere)  
- Quantization of Vertex Coordinates  
- Mesh Reconstruction  
- Error Measurement Using Mean Squared Error (MSE)

The goal is to compare how different normalization methods affect the fidelity of 3D mesh reconstruction.

---

## 🧠 Key Features
| Feature | Description |
|--------|-------------|
| Mesh Inspection | Extracts centroid, bounding box, spread, and vertex statistics |
| Adaptive Normalization | Automatically decides optimal method based on geometry |
| Quantization Support | Converts vertices to fixed integer precision |
| Reconstruction | Restores mesh structure from quantized form |
| Error Evaluation | Calculates per-axis & overall MSE values |

---

## 🗂️ Project Structure
AI-Mesh-Optimization/
│
├── data/ # Sample input 3D mesh models
│ └── cube.obj
│
├── scripts/ # Core project scripts
│ ├── load_inspect.py # Mesh inspection & statistical analysis
│ ├── normalize_quantize.py # Normalization + quantization pipeline
│ ├── reconstruct_error.py # Reconstruction & MSE computation
│
├── scripts/outputs/ # Reconstructed meshes (auto generated)
│ ├── reconstructed_min_max.ply
│ └── reconstructed_unit_sphere.ply
│
├── scripts/figures/ # Error visualization graphs (auto generated)
│ ├── mse_per_axis.png
│ └── error_histogram.png
│
├── outputs/
│ └── Final_Report.pdf # Final submission-ready project report
│
└── README.md # Project documentation


---

## ⚙️ How to Run

### 1. Install Dependencies
```bash
pip install numpy trimesh reportlab
python scripts/load_inspect.py data/cube.obj
python scripts/normalize_quantize.py data/cube.obj outputs/
python scripts/reconstruct_error.py data/cube.obj outputs/reconstructed_min_max.ply
python scripts/reconstruct_error.py data/cube.obj outputs/reconstructed_unit_sphere.ply

📊 Results Summary
Normalization Method	Overall MSE (Lower = Better)
Min–Max	1.12500000
Unit-Sphere	2.35048110

➡ Conclusion: Min–Max normalization gives better reconstruction accuracy for this mesh.

👤 Author

Hariharan B
Register No: RA2211004040028
SRM Institute of Science and Technology
Department of Electronics and Communication Engineering

⭐ Status

✅ Project Completed
✅ Report Generated
✅ Ready for Submission
