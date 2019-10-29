import networkx as nx 
import MDAnalysis as mda
from MDAnalysis.analysis import contacts 
import numpy as np
import itertools


class Network():
    def __init__(self, trajectory, topology, cutoff=5):
        self.u = mda.Universe(trajectory,topology)
        self.cutoff = cutoff
    
    def compute_average_contacts(self, cutoff=5, selection1="protein", selection2="protein"):
        atoms_1, atoms_2 = self.u.select_atoms(selection1), universe.select_atoms(selection2)
        ca = contacts.Contacts(self.u, selection=(selection1, selection2),
                        refgroup=(atoms_1, atoms_2), radius=self.cutoff)
        ca.run()
        return np.mean(ca.timeseries[:, 1])

if __name__ == '__main__':
    Network(,).compute_average_contacts()