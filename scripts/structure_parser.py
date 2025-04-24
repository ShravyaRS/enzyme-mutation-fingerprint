from Bio.PDB.MMCIFParser import MMCIFParser
from fingerprint_encoder import encode_amino_acid

def parse_structure(file_path):
    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure("enzyme", file_path)

    for model in structure:
        for chain in model:
            print(f"\n--- Chain {chain.id} ---")
            for residue in chain:
                if residue.id[0] == ' ':
                    res_id = residue.id[1]
                    res_name = residue.resname
                    fingerprint = encode_amino_acid(res_name)
                    print(f"Residue {res_name} at position {res_id} → {fingerprint}")

if __name__ == "__main__":
    parse_structure("data/1lox.cif")
