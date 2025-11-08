# AI-Based 3D Mesh Optimization System

## 📌 Project Overview
This project implements an AI-driven 3D mesh optimization pipeline that performs:

- Mesh Structure Inspection  
- Adaptive Normalization (Min–Max and Unit-Sphere)  
- Quantization of Vertex Coordinates  
- Mesh Reconstruction  
- Error Measurement Using Mean Squared Error (MSE)

---

## 🔗 Project Links

| Resource | Link |
|---------|------|
| **GitHub Repository** | https://github.com/Hari03750/AI-Mesh-Optimization |
| **Final Report (PDF)** | [Download Final Project Report](sandbox:/mnt/data/Final_AI_Mesh_Optimization_Report.pdf) |

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
├── data/
│ └── cube.obj
│
├── scripts/
│ ├── load_inspect.py
│ ├── normalize_quantize.py
│ ├── reconstruct_error.py
│
├── scripts/outputs/
│ ├── reconstructed_min_max.ply
│ └── reconstructed_unit_sphere.ply
│
├── scripts/figures/
│ ├── mse_per_axis.png
│ └── error_histogram.png
│
├── outputs/
│ └── Final_Report.pdf
│
└── README.md

---

## 📊 Results Summary

| Normalization Method | Overall MSE (Lower = Better) |
|---------------------|-----------------------------|
| **Min–Max**         | **1.12500000** |
| **Unit-Sphere**     | **2.35048110** |

➡ **Min–Max normalization provides better reconstruction accuracy** for this model.

---

## 👤 Author
**Hariharan B**  
Register No: **RA2211004040028**  
**SRM Institute of Science and Technology**  
Department of **Electronics and Communication Engineering**

---

## ✅ Status
| Item | Status |
|------|--------|
| Project Code | ✔️ Completed |
| Error Graphs | ✔️ Generated |
| Comparison Analysis | ✔️ Included |
| Final Report | ✔️ Ready to Submit |


✅ Report Generated
✅ Ready for Submission
