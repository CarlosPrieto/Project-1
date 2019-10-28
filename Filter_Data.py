import numpy as np
def filterData(data, Bacteria, minRate, maxRate):
    #Need to decide if Bacteria is an int or a string and if multiple can be passed through
    #check if Bacteria contains info
    data = data[data[:,2] == Bacteria]
    #check if minRate contains info
    data = data[data[:,1] > minRate]
    #check if maxRate contains info
    data = data[data[:,1] < maxRate]
    print(data)
    return data


filterData(np.array([[39.122, 0.81021, 1],
                    [13.534, 0.5742, 2],
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
                    [53.628, 0.48291, 2]]),2,0.4,0.7)