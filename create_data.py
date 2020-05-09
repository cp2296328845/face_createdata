#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 14:15
# @Author  : Lelsey
# @Site    : 
# @File    : create_data.py
# @Software: PyCharm
from sklearn.cross_validation import train_test_split
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
    data = np.ndarray((sampleNumaber*12, 112, 112, 3), dtype=np.float32)
    # print(data.shape)
    for i in range(12):
        file_name = "./label/"+str(i+1)+"_namelbel.csv"
        # print(file_name)
        name = pd.read_csv(file_name,header=0,sep=',')
        imageNames = np.array(name['image_name'])
        number = 0
        for image in imageNames:
            image_path = "./faces_change/"+image+"_1.jpg"
            print(str(number) + ":" + image)
            try:
                img=read_image(image_path,112,112)
                key = sampleNumaber * i + number
                data[key] = img
                print(key)
                number += 1
            except:
                imageErrorList.append(image_path)
                print(image_path+"error!!!!!")
            if number == sampleNumaber:
                break

    dataframe = pd.DataFrame({'image_name': imageErrorList})
    csv_name = "error.csv"
    dataframe.to_csv(csv_name, mode='a', sep=',')
    np.save("image_data_"+str(version)+".npy",data)

def create_label(sampleNumaber,version):
    label = np.ndarray((sampleNumaber*12, 12), dtype=np.float32)
    for i in range(12):
        for num in range(sampleNumaber):
            label[sampleNumaber * i + num][i] = 1
    np.save("image_label_" + str(version) + ".npy", label)


if __name__ == '__main__':
    # create_data(2000,0)
    # create_label(2000,0)
    num =2000
    version =0
    images = np.load("./image_data_" + str(version) + ".npy")
    # images = preprocessing.scale(images)
    # images = images.reshape(-1, 128, 14)
    label = np.load("./image_label_" + str(version) + ".npy")
    X_train, X_test, Y_train, Y_test = train_test_split(images, label, test_size=0.1)
    np.save("./image_X_train"+str(num)+"_"+str(version)+".npy", X_train)
    np.save("./image_X_test"+str(num)+"_"+str(version)+".npy", X_test)
    np.save("./image_Y_train"+str(num)+"_"+str(version)+".npy", Y_train)
    np.save("./image_Y_test"+str(num)+"_"+str(version)+".npy", Y_test)