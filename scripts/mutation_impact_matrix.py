import numpy as np
from fingerprint_encoder import encode_amino_acid

def create_mutation_matrix(structure_file):
    # Initialize matrix size based on number of residues
    residue_positions = []
    fingerprints = []

    # Read structure and store residues and their fingerprints
    with open(structure_file, "r") as f:
        # For simplicity, let's assume we already parsed residues
        # In reality, you'd parse the structure just like before
        residue_positions = ["MET", "TYR", "ALA"]  # Example positions
        for res in residue_positions:
            fingerprints.append(encode_amino_acid(res))

    # Create a mutation matrix (size: num_residues x num_residues)
    num_residues = len(residue_positions)
    matrix = np.zeros((num_residues, num_residues))

    # Compare fingerprints for each pair of residues
    for i in range(num_residues):
        for j in range(i + 1, num_residues):
            # Example: Calculating Hamming distance between binary fingerprints
            diff = sum(np.array(fingerprints[i]) != np.array(fingerprints[j]))
            matrix[i][j] = diff
            matrix[j][i] = diff

    return matrix

if __name__ == "__main__":
    mutation_matrix = create_mutation_matrix("data/1lox.cif")
    print("Mutation Co-Impact Matrix:")
    print(mutation_matrix)
