from __future__ import print_function
import numpy as np
from slab import Slab
from catalog import Catalog
import matplotlib.pyplot as plt

# Read in Syracuse slab catalog
def read_syracuse():
    file = open('data/syracuseetal_table1.txt','r')
    
    
    slabs=Catalog() # Initialize Catalog object
    for line in file.readlines():
        val = line.split()
        if val[0]!= '#':# skip comments at top of file
            name = val[0]
            savei=0
            for i in range(1,4): # Read in slab names that are more than one string in lenght
                try:
                    float(val[i])
                    break
                except:
                    savei=i
                    name = name + ' ' +val[i]
            print(val,savei)
            slab=Slab(name) # Initialize slab object
            slab.lon= float(val[savei+1])
            slab.lat = float(val[savei+2])
            slab.H = float(val[savei+3])
            slab.arc_trench_distance = float(val[savei+4])
            slab.slab_dip = float(val[savei+5])
            slab.Vc = float(val[savei+6])
            slab.age = float(val[savei+7])
            slab.decent_rate = float(val[savei+8])
            slab.sediment_thickness = float(val[savei+9])
            slab.subducted_sediment_thickness = float(val[savei+10])
            slab.upper_plate_type = val[savei+11]
            #slab.upper_plate_thickness = float(val[savei+12])
            #slab.upper_plate_age = float(val[savei+13])
            slabs.append(slab) # Add slab object to catalot
    return slabs


# Read in Syracuse thermal paramaters
def read_syracuse_thermal(sub='d80'):
    file = open('data/syracuseetal_parameters_'+sub+'.txt','r')


    slabs=Catalog() # Initialize Catalog object
    for line in file.readlines():
        val = line.split()
        if val[0]!= '#':# skip comments at top of file
            name = val[0]
            savei=0
            for i in range(1,4): # Read in slab names that are more than one string in lenght
                try:
                    float(val[i])
                    break
                except:
                    savei=i
                    name = name + ' ' +val[i]

            slab=Slab(name) # Initialize slab object
            slab.transition_depth = float(val[savei+1])
            slab.transition_T = float(val[savei+2])
            slab.slab_T = float(val[savei+3])
            slab.moho_T = float(val[savei+4])
            slab.max_mantle_T = float(val[savei+5])
            slab.max_mantle_T_depth = float(val[savei+6])
            slab.transition_offset = float(val[savei+7])
            slab.slab_surface_T_30km = float(val[savei+8])
            slab.slab_surface_T_240km = float(val[savei+9])
            slab.min_slab_T_240km = float(val[savei+10])
        slabs.append(slab) # Add slab object to catalot
    return slabs


# Read and plot Syracuse Catalog
slabs = read_syracuse()
slabs.scatter_corrplot_parameters(('slab_dip','Vc','age','decent_rate'))
plt.show()