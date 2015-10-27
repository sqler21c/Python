
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
  """Exception used to signal a timeout."""
  pass


class SigtermError(Exception):
  """Exception used to catch a sigterm."""
  pass

def getAttachedDevices(adb_cmd):
    try:
		out, err = subprocess.Popen([adb_cmd, 'devices'],
									stdout=subprocess.PIPE,
									stderr=subprocess.PIPE).communicate()
		if err:
			logging.warning('adb device error %s', err.strip())
		return  re.findall('^(\w+)\tdevice$', out, re.MULTILINE)
    except TimeoutException:
		logging.warning('adb devcies time out')
		return []
    except (IOError, OSError):
		logging.warning("exception from adb devices")
		return []
    finally:
		#signal.alarm(0)

if __name__ == '__main__':
    print(getAttachedDevices(adb_cmd='adb'))