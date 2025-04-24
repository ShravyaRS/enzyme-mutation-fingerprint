# Enzyme Mutation Resilience Modeling

This project models enzyme mutation resilience using binary fingerprint encoding and a Mutation Co-Impact Matrix. The study is based on enzymes such as **TPH1** and **PAH**, aiming to predict mutation impacts on enzyme stability.

## Methods
- **Structure Parsing**: Biopython's `MMCIFParser` was used to parse enzyme 3D structures.
- **Fingerprint Encoding**: Amino acids were encoded using binary fingerprints based on physical properties.
- **Mutation Co-Impact Matrix**: A pairwise comparison of residue fingerprints to determine mutation impact.

## Results
Example of a mutation co-impact matrix and residue analysis.

## Running the Scripts
1. Clone this repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run `structure_parser.py` to parse enzyme structures and generate a mutation matrix.

## License
MIT License
