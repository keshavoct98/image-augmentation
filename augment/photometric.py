import cv2
import numpy as np


def bright_contrast(img, alpha, beta):
    img_new = img.astype('int')
    
    img_new = img_new * alpha + beta
    img_new[img_new > 255] = 255
    img_new[img_new < 0] = 0
    img_new = img_new.astype(np.uint8)
    
    return img_new


def colorSpace(img, colorspace):
    img_new = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    if colorspace == 'hsv':
        img_new = cv2.cvtColor(img_new, cv2.COLOR_BGR2HSV)
    
    elif colorspace == 'ycrcb':
        img_new = cv2.cvtColor(img_new, cv2.COLOR_BGR2YCrCb)
    
    elif colorspace == 'lab':
        img_new = cv2.cvtColor(img_new, cv2.COLOR_BGR2Lab)
        
    return img_new


def noise(img, noise_type, mean = 0, var = 0.01, sp_ratio = 0.5, noise_amount = 0.01):
    img_new = img.copy()
    img_new = img_new/255
    
    if noise_type == 'gaussian':
        sigma = var**0.5
        gauss = np.random.normal(mean, sigma, (img_new.shape[0], img_new.shape[1], img_new.shape[2]))
        img_new = img_new + gauss
        
    elif noise_type == 'salt_pepper':
        # Salt mode
        num_salt = int(noise_amount * img_new.size * sp_ratio)
        coords = [np.random.randint(0, i - 1, num_salt) for i in img_new.shape[:2]]
        img_new[coords[0], coords[1], :] = 1

        # Pepper mode
        num_pepper = int(noise_amount * img_new.size * (1. - sp_ratio))
        coords = [np.random.randint(0, i - 1, num_pepper) for i in img_new.shape[:2]]
        img_new[coords[0], coords[1], :] = 0
        
    elif noise_type == 'poisson':
        img_new = img_new + (np.random.poisson(img_new * noise_amount) / float(noise_amount))
    
    img_new = img_new * 255
    img_new[img_new > 255] = 255
    img_new[img_new < 0] = 0
    img_new = img_new.astype(np.uint8)
    
    return img_new