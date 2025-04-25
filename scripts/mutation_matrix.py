import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def generate_coimpact_matrix(fingerprints):
    """Generates a co-impact matrix comparing mutation resilience across domains."""
    matrix = np.dot(fingerprints, np.transpose(fingerprints))
    return matrix

def plot_coimpact_matrix(matrix):
    """Plots the co-impact matrix as a heatmap."""
    sns.heatmap(matrix, cmap="YlGnBu", annot=True)
    plt.title("Mutation Co-Impact Matrix")
    plt.show()

if __name__ == "__main__":
    # Example fingerprints (use real data from your project)
    example_fingerprints = np.array([
        encode_amino_acid("ALA"),
        encode_amino_acid("VAL"),
        encode_amino_acid("LEU")
    ])
    coimpact_matrix = generate_coimpact_matrix(example_fingerprints)
    plot_coimpact_matrix(coimpact_matrix)
