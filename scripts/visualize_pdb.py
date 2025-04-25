import py3Dmol

def visualize_structure(pdb_file):
    """Visualizes the structure of a PDB file using Py3Dmol."""
    with open(pdb_file, 'r') as file:
        pdb_data = file.read()

    viewer = py3Dmol.view(width=800, height=400)
    viewer.addModel(pdb_data, "pdb")
    viewer.setStyle({'stick': {}})
    viewer.zoomTo()
    viewer.show()

if __name__ == "__main__":
    pdb_file = "data/lox.pdb"  # Adjust to your file path
    visualize_structure(pdb_file)
