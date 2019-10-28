import numpy as np
import matplotlib.pyplot as plt

def dataPlot(data): #Recieves a N x 3 matrix with Temperature, Growth rate and Bacteria type
    #Separate the data into each bacteria type, as this makes both graphs easier to make and ignores entries with incorrect bacteria numbers
    bac1 = data[data[:,2] == 1]
    bac2 = data[data[:,2] == 2]
    bac3 = data[data[:,2] == 3]
    bac4 = data[data[:,2] == 4]

    plt.bar(np.arange(1,5),np.array([np.size(bac1,axis=0),np.size(bac2,axis=0),np.size(bac3,axis=0),np.size(bac4,axis=0)]), width=0.75)
    plt.title("Number of Bacteria")
    plt.xlabel("Type of Bacteria")
    plt.ylabel("Frequency")
    plt.xticks(ticks=[1,2,3,4],labels=["Salmonella","Bacillus cereus","Listeria","Brochothrix"])
    plt.show()

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

dataPlot(np.array([ [39.122, 0.81021, 1],
                    [13.534, 0.5742, 3],
                    [56.137, 0.20517, 3],
                    [50.019, 0.4754, 3],
                    [24.297, 0.86149, 3],
                    [37.183, 0.85134, 3],
                    [59.239, 0.058406, 1],
                    [45.784, 0.62541, 1],
                    [51.948, 0.39315, 1],
                    [71.663, 0.9012, 1],
                    [33.531, -0.89771, 1],
                    [38.036, 0.83976, 5],
                    [83.455, -0.84315, 1],
                    [47.451, -0.57439, 0],
                    [135.194, -88134, -1],
                    [42.34, 0.73713, 1],
                    [25.387, 0.8774, 1],
                    [37.458, 0.7095, 2],
                    [57.187, 0.388, 2],
                    [46.419, 0.64312, 4],
                    [38.838, 0.70335, 4],
                    [11.293, 0.12138, 4],
                    [42.315, 0.69079, 4],
                    [32.327, 0.67083, 4],
                    [36.06, 0.70488, 2],
                    [28.616, 0.62475, 2],
                    [56.857, 0.39398, 2],
                    [51.477, 0.54097, 2],
                    [52.454, 0.51267, 2],
                    [28.627, 0.62481, 2],
                    [39.659, 0.70214, 2],
                    [53.628, 0.48291, 2]]))