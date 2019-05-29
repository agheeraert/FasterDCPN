import networkx as nx 
import mdtraj as md 
import numpy as np
import itertools

chunks = md.iterload('/home/agheerae/PDB/prot_apo_sim1_s10.dcd', chunk=100, top='/home/agheerae/PDB/prot.prmtop')
for chunk in chunks:
    contacts = md.compute_contacts(chunk, contacts=list(itertools.combinations(range(0, 250), r=2)))
    print(contacts)
            

