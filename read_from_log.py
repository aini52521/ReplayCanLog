#! /usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    类型包含
    时间：time
    报文ID：id
    数据桢类型：type
    数据：data
"""
alldata = []
class can_t():
    def __init__(self):
        self.time = 0
        self.id = 0
        self.type = ''
        self.dlc = 0
        self.channel = 0
        self.data = []

def readlog():
    onedata = can_t()
    file = open("test.log")
    for line in file:
       line = line.strip('\n')      #去除转行
       alist = line.split(' ')      #按空格切割
       alist.remove('')             #去除最后一个空格
       onedata.time = alist[0]      #以下为赋值  
       onedata.channel = int(alist[2])
       onedata.id = int(alist[3],16)
       onedata.type = alist[4]
       onedata.dlc = int(alist[5])
       for i in range(1,onedata.dlc):
           onedata.data.append(int(alist[5 + i]))
       alldata.append(onedata)
       #print(alist)
    print(len(alldata))
    file.close()

if __name__ == "__main__":
    #file = open("test_short.log")
    readlog()
