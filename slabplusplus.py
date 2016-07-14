#!/usr/bin/env python 


from __future__ import print_function
import numpy as np
from slab import Slab
from catalog import Catalog
import matplotlib.pyplot as plt
import seaborn as sns
from xlrd import open_workbook


def read_excel(file='slab++.xlsx'):
    wb = open_workbook(file)
    sheet = wb.sheets()[0]
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols
        
    items = []
    
    rows = []
    slabs= Catalog()
    for row in range(4, number_of_rows):
        slab= Slab()
        values = []
        for col in range(number_of_columns):
            par=str(sheet.cell(3,col).value)
            if par:
                print(par)
            value  = sheet.cell(row,col).value
            print(par,value)
            try:
                slab.params[par]= float(value)
            except:
                slab.params[par] = str(value)

        print(slab.params)
        slabs.append(slab)
    return slabs

# Read and plot Syracuse Catalog
slabs = read_excel()
print(slabs.list('Fukao'))
plt.plot(slabs.list('Fukao'), slabs.list('thermalPar'),'.k')
plt.xlim([0,6.0])
plt.xlabel('Fukao categories')
plt.xticks([1,2,3,4,5],['above 660','through 660', 'above 1000', 'deep','uncateg.'])
plt.ylabel('thermal parameter')
plt.show()

