import numpy as np
from PIL import Image
import torchvision.transforms.functional as TF
from torchvision import transforms
import cv2

def iou(predicted, target):
    smooth = 1
    product = np.multiply(predicted, target)
    intersection = np.sum(product)
    coefficient = (intersection + smooth) / (np.sum(predicted) + np.sum(target) - intersection + smooth)
    return coefficient

if __name__ == "__main__":
    name = '19'

    predicted = cv2.imread('prediction/{}.png'.format(name))
    target = cv2.imread('ground_truth/{}.png'.format(name))
    
    predicted = predicted / 255
    target = target / 255

    print(iou(predicted, target))