import numpy as np
from Data_Load import dataLoad
from Data_Statistics import dataStatistics
from Data_Plot import dataPlot

data = np.array([["nothing","nothing"],["nothing","nothing"]])
names = np.array(["Salmonella enterica","Bacillus cereus","Listeria","Brochothrix thermosphacta"])
filtersOn = False
while True:
    #\n is used to separate options as well as to allow input on a new line, to avoid confusing the user. This is used throughout the script
    function = str(input("1. Load Data\n2. Filter Data\n3. Display Statistics\n4. Generate Plots\n5. Quit\nChoose a function\n"))
    if function == "1":
        data = dataLoad(str(input("Input the name of the text file\n")))
        nameFilters = np.zeros(4, dtype=bool)
        growthFilters = ""
        filtersOn = False
        #originalData is defined to be able to remove filters in the filter section
        originalData = data
        #Checks if dataLoad gave an error and ignored every single line of data, making data an empty array
        if np.size(data) == 0:
            print("\nPlease choose a text file with data within the requirements")
            data = np.array([["nothing","nothing"],["nothing","nothing"]])
        
    elif function == "2":
        #Check if data has been defined yet, comparing with a value that was set at the beginning, same is used for options 3 and 4
        if data[0][0] != "nothing":
            #Nested while loop to allow for multiple filters to be used without having to choose the filter function again
            while True:
                option = str(input("0. Remove filters\n1. Bacteria name\n2. Growth Rate\n3. Exit\nChoose a filter\n"))
                if option == "0":
                    data = originalData
                    nameFilters = np.zeros(4, dtype=bool)
                    growthFilters = ""
                    filtersOn = False
                
                elif option == "1":
                    bacteria = str(input("1. Salmonella enterica\n2. Bacillus cereus\n3. Listeria\n4. Brochothrix thermosphacta\nChoose a bacteria to filter out\n"))
                    if bacteria == "1" or bacteria == "2" or bacteria == "3" or bacteria == "4":
                        temporaryData = data
                        data = data[data[:,2] != int(bacteria)]
                        #Make sure that the filter isn't filtering out every value, as this would cause an error for other functions
                        if np.size(data) == 0:
                            data = temporaryData
                            print("\nThis would filter out all data, please choose a different filter")
                        else:
                            nameFilters[int(bacteria)-1] = True
                            filtersOn = True
                    else:
                        print("\nA number between 1 and 4 was not input")
                
                elif option == "2":
                    while True:
                        try:
                            minRate = float(input("Input a minimum growth rate\n"))
                            maxRate = float(input("Input a maximum growth rate\n"))
                            break
                        except ValueError:
                            print("\nPlease input valid growth rate")
                    temporaryData = data
                    data = data[data[:,1] > minRate]
                    data = data[data[:,1] < maxRate]
                    #Make sure that the filter isn't filtering out every value, as this would cause an error for other functions
                    if np.size(data) == 0:
                        data = temporaryData
                        growthFilters = ""
                        print("\nThese values would filter out all data, please choose different growth rate values")
                    else:
                        growthFilters = (str(minRate)+" < rate < "+str(maxRate))
                        filtersOn = True
                
                elif option == "3":
                    break
                else:
                    print("\nPlease choose an avaliable option")
        else:
            print("\nPLEASE LOAD DATA FIRST")
            
    elif function == "3":
        if data[0][0] != "nothing":
            while True:
                statistic = str(input("Options:\nMean Temperature\nMean Growth rate\nStd Temperature\nStd Growth rate\nRows\nMean Cold Growth rate\nMean Hot Growth rate\nExit\n\nType in the name of the desired statistic:\n"))
                #"0" is passed from the dataStatistics function if a correct statistic name is not input
                if statistic == "exit":
                    break
                if str(dataStatistics(data,statistic)) != "0": ## Keep inside the statistics function and ask for a string again (while)1
                    print("\nThe " + statistic + " is {:g}".format(dataStatistics(data,statistic)))
                else:
                    print('\nPlease input a valid statistic')
        else:
            print("\nPLEASE LOAD DATA FIRST")
            
    elif function == "4":
        if data[0][0] != "nothing":
            dataPlot(data)
        else:
            print("\nPLEASE LOAD DATA FIRST")
                      
    elif function == "5":
        break
    else:
        print("\nPlease choose an avaliable option")
    
    #Display current filters
    if filtersOn == True:
        print("\nCurrent filters are:\nBacteria types removed:", names[nameFilters], "\nGrowth rate:", growthFilters)
    elif filtersOn == False:
        print("\nNo current filters are active")