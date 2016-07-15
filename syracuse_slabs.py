#!/usr/bin/env python 


from __future__ import print_function
import numpy as np
from slab import Slab
from catalog import Catalog
import matplotlib.pyplot as plt
import seaborn as sns

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
            slab.params['lon']= float(val[savei+1])
            slab.params['lat'] = float(val[savei+2])
            slab.params['H'] = float(val[savei+3])
            slab.params['arc_trench_distance'] = float(val[savei+4])
            slab.params['slab_dip'] = float(val[savei+5])
            slab.params['Vc'] = float(val[savei+6])
            slab.params['age'] = float(val[savei+7])
            slab.params['decent_rate'] = float(val[savei+8])
            slab.params['thermal_parameter'] = float(val[savei+9])
            slab.params['sediment_thickness'] = float(val[savei+10])
            slab.params['subducted_sediment_thickness'] = float(val[savei+11])
            slab.params['upper_plate_type'] = val[savei+12]
            #slab.upper_plate_thickness = float(val[savei+12])
            #slab.upper_plate_age = float(val[savei+13])
            slabs.append(slab) # Add slab object to catalot
    return slabs

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
            slab.params['transition_depth'] = float(val[savei+1])
            slab.params['transition_T'] = float(val[savei+2])
            slab.params['slab_T'] = float(val[savei+3])
            slab.params['moho_T'] = float(val[savei+4])
            slab.params['max_mantle_T'] = float(val[savei+5])
            slab.params['max_mantle_T_depth'] = float(val[savei+6])
            slab.params['transition_offset'] = float(val[savei+7])
            slab.params['slab_surface_T_30km']= float(val[savei+8])
            slab.params['slab_surface_T_240km'] = float(val[savei+9])
            slab.params['min_slab_T_240km'] = float(val[savei+10])
            slabs.append(slab) # Add slab object to catalot
    return slabs


# Read and plot Syracuse Catalog
slabs = read_syracuse()

#Read and add in in thermal parameters
slabs = slabs+ read_syracuse_thermal('d80'))

## Plots scatter plot # cannot deal yet with NaN
#slabs.scatter_corrplot_parameters(('slab_dip','Vc','age','decent_rate','sediment_thickness','subducted_sediment_thickness','thermal_parameter','sediment_thickness'))
#plt.savefig('scatter.png')

# create a Pandas data frame
df= slabs.pandas_data_frame(slabs.slabs[0].params.keys())

## Plot correlation matrix (I think this ignores parameters with NaN)
corr = df.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask,k=1)] = True
sns.heatmap(corr,mask=mask)
plt.show()
