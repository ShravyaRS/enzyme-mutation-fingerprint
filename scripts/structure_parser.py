import argparse

def parse_pdb(pdb_file):
    """Extracts the amino acid sequence from a PDB file and encodes each residue."""
    sequence = []
    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith("ATOM") and line[13:15].strip() == "CA":  # Only alpha-carbon atoms
                resname = line[17:20].strip()  # Amino acid name
                sequence.append(resname)
    return sequence

def encode_amino_acid(residue):
    """Simple example encoder: convert residue names into binary-like fingerprints."""
    amino_acids = [
        'ALA','ARG','ASN','ASP','CYS','GLN','GLU','GLY','HIS','ILE',
        'LEU','LYS','MET','PHE','PRO','SER','THR','TRP','TYR','VAL'
    ]
    fingerprint = [0] * len(amino_acids)
    if residue in amino_acids:
        fingerprint[amino_acids.index(residue)] = 1
    return fingerprint

def encode_sequence(sequence):
    """Encodes an entire amino acid sequence into binary fingerprints."""
    fingerprints = [encode_amino_acid(res) for res in sequence]
    return fingerprints

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse a PDB file and encode sequence")
    parser.add_argument("--pdb", required=True, help="Path to the PDB file")
    args = parser.parse_args()

    sequence = parse_pdb(args.pdb)
    fingerprints = encode_sequence(sequence)

    print(f"Parsed sequence length: {len(sequence)} residues")
    print(f"Encoded sequence (first 5 residues): {fingerprints[:5]}")
