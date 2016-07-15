  
#!/usr/bin/env python 

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import plotting_tools as pts


class Slab(object):

    """
    Base class for all slabs.

    """

    def __init__(self,name=None):
        self.params=dict()
        self.params['name'] = name
        self.shape = None
        self.seismicity = None
        self.slabneighbors = None
        self.slab1_details = None
    
    def merge_in_dict(self, y):
        '''Merge new dictionary .'''
        self.params.update(y.params)
        return self

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

    def map_slab1(self):
        '''
        Creates a map of the slab1.0 contours
        '''

        if self.slab1_details:
            bbox = self.slab1_details['Bounding_box']
            print(bbox)

            minlon = bbox[0]
            maxlon = bbox[1]
            minlat = bbox[2]
            maxlat = bbox[3]

            print('------------------------\nPlotting map...\n------------------------')

            figure = plt.figure(facecolor='white',figsize=(10,8))
            a = figure.add_subplot(111)
            m = Basemap(ax=a,lat_0=(minlat+((maxlat-minlat)/2.0)),lon_0=(minlon+((maxlon-minlon)/2.0)),resolution ='l',llcrnrlon=minlon,llcrnrlat=minlat,urcrnrlon=maxlon,urcrnrlat=maxlat)

            #Create grid uniformly spaced grid
            nx = int((m.xmax-m.xmin)/0.1)+1; ny = int((m.ymax-m.ymin)/0.1)+1

            slabdat = m.transform_scalar(self.slab1_details['Depth_array'],self.slab1_details['Lon_array'],self.slab1_details['Lat_array'],nx,ny)
            im = m.imshow(slabdat)

            m.drawparallels(np.arange(minlat,maxlat,((maxlat-minlat)/5)),labels=[1,1,0,0],linewidth=0.5,fontsize=10)
            m.drawmeridians(np.arange(minlon,maxlon,((maxlon-minlon)/5)),labels=[0,0,0,1],linewidth=0.5,fontsize=10)

            m.drawcoastlines()

            #Add tectonic plate boundaries - this doesn't work very well
            # self.faults = pts.read_faults('data/plates.xy')
            # for i in self.faults:
            #     faults_lons = self.faults[i][0]
            #     faults_lats = self.faults[i][1]
            #     x,y = m(faults_lons, faults_lats)
            #     m.plot(x,y,'b--',linewidth=1.0)

            #add a colorbar
            cb = m.colorbar(im,"bottom", size="5%", pad='15%')
            cb.set_label('Depth to slab surface [km]')

            #add a figure title
            a.set_title('Slab1.0 upper surface depths: %s' %self.name)

            return a,m

        else:
            print('Nothing to do: no slab1_details added!')



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









