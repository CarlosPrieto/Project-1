import numpy as np
import matplotlib.pyplot as plt

def dataPlot(data): #Recieves a N x 3 matrix with Temperature, Growth rate and Bacteria type
    #Separate the data into each bacteria type, as this makes both graphs easier to make and ignores entries with incorrect bacteria numbers
    bac1 = data[data[:,2] == 1]
    bac2 = data[data[:,2] == 2]
    bac3 = data[data[:,2] == 3]
    bac4 = data[data[:,2] == 4]

    #Plots the size of each of the arrays that were just defined with a bar chart
    plt.bar(np.arange(1,5),np.array([np.size(bac1,axis=0),np.size(bac2,axis=0),np.size(bac3,axis=0),np.size(bac4,axis=0)]), width=0.75)
    plt.title("Number of Bacteria")
    plt.xlabel("Type of Bacteria")
    plt.ylabel("Frequency")
    #Change the x-axis ticks from numbers to the name of each bacteria
    plt.xticks(ticks=[1,2,3,4],labels=["Salmonella","Bacillus cereus","Listeria","Brochothrix"])
    plt.show()

    #Plots Growth rate against temperature for each type of bacteria individually
    #Gives each line a color in RGB from 0 to 1 and adds a dot at each data point
    plt.plot(bac1[:,0],bac1[:,1], color=((0,0.25,0.9)), marker="o")
    plt.plot(bac2[:,0],bac2[:,1], color=((1,0.535,0.1)), marker="o")
    plt.plot(bac3[:,0],bac3[:,1], color=((0.0275,0.675,0.2)), marker="o")
    plt.plot(bac4[:,0],bac4[:,1], color=((0.48,0.2,0.656)), marker="o")
    plt.title("Growth Rate by Temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth Rate")
    plt.legend(["Salmonella","Bacillus cereus","Listeria","Brochothrix"])
    plt.xlim(10,60)
    plt.ylim(0)
    plt.show()
    return

dataPlot(np.array([[10,0.2,1],[20,0.43,1],[30,0.57,1],[40,0.91,1],[5,0.15,2],[15,0.45,2],[25,0.75,2],[70,0.3,3],[60,0.5,3],[50,0.7,3],[40,0.9,3],[30,0.4,4],[40,0.4,4],[60,0.4,4],[80,0.4,4]]))