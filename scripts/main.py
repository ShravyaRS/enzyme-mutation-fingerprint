from structure_parser import parse_pdb, encode_sequence
from fingerprint_encoder import encode_amino_acid
from visualize_pdb import visualize_structure
from mutation_matrix import generate_coimpact_matrix, plot_coimpact_matrix

def main():
    pdb_file = "data/lox.pdb"  # Adjust to your file path

    # Step 1: Parse PDB file and encode sequence
    sequence = parse_pdb(pdb_file)
    fingerprints = encode_sequence(sequence)
    print(f"Encoded fingerprints: {fingerprints}")

    # Step 2: Visualize the structure in 3D
    visualize_structure(pdb_file)

    # Step 3: Generate and plot the mutation co-impact matrix
    coimpact_matrix = generate_coimpact_matrix(fingerprints)
    plot_coimpact_matrix(coimpact_matrix)

if __name__ == "__main__":
    main()
