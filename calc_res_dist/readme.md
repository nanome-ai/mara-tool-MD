Calculate pairwise distance from an MD trajectory (Informatics)

Input: trajectory_file - A trajectory file in the format .binops, .lh5, .xml, .arc, .dcd, .dtr, .hdf5, .h5, .netcdf, .trr, .xtc, .prmtop, .xyz, .lammpstrj, .hoomdxml; topology_file - when the trajectory file does not contain topological information, this parameter specifies the topologies in the trajectory. This is usually a .pdb file; residue1 - full name of a residue, i.e. ALA100, or just the residue index; atom1 - name of the atom in residue 1; residue2 - full name of a residue or just the residue index; atom2 - name of the atom in residue 2
Output: List of pairwise distance values (in the unit of Angstrom) throughout the trajectory and a figure showing the pairwise atom distance over time
This tool reads in a molecular dynamics trajectory and calculates the pairwise distance between two atoms throughout the trajectory. 

# requirements
mdtraj
matplotlib