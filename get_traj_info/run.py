import mdtraj as md


def run(trajectory_file, topology_file=None):
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
    length = traj.n_frames
    timestep = traj.timestep
    sim_time = traj.time[-1] * timestep

    units = ['ps', 'ns', 'μs', 'ms', 's']
    unit_level = 0
    while sim_time >= 1000 and unit_level < 4:
        sim_time /= 1000
        unit_level += 1

    print(f"Length of trajectory: {length} frames")
    print(f"Time step: {timestep} ps")
    print(f"Simulation time: {sim_time} {units[unit_level]}")

if __name__ == "__main__":
    run('prod_align.xtc', 'prod_align.pdb')