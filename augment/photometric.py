import cv2
import numpy as np


def brightness_contrast(img, alpha = 1.5, beta = 0):
    '''Brightness and contrast of the passed image 
    are modified using 'alpha' and 'beta' arguments.'''
    
    assert (type(alpha) == int or type(alpha) == float) and (type(beta) == int or type(beta) == float), "Arguments 'alpha' and 'beta' must be of type int or float."
    
    assert alpha >= 0, "Argument 'alpha' must be greater than or equal to 0."
    
    img_new = img.astype('int')
    
    img_new = img_new * alpha + beta
    img_new[img_new > 255] = 255
    img_new[img_new < 0] = 0
    img_new = img_new.astype(np.uint8)
    
    return img_new


def colorSpace(img, colorspace = 'hsv'):
    '''Change the colorspace of given image to
    the provided 'colorspace' argument.'''
    
    assert type(colorspace) == str, "Argument 'colorspace' must be of type str."
    
    assert colorspace in (['hsv', 'ycrcb', 'lab']), "Wrong choice of argument 'colorspace'. Argument 'colorspace' can only be one of the following types - 'hsv', 'ycrcb' 'lab'."
    
    img_new = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    if colorspace == 'hsv':
        img_new = cv2.cvtColor(img_new, cv2.COLOR_RGB2HSV)
    
    elif colorspace == 'ycrcb':
        img_new = cv2.cvtColor(img_new, cv2.COLOR_RGB2YCrCb)
    
    elif colorspace == 'lab':
        img_new = cv2.cvtColor(img_new, cv2.COLOR_RGB2Lab)
        
    return img_new


def addNoise(img, noise_type = 'gaussian', mean = 0, var = 0.05, sp_ratio = 0.5, noise_amount = 0.02):
    '''Add noise to the passed image. gaussian, salt n pepper
    and poisson are the types of noises that are supported.'''
    
    assert noise_type in ['gaussian', 'salt_pepper', 'poisson'], "Wrong choice of argument 'noise_type'. Argument 'noise_type' can only be one of the following types - 'gaussian', 'salt_pepper' 'poisson'."
    
    assert (type(mean) == int or type(mean) == float), "Argument 'mean' must be of type int or float."
    
    assert (type(var) == int or type(var) == float) and (var >= 0), "Argument 'var' must be of type int or float and value of 'var' must be greater than or equal to zero."
    
    assert (type(sp_ratio) == int or type(sp_ratio) == float) and sp_ratio >= 0 and sp_ratio <= 1, "Argument 'sp_ratio' must be of type int or float and value of 'sp_ratio' must be greater than or equal to zero and smaller than or equal to one."
    
    assert (type(noise_amount) == int or type(noise_amount) == float) and noise_amount > 0, "Argument 'noise_amount' must be of type int or float and value of 'noise_amount' must be greater than zero"
    
    img_new = img.copy()
    img_new = img_new/255
    
    if noise_type == 'gaussian':
        sigma = var**0.5
        gauss = np.random.normal(mean, sigma, (img_new.shape[:]))
        img_new = img_new + gauss
        
    elif noise_type == 'salt_pepper':
        # Salt mode
        num_salt = int(noise_amount * img_new.size * sp_ratio)
        coords = [np.random.randint(0, i - 1, num_salt) for i in img_new.shape[:2]]
        img_new[coords[0], coords[1]] = 1

        # Pepper mode
        num_pepper = int(noise_amount * img_new.size * (1. - sp_ratio))
        coords = [np.random.randint(0, i - 1, num_pepper) for i in img_new.shape[:2]]
        img_new[coords[0], coords[1]] = 0
        
    elif noise_type == 'poisson':
        img_new = img_new + (np.random.poisson(img_new * noise_amount) / float(noise_amount))
    
    img_new = img_new * 255
    img_new[img_new > 255] = 255
    img_new[img_new < 0] = 0
    img_new = img_new.astype(np.uint8)
    
    return img_new