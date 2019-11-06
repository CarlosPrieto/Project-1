# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:35:35 2019

@author: Nico1
"""

import numpy as np

def dataLoad(filename):
    #Import file as array split in rows
    try:
        fileIn=open(filename,"r")
    except FileNotFoundError:
        print("Please input an existing text file")
        return np.array([["nothing","nothing"],["nothing","nothing"]])
    rawData=fileIn.read().split("\n")
    #Check intervals/values of numbers in the rows
    dataArray=[]
    bacteriaTypes=np.arange(1,5)
    for i in range(0,np.size(rawData)):
        line=rawData[i].split(" ")
        if (float(line[0])>=10 and float(line[0])<=60) and (float(line[1])>0) and (np.any(bacteriaTypes==float(line[2]))==True) and (np.size(line)==3):
            dataArray.extend([float(line[0]),float(line[1]),float(line[2])])
        #print fitting error-message
        else:
            if float(line[0])<=10 or 60<=float(line[0]):
                print("The temperature in line {:g} is not a number between 10 and 60.".format(i+1))
            if float(line[1])<=0:
                print("The growth rate in line {:g} is not a positive number.".format(i+1))
            if np.any(bacteriaTypes==float(line[2]))==False:
                print("The bacteria in line {:g} is not a whole number between 1 and 4, and therefore doesn't exist.".format(i+1))
            if np.size(line)!=3:
                print("Line {:g} does not contain exactly 3 numbers.".format(i+1))
    #Format corrected data in matrix
    N=int(np.size(dataArray)/3)
    data=np.reshape(dataArray,[N,3])
    return data