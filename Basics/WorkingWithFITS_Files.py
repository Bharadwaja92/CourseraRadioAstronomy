"""
FITS:   FLEXIBLE IMAGE TRANSPORT SYSTEM
fits.open('<file>.fits')  ->  opens a list of HDU(Header/Data Unit) items
Header contains metadata of the HDU object
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hdulist = fits.open('<fitsFile>')

data = hdulist[0].data

print('data is ', data, 'shape is ', data.shape)


plt.imshow(data, cmap=plt.cm.viridis)

plt.colorbar()

plt.show()

def load_fits(imageFile):
    hduList = fits.open(imageFile)
    data = hduList[0].data
    arg_max = np.argmax(data)
    return (np.unravel_index(arg_max, data.shape))

load_fits('ImageFile.fits')
