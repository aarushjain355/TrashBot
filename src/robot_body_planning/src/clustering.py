import numpy as np
import pandas as pd
import seaborn as sns
import math
import warnings

class DENCLUECLUSTERING:

    def __init__(self, points):

        self.points = points
        data_points = np.array(self.points)
        x_coord = data_points[:, 0]
        y_coord = data_points[:, 1]
        std_dev_x = np.std(x_coord)
        std_dev_y = np.std(y_coord)
        self.h_x = 1.06*std_dev_x*len(data_points)**(-0.2)
        self.h_y = 1.06*std_dev_y*len(data_points)**(-0.2)
        self.t = 0
        self.e = 0

    
    def kernel_density_function(self):
        density = []

        for i in range(len(self.points)):
            density_sum_value = 0
            for j in range(len(self.points)):
                if j != i:
                    u = (self.points[i] - self.points[j]) // self.h_x
                    v = (self.points[i] - self.points[j]) // self.h_y
                    kernel_value = (1//(2*math.pi))*math.e**(-0.5*(u**2 + v**2))
                    density_sum_value += kernel_value
            density.append((1//(len(self.points)*self.h_x*self.h_y))*density_sum_value)
