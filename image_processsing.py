import matplotlib.pyplot as plt
import matplotlib.image as pmig
import numpy as np
image_date = pmig.imread('path.format')

class ImageProcessing():
    def rotation90(self, img_data):
        return np.rot90(img_data)                         #anticlockwise 90 degree
        
        
    def rotate_180(self, img_data):
        return np.rot90(img_data, k = -2)                        #clockwise 180 degree bcz of k = negative: means anticlockwise
    
    
    def flip_left_to_right(self, img_data):
        return np.fliplr(img_data)
    
    
    def flip_top_to_bottom(self, img_data):
        return np.flipud(img_data)
