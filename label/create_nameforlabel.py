#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 13:30
# @Author  : Lelsey
# @Site    : 
# @File    : create_nameforlabel.py
# @Software: PyCharm
from pymongo import MongoClient
import pandas as pd
import numpy as np
def create_csv():
    user = 'linkedin'
    pwd = 'Q*9JNi96'
    host = '121.48.165.65'
    port = '9055'

    uri = "mongodb://%s:%s@%s" % (user, pwd, host + ":" + port + "/linkedin")
    client = MongoClient(uri)
    db = client["linkedin"]
    DataSet = db.DataSet
    for i in range(1,15):
        datalist = DataSet.find({'job_label': i})
        image_name_list = []
        label_list = []
        for data in datalist:
            image_name = data['image_name']
            image_name_list.append(image_name)
            label = data['job_label']
            label_list.append(label)
        print(image_name_list)
        print(label_list)
        dataframe = pd.DataFrame({'image_name': image_name_list, 'label': label_list})
        csv_name = str(i)+'_namelbel.csv'
        dataframe.to_csv(csv_name, mode='a', sep=',')


if __name__ == '__main__':
    create_csv()
