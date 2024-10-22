import numpy as np
import pandas as pd
import seaborn as sns
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
            

