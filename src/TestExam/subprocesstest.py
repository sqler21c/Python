#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2015. 10. 29.

@author: User
'''
import subprocess



def getCallResult(cmdARGS):
    fd_popen = subprocess.Popen(cmdARGS.split(), stdout=subprocess.PIPE).stdout
    data = fd_popen.read().strip()
    fd_popen.close()
    return data

data = getCallResult("adb")
print (data)