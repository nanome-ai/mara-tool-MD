Calculate RMSD from an MD trajectory (Informatics)

Input: trajectory_file - A trajectory file in the format .binops, .lh5, .xml, .arc, .dcd, .dtr, .hdf5, .h5, .netcdf, .trr, .xtc, .prmtop, .xyz, .lammpstrj, .hoomdxml; topology_file - when the trajectory file does not contain topological information, this parameter specifies the topologies in the trajectory. This is usually a .pdb file; reference_frame - which frame the RMSD calculation is based on, usually 0 (the first frame); selection - can be one of ["all", "protein", "backbone", "CA", "ligand" (only when there is one ligand in the trajectory), "non_water", or a certain ligand residue name] When the user asks to calculate RMSD based on a ligand or a certain ligand name, you should run this tool directly with user specified ligand name (or the keyword "ligand") with this tool, without using other tools.
Output: List of RMSD values (in the unit of Angstrom) and a figure showing the RMSD values over time
This tool reads in a molecular dynamics trajectory and calculates the RMSD for either the whole system, for protein only or for ligand only. 

# requirements
mdtraj
matplotlib