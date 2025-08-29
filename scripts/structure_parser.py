import os
from Bio.PDB import PDBParser, MMCIFParser

def parse_structure(file_path):
    """Parses a structure file (.pdb or .cif) and extracts amino acid sequence."""
    if file_path.endswith(".pdb"):
        parser = PDBParser(QUIET=True)
    elif file_path.endswith(".cif"):
        parser = MMCIFParser(QUIET=True)
    else:
        return []

    structure = parser.get_structure("structure", file_path)

    sequence = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if "CA" in residue:  # Alpha-carbon only
                    sequence.append(residue.get_resname())
    return sequence


def encode_amino_acid(resname):
    """Encodes a residue into a one-hot vector."""
    amino_acids = [
        "ALA","ARG","ASN","ASP","CYS","GLN","GLU","GLY",
        "HIS","ILE","LEU","LYS","MET","PHE","PRO","SER",
        "THR","TRP","TYR","VAL"
    ]
    return [1 if resname == aa else 0 for aa in amino_acids]


def encode_sequence(sequence):
    """Encodes entire amino acid sequence into fingerprints."""
    return [encode_amino_acid(res) for res in sequence]


if __name__ == "__main__":
    data_dir = "data"
    for file_name in os.listdir(data_dir):
        if file_name.endswith((".pdb", ".cif")):
            file_path = os.path.join(data_dir, file_name)
            try:
                sequence = parse_structure(file_path)
                fingerprints = encode_sequence(sequence)
                print(f"✅ {file_name}: length={len(sequence)}")
                print(f"   First 5 residues: {sequence[:5]}")
            except Exception as e:
                print(f"❌ Error with {file_name}: {e}")
