#THIS IS A ROUGH DRAFT
#THIS IS A ROUGH DRAFT
#THIS IS A ROUGH DRAFT
import numpy as np
from Data_Plot import dataPlot

def getInput():
    #Print "Please select an action"
    #Display five options, user presses a number 1-5
    #numberInput = --get input-- (int)
    return numberInput

def callFunction():
    numberInput = getInput()
    if numberInput == 1:
        #Print ("Please input the file name")
        #filename = --get input-- (string)
        data = loadData(filename)
    if numberInput == 2:
        #Print ("Please input the conditions of the filter. Leave empty any fields you wish to not filter")
        #Bacteria = --get input-- (string)
        #minRate = --get input-- (float)
        #maxRate = --get input-- (float)
        data = filterData(data, Bacteria, minRate, maxRate)
    if numberInput == 3:
        #Print ("Please input the desired type of statistic")
        #statistic = --get input-- (string)
        print(statistic + " = " + str(dataStatistics(data,statistic)))
    if numberInput == 4:
        dataPlot(data)
    if numberInput == 5:
        #Quit
    return