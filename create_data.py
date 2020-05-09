#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 14:15
# @Author  : Lelsey
# @Site    : 
# @File    : create_data.py
# @Software: PyCharm
from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd
import os

def read_image(file_path,width,height):
    img = image.load_img(file_path, target_size=(width,height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return x

def create_data(sampleNumaber,version):
    imageErrorList = []
    # data = np.ndarray((sample_num, 80, 80, 3), dtype=np.float32)
    for i in range(1,13):
        file_name = "./label/"+str(i)+"_namelbel.csv"
        print(file_name)
        imageNames = pd.read_csv("label/12_namelbel.csv")
        for image in imageNames:
            print(image)

if __name__ == '__main__':
    create_data(10,10)