#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:     SUN
@copyright:  2015 organization_name. All rights reserved.
@license:    MIT
@contact:    sqler21c@gmail.com
@deffield    updated: Updated
'''
__author__ = 'SUN(sqler21c@gmail.com)'
__version__ = '0.0.1'


import time
import logging
import os

class clsLog:
    def __init__(self,logtype,devLoc):
        self.__strLocaltime = time.localtime()
        #self.__strFileName = '%d%d%d%d%d%d' %(self.__strLocaltime[0:6])
        
        fileName=''
        for x in self.__strLocaltime[0:6]:
            fileName=fileName+str(x)
        
        try:
            os.listdir('./Log')
        except FileNotFoundError:
            os.mkdir('./Log')
                    
        logging.basicConfig(filename = './log/'+ fileName +'.log', 
                            filemode = 'w', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    def setData(self):
        pass
        
    def SendToLog(self,strLogType,strLocDev,strLogData):
        logging.warning(strLogData)
    
    def __del__(self):
        pass
    

    

if __name__ == "__main__":
    logIn = clsLog("skdf","M")
    logIn.SendToLog("dkdk", "dkdkstrLocDev", "strLogData")
    logIn.__strFileName="dkdkdk"
    print(logIn.__strFileName)
    

    