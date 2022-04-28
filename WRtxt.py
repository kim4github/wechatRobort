# coding=UTF-8
# encoding:utf-8
# -*- coding:utf-8 -*-
import datetime
#写入txt
def write(A,filename):
    now_time = datetime.datetime.now()
    now_time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    file = open(filename, 'a', encoding='utf-8')
    file.write(A)
    file.write('\n')
    # file.write(A.replace('机器猫，登记开团，', '') + ',' + now_time_str + '\n')  # 写入开团信息
    file.close()

#读取txt
def read(file_name):
    f = open(file_name, "r", encoding='utf-8')  # 设置文件对象

    str = f.read()  # 将txt文件的所有内容读入到字符串str中

    f.close()  # 将文件关闭
    return str

def readKeyword(file_name):
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            result.append(list(line.strip('\n').split(',')))
    print(result)
    return result