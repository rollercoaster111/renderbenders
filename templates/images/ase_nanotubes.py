
import scipy.spatial.distance as sc
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# https://wiki.fysik.dtu.dk/ase/ase/atoms.html#ase.Atoms
# https://wiki.fysik.dtu.dk/ase/ase/build/build.html#nanotubes
from ase.build import molecule
# atoms = molecule('H2O') # ase allows to use various basic molecules

# from ase.build import bulk
# a1 = bulk('Cu', 'fcc', a=3.6)
# a2 = bulk('Cu', 'fcc', a=3.6, orthorhombic=True)
# a3 = bulk('Cu', 'fcc', a=3.6, cubic=True)
# print(a1.cell)

# code from ase library, listed above
# from ase.build import graphene_nanoribbon
# gnr1 = graphene_nanoribbon(3, 4, type='armchair', saturated=True, vacuum=3.5)
# gnr2 = graphene_nanoribbon(2, 6, type='zigzag', saturated=True,
#                            C_H=1.1, C_C=1.4, vacuum=3.0,
#                            magnetic=True, initial_mag=1.12)
# print(gnr2)

# let's create nanotubes
# code from ase library, listed above, with no modification
from ase.build import nanotube
cnt1 = nanotube(6, 0, length=400)  # see ase doc for significance of parameters
bond_length = 1.4  # we give the covalent bond length so we can easily plot them (bonds are not real)
cnt2 = nanotube(3, 3, length=6, bond=bond_length, symbol='Si')  # generates 72 atoms

# https://wiki.fysik.dtu.dk/ase/ase/neighborlist.html?highlight=covalent%20bond#building-neighbor-lists
from ase.neighborlist import neighbor_list
d = neighbor_list('d', cnt2, bond_length)

# ase gives atoms locations, but not the covalent bonds between them
# so we have to do it ourselves (or use complex software used by chemists)

# # let's get the distances between every atom
# from ase.geometry import get_distances
positions = cnt2.positions
# xyz, dist = get_distances(positions, p2=None, cell=None, pbc=None)
# covalent bonds exist only between closest ones, ie at bond_length
dist = sc.cdist(positions,positions)
# argwhere does fantastic job at finding all bonded atoms (indices) with condition
bondsidx = np.argwhere((dist < bond_length*1.1) * (dist > bond_length*0.9))

# let's get the xyz coordinates of every atom in the nanotube
x,y,z = positions.T

fig = plt.figure()
# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
ax = plt.axes(projection='3d')  # we want a 3D scatter plot to see all atoms
ax.scatter(x,y,z,c='black',s=50)

# let's plot each bond 1 by 1 because we want line interruption after each bond
for bond in bondsidx:
    x = positions[bond[0]]
    y = positions[bond[1]]
    ax.plot((x[0],y[0]),(x[1],y[1]),(x[2],y[2]))

plt.savefig('nanotube.png')
plt.show()




