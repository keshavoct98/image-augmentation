import cv2
import numpy as np
import random


def blur(img, blur_type, kernel_size = (5, 5), sigma1 = 0, sigma2 = 0, diameter = 9):
    img_new = img.copy()
    
    if blur_type == 'avg':
        img_new = cv2.blur(img_new, kernel_size)
        
    elif blur_type == 'gaussian':
        img_new = cv2.GaussianBlur(img_new, kernel_size, sigma1, sigma2)
            
    elif blur_type == 'median':
        img_new = cv2.medianBlur(img_new, max(kernel_size))
        
    elif blur_type == 'bilateral':
        img_new = cv2.bilateralFilter(img_new, diameter, sigma1, sigma2)
    
    return img_new


def random_crop(img, crop_size, box = None):
    img_new = img.copy()
    pixels_mean = [int(img_new[:,:,0].mean()), int(img_new[:,:,1].mean()), int(img_new[:,:,2].mean())]
    
    if box == None:
        x = random.randint(0, img.shape[1] - (crop_size[0] + 1))
        y = random.randint(0, img.shape[0] - (crop_size[0] + 1))
        img_new[y : y + crop_size[1], x : x + crop_size[0], :] = pixels_mean
        
    else:
        x = random.randint(box[0], box[2] - crop_size[0])
        y = random.randint(box[1], box[3] - crop_size[1])
        img_new[y : y + crop_size[1], x : x + crop_size[0], :] = pixels_mean
    
    return img_new


def randomCropAdd(img, crop_size, box = None):
    img_new = img.copy()
    
    if box == None:
        x_old = random.randint(0, img.shape[1] - (crop_size[0] + 1))
        y_old = random.randint(0, img.shape[0] - (crop_size[0] + 1))
        x_new = random.randint(0, img.shape[1] - (crop_size[0] + 1))
        y_new = random.randint(0, img.shape[0] - (crop_size[0] + 1))
        img_new[y_old : y_old + crop_size[1], x_old : x_old + crop_size[0], :] = img_new[
            y_new : y_new + crop_size[1], x_new : x_new + crop_size[0], :]
        
    else:
        x_old = random.randint(box[0], box[2] - crop_size[0])
        y_old = random.randint(box[1], box[3] - crop_size[1])
        x_new = random.randint(box[0], box[2] - crop_size[0])
        y_new = random.randint(box[1], box[3] - crop_size[1])
        img_new[y_old : y_old + crop_size[1], x_old : x_old + crop_size[0], :] = img_new[
            y_new : y_new + crop_size[1], x_new : x_new + crop_size[0], :]
    
    return img_new


def sharpen(img):
    img_new = img.copy()
    
    kernel = np.array([[0, -1, 0], 
                   [-1, 5,-1], 
                   [0, -1, 0]])
    img_new = cv2.filter2D(img_new, -1, kernel)
    
    return img_new