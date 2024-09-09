import mdtraj as md
import matplotlib.pyplot as plt
from datetime import datetime

def create_timestamp() -> str:
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

def get_resname_from_resid(resid):
    """resid will be resname+res_index, i.e. ALA100. This function extracts the resname part"""
    resname = ""
    for char in resid:
        if not char.isdigit():
            resname += char
    return resname

def run(trajectory_file, topology_file=None, reference_frame=0, selection="all"):
    # load the trajectory
    try:
        traj = md.load(trajectory_file)
    except:
        try:
            traj = md.load(trajectory_file, top=topology_file)
        except:
            print("Cannot read trajectory file. Please check your input files!")
            return
    
    # get basic infos
    timestep = traj.timestep
    sim_time = traj.time * timestep

    units = ['ps', 'ns', 'μs', 'ms', 's']
    unit_level = 0
    while sim_time[-1] >= 1000 and unit_level < 4:
        sim_time /= 1000
        unit_level += 1

    # processing selection logic
    if selection == "all":
        atoms = None
    elif selection in ["protein", "backbone"]:
        atoms = traj.topology.select(selection)
    elif selection == "CA":
        atoms = traj.topology.select("name CA")
    elif selection == "non_water":
        atoms = traj.topology.select("not water")
    else:
        # it would be either a ligand residue name, or the "ligand" keyword
        # get all ligand names
        ligands = [res.name for res in traj.topology.residues if res.is_protein == False]
        if selection == "ligand":
            assert len(ligands) == 1, "There are multiple ligands in the system. Please use an explicit ligand name."
            atoms = traj.topology.select("resname " + ligands[0])
        elif selection in ligands:
            atoms = traj.topology.select("resname " + selection)
        else:
            print('Invalid selection. It can only be one of the following options: ["all", "protein", "backbone", "CA", "ligand", "non_water", or a certain ligand residue name]')
            return

    rmsds = md.rmsd(traj, traj, frame=reference_frame, atom_indices=atoms) * 10 # converting nm to angstrom

    # draw figure
    filename = f"rmsd.{create_timestamp()}.svg"
    plt.figure(figsize=(8, 6))
    # update font size
    plt.rcParams.update({'font.size': 20})
    plt.plot(sim_time, rmsds)
    plt.xlabel("Simulation time (" + units[unit_level] + ")")
    plt.ylabel("RMSD (Å)")
    plt.savefig(filename)
    print(f"RMSD plot created as: {filename}")
    return rmsds

if __name__ == "__main__":
    print(run('prod_align.xtc', 'prod_align.pdb', selection="ligand"))