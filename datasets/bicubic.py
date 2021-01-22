import os.path as osp
import cv2
import numpy as np
import math
import sys, time
import glob

gt_tr_img_folder = 'Training_GT/*'
lr_tr_img_folder = 'Training_LR/'
gt_ev_img_folder = 'Eval_GT/*'
lr_ev_img_folder = 'Eval_LR/'

idx = 0
for path in glob.glob(gt_tr_img_folder):
    idx += 1
    base = osp.splitext(osp.basename(path))[0]
    print(idx, base)
    # read images
    img = cv2.imread(path)
    height, width, channels = img.shape
    bicubic_img = cv2.resize(img,None, fx = 1/4, fy = 1/4, interpolation = cv2.INTER_CUBIC)
    #im = bicubic(img,4,(-1/2))
    cv2.imwrite(lr_tr_img_folder + base + '.jpg',img)

for path in glob.glob(gt_ev_img_folder):
    idx += 1
    base = osp.splitext(osp.basename(path))[0]
    print(idx, base)
    # read images
    img = cv2.imread(path)
    height, width, channels = img.shape
    bicubic_img = cv2.resize(img,None, fx = 1/4, fy = 1/4, interpolation = cv2.INTER_CUBIC)
    #im = bicubic(img,4,(-1/2))
    cv2.imwrite(lr_ev_img_folder + base + '.jpg',img)
    

    
