from Bio.PDB import PDBParser, MMCIFParser

def parse_structure(file_path):
    """Parses a structure file (.pdb or .cif) and extracts amino acid sequence."""
    if file_path.endswith(".pdb"):
        parser = PDBParser(QUIET=True)
    elif file_path.endswith(".cif"):
        parser = MMCIFParser(QUIET=True)
    else:
        raise ValueError("Unsupported file format. Use .pdb or .cif")

    structure = parser.get_structure("structure", file_path)

    sequence = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if "CA" in residue:  # Use alpha-carbon only
                    sequence.append(residue.get_resname())
    return sequence


def encode_amino_acid(resname):
    """Example encoder: convert residue name into a simple one-hot vector (customize later)."""
    amino_acids = [
        "ALA","ARG","ASN","ASP","CYS","GLN","GLU","GLY",
        "HIS","ILE","LEU","LYS","MET","PHE","PRO","SER",
        "THR","TRP","TYR","VAL"
    ]
    vector = [1 if resname == aa else 0 for aa in amino_acids]
    return vector


def encode_sequence(sequence):
    """Encodes entire amino acid sequence into binary fingerprints."""
    return [encode_amino_acid(res) for res in sequence]


if __name__ == "__main__":
    file_path = "data/1lox.cif"  # Change to whichever structure you want
    sequence = parse_structure(file_path)
    fingerprints = encode_sequence(sequence)
    print(f"Extracted sequence length: {len(sequence)}")
    print(f"First 5 residues: {sequence[:5]}")
    print(f"First 5 fingerprints: {fingerprints[:5]}")
