#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:44:39 2019

@author: margueritehuck
"""

#Data statistics function of project 1
import numpy as np
def dataStatistics(data, statistic):
#first we put the input in lower case
    statistic=statistic.lower()
#secondly initiallise every valllue
    totalNumbers=0
    coldGrowthRate=0
    hotGrowthRate=0
    sumOfColumns=np.sum(data, axis=0)
    numberOfRows=len(data)
#thirdly we decompose the diferent senarios for the type of static is denmanded of us
    if statistic=='mean temperature':
        # we work out the average temperature 
        #help from https://mail.python.org/pipermail/tutor/2005-February/035475.html column access m[:,1]
        #https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.matrix.item.html
        # we seperate the temperature in the data from the rest
        #https://stackoverflow.com/questions/10713004/find-length-of-2d-array-python/10713016
        #totaltemperature
        totalTemperature=sumOfColumns.item(0)
        result=totalTemperature/numberOfRows
    
    elif statistic=='mean growth rate':
        totalGrowthRate=sumOfColumns.item(1)
        result=totalGrowthRate/numberOfRows
        
    elif statistic=='std temperature':
        result=np.std(data[:,0])

    elif statistic=='std growth rate':
        result=np.std(data[:,1])
    
    elif statistic=='rows':
        result=numberOfRows
        
    elif statistic=='mean cold growth rate':
        for i in range(numberOfRows):
            if data[i,0]<20:
                coldGrowthRate+=data[i,1]
                totalNumbers+=1
        result=coldGrowthRate/totalNumbers
        
    elif statistic=='mean hot growth rate':
        for i in range(numberOfRows):
            if data[i,0]>20:
                hotGrowthRate+=data[i,1]
                totalNumbers+=1
        result=hotGrowthRate/totalNumbers
    else:
        result = "0"
    return result