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

* **Install using pip**:

.. code-block:: python

    pip install augment-auto

* **Install by building from scratch**:

.. code-block:: python

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
        #. box = *list*, default = None
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, new coordinates are calculated and returned along with output image.

    * rotate(img, angle, keep_resolution = True, box = None)
        Returns image rotated at the given angle.

        #. img = *numpy.ndarray*
                    Image to be rotated.
        #. angle = *integer or float*
                    value of angle at which image is to be rotated.
        #. keep_resolution = *bool*, default = True
                    If True, resolution of image remains same after rotation, else resolution is modified.
        #. box = *list*
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, new coordinates are calculated and returned along with output image.

    * scale(img, fx, fy, keep_resolution = False, box = None)
        Returns scaled image.

        #. img = *numpy.ndarray*
                    Image to be rotated.
        #. fx = *integer or float*
                    scaling value for x-axis.
        #. fy = *integer or float*
                    scaling value for y-axis.
        #. keep_resolution = *bool*, default = False
                    If True, resolution of image remains same after scaling, extra region is cropped.
        #. box = *list*
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, new coordinates are calculated and returned along with output image.

    * shear(img, shear_val, axis = 0, box = None)
        Returns sheared image along given axis.

        #. img = *numpy.ndarray*
                    Image to be sheared.
        #. shear_val = *integer or float*
                    shearing value for given axis.
        #. axis = *{0,1}*, default = 0
                    0 for shear along x-axis, 1 for shear along y-axis.
        #. box = *list*
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, new coordinates are calculated and returned along with output image.

    * translate(img, tx, ty, box = None)
        Returns translated image.

        #. img = *numpy.ndarray*
                    Image to be sheared.
        #. tx = *integer or float*
                    translation magnitude along x-axis.
        #. ty = *integer or float*
                    translation magnitude along y-axis.
        #. box = *list*
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, new coordinates are calculated and returned along with output image.

.. code-block:: python

    # Geometric Transformations
    
    img = cv2.imread('images/3.jpg')
      
    img_new = crop(img, point1 = (100, 100), point2 = (450, 400))
    
    img_new = rotate(img, angle = 15, keep_resolution = True)
    
    img_new = scale(img, fx = 1.5, fy = 1.5, keep_resolution = False)
    
    img_new = shear(img, shear_val = 0.2, axis = 1)
    
    img_new = translate(img, tx = 50, ty = 60)

.. code-block:: python

    # Geometric Transformations with bounding box
    
    img = cv2.imread('images/0.jpeg')
    bbox = [581, 274, 699, 321]
    
    img_new, bbox_new = crop(img, point1 = (100, 100), point2 = (650, 400), box = bbox)
    
    img_new, bbox_new = rotate(img, angle = 15, keep_resolution = True, box = bbox)
    
    img_new, bbox_new = scale(img, fx = 1.5, fy = 1.3, keep_resolution = False, box = bbox)
    
    img_new, bbox_new = shear(img, shear_val = 0.2, axis = 0, box = bbox)
    
    img_new, bbox_new = translate(img, tx = 50, ty = 160, box = bbox)


#. **Photometric Features** - Image augmentation with photometric transformation of images.

    * brightness_contrast(img, alpha = 1.5, beta = 0)
        Returns image with new pixel intensities.
        
        *img_new = img * alpha + beta*

        #. img = *numpy.ndarray*
                    Image whose brightness and contrast has to be modified.
        #. alpha = *integer or float*, default = 1.5
                    All pixel values of the passed image are multiplied by this value.
        #. beta = *integer or float*, default = 0
                    Vaue of beta is added to all pixel values of the passed image.

    * colorSpace(img, colorspace = 'hsv')
        Returns image with in the new colorspace. Three types of colorspace are supported - HSV, YCrCb, LAB.
        
        #. img = *numpy.ndarray*
                    Image whose colorspace has to be converted.
        #. colorspace = *{'hsv', 'ycrcb', 'lab'}*, default = 'hsv'
                    Colorspace to which image is to be converted.

    * addNoise(img, noise_type = 'gaussian', mean = 0, var = 0.05, sp_ratio = 0.5, noise_amount = 0.02)
        Returns image with added noise. Three different types of noise are supported - GAUSSIAN, Salt n Pepper, Poisson.

        #. img = *numpy.ndarray*
                    Image to which noise has to be added.
        #. noise_type = *{'gaussian', 'salt_pepper', 'poisson'}*, default = 'gaussian
                    Type of noise to add.
        #. mean = *int or float, (required only with noise_type = 'gaussian').*, default = 0
                    Gaussian noise is generated using this mean.
        #. var = *int or float, (required only with noise_type = 'gaussian').*, default = 0.05
                    Gaussian noise is generated from the standard deviation calculated using this variance.
        #. sp_ratio = *int or float, (required only with noise_type = 'salt_pepper').*, default = 0.5
                    Percentage of salt noise and pepper noise.
        #. noise_amount = *int or float, (required only with noise_type = 'salt_pepper' or 'poisson').*, default = 0.02
                    magnitude of salt n pepper/poisson noise is calculated using noise_amount.

