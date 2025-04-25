# Amino acid binary fingerprint dictionary
amino_acid_fingerprints = {
    "ALA": [1, 0, 0, 1, 0],  # small, non-polar
    "ARG": [0, 1, 1, 0, 0],  # large, +charge
    "ASN": [0, 0, 1, 0, 0],  # polar
    "ASP": [0, 1, 0, 0, 0],  # -charge
    "CYS": [1, 0, 0, 1, 0],  # small, polar
    "GLN": [0, 0, 1, 0, 0],  # polar
    "GLU": [0, 1, 0, 0, 0],  # -charge
    "GLY": [1, 0, 0, 1, 0],  # small, non-polar
    "HIS": [0, 1, 1, 0, 1],  # +charge, aromatic
    "ILE": [1, 0, 0, 1, 0],  # small, non-polar
    "LEU": [1, 0, 0, 1, 0],  # non-polar
    "LYS": [0, 1, 1, 0, 0],  # +charge
    "MET": [1, 0, 0, 1, 0],  # small, non-polar
    "PHE": [0, 0, 0, 1, 1],  # aromatic
    "PRO": [1, 0, 0, 1, 0],  # small, non-polar
    "SER": [1, 0, 1, 0, 0],  # polar
    "THR": [1, 0, 1, 0, 0],  # polar
    "TRP": [0, 0, 0, 1, 1],  # aromatic
    "TYR": [0, 0, 1, 1, 1],  # aromatic, polar
    "VAL": [1, 0, 0, 1, 0],  # small, non-polar
}

def encode_amino_acid(resname):
    """Encodes amino acid properties into a binary fingerprint."""
    return amino_acid_fingerprints.get(resname, [0, 0, 0, 0, 0])

# Example usage
if __name__ == "__main__":
    test_res = "TYR"
    print(f"{test_res} → {encode_amino_acid(test_res)}")
