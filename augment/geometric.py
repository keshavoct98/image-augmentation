import cv2
import numpy as np


def crop(img, point1, point2, box = None):
    ''' Returns cropped image from point1 to point2. If box coordinates are passed, new bounding box 
    coordinates are calculated and returned.'''
    
    assert ((type(point1) == tuple and len(point1) == 2) and (type(point2) == tuple and len(point2) == 2)
            ), 'point1 and point2 must be of type tuple and must have a lenght of two.'
    assert (point1[0] >= 0 and point2[0] < img.shape[1]) and (point1[1] >= 0 and point2[1] < img.shape[0]
            ), 'point1 and point2 must not exceed image dimensions.'
    assert (point2[0] > point1[0]) and (point2[1] > point1[1]), 'point2 must be greater than point1.' 
    
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    img_new = img.copy()
    img_new = img_new[y1:y2, x1:x2]    # image cropped
    
    if box == None:
        return img_new
    
    else:
        ''' New bounding box coordinates after calculated image cropping.'''
        
        assert (type(box) == list and len(box) == 4
               ), 'box argument must be of type list and must have a lenght of four.'
        assert (box[0] < box[2] and box[1] < box[3]
               ), 'top-left coordinates of bounding box must be smaller than bottom-right coordinates.' 
        
        box_new = []
        
        if (x1 >= box[0] and x2 <= box[2]) and (y1 >= box[1] and y2 <= box[3]):
            box_new = [0, 0, img_new.shape[1], img_new.shape[0]]
            
        else:
            box_new.append(min(max(0, box[0] - x1), img_new.shape[1]-1))
            box_new.append(min(max(0, box[1] - y1), img_new.shape[0]-1))
            box_new.append(min(max(0, box[2] - x1), img_new.shape[1]-1))
            box_new.append(min(max(0, box[3] - y1), img_new.shape[0]-1))
        
        if (box_new[0] == box_new[2]) and (box_new[1] == box_new[3]):
            box_new = [0,0,0,0]
            
        return img_new, box_new
    

def rotate(img, angle, box = None, keep_resolution = True):

    img_new = img.copy()
    h, w = img_new.shape[:2]
    M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
    cos, sin = np.abs(M[0, 0]), np.abs(M[0, 1])
    
    if box == None:
        if keep_resolution == True:
            img_new = cv2.warpAffine(img_new, M, (w, h))
        
        else:
            nW, nH = int((h * sin) + (w * cos)), int((h * cos) + (w * sin))
            M[0, 2] += (nW / 2) - (w / 2)
            M[1, 2] += (nH / 2) - (h / 2)
            img_new = cv2.warpAffine(img_new, M, (nW, nH))
            
        return img_new

    else:
        box_new = []
        box_temp = [box[0], box[1], box[0], box[3], box[2], box[3], box[2], box[1]]
        
        if keep_resolution == True:
            img_new = cv2.warpAffine(img_new, M, (w, h))

        else:
            nW, nH = int((h * sin) + (w * cos)), int((h * cos) + (w * sin))
            M[0, 2] += (nW / 2) - (w / 2)
            M[1, 2] += (nH / 2) - (h / 2)
            img_new = cv2.warpAffine(img_new, M, (nW, nH))

        box_temp[0:2] = np.dot(M, [box_temp[0], box_temp[1], 1])[0:2]
        box_temp[2:4] = np.dot(M, [box_temp[2], box_temp[3], 1])[0:2]
        box_temp[4:6] = np.dot(M, [box_temp[4], box_temp[5], 1])[0:2]
        box_temp[6:8] = np.dot(M, [box_temp[6], box_temp[7], 1])[0:2]

        box_new.append(min(box_temp[0], box_temp[2], box_temp[4], box_temp[6]))
        box_new.append(min(box_temp[1], box_temp[3], box_temp[5], box_temp[7]))
        box_new.append(max(box_temp[0], box_temp[2], box_temp[4], box_temp[6]))
        box_new.append(max(box_temp[1], box_temp[3], box_temp[5], box_temp[7]))

        box_new[0] = min(max(0, box_new[0]), img_new.shape[1]-1)
        box_new[1] = min(max(0, box_new[1]), img_new.shape[0]-1)
        box_new[2] = min(max(0, box_new[2]), img_new.shape[1]-1)
        box_new[3] = min(max(0, box_new[3]), img_new.shape[0]-1)

        return img_new, box_new


