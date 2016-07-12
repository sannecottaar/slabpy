#!/usr/bin/env python
#use the Ritsema codes to extract slices through a tomography model, ready for conversion into a format that can be used for various other things

import os
import glob
import sys
import numpy as np


def prep_depmap(model,depth):
	'''
	prepare input file for fortran depmap code
	'''

	ofile = open('in_depmaphj_jr','w')
	ofile.write('%s\n' %model)
	ofile.write('%g' %depth)
	ofile.close()

	#run the fortran code to produce the map template

	os.system('bin/depmaphj_jr <  in_depmaphj_jr > out_depmax')
	os.system('rm in_depmaphj_jr')
	#This also creates a .raw file

def prep_raw2xyz(model,depth,isp=1,lmin=0,lmax=50,xmin=-180):
	'''
	prepare input file for raw2xyz fortran code - this creates the slice through the specified model
	'''

	ofile=open('in_raw2xyz','w')

	rfile = model.split('/')[-1][:-3]+'raw'
	ofile.write('%s\n' %rfile)
	ofile.write('%s.map_%s.xzy\n' %(rfile[:-4],str(depth)))
	ofile.write('%g\n' %isp)
	ofile.write('1.00\n')
	ofile.write('%g %g\n' %(lmin,lmax))
	ofile.write('%g' %xmin)
	ofile.close()

	os.system('bin/raw2xyz_jr   < in_raw2xyz')
	os.system('rm in_raw2xyz')



def main():

	modelnames=['GAP_P4','SEM_WM_s','s362ani_m_s'] #defualt model name

	for modelname in modelnames:

		model = 'Models/'+modelname+'.sph'

		if os.path.isfile(model):
			print 'Found model file %s' %model
		else:
			sys.exit(1)

		#will be a list
		depths = np.linspace(50,2850,281)
		for value in depths:
			prep_depmap(model,value)
			prep_raw2xyz(model,value)
			print 'Done depth %g' %value

		print 'Done model %s' %modelname


if __name__ == '__main__':

	main()


