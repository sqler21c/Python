'''
Created on 2015. 10. 22.

@author: User
'''
from Libs import ClsActivity as CLS
import os, sys
from uiautomator import Device, Adb, AutomatorDevice
from Libs import SaveToLog as saveLog

instAdb=Adb()
devSerials= instAdb.devices().keys()
if len(devSerials) == 1:
    devSerials = instAdb.device_serial()
    mstrDevice = devSerials
else:
    mstrDevSerial, slavDevSerial = devSerials
    mstrDevice = Device(mstrDevSerial)
    SlavDevice = Device(slavDevSerial)

deviceInfo = d.info
print(deviceInfo)
# d.screen.on()
#deviceInfo = d.info


for irr in deviceInfo:
    print(deviceInfo[irr])

if deviceInfo['screenOn'] == True:
    print('device screen is On('+ str(deviceInfo['screenOn'])+ ')')
elif deviceInfo['screenOn'] ==False:
    print(deviceInfo['screenOn'])
else:
    print('nothing')

Logsave = saveLog.clsLog("dkdk", "dkdk")
Logsave.SendToLog("dkdk", "trLocDev", "strLogData")

#d.dump("./tmp/her.xml")