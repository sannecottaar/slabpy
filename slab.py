  
#!/usr/bin/env python 

from __future__ import print_function
import numpy as np


class Slab(object):

    """
    Base class for all slabs.

    """

    def __init__(self,name=None):
        self.name = name
        self.shape = None
        self.seismicity = None
        self.slabneighbors = None
        self.slab1_details = None

    def add_slab1_details(self,indict):
        '''
        Add a dictionary containing information from the slab 1.0 model (Hayes et al, 2003)
        '''
        self.slab1_details = indict

    def print_slab1_details(self):
        '''
        For debugging
        '''
        print(self.slab1_details)


    def plot_tomography(model):
        '''
        Plot slab cross section in given model.
        Potential model names are : ???
        '''
        pass

    def plot_seismicity():
        '''
        Plot slab cross section in given model.
        Potential model names are : ???
        '''
        pass








