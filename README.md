# Enzyme Mutation Fingerprint Analysis

This project focuses on **mutation resilience analysis** in enzymes using **binary fingerprint encoding** and **dual mutation co-impact matrices**. The two enzymes analyzed are:

- **Lysyl Oxidase (LOX)** – involved in connective tissue cross-linking
- **Glutamate Decarboxylase (GAD)** – key in neurotransmitter GABA synthesis

---

## 🔬 Key Features

- Parses `.pdb` structural data of LOX and GAD enzymes
- Encodes amino acid sequences into **binary fingerprints**
- Compares mutation resilience between enzymes
- Visualizes 3D structures with residue highlights

---

## 📁 Directory Overview

- `data/`: Contains raw `.pdb` files for LOX and GAD
- `scripts/`: Main Python scripts:
  - `fingerprint_encoder.py` – Binary encoding logic
  - `structure_parser.py` – Extracts sequence from `.pdb`
  - `visualize_pdb.py` – 3D viewer using Py3Dmol
- `results/`: Will contain fingerprint comparisons and graphs

---

## 🧪 Getting Started

### 1. Set up environment (Recommended: Python 3.9)

```bash
pip install -r requirements.txt

Run structural parser
bash
Copy
Edit
python scripts/structure_parser.py

Visualize structures
bash
Copy
Edit
python scripts/visualize_pdb.py

📊 Mutation Fingerprint Concept
Each amino acid is assigned a fixed-length binary vector representing:
Polarity
Charge
Hydrophobicity
Size
These fingerprints enable:
Easy comparison of mutational impacts
Co-impact matrix generation across enzyme domains

📌 Future Scope
Integrate AlphaFold2 predicted mutations
Predict disease-linked residue vulnerability
Extend to multi-enzyme mutation resilience clusters

🧬 Credits
Sequence & structure: RCSB PDB
Py3Dmol for structure visualization
Created as part of a bioinformatics research initiative 
