# Get basic information about an MD trajectory (Informatics)

## Description
This tool reads in a molecular dynamics trajectory and reports basic information about the trajectory, including the number of frames, timestep and total length of the simulation.

## Input
* trajectory_file - A trajectory file in the format .binops, .lh5, .xml, .arc, .dcd, .dtr, .hdf5, .h5, .netcdf, .trr, .xtc, .prmtop, .xyz, .lammpstrj, .hoomdxml
* topology_file - when the trajectory file does not contain topological information, this parameter specifies the topologies in the trajectory. This is usually a .pdb file

## Output
Length and timestep about the trajectory

## Setup
### requirements
mdtraj