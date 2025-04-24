# Enzyme Mutation Resilience Using Binary Fingerprints

This project focuses on the study of enzyme mutation resilience, particularly for the **TPH1** and **PAH** enzymes. We aim to assess how mutations in these enzymes affect their functions by creating a **mutation co-impact matrix** using **binary fingerprint encoding**.

## Project Overview

In this research, we analyze the **TPH1** and **PAH** enzymes' structures to identify key mutations that influence enzyme stability and activity. Using **Biopython**, we parse enzyme structure files (MM-CIF format) and apply **binary fingerprint encoding** to generate structural descriptors. Additionally, we develop a **mutation co-impact matrix** to evaluate the interaction and potential impact of mutations within the enzyme structure.

### Objective

The main objectives of this project are to:
- Extract structural data of **TPH1** and **PAH** enzymes.
- Encode amino acids using binary fingerprints based on their physicochemical properties.
- Develop a mutation co-impact matrix to predict potential mutations affecting enzyme function.

## Methods

### 1. **Enzyme Structure Parsing**
   We use the **Biopython MMCIFParser** to parse enzyme structure files. These files contain detailed 3D atomic structures of enzymes, from which relevant data points (e.g., residues, chain IDs, atom coordinates) are extracted.

### 2. **Binary Fingerprint Encoding**
   Each amino acid residue in the enzyme is encoded into a binary fingerprint representing its physicochemical properties. These fingerprints are used to represent the enzyme structure in a simplified and computationally efficient way.

### 3. **Mutation Co-Impact Matrix**
   We then build a mutation co-impact matrix that identifies potential interactions between different residues in the enzyme. By analyzing mutations across these residues, we determine which mutations may have the most significant effect on enzyme stability or function.

## Requirements

To run this project, you'll need the following dependencies:

- Python 3.x
- Biopython (for enzyme structure parsing)
- NumPy (for matrix operations)

You can install the dependencies by running the following:

```bash
pip install -r requirements.txt
Installation
git clone https://github.com/ShravyaRS/enzyme-mutation-fingerprint.git
cd enzyme-mutation-fingerprint
Virtual environment
python -m venv venv

On Windows:
bash
Copy code
venv\Scripts\activate

On macOS/Linux:
bash
Copy code
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Script Overview
scripts/fingerprint_encoder.py: This script encodes the amino acid sequences into binary fingerprints based on their physicochemical properties.

scripts/structure_parser.py: This script parses enzyme structure files (MM-CIF format) to extract relevant data points like residues, chain IDs, and atom coordinates.

scripts/mutation_impact_matrix.py: This script builds a mutation co-impact matrix to evaluate the interactions and potential impacts of mutations.

scripts/test_script.py: A simple test script to check if the Git setup and scripts are functioning as expected

To run the test script:
bash
Copy code
python scripts/test_script.py

Contribution
Feel free to fork the repository and submit pull requests for improvements. Issues can be raised in the Issues tab for any bugs or feature requests.

Note: The test script is designed to ensure all other scripts are functioning correctly. If you encounter any issues with the test script, double-check that your environment is set up properly and that all dependencies are installed.




