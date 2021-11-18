import xml.etree.ElementTree as ET
import numpy as np
import cv2 
import os
from glob import glob

def read_content(xml_file: str):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    list_with_all_boxes = []

    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)


    for boxes in root.iter('object'):
        ymin, xmin, ymax, xmax = None, None, None, None

        ymin = int(boxes.find("bndbox/ymin").text)
        xmin = int(boxes.find("bndbox/xmin").text)
        ymax = int(boxes.find("bndbox/ymax").text)
        xmax = int(boxes.find("bndbox/xmax").text)

        list_with_single_boxes = [xmin, ymin, xmax, ymax]
        list_with_all_boxes.append(list_with_single_boxes)

    return xml_file.split('.')[0], width, height, list_with_all_boxes

xml_files = glob('*.xml')

for xml_file in xml_files:
    name, w, h, boxes = read_content(xml_file)

    img = np.zeros( (h, w), dtype=np.uint8)
    # cv2.imshow("IMG", img)
    # cv2.waitKey(0)
    print()

    for box in boxes:
        img = cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), 255, -1)

    cv2.imwrite("ground_truth/{}.png".format(name), img)