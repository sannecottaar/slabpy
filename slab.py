from __future__ import print_function
import numpy as np



class Slab(object):

    """
    Base class for all slabs.

    """

    def __init__(self,name):
        self.name = name
        self.shape = None
        self.seismicity = None
        self.slabneighbors = None



    def plot_tomography(model):
        '''
        Plot slab cross section in given model.
        Potential model names are : ???
        '''
        pass

    def plot_seismicity(model):
        '''
        Plot slab cross section in given model.
        Potential model names are : ???
        '''
        pass








