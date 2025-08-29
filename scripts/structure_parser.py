# scripts/structure_parser.py
import os, json, csv
from collections import Counter
from Bio.PDB import MMCIFParser, PDBParser, PPBuilder

DATA_DIR = "data"
OUTPUT_JSON = os.path.join(DATA_DIR, "encoded_sequences.json")
OUTPUT_CSV = os.path.join(DATA_DIR, "encoded_sequences.csv")

AMINO_ACIDS = [
    "ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY",
    "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO",
    "SER", "THR", "TRP", "TYR", "VAL"
]

def parse_structure(file_path):
    parser = MMCIFParser(QUIET=True) if file_path.endswith(".cif") else PDBParser(QUIET=True)
    structure = parser.get_structure("protein", file_path)
    ppb = PPBuilder()
    residues = []
    for pp in ppb.build_peptides(structure):
        residues.extend([res.get_resname() for res in pp])
    return residues

def main():
    results = []
    os.makedirs(DATA_DIR, exist_ok=True)

    # gather .cif and .pdb
    files = [f for f in os.listdir(DATA_DIR) if f.endswith((".cif", ".pdb"))]

    for f in files:
        path = os.path.join(DATA_DIR, f)
        residues = parse_structure(path)
        length = len(residues)
        first5 = residues[:5]

        # amino acid counts
        counts = Counter(residues)
        row = {
            "File": f,
            "Length": length,
            "First_5": " ".join(first5)
        }
        for aa in AMINO_ACIDS:
            row[aa] = counts.get(aa, 0)

        results.append(row)

        print(f"✅ {f}: length={length} | First 5 residues: {first5}")

    # save JSON
    with open(OUTPUT_JSON, "w") as jf:
        json.dump(results, jf, indent=2)

    # save CSV
    fieldnames = ["File", "Length", "First_5"] + AMINO_ACIDS
    with open(OUTPUT
