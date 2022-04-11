from pycocotools.coco import COCO
import numpy as np
import cv2
import os
import shutil


data_dir = 'E:/COCO2017/train2017_single_json/'
ann_file='E:/COCO2017/annotations/instances_train2017.json'
out_dir = 'E:/COCO2017/catdog_train2017/'
coco = COCO(ann_file)

extracted_classes = ['cat','dog']

for catId in extracted_classes:
	catIds = coco.getCatIds(catNms=catId) #Add more categories ['person','dog']
	imgIds = coco.getImgIds(catIds=catIds)

	for img_ind in imgIds:
		img_name = str(img_ind).rjust(12,'0')+'.jpg'
		json_name = str(img_ind).rjust(12,'0')+'.json'
		shutil.copy(os.path.join(data_dir,img_name), os.path.join(out_dir,img_name))
		shutil.copy(os.path.join(data_dir, json_name), os.path.join(out_dir, json_name))

