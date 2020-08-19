Welcome to augment-auto's documentation!
========================================

**********
User Guide
**********

#. Installation
    * via pip
    * via git
#. Features
    * Photometric features
    * Geometric features
    * Kernel based features


##################
Installation guide
##################

* **Install using pip**::

    pip install augment-auto

* **Install by building from scratch**::

    git clone https://github.com/keshavoct98/image-augmentation
    cd image-augmentation
    python setup.py install


########
Features
########

#. **Geometric Features** - Image augmentation with geometric transformation of images.

    * crop(img, point1, point2, box = None)
        Returns cropped image.

        #. img = *numpy.ndarray*
                    Image to be cropped.
        #. point1 = *tuple*
                    initial crop coordinates in the format - (x1,y1).
        #. point2 = *tuple*
                    final crop coordinates in the format - (x2,y2).
        #. box = *list*, optional
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, new coordinates are calculated and returned along with output image.


   * rotate(img, angle, keep_resolution = True, box = None)
        Returns image rotated at the given angle.

        #. img = *numpy.ndarray*
                    Image to be rotated.
        #. angle = *integer or float*
                    value of angle at which image is to be rotated.
        #. keep_resolution = *bool*, default = True, optional
                    If True, resolution of image remains same after rotation, else resolution is modified.
        #. box = *list*, optional
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, new coordinates are calculated and returned along with output image.


    * scale(img, fx, fy, keep_resolution = False, box = None)
        Returns scaled image.

        #. img = *numpy.ndarray*
                    Image to be rotated.
        #. fx = *integer or float*
                    scaling value for x-axis.
        #. fy = *integer or float*
                    scaling value for y-axis.
        #. keep_resolution = *bool*, default = False, optional
                    If True, resolution of image remains same after scaling, extra region is cropped.
        #. box = *list*, optional
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, new coordinates are calculated and returned along with output image.


    * shear(img, shear_val, axis = 0, box = None)
        Returns sheared image along given axis.

        #. img = *numpy.ndarray*
                    Image to be sheared.
        #. shear_val = *integer or float*
                    shearing value for given axis.
        #. axis = {0,1}, default = 0
                    0 for shear along x-axis, 1 for shear along y-axis.
        #. box = *list*, optional
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, new coordinates are calculated and returned along with output image.


    * translate(img, tx, ty, box = None)
        Returns translated image.

        #. img = *numpy.ndarray*
                    Image to be sheared.
        #. tx = *integer or float*
                    translation magnitude along x-axis.
        #. ty = *integer or float*
                    translation magnitude along y-axis.
        #. box = *list*, optional
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, new coordinates are calculated and returned along with output image.



.. code-block:: python

    import augment.geometric





.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
