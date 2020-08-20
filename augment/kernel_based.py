import cv2
import numpy as np
import random


def blur(img, blur_type = 'avg', ksize = (5, 5), median_ksize = 5, gaussian_sigma = 0):
    '''Blur the passed image. Four different types of
    blurring can be performed - Average, Gaussian,
    Median and bilateral.'''
    
    assert blur_type in ['avg', 'gaussian', 'median'], "Argument 'blur_type' can only have one of these three vales - 'avg', 'gaussian', 'median'."
    
    assert type(ksize) == tuple and len(ksize) == 2 and (ksize[0] > 0 and ksize[0] % 2 != 0) and (ksize[1] > 0 and ksize[1] % 2 != 0), "Argument 'ksize' can only be of type tuple with length equal to two and 'ksize' values must be odd positive integers."
    
    assert type(median_ksize) == int and median_ksize > 0 and median_ksize % 2 != 0, "Argument 'median_ksize' can only be of type int and must be an odd positive integer."
    
    assert (type(gaussian_sigma) == int or type(gaussian_sigma) == float), "Argument 'gaussian_sigma' must be of type int or float."
    
    img_new = img.copy()
    
    if blur_type == 'avg':
        img_new = cv2.blur(img_new, ksize)
        
    elif blur_type == 'gaussian':
        img_new = cv2.GaussianBlur(img_new, ksize, gaussian_sigma)
            
    elif blur_type == 'median':
        img_new = cv2.medianBlur(img_new, median_ksize)
    
    return img_new


def randomErase(img, size, box = None):
    '''Replace random rectangular region from the passed
    image with image mean. If box coordinates are passed,
    random region is choosen from inside the bounding box.'''
    
    assert type(size) == tuple and (type(size[0]) == int and type(size[1]) == int), "Argument 'size' can only be of type tuple and values inside 'size' must be of type int."
    
    assert (size[0] < img.shape[1] and size[1] < img.shape[0]), "Values inside 'size' must be smaller then image dimensions."
    
    img_new = img.copy()
    pixels_mean = int(img_new[:,:].mean())
    
    if box == None:
        x = random.randint(0, img.shape[1] - (size[0] + 1))
        y = random.randint(0, img.shape[0] - (size[1] + 1))
        img_new[y : y + size[1], x : x + size[0]] = pixels_mean
        
    else:
        assert (size[0] + box[2]) < img.shape[1] and (size[1] + box[3]) < img.shape[0], "Values passed inside 'size' are too big for the image. Either reduce the values inside 'size' argument or try 'randomErase' without passing 'box' argument."
        
        x = random.randint(box[0], box[2])
        y = random.randint(box[1], box[3])
        img_new[y : y + size[1], x : x + size[0]] = pixels_mean
    
    return img_new


def randomCropAdd(img, size, box = None):
    '''Random rectangular region is cropped and pasted at another
    location. If box coordinates are passed, rectangular region is
    cropped and pasted from inside the bounding box.'''
    
    assert type(size) == tuple and (type(size[0]) == int and type(size[1]) == int), "Argument 'size' can only be of type tuple and values inside 'size' must be of type int."
    
    assert (size[0] < img.shape[1] and size[1] < img.shape[0]), "Values inside 'size' must be smaller then image dimensions."
    
    img_new = img.copy()
    
    if box == None:
        x_old = random.randint(0, img.shape[1] - (size[0] + 1))
        y_old = random.randint(0, img.shape[0] - (size[0] + 1))
        x_new = random.randint(0, img.shape[1] - (size[0] + 1))
        y_new = random.randint(0, img.shape[0] - (size[0] + 1))
        img_new[y_old : y_old + size[1], x_old : x_old + size[0]] = img_new[
            y_new : y_new + size[1], x_new : x_new + size[0]]
        
    else:
        assert (size[0] + box[2]) < img.shape[1] and (size[1] + box[3]) < img.shape[0], "Values passed inside 'size' are too big for the image. Either reduce the values inside 'size' argument or try 'randomErase' without passing 'box' argument."
        
        x_old = random.randint(box[0], box[2])
        y_old = random.randint(box[1], box[3])
        x_new = random.randint(box[0], box[2])
        y_new = random.randint(box[1], box[3])
        img_new[y_old : y_old + size[1], x_old : x_old + size[0]] = img_new[
            y_new : y_new + size[1], x_new : x_new + size[0]]
    
    return img_new


def sharpen(img):
    '''Sharpens the features of image
    with a 3*3 filter.'''
    
    img_new = img.copy()
    
    kernel = np.array([[-1, -1, -1], 
                   [-1, 9,-1], 
                   [-1, -1, -1]])
    img_new = cv2.filter2D(img_new, -1, kernel)
    
    return img_new