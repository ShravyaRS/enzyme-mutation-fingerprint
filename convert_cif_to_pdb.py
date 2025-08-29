from Bio.PDB import MMCIFParser, PDBIO
import os

# Input and output folders
input_dir = "data"
output_dir = "data"

parser = MMCIFParser(QUIET=True)
io = PDBIO()

for file in os.listdir(input_dir):
    if file.endswith(".cif"):
        cif_path = os.path.join(input_dir, file)
        pdb_path = os.path.join(output_dir, file.replace(".cif", ".pdb"))

        structure = parser.get_structure(file, cif_path)
        io.set_structure(structure)
        io.save(pdb_path)
        print(f"✅ Converted {file} → {pdb_path}")
