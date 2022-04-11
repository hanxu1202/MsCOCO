import json
import cv2
import numpy as np
import os
from utils.labelme import utils
import shutil

json_dir = 'E:/COCO2017/catdog_train2017/'
out_dir='E:/COCO2017/catdog_train2017_mask/'
json_files=[]
img_files=[]
label_names={'_background_':0}
classes_names=[]
save_colored_mask = False

color_map = {0:[0,0,0],
             1:[0,0,128],
             2:[0,128,0]}


with open('./label_names.txt', 'r') as f:
    count = 1
    for line in f.readlines():
        line = line.strip("\n")
        label_names[line] =c ount
        classes_names.append(line)
        count+=1


for curDir, dir, files in os.walk(json_dir):
    for file in files:
        if file.endswith(".json"):
            json_files.append(os.path.join(curDir, file))
        if file.endswith(".jpg"):
            img_files.append(os.path.join(curDir, file))

for index, json_file in enumerate(json_files):
    print(str(index)+'/'+str(len(json_files)))
    out = out_dir+json_file.split('/')[-1].split('.')[0]
    img = cv2.imread(img_files[index])
    img_shape=img.shape[0:2]
    data = json.load(open(json_file))
    h = data['imageHeight']
    w = data['imageWidth']
    shapes = data['shapes']
    mask = utils.shapes_to_label(img.shape, shapes, label_names, classes_names)
    mask = np.array(mask, dtype='uint8')
    cv2.imwrite(out+'.png', mask)
    shutil.copy(img_files[index], out+'.jpg')

    if save_colored_mask:
        x = cv2.imread(out+'.png',-1)
        x = np.expand_dims(x,-1)

        colored_mask = np.zeros((img.shape), dtype='uint8')
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                colored_mask[i][j][:] = color_map[x[i][j][0]]

        cv2.imwrite(out+'_colored.png', colored_mask)
