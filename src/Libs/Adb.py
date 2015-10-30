'''
Created on 2015. 10. 30.

@author: User
'''
from uiautomator import Adb

class adb(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.instAdb=Adb()
        
        self.devSerialNoms= self.instAdb.devices().keys()
        self.devcount = len(self.devSerialNoms)
        self.devSerial = self.instAdb.device_serial()
        
        
    def getSerials(self):
        return self.devSerialNoms
        #return self.devSerialNoms
    
    def getDeviceCount(self):
        return self.devcount
    
    def getSerial(self):
        return self.devSerial
    
