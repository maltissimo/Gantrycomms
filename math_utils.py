import numpy as np
from scipy import ndimage

def get_centroid (ndarray):
    centroid = ndimage.center_of_mass((ndarray))
    return (centroid)