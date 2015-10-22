#!/usr/bin/env python
# encoding: utf-8
'''
TestExam.FaileHanld_ex -- shortdesc

TestExam.FaileHanld_ex is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2015 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import time
import logging

class clsLog:
    def __init__(self,logtype,devLoc):
        self.__strLocaltime = time.localtime()
        self.__strFileName = '%d%d%d%d%d%d' %(self.__strLocaltime[0:6])
        logging.basicConfig(filename = './log/'+ self.__strFileName +'.log', 
                            filemode = 'w', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    def setData(self):
        pass
        
    def SendToLog(self,strLogType,strLocDev,strLogData):
        logging.warning(strLogData)


    

if __name__ == "__main__":
    logIn = clsLog("skdf","M")
    logIn.SendToLog("dkdk", "dkdkstrLocDev", "strLogData")
    logIn.__strFileName="dkdkdk"
    print(logIn.__strFileName)
    
    
