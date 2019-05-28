import networkx as nx 
import mdtraj as md 
import numpy as np

t = md.load()
contacts = t.compute_contacts()
print(contacts)