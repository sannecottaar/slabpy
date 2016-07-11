from __future__ import print_function
import numpy as np
from slab import Slab
import matplotlib.pyplot as plt



file = open('data/syracuseetal_parameters.txt','r')


slabs=[]
for line in file.readlines():
    val = line.split()
    name = val[0]
    savei=0
    for i in range(1,4):
        try:
            float(val[i])
            break
        except:
            savei=i
            name = name + ' ' +val[i]

    slabs.append(Slab(name))
    print(slabs[-1].name,savei,val[savei+1])
    slabs[-1].transition_depth = float(val[savei+1])
    slabs[-1].transition_T = float(val[savei+2])
    slabs[-1].slab_T = float(val[savei+3])
    slabs[-1].moho_T = float(val[savei+4])
    slabs[-1].max_mantle_T = float(val[savei+5])
    slabs[-1].max_mantle_T_depth = float(val[savei+6])
    slabs[-1].transition_offset = float(val[savei+7])
    slabs[-1].slab_surface_T_30km = float(val[savei+8])
    slabs[-1].slab_surface_T_240km = float(val[savei+9])
    slabs[-1].min_slab_T_240km = float(val[savei+10])
for i in range(len(slabs)):
    print(slabs[i].slab_surface_T_30km, slabs[i].slab_surface_T_240km)
    plt.plot(slabs[i].slab_surface_T_30km, slabs[i].slab_surface_T_240km,'.k')

plt.show()

