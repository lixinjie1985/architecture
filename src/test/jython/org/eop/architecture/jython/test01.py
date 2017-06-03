# coding=utf-8
'''
Created on 2017年6月4日

@author: Admin
'''
from java.util import Date
from java.text import SimpleDateFormat
if __name__ == '__main__':
    d = Date()
    f = SimpleDateFormat('yyyy-MM-dd HH:mm:ss')
    print f.format(d)