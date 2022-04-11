import numpy as np
import os

trainset_dir = 'E:\COCO2017\catdog_train2017_mask'
valset_dir = 'E:\COCO2017\catdog_val2017_mask'
train_list = 'E:\COCO2017\coco_train2017_catdog.txt'
val_list = 'E:\COCO2017\coco_val2017_catdog.txt'

def gen_seg_list(dataset_dir, list_file_name):
    with open(list_file_name, 'a+') as f:
        for cur_dir, dir, filenames in os.walk(dataset_dir):
            for file in filenames:
                if file.endswith('.jpg'):
                    img_name = os.path.join(dataset_dir, file)
                    mask_name = os.path.join(dataset_dir, file.strip('.jpg')+'.png')
                    f.write(img_name+' '+mask_name+'\n')


gen_seg_list(trainset_dir, train_list)
gen_seg_list(valset_dir, val_list)
