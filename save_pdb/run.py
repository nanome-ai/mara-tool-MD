import mdtraj as md
from datetime import datetime

def create_timestamp() -> str:
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

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
    
    # save the trajectory to a pdb file
    output_file = f"trajectory.{create_timestamp()}.pdb"
    traj.save(output_file)
    print(f"Trajectory saved to: {output_file}")