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

🧬 Mutation Prediction and Analysis
This project involves analyzing mutations in two enzymes, Lysyl Oxidase (LOX) and Glutamate Decarboxylase (GAD), to study their resilience using binary fingerprint encoding and mutation co-impact matrices. The mutation prediction process can be divided into several stages:
1. Mutation Data Collection:
Mutations in the enzyme sequences are collected from public mutation databases or experimental data (if available).
You can also predict potential mutations using tools like AlphaFold2 for structure-based mutation analysis.
2. Mutation Mapping:
Predicted or known mutations are mapped onto the enzyme's amino acid sequence.
Mutations are categorized into specific residue positions and the type of change (e.g., substitution, insertion, or deletion).
3. Mutation Fingerprint Encoding:
Each mutation is encoded as a binary fingerprint representing the altered residue's properties.
This encoding helps analyze the impact of mutations on enzyme function by comparing differences in polarity, charge, hydrophobicity, and other characteristics of amino acids.
4. Mutation Hotspot Identification:
Areas in the enzyme sequence where mutations frequently occur or have high functional impact are identified as mutation hotspots.
These hotspots are visualized in the enzyme's 3D structure, highlighting residues that may be crucial for function or stability.
5. Co-impact Matrix Generation:
A mutation co-impact matrix is generated to understand how mutations in one part of the enzyme might affect other regions or residues.
This matrix can help identify residue pairs that are more likely to influence each other’s functionality when mutated.
6. Potential Disease Association:
The predicted mutations are analyzed for their potential links to diseases or functional deficiencies.
Mutation mapping with disease-linked databases like ClinVar or dbSNP can provide further insights.

🔮 Future Work
AlphaFold Integration: Integrate AlphaFold2 predictions to enhance the accuracy of mutation models, helping to predict the effect of mutations on the 3D structure of enzymes.
Mutation Prediction Enhancement: Implement tools like SIFT or PolyPhen to predict the functional impact of mutations on enzyme stability and function.
Interactive Mutation Visualizations: Develop interactive visualizations using Py3Dmol or other tools to view mutations directly on 3D structures of enzymes, with color-coded mutation hotspots and residue interactions.
Multi-enzyme Mutation Clustering: Extend the analysis to multiple enzymes to generate mutation resilience clusters, identifying broader mutation patterns and evolutionary insights.
