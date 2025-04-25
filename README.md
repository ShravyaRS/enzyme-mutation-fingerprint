# Enzyme Mutation Fingerprint Analysis

This project focuses on **mutation resilience analysis** in enzymes using **binary fingerprint encoding** and **dual mutation co-impact matrices**. The two enzymes analyzed are:

- **Lysyl Oxidase (LOX)** – involved in connective tissue cross-linking
- **Glutamate Decarboxylase (GAD)** – key in neurotransmitter GABA synthesis

---

## Project Overview
## Enzyme Mutation Fingerprint Analysis

This project focuses on analyzing mutations in two enzymes, **Lysyl Oxidase (LOX)** and **Glutamate Decarboxylase (GAD)**, to study mutation resilience. We use **binary fingerprint encoding** to analyze amino acid changes and **mutation co-impact matrices** to identify the most critical mutation hotspots.

The project includes:
- **Enzyme sequence analysis** and **mutation prediction** using structural data.
- **3D visualization** of enzymes with mutation highlights.
- **Tools to compare mutation impacts** across enzyme structures.

## Installation

To run this project locally, you'll need Python and the necessary dependencies. Here's how you can set it up:

1. Clone the repository:
   ```bash
   git clone https://github.com/ShravyaRS/enzyme-mutation-fingerprint.git
   cd enzyme-mutation-fingerprint

Set up the environment:
Make sure you're using Python 3.9 or higher.
Install the required dependencies:
bash
Copy
Edit
pip install -r requirements.txt

  
### 3. **Usage Instructions**

Explain how to use each script in your project.

#### Example:
```markdown
## Usage

### 1. Parse Enzyme Sequence and Structure

Run the `structure_parser.py` script to extract the amino acid sequence from a PDB file.

```bash
python scripts/structure_parser.py

## Visualize Enzyme Structure with Mutations
python scripts/fingerprint_encoder.py

### 4. **Detailed Explanation of Scripts**

Provide a brief explanation of what each script does. This helps users understand how the code works and how to use it effectively.

#### Example:
```markdown
## Scripts

### `structure_parser.py`
- **Function**: Extracts the amino acid sequence from a PDB file.
- **Usage**: Run this script on a PDB file to get the amino acid sequence for analysis.

### `visualize_pdb.py`
- **Function**: Visualizes enzyme 3D structures using Py3Dmol, highlighting mutated residues.
- **Usage**: Visualize the enzyme structures with mutations mapped onto them.

### `fingerprint_encoder.py`
- **Function**: Encodes the amino acid sequence into binary fingerprints.
- **Usage**: Encode the sequence to represent properties like charge, polarity, size, etc.

### `mutation_analysis.py`
- **Function**: Analyzes mutation resilience by comparing mutation fingerprints and generating a co-impact matrix.
- **Usage**: Compare mutation impacts across multiple enzyme sequences.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request with your changes. Here’s how you can contribute:

1. Fork the repository.
2. Create a branch for your feature or bug fix.
3. Write tests if applicable.
4. Update the documentation (if applicable).
5. Submit a pull request.

We follow the **[Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/)**, and ask that you be respectful to others.
 
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

🔬 Mutation Visualization
This project includes visualization tools that allow you to observe mutations on the 3D structures of enzymes.
Py3Dmol: A Python-based visualization tool that renders enzyme structures and highlights mutated residues.
Steps to Visualize:
Run scripts/visualize_pdb.py to load and visualize enzyme structures.
Mutations are highlighted in a distinct color to show their positions on the enzyme.
You can rotate and zoom in the 3D view to better analyze mutation impacts.


🔬 Mutation Visualization
This project includes tools to visualize mutations on the 3D structures of enzymes, aiding in the identification of mutation-sensitive regions and structure-preserving zones.

🧪 Tools Used
Py3Dmol: A Python-based visualization tool that renders enzyme structures and highlights mutated residues.

🖼️ How to Visualize Mutations
Run the Visualization Script: Execute the scripts/visualize_pdb.py script to load and visualize the enzyme structures.

bash
Copy
Edit
python scripts/visualize_pdb.py
Input Files: The script requires the following input files:
A PDB file containing the enzyme structure (e.g., 1SIX.pdb).
A list of mutations to be visualized.

Output: The script generates an interactive 3D visualization of the enzyme structure with mutated residues highlighted in a distinct color.
Interactive Exploration: Users can rotate and zoom in the 3D view to better analyze mutation impacts.

📌 Example
Note: Replace path/to/your/example_image.png with the actual path to an example image showcasing the mutation visualization.

🔮 Future Work
AlphaFold Integration: Integrate AlphaFold2 predictions to enhance the accuracy of mutation models, helping to predict the effect of mutations on the 3D structure of enzymes.
Mutation Prediction Enhancement: Implement tools like SIFT or PolyPhen to predict the functional impact of mutations on enzyme stability and function.
Interactive Mutation Visualizations: Develop interactive visualizations using Py3Dmol or other tools to view mutations directly on 3D structures of enzymes, with color-coded mutation hotspots and residue interactions.
Multi-enzyme Mutation Clustering: Extend the analysis to multiple enzymes to generate mutation resilience clusters, identifying broader mutation patterns and evolutionary insights.

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
## Credits
- **RCSB PDB** for enzyme structural data.
- **Py3Dmol** for structure visualization.
- **AlphaFold2** (future enhancement) for predicting enzyme structures.

🧬 Credits
Sequence & structure: RCSB PDB
Py3Dmol for structure visualization
Created as part of a bioinformatics research initiative
