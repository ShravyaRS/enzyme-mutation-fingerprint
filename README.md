# Enzyme Mutation Fingerprint Analysis

Mutation resilience analysis in enzymes using binary fingerprint encoding and dual mutation co-impact matrices. The two enzymes analyzed are Lysyl Oxidase (LOX), involved in connective tissue cross-linking, and Glutamate Decarboxylase (GAD), key in neurotransmitter GABA synthesis.

---

## Features

- Parses `.pdb` structural data of LOX and GAD enzymes
- Encodes amino acid sequences into binary fingerprints (polarity, charge, hydrophobicity, size)
- Compares mutation resilience between enzymes
- Generates co-impact matrices to identify critical mutation hotspots
- Visualizes 3D structures with mutated residue highlights using Py3Dmol

---

## Directory Structure
```
enzyme-mutation-fingerprint/
├── data/                       Raw .pdb files for LOX and GAD
├── scripts/
│   ├── structure_parser.py     Extracts amino acid sequence from PDB files
│   ├── fingerprint_encoder.py  Binary encoding of amino acid properties
│   ├── mutation_analysis.py    Mutation resilience comparison and co-impact matrix
│   └── visualize_pdb.py       3D visualization using Py3Dmol
├── main.py                     Main entry point
├── requirements.txt
└── README.md
```

## Getting Started
```bash
git clone https://github.com/ShravyaRS/enzyme-mutation-fingerprint.git
cd enzyme-mutation-fingerprint
pip install -r requirements.txt
```

## Usage

Parse enzyme sequence and structure:
```bash
python scripts/structure_parser.py
```

Generate binary fingerprints:
```bash
python scripts/fingerprint_encoder.py
```

Visualize enzyme structures with mutation highlights:
```bash
python scripts/visualize_pdb.py
```

## Mutation Fingerprint Concept

Each amino acid is assigned a fixed-length binary vector representing polarity, charge, hydrophobicity, and size. These fingerprints enable straightforward comparison of mutational impacts and co-impact matrix generation across enzyme domains.

## Credits

- [RCSB PDB](https://www.rcsb.org/) for enzyme structural data
- [Py3Dmol](https://3dmol.csb.pitt.edu/) for structure visualization

## License

MIT License. See [LICENSE](LICENSE) for details.
