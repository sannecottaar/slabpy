#!/usr/bin/env python 

from __future__ import print_function
import numpy as np

from slab import Slab
import matplotlib.pyplot as plt
import pandas
import seaborn as sns

"""
Shamelessly copied implementations from Stream() and Trace() in ObsPy
"""

class Catalog(object):

    """
    Base class for slab Catalogs

    """

    def __init__(self,slabs=None):
        self.slabs=[]
        if slabs:
            self.slabs.extend([slabs])

    def __len__(self):
        """
        """
        return len(self.slabs)

    def print_slabs(self):
        '''
        For debugging - just print the slab database
        '''

        for slab in self.slabs:
            slab.print_slab1_details()
>>>>>>> 6b3f67d839095bc67c56f1cb4e5bed89bed3fc4a


    def list(self,name):
        """
        Return a parameter across all slabs
        """
        z=[]
        for i in range(len(self.slabs)):
            z.append(getattr(self.slabs[i],name))
        return z

    def pandas_data_frame(self,params):
        """
        Return a parameter across all slabs
        """
        d = dict()
        for p in range(len(params)):
            z=[]
            for i in range(len(self.slabs)):
                z.append(getattr(self.slabs[i],params[p]))
            d[params[p]]=z
        df=pandas.DataFrame(data=d)
        return df

    def seaborn_data_frame(self,params):
        """
        Return a parameter across all slabs
        """
        d = np.zeros((len(self),len(params)))
        for p in range(len(params)):
            for i in range(len(self.slabs)):
                d[i,p]=getattr(self.slabs[i],params[p])
        return d


    def append(self, slab):
        """
        append slab
        """
        if isinstance(slab, Slab):
            self.slabs.append(slab)
        else:
            msg = 'Append only supports a single Slab object as an argument.'
            raise TypeError(msg)
        return self

    def plot_two_parameters(self,param1,param2):
        """
        Plots two parameters from the catalog against each other. 
        """
        plt.plot(self.list(param1),self.list(param2),'.k' )
        plt.xlabel(param1)
        plt.ylabel(param2)


    def scatter_corrplot_parameters(self,params):
        """
        Plots two parameters from the catalog against each other.
        """
        snsdf = self.pandas_data_frame(params)
        print(snsdf)
        sns.pairplot(snsdf)


