import numpy as np
from Data_Load import dataLoad
from Data_Statistics import dataStatistics
from Data_Plot import dataPlot

data = "nothing"
while True:
    function = int(input("1. Load Data\n2. Filter Data\n3. Display Statistics\n4. Generate Plots\n5. Quit\nChoose a function\n"))
    if function == 1:
        while True:
            try:
                data = dataLoad(str(input("Input the name of the text file\n")))
                break
            except ValueError:
                print("Input an existing text file")
            originalData = data
        
    elif function == 2:
        if data.any(data == "nothing") == False:
            while True:
                option = int(input("0. Remove filters\n1. Bacteria name\n2. Growth Rate\n3. Exit\nChoose a filter\n"))
                if option == 0:
                    data = originalData
                elif option == 1:
                    Bacteria = int(input("1. Salmonella enterica\n2. Bacillus cereus\n3. Listeria\n4. Brochothrix thermosphacta\nChoose a bacteria\n"))
                    data = data[data[:,2] == Bacteria]
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
        if np.any(data == "nothing") == False:
            statistic = str(input("Type in the name of the desired statistic\n"))
            print("The ", statistic, " is ", str(dataStatistics(data,statistic)))
        else:
            print("\nPLEASE LOAD DATA FIRST")
            
    elif function == 4:
        if np.any(data == "nothing") == False:
            dataPlot(data)
        else:
            print("\nPLEASE LOAD DATA FIRST")
                      
    elif function == 5:
        break