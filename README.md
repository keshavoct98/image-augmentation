# augment-auto
A python image augmentation library based on opencv and numpy. It can be used for augmenting images in both image classification and object detection tasks. Many different techniques of augmentation are supported, which can be clustered into three major types - geometric transformations, photometric transformations and kernel-based transformations.
Library has support for images with bounding boxes as well.

### Installation
Install using pip: </br>
```python
pip install augment-auto
```

Install from github: </br>
```python
git clone https://github.com/keshavoct98/image-augmentation.git
python setup.py install
```

### Documentation
Complete documentaion - [https://augment-auto.readthedocs.io/en/latest/](https://augment-auto.readthedocs.io/en/latest/) </br>
Demo ipython notebokk - [demo.ipynb](https://github.com/keshavoct98/image-augmentation/blob/master/demo.ipynb)

### Examples
```python
# Geometric Transformations
img = cv2.imread('images/3.jpg')
img_new = crop(img, point1 = (100, 100), point2 = (450, 400))
img_new = rotate(img, angle = 15, keep_resolution = True)
img_new = scale(img, fx = 1.5, fy = 1.5, keep_resolution = False)
img_new = shear(img, shear_val = 0.2, axis = 1)
img_new = translate(img, tx = 50, ty = 60)
```
![output1](https://github.com/keshavoct98/image-augmentation/blob/master/images/out_geometric0.jpg)

```python
# Geometric Transformations with bounding box
img = cv2.imread('images/0.jpeg')
bbox = [581, 274, 699, 321]
img_new, bbox_new = crop(img, point1 = (100, 100), point2 = (650, 400), box = bbox)
img_new, bbox_new = rotate(img, angle = 15, keep_resolution = True, box = bbox)
img_new, bbox_new = scale(img, fx = 1.5, fy = 1.3, keep_resolution = False, box = bbox)
img_new, bbox_new = shear(img, shear_val = 0.2, axis = 0, box = bbox)
img_new, bbox_new = translate(img, tx = 50, ty = 160, box = bbox)
```
![output2](https://github.com/keshavoct98/image-augmentation/blob/master/images/out_geometric1.jpg)

```python
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
```
![output3](https://github.com/keshavoct98/image-augmentation/blob/master/images/out_photometric.jpg)

```python
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
```
![output3](https://github.com/keshavoct98/image-augmentation/blob/master/images/out_kernel_based.jpg)

### References
1. https://numpy.org/doc/
2. https://docs.opencv.org/master/
3. https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
4. https://stackabuse.com/affine-image-transformations-in-python-with-numpy-pillow-and-opencv/
5. https://cristianpb.github.io/blog/image-rotation-opencv 
