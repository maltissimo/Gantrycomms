import numpy as np
from scipy import ndimage

def get_centroid (ndarray):
    centroid = ndimage.center_of_mass((ndarray))
    return (np.array(centroid))

def deviation( undeflected, actual):
    """
    Outputs the deviation of the centroid of the n-th point in the measurement as a 1D, 2 elemet array
    starting from the undeflected laser position.
    :param undeflected: a 1D array containing the centroid of the undeflected laser image
    :param actual: a 1D array containing the centroid of the actual laser image.

    :return: a 1D array containing the relative deflection
    """
    deviation = np.zeros(2)
    deviation[0] = actual[0] - undeflected[0]
    deviation[1] = actual[1] - undeflected[1]
    return(deviation)