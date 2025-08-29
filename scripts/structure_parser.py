# scripts/structure_parser.py

import os
import json
import csv
from Bio.PDB import PDBParser, MMCIFParser

# === Amino acid encoding dictionary (20-D binary) ===
AA_DICT = {
    "ALA": 0, "CYS": 1, "ASP": 2, "GLU": 3, "PHE": 4,
    "GLY": 5, "HIS": 6, "ILE": 7, "LYS": 8, "LEU": 9,
    "MET": 10, "ASN": 11, "PRO": 12, "GLN": 13, "ARG": 14,
    "SER": 15, "THR": 16, "VAL": 17, "TRP": 18, "TYR": 19
}

def encode_amino_acid(resname):
    """One-hot encode a residue into a 20-length vector."""
    vec = [0] * 20
    if resname in AA_DICT:
        vec[AA_DICT[resname]] = 1
    return vec

def parse_structure(file_path):
    """Extract residue sequence from CIF/PDB using CA atoms."""
    ext = os.path.splitext(file_path)[1].lower()
    parser = MMCIFParser(QUIET=True) if ext == ".cif" else PDBParser(QUIET=True)

    structure = parser.get_structure("protein", file_path)
    sequence = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if "CA" in residue:  # Only count residues with CA atom
                    sequence.append(residue.get_resname())
    return sequence

if __name__ == "__main__":
    data_dir = "data"
    results = {}

    for file in os.listdir(data_dir):
        if file.endswith((".cif", ".pdb")):
            path = os.path.join(data_dir, file)
            try:
                sequence = parse_structure(path)
                fingerprints = [encode_amino_acid(res) for res in sequence]

                results[file] = {
                    "length": len(sequence),
                    "sequence": sequence,
                    "fingerprints": fingerprints
                }

                print(f"✅ {file}: length={len(sequence)} | First 5 residues: {sequence[:5]}")

            except Exception as e:
                print(f"❌ Error with {file}: {e}")

    # === Save JSON (full details) ===
    with open("data/encoded_sequences.json", "w") as jf:
        json.dump(results, jf, indent=2)

    # === Save CSV (summary only) ===
    with open("data/encoded_sequences.csv", "w", newline="") as cf:
        writer = csv.writer(cf)
        writer.writerow(["File", "Length", "First 10 residues"])
        for f, data in results.items():
            writer.writerow([f, data["length"], " ".join(data["sequence"][:10])])

    print("\n📂 Saved results -> data/encoded_sequences.json & data/encoded_sequences.csv")
