import os
import json
import csv
import matplotlib.pyplot as plt
from Bio.PDB import PDBParser, MMCIFParser
from collections import Counter

DATA_DIR = "data"
RESULT_JSON = os.path.join(DATA_DIR, "encoded_sequences.json")
RESULT_CSV = os.path.join(DATA_DIR, "encoded_sequences.csv")
RESULTS_PLOT_DIR = os.path.join(DATA_DIR, "plots")

# Amino acid mapping (one-hot encoding)
AMINO_ACIDS = [
    "ALA", "ARG", "ASN", "ASP", "CYS",
    "GLN", "GLU", "GLY", "HIS", "ILE",
    "LEU", "LYS", "MET", "PHE", "PRO",
    "SER", "THR", "TRP", "TYR", "VAL"
]

def encode_amino_acid(res):
    return [1 if res == aa else 0 for aa in AMINO_ACIDS]

def parse_structure(file_path):
    """Parse PDB or CIF file and extract sequence."""
    if file_path.endswith(".pdb"):
        parser = PDBParser(QUIET=True)
    elif file_path.endswith(".cif"):
        parser = MMCIFParser(QUIET=True)
    else:
        return None

    structure = parser.get_structure("struct", file_path)
    sequence = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if "CA" in residue:  # Alpha carbon filter
                    sequence.append(residue.get_resname())
    return sequence

def save_results(all_results):
    """Save extracted data to JSON and CSV."""
    os.makedirs(DATA_DIR, exist_ok=True)

    # JSON full detail
    with open(RESULT_JSON, "w") as jf:
        json.dump(all_results, jf, indent=4)

    # CSV summary
    with open(RESULT_CSV, "w", newline="") as cf:
        writer = csv.writer(cf)
        writer.writerow(["File", "Length", "First_5_Residues"])
        for fname, data in all_results.items():
            writer.writerow([fname, len(data["sequence"]), " ".join(data["sequence"][:5])])

def generate_plots(all_results):
    """Generate figures for research documentation."""
    os.makedirs(RESULTS_PLOT_DIR, exist_ok=True)

    # 1. Sequence length distribution
    lengths = [len(data["sequence"]) for data in all_results.values()]
    plt.hist(lengths, bins=20, color="skyblue", edgecolor="black")
    plt.xlabel("Sequence Length")
    plt.ylabel("Count")
    plt.title("Sequence Length Distribution")
    plt.savefig(os.path.join(RESULTS_PLOT_DIR, "sequence_length_distribution.png"))
    plt.close()

    # 2. Amino acid frequency
    aa_counts = Counter()
    for data in all_results.values():
        aa_counts.update(data["sequence"])
    aa_sorted = [aa for aa in AMINO_ACIDS if aa in aa_counts]
    counts = [aa_counts[aa] for aa in aa_sorted]
    plt.bar(aa_sorted, counts, color="orange")
    plt.xticks(rotation=90)
    plt.xlabel("Amino Acid")
    plt.ylabel("Frequency")
    plt.title("Amino Acid Composition")
    plt.savefig(os.path.join(RESULTS_PLOT_DIR, "amino_acid_composition.png"))
    plt.close()

    # 3. CIF vs PDB consistency
    pdb_lengths, cif_lengths = [], []
    for fname, data in all_results.items():
        if fname.endswith(".pdb"):
            base = fname.replace(".pdb", "")
            if base + ".cif" in all_results:
                pdb_lengths.append(len(data["sequence"]))
                cif_lengths.append(len(all_results[base + ".cif"]["sequence"]))
    if pdb_lengths:
        plt.scatter(pdb_lengths, cif_lengths, c="green")
        plt.plot([min(pdb_lengths), max(pdb_lengths)], [min(pdb_lengths), max(pdb_lengths)], "r--")
        plt.xlabel("PDB Length")
        plt.ylabel("CIF Length")
        plt.title("CIF vs PDB Consistency")
        plt.savefig(os.path.join(RESULTS_PLOT_DIR, "cif_vs_pdb_consistency.png"))
        plt.close()

if __name__ == "__main__":
    all_results = {}
    for fname in os.listdir(DATA_DIR):
        if fname.endswith(".pdb") or fname.endswith(".cif"):
            fpath = os.path.join(DATA_DIR, fname)
            seq = parse_structure(fpath)
            if seq:
                all_results[fname] = {
                    "sequence": seq,
                    "fingerprints": [encode_amino_acid(res) for res in seq]
                }
                print(f"✅ {fname}: length={len(seq)} | First 5 residues: {seq[:5]}")

    save_results(all_results)
    generate_plots(all_results)

    print(f"\n📂 Saved results -> {RESULT_JSON} & {RESULT_CSV}")
    print(f"📊 Figures saved -> {RESULTS_PLOT_DIR}")
