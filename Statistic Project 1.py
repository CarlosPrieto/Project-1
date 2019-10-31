#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:44:39 2019

@author: margueritehuck
"""

#Data statistics function of project 1
import numpy as np
import math
def dataStatistics(data, statistic):
#first we put the input in lower case
    Statistic=statistic.lower()
#secondly initiallise every valllue
    coldgrowthrate=0
    totalnumbers=0
    sumofthings=0
    hotgrowthrate=0
    sumofcolumns=np.sum(data, axis=0)
    numberofrows=len(data)
#thirdly we decompose the diferent senarios for the type of static is denmanded of us
    if Statistic== 'mean temperature':
        # we work out the average temperature 
        #help from https://mail.python.org/pipermail/tutor/2005-February/035475.html column access m[:,1]
        #https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.matrix.item.html
        # we seperate the temperature in the data from the rest
        #https://stackoverflow.com/questions/10713004/find-length-of-2d-array-python/10713016
        #totaltemperature
        totaltemperature=sumofcolumns.item(0)
        result=totaltemperature/numberofrows
    
    if Statistic=='mean growth rate':
        totalgrowthrate=sumofcolumns.item(1)
        result=totalgrowthrate/numberofrows
        
    if Statistic=='std temperature':
        totaltemperature=sumofcolumns.item(0)
        averagetemperature=totaltemperature/numberofrows
        for i in range(numberofrows):
            sumofthings+=((data.item(0)-averagetemperature)**2)
        result=math.sqrt(sumofthings/numberofrows)
        
    if Statistic=='std growth rate':
        totalgrowthrate=sumofcolumns.item(1)
        avearagegrowth=totalgrowthrate/numberofrows
        for i in range(numberofrows):
            sumofthings+=((data.item(0)-avearagegrowth)**2)
        result=math.sqrt(sumofthings/numberofrows)
        
    
    if Statistic=='rows':
        result=numberofrows
        
    if Statistic=='mean cold growth rate':
        for i in range(numberofrows):
            if data[i,0]<20:
                coldgrowthrate=coldgrowthrate+data[i,1]
                totalnumbers=totalnumbers+1
        result=coldgrowthrate/totalnumbers
        
    if Statistic=='mean hot growth rate':
        for i in range(numberofrows):
            if data[i,0]>20:
                hotgrowthrate=hotgrowthrate+data[i,1]
                totalnumbers=totalnumbers+1
        result=hotgrowthrate/totalnumbers
    else:
        print('please choose one of the availble inputs between 1 and 7')
    return result