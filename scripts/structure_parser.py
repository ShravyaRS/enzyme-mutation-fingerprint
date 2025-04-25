def parse_pdb(pdb_file):
    """Extracts the amino acid sequence from a PDB file and encodes each residue."""
    sequence = []
    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith("ATOM") and line[13:15].strip() == "CA":  # Only alpha-carbon atoms
                resname = line[17:20].strip()  # Amino acid name
                sequence.append(resname)
    return sequence

def encode_sequence(sequence):
    """Encodes an entire amino acid sequence into binary fingerprints."""
    fingerprints = [encode_amino_acid(res) for res in sequence]
    return fingerprints

if __name__ == "__main__":
    pdb_file = "data/lox.pdb"  # Adjust to your file path
    sequence = parse_pdb(pdb_file)
    fingerprints = encode_sequence(sequence)
    print(f"Encoded sequence: {fingerprints}")
