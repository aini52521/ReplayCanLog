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
class can_t:
    def __init__(self):
        self.time = 0
        self.id = 0
        self.type = ''
        self.dlc = 0
        self.channel = 0
        self.data = []
    def clear(self):
        self.time = 0
        self.id = 0
        self.type = ''
        self.dlc = 0
        self.channel = 0
        self.data = []

def hour2ms(log):
    return log*60*60*1000
def min2ms(log):
    return log*60*1000
def s2ms(log):
    return log*1000

def log2time(log):
    log = log.split(':')
    return int((hour2ms(int(log[0])) + \
            min2ms(int(log[1])) + \
            s2ms(int(log[2])) + \
            int(log[3])/10))/1000

def readlog():
    file = open("test.log")
    for line in file:
       onedata = can_t()
       line = line.strip('\n')      #去除转行
       alist = line.split(' ')      #按空格切割
       alist.remove('')             #去除最后一个空格
       onedata.time = log2time(alist[0])      #以下为赋值         
       onedata.channel = int(alist[2])
       onedata.id = int(alist[3],16)
       onedata.type = alist[4]
       onedata.dlc = int(alist[5])
       for i in range(0,onedata.dlc):
           onedata.data.append(int(alist[6 + i]))
       alldata.append(onedata)
       #print(alist)
    print(len(alldata))
    file.close()

if __name__ == "__main__":
    #file = open("test_short.log")
    readlog()
