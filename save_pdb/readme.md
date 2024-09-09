# Convert a molecular dynamics (MD) trajectory to a PDB file (Conversion)

## Description
This tool reads in a molecular dynamics trajectory as either a single file or a combination of a trajectory file and a topology file. It then converts the trajectory to a PDB file containing all the frames in the trajectory. The output PDB file can be visualized using Mol*.


## Input
* trajectory_file - A trajectory file in the format .binops, .lh5, .xml, .arc, .dcd, .dtr, .hdf5, .h5, .netcdf, .trr, .xtc, .prmtop, .xyz, .lammpstrj, .hoomdxml
* topology_file - when the trajectory file does not contain topological information, this parameter specifies the topologies in the trajectory. This is usually a .pdb file

## Output
 a pdb file containing all the frames in the trajectory

## Setup
### requirements
mdtraj