.. code-block:: python

    # Photometric Transformations
    
    img = cv2.imread('images/1.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img_new = brightness_contrast(img, alpha = 1.3, beta = 20)            
    img_new = brightness_contrast(img, alpha = 0.7, beta = -10)
    
    img_new = colorSpace(img, colorspace = 'hsv')             
    img_new = colorSpace(img, colorspace = 'ycrcb')           
    img_new = colorSpace(img, colorspace = 'lab')
    
    img_new = addNoise(img, 'gaussian', mean = 0, var = 0.08)
    img_new = addNoise(img, 'salt_pepper', sp_ratio = 0.5, noise_amount = 0.1)
    img_new = addNoise(img, 'poisson', noise_amount = 0.5)

#. Kernel-based features

    * blur(img, blur_type = 'avg', ksize = (5, 5), median_ksize = 5, gaussian_sigma = 0)
        Returns blurred image. Three different types of blurring are supported - GAUSSIAN, Salt n Pepper, Poisson.

        #. img = *numpy.ndarray*
                    Image to be blurred.
        #. blur_type = *{'avg', 'gaussian', 'median'}*, default = 'avg'
                    Type of blurring to perform.
        #. ksize = *tuple, (required only with blur_type = 'avg' or 'gaussian').*, default = (5, 5)
                    kernel size used for average or gaussian blurring.
        #. median_ksize = *int, (required only with blur_type = 'median').*, default = 5
                    kernel size used for median blurring.
        #. gaussian_sigma = *int or float, (required only with blur_type = 'gaussian').*, default = 0
                    Standard deviation used to calculate gaussian kernel.

    * randomErase(img, size, box = None)
        A random rectangular region is replaced by mean value of image pixels. Returns modified image.

        #. img = *numpy.ndarray*
                    Image to be modified.
        #. size = *tuple*
                    Size of rectangular region to erase.
        #. box = *list*
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, rectangular region is erased from the bounding box region.

    * randomCropAdd(img, size, box = None)
        A random rectangular region is cropped and added to another region of image. Returns modified image.

        #. img = *numpy.ndarray*
                    Image to be modified.
        #. size = *tuple*
                    Size of rectangular region to crop and add.
        #. box = *list*
                    Coordinates of bounding box in the format - (x1,y1,x2,y2). If bounding box coordinates are passed, rectangular region is cropped from and added to the bounding box region.

    * sharpen(img)
        Returns sharpened image.

        #. img = *numpy.ndarray*
                    Image to be sharpened.

.. code-block:: python

    # Kernel-based Transformations
    
    img = cv2.imread('images/0.jpeg')
    bbox = [581, 274, 699, 321]
    
    img_new = randomErase(img, size = (100, 100))
    
    img_new = randomCropAdd(img, size = (100, 100))
    
    img_new = sharpen(img)
    
    img_new = randomErase(img, size = (60, 40), box = bbox)
    
    img_new = randomCropAdd(img, size = (60, 40), box = bbox)
    
    img_new = blur(img, 'avg', ksize = (9,9))
    img_new = blur(img, 'gaussian', ksize = (9,9), gaussian_sigma = 0)
    img_new = blur(img, 'median', median_ksize = 11)









.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
