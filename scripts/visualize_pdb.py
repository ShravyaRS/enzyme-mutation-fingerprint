import py3Dmol

def visualize_pdb(pdb_file):
    """Visualizes the PDB structure using py3Dmol."""
    with open(pdb_file, 'r') as file:
        pdb_data = file.read()

    viewer = py3Dmol.view(width=800, height=400)
    viewer.addModel(pdb_data, "pdb")
    viewer.setStyle({'stick': {}})
    viewer.zoomTo()
    viewer.show()

# Example usage
if __name__ == "__main__":
    # List of PDB files to visualize
    pdb_files = ["data/1lox.pdb", "data/1six.pdb", "data/3v08.pdb", "data/4v7w.pdb"]
    
    for pdb_file in pdb_files:
        visualize_pdb(pdb_file)
