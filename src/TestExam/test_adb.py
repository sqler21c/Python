'''
Created on 2015. 10. 23.

@author: User
'''
import sys
import queue
import string
import subprocess
import threading
import logging
import time
import os
import re
import shutil
import signal

class TimeoutException(Exception):
    pass

class SigtermError(Exception):
    pass

def getAttachedDevcies(adb_cmd):
    
    try:
        out, err = subprocess.Popen([adb_cmd, 'devices'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE).communicate()
        if err:
            logging.warning('adb device error %s', err.strip())
        
        return  re.findall('^(\w+)\tdevice$', out, re.MULTILINE)
    
    except TimeoutException:
        logging.warning("Time out exception")
        return []
    except (IOError, OSError):
        logging.warning('Io error')
        return []
    finally:
        print(out, err)
        pass

if __name__ == '__main__':
    print(getAttachedDevcies(adb_cmd="adb"))
    