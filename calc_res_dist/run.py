import mdtraj as md
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

def create_timestamp() -> str:
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

def get_idx_from_resid(resid):
    """resid will be resname+res_index, i.e. ALA100. This function extracts the index part (100) as a string"""
    resname = ""
    idx = ""
    for char in resid:
        if not char.isdigit():
            resname += char
        else:
            idx += char
    if resname + idx != resid:
        raise RuntimeError("Invalid resid! It should be resname+res_index, i.e. ALA100")
    return idx

def run(trajectory_file, topology_file=None, residue1="", atom1="", residue2="", atom2=""):
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

    # identify the atom indices
    all_restags = [str(residue) for residue in traj.topology.residues]
    all_resSeqs = [str(residue.resSeq) for residue in traj.topology.residues]
    if not residue1.isdigit():
        assert residue1 in all_restags, f"Cannot find {residue1} in the structure"
        residx1 = all_restags.index(residue1)
    else:
        assert residue1 in all_resSeqs, f"Cannot find residue {residue1} in the structure"
        residx1 = all_resSeqs.index(residue1)
        residue1 = str(traj.topology.residue(residx1))

    if not residue2.isdigit():
        assert residue2 in all_restags, f"Cannot find {residue2} in the structure"
        residx2 = all_restags.index(residue2)
    else:
        assert residue2 in all_resSeqs, f"Cannot find residue {residue2} in the structure"
        residx2 = all_resSeqs.index(residue2)
        residue2 = str(traj.topology.residue(residx2))

    # identify the actual atom idx
    atom_idx1 = traj.topology.select(f"resid {residx1} and name {atom1}")
    atom_idx2 = traj.topology.select(f"resid {residx2} and name {atom2}")
    assert len(atom_idx1) == 1, f"Cannot identify atom {atom1} in residue {residue1}"
    assert len(atom_idx2) == 1, f"Cannot identify atom {atom2} in residue {residue2}"

    atom_pairs = [[atom_idx1[0], atom_idx2[0]]]
    dists = md.compute_distances(traj, atom_pairs)[:, 0] * 10 # converting nm to angstrom

    # draw figure
    filename = f"dist.{create_timestamp()}.svg"
    plt.figure(figsize=(10, 6))
    # update font size
    plt.rcParams.update({'font.size': 20})
    plt.plot(sim_time, dists)
    plt.xlabel("Simulation time (" + units[unit_level] + ")")
    plt.ylabel(f"$d$({residue1}-{atom1}, {residue2}-{atom2}) (Å)")
    plt.savefig(filename)
    print(f"Distance plot created as: {filename}")

    # save numerical data
    df = pd.Series(dists, name="Pairwise Distance")
    csv_filename = f"dist.{create_timestamp()}.csv"
    df.to_csv(csv_filename)
    print(f"Distance values saved in: {csv_filename}")

if __name__ == "__main__":
    print(run('../test_files/prod_align.xtc', '../test_files/prod_align.pdb', "142", "OE1", "600", "H35"))
    # print(run('../test_files/6OIM_traj.xtc', '../test_files/6OIM_coord.pdb', "12", "SG", "338", "C25"))