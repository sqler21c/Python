

'''
Created on 2015. 10. 22.

@author: User
'''

import os, sys
from Libs import ClsActivity as CLS

from uiautomator import Device, Adb, AutomatorDevice
from Libs import SaveToLog as saveLog
from Libs import ModelInfo
import Libs.ClsKeyCode


instAdb=Adb()
devSerials= instAdb.devices().keys()
print(type(devSerials))
osType = sys.platform
sndLog = saveLog()

#sndLog = CLS("test", "test")

if len(devSerials) == 1:
    devSerials = instAdb.device_serial()
    mstrDevice = Device(devSerials)
    mstrInfo = mstrDevice.info
else:
    mstrDevSerial, slavDevSerial = devSerials
    mstrDevice = Device(mstrDevSerial)
    slvDevice = Device(slavDevSerial)
    mstrInfo = mstrDevice.info
    slvInfo = slvDevice.info

sndLog.SendToLog("start")

modinfo = ModelInfo(mstrInfo)





    


#d.dump("./tmp/her.xml")