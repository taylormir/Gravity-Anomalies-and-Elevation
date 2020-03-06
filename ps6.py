# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:55:35 2020

@author: taylor
"""
# This document was greated to determine the average density of Mt. Sentenial 
# given the gravity measurements taken at various elevations.

import numpy as np
import matplotlib.pyplot as py
import math 

h= np.array([20.0,42.0,53.0,65.0,72.0,81.0,96.0,104.0,119.0,127.0])
dg= np.array([-3.620,-8.271,-10.216,-12.656,-14.471,-15.626,-18.872,-20.302,-23.657,-24.417])

# Free Air Correction - added
fac= 0.3086*h #mGal
g_fac= dg+fac #mGal

# plot data
py.figure(1)
py.plot(h,g_fac)
py.xlabel('Height') 
py.ylabel('Gravity Anomaly Corrected for Elevation')
py.title('Gravity Anomalies as a Function of Height')

py.show

# Bouguer Correction 
#Solved for density, using the elevation corrected anomalies:

rho= g_fac/(0.00004192*h)

#plot density calculations
py.figure(2)
py.plot(rho,h, color='black')

py.title('Density with Increasing Elevation' )
py.xlabel('Density')
py.ylabel('Height Above Base Station')


#take average = bulk density 
average_d= sum(rho)/len(rho)
mtsentinel= 'The average density of Mt Sentinel is {} kg/m3'
print (mtsentinel.format(average_d))
py.axvline(x=average_d, color= 'red', label='Average Density')

py.legend(loc='upper right') 
py.show()


print ('Quartzite has a density of 2.6 to 2.7 g/cm3 which is very close to my value, and the most likely composition of Mt. Sentinel')