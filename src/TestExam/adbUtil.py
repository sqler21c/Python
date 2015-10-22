'''
Created on 2015. 10. 22.

@author: User
'''

import string
import pickle
import subprocess
import threading
import queue

class ADBUtil(threading.Thread):
    '''
    Helper class to implement asynchronous reading of a file
    in a separate thread. Pushes read lines on a queue to
    be consumed in another thread.
    '''
    def __init__(self):
        self.adb = 'adb '
        self.command = ('devices', 'logcat')
        self.Queue = queue.Queue

    def StartLogCat(self):
        '''The body of the tread: read lines and put them on the queue.
         # cmd : adb logcat
         # strOption : -v
        '''
        for line in iter(self._fd.readline, ''):
            self._queue.put(line)
            
    def eof(self):
        '''Check whether there is no more content to expect.'''
        return not self.is_alive() and self._queue.empty()
    
    def getDeviceNo(self):
        self.cmd("adb ", "get-serialno")
        pass
    
    def installApp(self):
        pass
    def uninstallApp(self):
        pass
    def getBugreport(self):
        pass
    
    def cmd(self, adb, strCmd):
        process = subprocess.Popen([adb + strCmd], stdout=subprocess.PIPE)
        assert isinstance(self.Queue, queue.Queue)
        assert callable(process.stdout.readline)
        threading.Thread.__init__(self)
        return process.stdout


if __name__ = "__main__":
    # You'll need to add any command line arguments here.
#    process = subprocess.Popen(["adb devices"], stdout=subprocess.PIPE)

    # Launch the asynchronous readers of the process' stdout.
    '''
    stdout_queue = queue.Queue()
    stdout_reader = ADBUtil(process.stdout, stdout_queue)
    stdout_reader.start()
    
    # Check the queues if we received some output (until there is nothing more to get).
    while not stdout_reader.eof():
        while not stdout_queue.empty():
            line = stdout_queue.get()
            if is_fps_line(line):
                update_fps(line)
                
    '''
    dev = ADBUtil()
    devceno = dev.getDeviceNo()
    dev.start()
    while not dev.eof():
        while not dev.