__author__ = 'Meghan'

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

nom = 'pamtest_RC2_pam.nc' ###############

# open file nom='filename.nc' in read mode and store in variable c
c = Dataset( 'C:\Users\Meghan\Desktop\MSC1\Research\Output files\{0}'.format(nom), 'r', format='NETCDF4')

# find out what variables are in c
print c.variables

# print variable header information for 'v'
v = 'raddry' ##########
print c.variables[v]

# store 'v' value in x
x = c.variables[v][:]

unite = c.variables[v].__dict__['units']           # units
nomlonge = c.variables[v].__dict__['long_name']    # long name
temps = c.variables['time'][:]                     # time
altitude = c.variables['level'][:]                 # altitude

# plot x
plt.plot(x)


# from http://matplotlib.org/users/pyplot_tutorial.html
#plt.xlabel('x-label')
#plt.ylabel(nomlonge) ##still not totally sure this is true
#plt.title('Histogram of IQ')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
#plt.grid(True)
#plt.show()

