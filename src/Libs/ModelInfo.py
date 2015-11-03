#-*- encoding: utf-8 -*-

'''
Created on 2015. 10. 29.

@author: User
'''
import sys, os
from uiautomator import Device
import Libs.GlobalVar
#Test module
import Libs.ClsActivity
import Libs.ClsKeyCode
import Libs.Adb

from testcases.ef63.ef63common import GlobalVar as GLBVAR


class ModelInfo():
    '''
    classdocs
    '''
    
    def __init__(self, deviceserial):
        '''
        Constructor
        '''
    
    #sndLog = CLS("test", "test")
        self.osType = sys.platform
        
        self.mstrInfo = {}
        
        #self.devSerials = self.instAdb.device_serial()
        self.mstrDevice = Device(deviceserial)
        self.mstrInfo = self.mstrDevice.info
    
    '''
        DEVICE Infoamtions
        { u'displayRotation': 0,
          u'displaySizeDpY': 640,
          u'displaySizeDpX': 360,
          u'currentPackageName': u'com.android.launcher',
          u'productName': u'takju',
          u'displayWidth': 720,
          u'sdkInt': 18,
          u'displayHeight': 1184,
          u'naturalOrientation': True
        }
    '''        
    def getCurrntProductInfo(self):
        return self.mstrInfo
        
    def getProductNmae(self):
        return self.mstrInfo['productName']
        
    def getCurrntPkg(self):
        return self.mstrInfo['currentPackageName']
    
    def getSDKInt(self):
            return self.mstrInfo['sdkInt']
        
    def getRotation(self):
        return self.mstrInfo['displayRotation']
    
    
    def getNaturalOri(self):
        return self.mstrInfo['naturalOrientation']
    
    def getDisplayState(self):
        return self.mstrDevice.screen
                
    def setReflash(self):
        pass
    
    #define Key activity
    def setDevScrnOn(self):
        self.mstrDevice.screen.on()
    
    
    def setMstDevScrnOff(self):
        self.mstrDevice.screen.off()

            
    def setWakeup(self):
        self.mstrDevice.wakeup()
            
    def setSleep(self):
        self.mstrDevice.sleep()
            
     #Hard key Soft key       
    def pressHome(self):
        return self.mstrDevice.press.home()
    
    def pressBack(self):
        return self.mstrDevice.press.back()
        
    
    ######################################################################
    
    def pressLeft(self):
        return self.mstrDevice.press.left()
        
    def pressRight(self):
        return self.mstrDevice.press.right()
    
    def pressUp(self):
        return self.mstrDevice.press.up()
        
    def pressDown(self):
        return self.mstrDevice.press.down()
        
    def pressCenter(self):
        return self.mstrDevice.press.center()
    
    ######################################################################    
        
    def pressMenu(self):
        return self.mstrDevice.press.menu()
        
    def pressSearch(self):
        return self.mstrDevice.press.search()
           
    def pressEnter(self):
        return self.mstrDevice.press.enter()
            
    def pressDelete(self):
        return self.mstrDevice.press.delete() # or del
        
    def pressRecent(self):
        return self.mstrDevice.press.recent()
            
    def pressVol_Up(self):
        return self.mstrDevice.press.volume_up()
            
    def pressVol_Down(self):
        return self.mstrDevice.press.volume_down()
            
    def pressVol_Mute(self):
        return self.mstrDevice.press.volume_mute()
            
    def pressPower(self):
        return self.mstrDevice.press.power()
            
    def clik(self, x, y):
        return self.mstrDevice.click(x, y)
            
    def longClik(self,x, y):
        '''
            Description:
                
            param:
                x, y : start first point x, y
                
            return : Boolean
        '''
        return self.mstrDevice.long_click(x, y)
            
    def swipe(self, sx, sy, ex, ey, steps=10):
        '''
            Description:
                
            param:
                sx, xy : start first x, y
                ex, ey : move to x, y
            return : Boolean
        '''
        return self.mstrDevice.swipe(sx, sy, ex, ey, steps)
           
    def drage(self,sx, sy, ex, ey, steps=10):
        '''
            Description:
                
            param:
                sx, xy : start first x, y
                ex, ey : move to x, y
            return : Boolean
        '''
        return self.mstrDevice.drag(sx, sy, ex, ey, steps)
       
    #screen action of the device   
    def setOrientation(self,scrAct='natural', choiceDevice='mstr'):
        '''
            Description
                
            param
                d.orientation = 'l' or 'left'
                d.orientation = 'r' or 'right'
                d.orientation = 'n' or 'natural'
            return : None
        '''
        self.mstrDevice.orientation = scrAct
    
    def setFreezeRotation(self,condition=False,choiceDevice='mstr'):
        '''
            param:
                condition : False un-freeze rotation
            return : None
        '''
        self.mstrDevice.freeze_rotation(condition)
    
    
            
    def takeScreenShot(self, choiceDevice = 'mstr'):
        '''
            Description:
                take screenshot and save to local file 'home.png' can work until android 4.2
            param
                image name
        '''
        
    def dumpWindowHeirarchy(self,filename='./log/hierachy.xml'):
        return self.mstrDevice.dump(filename)
        
    def dumpWindowHeirarchyStream(self):
        return self.mstrDevice.dump()
        
    def notification(self):
        '''
            Open notification, can not work until android 4.3
            return : Boolean
        '''
        return self.mstrDevice.open.Notification()
    
    def quickSettings(self):
        '''
            open quick settins, can not work until android 4.3
            return : Boolean 
        '''
        return self.mstrDevice.open.quick_settings()
    def waitidle(self):
        '''
            wait for current window to idle
            return : None
        '''
        self.mstrDevice.wait.idle()
        
    def waitWindowUpdate(self):
        '''
            wait until window upate event occurs
            return : Boolean
        '''
        self.mstrDevice.wait.update()
        
    def getCurrentActivityInfo(self, text):
        '''
          INFOMATION:
              { u'contentDescription': u'',
              u'checked': False,
              u'scrollable': False,
              u'text': u'Settings',
              u'packageName': u'com.android.launcher',
              u'selected': False,
              u'enabled': True,
              u'bounds': {u'top': 385,
                          u'right': 360,
                          u'bottom': 585,
                          u'left': 200},
              u'className': u'android.widget.TextView',
              u'focused': False,
              u'focusable': True,
              u'clickable': True,
              u'chileCount': 0,
              u'longClickable': True,
              u'visibleBounds': {u'top': 385,
                                 u'right': 360,
                                 u'bottom': 585,
                                 u'left': 200},
              u'checkable': False
            }
        '''  
        return self.mstrDevice(text).info
    
    def uiObjExist(self,text):
        '''
            ture if exists, else False
        '''
        return self.mstrDevice.exists(text)
    
    def watcher(self):
        pass
    def handler(self):
        pass
    def selector(self):
        pass
        
    def __del__(self):
        pass    

def startTestcase():
    print('start test case')

if __name__ == '__main__':
    instadb = Libs.Adb.adb()
    glbVar = GLBVAR()
        
    if instadb.getDeviceCount() == 1:
        seri = instadb.getSerials()
        testDev=ModelInfo(seri)
    elif instadb.getDeviceCount() == 2:
        seri = instadb.getSerials()
        mstseri, slvseri = seri
        mstDev = ModelInfo(mstseri)
        slvDevice = ModelInfo(slvseri)
        
    #print(isinstance(testDev.getCurrntPkg(), tuple))
  
 
    if testDev.getCurrntPkg() == glbVar.strLockPachate:
        testDev.swipe(200, 600, 700, 600, steps=10)
    
    if testDev.getCurrntPkg() == glbVar.strHomePackage:
        ''' start test
        '''
        if testDev.exists(text='Settings'):
            print('pass')
    #print(testDev.getCurrntPkg())
    '''   
    print(testDev.mstrInfo)
    if str(testDev.getCurrntPkg()) == 'com.android.keyguard':
        testDev.swipe(300, 600, 700, 600, steps=10)
    print(testDev.getCurrntPkg())
    '''