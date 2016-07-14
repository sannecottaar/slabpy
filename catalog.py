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
    
    
    def __add__(self, Cat2):
        """
        """
        names = Cat2.list('name')
        for i,slab in enumerate(self.slabs):
            if slab.params['name'] in names:
                ind =[i for i in range(len(names)) if slab.params['name']== names[i]]
                self.slabs[i]= slab.merge_in_dict(Cat2.slabs[ind[0]])

        return self
    


    def print_slabs(self):
        '''
        For debugging - just print the slab database
        '''

        for slab in self.slabs:
            slab.print_slab1_details()


    def list(self,name):
        """
        Return a parameter across all slabs
        """
        z=[]
        for i in range(len(self.slabs)):
            try:
                z.append(self.slabs[i].params['name'])
            except:
                z.append(np.nan)
        return z

    def pandas_data_frame(self,params):
        """
        Setup Pandas data frame
        """
        d = dict()
        for p in range(len(params)):
            z=[]
            for i in range(len(self.slabs)):
                try:
                    z.append(self.slabs[i].params[params[p]])
                except:
                    z.append(np.nan)
            d[params[p]]=z
        df=pandas.DataFrame(data=d)
        df.fillna(0.)
        return df

    def seaborn_data_frame(self,params):
        """
        Setup Seaborn data frame
        """
        d = np.zeros((len(self),len(params)))
        for p in range(len(params)):
            for i in range(len(self.slabs)):
                d[i,p]=self.slabs[i].params[params[p]]
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
        sns.pairplot(snsdf,dropna=True, size=10)


