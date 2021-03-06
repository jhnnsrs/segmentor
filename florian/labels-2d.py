"""
Display a labels layer above of an image layer using the add_labels and
add_image APIs
"""

from skimage import data
from skimage.color import rgb2gray
from skimage.segmentation import slic
from skimage.io import imread
import napari

with napari.gui_qt():
    image = imread('./test2/images/05_w2Spinning - DAPI-1.tif')
    label = imread('./test2/images/05_w2Spinning - DAPI-1_masks.tif')

    # initialise viewer with astro image
    viewer = napari.view_image(image, name='image', rgb=False)

    # add the labels
    label_layer = viewer.add_labels(label, name='label')

#with napari.gui_qt():
 #   astro = data.astronaut()

    # initialise viewer with astro image
#    viewer = napari.view_image(rgb2gray(astro), name='astronaut', rgb=False)

    # add the labels
    # we add 1 because SLIC returns labels from 0, which we consider background
 #   labels = slic(astro, multichannel=True, compactness=20) + 1
#    label_layer = viewer.add_labels(labels, name='segmentation')

    # Set the labels layer mode to picker with a string
 #   label_layer.mode = 'PICK'
#    print(f'The color of label 5 is {label_layer.get_color(5)}')
