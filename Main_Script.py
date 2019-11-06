import numpy as np
from Data_Load import dataLoad
from Data_Statistics import dataStatistics
from Data_Plot import dataPlot

data = np.array([["nothing","nothing"],["nothing","nothing"]])
while True:
    function = int(input("1. Load Data\n2. Filter Data\n3. Display Statistics\n4. Generate Plots\n5. Quit\nChoose a function\n"))
    if function == 1:
        data = dataLoad(str(input("Input the name of the text file\n")))
        #originalData is defined to be able to remove filters in the filter section
        originalData = data
        
    elif function == 2:
        if data[0][0] != "nothing":
            while True:
                option = int(input("0. Remove filters\n1. Bacteria name\n2. Growth Rate\n3. Exit\nChoose a filter\n"))
                if option == 0:
                    data = originalData
                elif option == 1:
                    try:
                        bacteria = int(input("1. Salmonella enterica\n2. Bacillus cereus\n3. Listeria\n4. Brochothrix thermosphacta\nChoose a bacteria\n"))
                    except ValueError:
                        print("A number between 1 and 4 was not input")
                    if bacteria == 1 or bacteria == 2 or bacteria == 3 or bacteria == 4:
                        data = data[data[:,2] == bacteria]
                    else:
                        print("A number between 1 and 4 was not input")
                elif option == 2:
                    minRate = float(input("Input a minimum growth rate\n"))
                    maxRate = float(input("Input a maximum growth rate\n"))
                    data = data[data[:,1] > minRate]     
                    data = data[data[:,1] < maxRate]
                elif option == 3:
                    break
                else:
                    print("Please choose an avaliable option")
        else:
            print("\nPLEASE LOAD DATA FIRST")
            
    elif function == 3:
        if data[0][0] != "nothing":
            statistic = str(input("Type in the name of the desired statistic\n"))
            if str(dataStatistics(data,statistic)) != "0":
                print("The ", statistic, " is ", str(dataStatistics(data,statistic)))
            else:
                print('Please choose one of the availble inputs between 1 and 7')
        else:
            print("\nPLEASE LOAD DATA FIRST")
            
    elif function == 4:
        if data[0][0] != "nothing":
            dataPlot(data)
        else:
            print("\nPLEASE LOAD DATA FIRST")
                      
    elif function == 5:
        break