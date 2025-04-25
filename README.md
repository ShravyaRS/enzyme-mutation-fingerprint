# Enzyme Mutation Fingerprint

This research project investigates the **mutation resilience of two enzymes** — Lysyl Oxidase (LOX) and Glutamate Decarboxylase (GAD) — using a **binary amino acid fingerprint encoding model**. It combines sequence analysis and structure parsing to model how each amino acid contributes to overall enzyme stability and function in the presence of mutations.

---

## 🔬 Project Objectives

- To analyze the sequence and structure of LOX and GAD enzymes.
- To convert amino acids into binary-encoded fingerprints.
- To map these fingerprints across the enzyme structure.
- To enable visualization of the enzyme 3D structures using PDB data.
- *(Optional future work: Add co-impact mutation matrix and functional impact prediction.)*

---

## 🧬 Features

- ✅ Binary fingerprint encoding for each amino acid residue.
- ✅ Parsing of `.pdb` files to extract and process enzyme sequences.
- ✅ Integrated visualization of enzyme 3D structures.
- 📌 Ready for extension to include mutation co-impact matrices.

---

## 📁 Folder Structure

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/enzyme-mutation-fingerprint.git
cd enzyme-mutation-fingerprint

Install dependencies
pip install biopython nglview

To parse and encode fingerprints:
bash
Copy
Edit
cd scripts
python structure_parser.py

o visualize enzyme 3D structure:
(Run in Jupyter Notebook for best results)

python
Copy
Edit
from visualize_structure import visualize_pdb
view = visualize_pdb("../data/LOX.pdb")  # Or GAD.pdb
view

Sample Output (Console)
python-repl
Copy
Edit
First 5 Fingerprints:
000000000001
000000000010
000000000100
...
📚 References
Protein Data Bank (PDB): https://www.rcsb.org

Biopython documentation: https://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ

NGLView: https://nglviewer.org/nglview/latest/