def scale(img, fx, fy, box = None, scale_object = False):

    img_new = img.copy()
    img_new = cv2.resize(img_new, dsize = None, fx=fx, fy=fy)
    
    if box == None:
        return img_new
    
    else:
        box_new = []
        box_new.append(box[0] * fx)
        box_new.append(box[1] * fy)
        box_new.append(box[2] * fx)
        box_new.append(box[3] * fy)
        
        if scale_object == True:
            x1, y1 = int(img_new.shape[1]/2 - img.shape[1]/2), int(img_new.shape[0]/2 - img.shape[0]/2)
            x2, y2 = int(img_new.shape[1]/2 + img.shape[1]/2), int(img_new.shape[0]/2 + img.shape[0]/2)
            img_new = img_new[y1:y2, x1:x2]
            
            if ((box_new[0] - x1) <= 0 or (box_new[0] - x1) >= img_new.shape[1]) and ((
                box_new[2] - x1) <= 0 or (box_new[2] - x1) >= img_new.shape[1]):
                box_new = [0, 0, 0, 0]

            elif ((box_new[1] - y1) <= 0 or (box_new[1] - y1) >= img_new.shape[0]) and ((
                box_new[3] - y1) <= 0 or (box_new[3] - y1) >= img_new.shape[0]):
                box_new = [0, 0, 0, 0]

            else:
                box_new[0] = min(max(0, box_new[0] - x1), img_new.shape[1]-1)
                box_new[1] = min(max(0, box_new[1] - y1), img_new.shape[0]-1)
                box_new[2] = min(max(0, box_new[2] - x1), img_new.shape[1]-1)
                box_new[3] = min(max(0, box_new[3] - y1), img_new.shape[0]-1)
            
        return img_new, box_new

        
def shear(img, shear_val, axis = 0, box = None):

    img_new = img.copy()
    
    if axis == 0:
        M = np.float32([[1, shear_val, 0],
                        [0, 1, 0]])
    else:
        M = np.float32([[1, 0, 0],
                        [shear_val, 1, 0]])
        
    img_new = cv2.warpAffine(img_new, M, (img_new.shape[1], img_new.shape[0]))
    
    if box == None:
        return img_new
    
    else:
        box_new = box.copy()
        box_temp = [box[0], box[1], box[0], box[3], box[2], box[3], box[2], box[1]]
        
        if axis == 0:
            box_temp[0] = box_temp[0] + shear_val * box_temp[1]
            box_temp[2] = box_temp[2] + shear_val * box_temp[3]
            box_temp[4] = box_temp[4] + shear_val * box_temp[5]
            box_temp[6] = box_temp[6] + shear_val * box_temp[7]
            
            box_new[0] = min(box_temp[0], box_temp[2], box_temp[4], box_temp[6])
            box_new[2] = max(box_temp[0], box_temp[2], box_temp[4], box_temp[6])
            
            if (box_new[0] <= 0 or box_new[0] >= img_new.shape[1]) and (
               box_new[2] <= 0 or box_new[2] >= img_new.shape[1]):
                box_new = [0, 0, 0, 0]
            
            else:
                box_new[0] = min(max(0, box_new[0]), img_new.shape[1]-1)
                box_new[2] = min(max(0, box_new[2]), img_new.shape[1]-1)
        else:
            box_temp[1] = box_temp[1] + shear_val * box_temp[0]
            box_temp[3] = box_temp[3] + shear_val * box_temp[2]
            box_temp[5] = box_temp[5] + shear_val * box_temp[4]
            box_temp[7] = box_temp[7] + shear_val * box_temp[6]
            
            box_new[1] = min(box_temp[1], box_temp[3], box_temp[5], box_temp[7])
            box_new[3] = max(box_temp[1], box_temp[3], box_temp[5], box_temp[7])
            
            if (box_new[1] <= 0 or box_new[1] >= img_new.shape[0]) and (
               box_new[3] <= 0 or box_new[3] >= img_new.shape[0]):
                box_new = [0, 0, 0, 0]
                
            else:
                box_new[1] = min(max(0, box_new[1]), img_new.shape[0]-1)
                box_new[3] = min(max(0, box_new[3]), img_new.shape[0]-1)
            
        return img_new, box_new
    

def translate(img, tx, ty, box = None):

    img_new = img.copy()
    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])
    img_new = cv2.warpAffine(img_new, M, (img_new.shape[1],img_new.shape[0]))
    
    if box == None:
        return img_new

    else:
        box_new = []
        box_new.append(min(max(0, box[0] + tx), img_new.shape[1]-1))
        box_new.append(min(max(0, box[1] + ty), img_new.shape[0]-1))
        box_new.append(min(max(0, box[2] + tx), img_new.shape[1]-1))
        box_new.append(min(max(0, box[3] + ty), img_new.shape[0]-1))
        
        return img_new, box_new