# Amino acid binary fingerprint dictionary
amino_acid_fingerprints = {
    "ALA": [1, 0, 0, 1, 0],  # small, non-polar
    "ARG": [0, 1, 1, 0, 0],  # large, +charge
    "ASN": [0, 0, 1, 0, 0],  # polar
    "ASP": [0, 1, 0, 0, 0],  # -charge
    "CYS": [1, 0, 0, 1, 0],  # small, polar
    "GLN": [0, 0, 1, 0, 0],
    "GLU": [0, 1, 0, 0, 0],
    "GLY": [1, 0, 0, 1, 0],
    "HIS": [0, 1, 1, 0, 1],  # +charge, aromatic
    "ILE": [1, 0, 0, 1, 0],
    "LEU": [1, 0, 0, 1, 0],
    "LYS": [0, 1, 1, 0, 0],
    "MET": [1, 0, 0, 1, 0],
    "PHE": [0, 0, 0, 1, 1],  # aromatic
    "PRO": [1, 0, 0, 1, 0],
    "SER": [1, 0, 1, 0, 0],
    "THR": [1, 0, 1, 0, 0],
    "TRP": [0, 0, 0, 1, 1],
    "TYR": [0, 0, 1, 1, 1],
    "VAL": [1, 0, 0, 1, 0],
}

def encode_amino_acid(resname):
    return amino_acid_fingerprints.get(resname, [0, 0, 0, 0, 0])

# Example usage:
if __name__ == "__main__":
    test_res = "TYR"
    print(f"{test_res} → {encode_amino_acid(test_res)}")
