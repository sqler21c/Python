#!/usr/bin/env python
# -*- endoding : utf8
import queue
import threading
#import thread
import time
import datetime
import random
###############################################################################
class cmdQ():
    #==========================================================================
    CMDS = {}
    #==========================================================================
    def __init__(self, cmd, *args, **kwargs):
        if not cmdQ.CMDS.has_key(cmd):
            raise ReferenceError('Invalid cmdQ.command<%s>' % cmd)
        self.cmd = cmd
        self.args = args
        self.kwargs = kwargs
    #==========================================================================
    def __repr__(self):
        sb = ['cmdQ instance{']
        sb.append('cmd="%s"' % self.cmd)
        for arg in self.args: sb.append(',%s' % arg)
        for k,v in self.kwargs.items(): sb.append(',%s="%s"' % (k,v))
        sb.append('}')
        return ''.join(sb)
    #==========================================================================
    @staticmethod
    def SetCommands(cmds):
        if not isinstance(cmds,dict):
            raise TypeError('cmdQ.SetCommands need only dictionary type parameters but <%s>' % type(cmds))
        cmdQ.CMDS = cmds
###############################################################################
class BackgroundWorker(threading.Thread):
    """Background worker using threads"""
    #==========================================================================
    DO=0
    DONE=1
    EXCEPT=2
    #==========================================================================
    def __init__(self, Q):
        threading.Thread.__init__(self)
        self.Q = Q
        self.is_doing = False
    #==========================================================================
    
    
    def run(self):
        t_ident = str(threading.get_ident())[-4:]
        print('[%s] BackgroundWorker.run Starting...' % t_ident)
        while True:
            cmdq = self.Q.get()
            cmdq.kwargs['t_ident'] = t_ident
            self.is_doing = True
            try:
                if not cmdQ.CMDS.has_key(cmdq.cmd):
                    raise LookupError('Cannot find command "%s"' % cmdq.cmd)
                cmdQ.CMDS[cmdq.cmd][BackgroundWorker.DO](cmdq)
                cmdQ.CMDS[cmdq.cmd][BackgroundWorker.DONE](cmdq)
            except Exception:
                cmdQ.CMDS[cmdq.cmd][BackgroundWorker.EXCEPT](cmdq,Exception)
            finally:
                # send done signal to Q
                self.is_doing = False
                self.Q.task_done()
        print('[%s] BackgroundWorker.run end.' % t_ident)
    #==========================================================================
    def isDoing(self):
        return self.is_doing
###############################################################################
class doJob():
    def doA(self, cmdq):
        print('[%s] %s doing~' % (datetime.datetime.now(),cmdq))
        time.sleep(1)
    def doneA(self, cmdq):
        print('[%s] %s done!' % (datetime.datetime.now(),cmdq))
    def doB(self, cmdq):
        print('[%s] %s doing~' % (datetime.datetime.now(),cmdq))
        time.sleep(2)
        raise NotImplementedError('Test Error') # �׽�Ʈ�� ���ܹ߻�
    def doneB(self, cmdq):
        print('[%s] %s done!' % (datetime.datetime.now(),cmdq))
    def doC(self, cmdq):
        print('[%s] %s doing~' % (datetime.datetime.now(),cmdq))
        time.sleep(3)
    def doneC(self, cmdq):
        print('[%s] %s done!' % (datetime.datetime.now(),cmdq))
    def doFail(self, cmdq, e):
        print('[%s] %s fail! <%s>' % (datetime.datetime.now(),cmdq,e))
###############################################################################
def main():
    # 1) ���� �۾��� ������ ��ü�� �����Ѵ�
    job = doJob()
    # 2) �������۾����� ������ ��ɾ� �� �ݹ��Լ��� �����Ѵ�
    #  '���':(�����۾��Լ�, �Ϸ����۾��Լ�, ���н��۾��Լ�)
    #  ������ �Լ� ��� ù��° ���ڷ� cmdQ ��ü�� �Ѿ����
    #  ���н��۾��Լ��� ��� �ι�° ���ڷ� Exception ��ü�� �Ѿ��
    cmds = {
        'A':(job.doA,job.doneA,job.doFail),
        'B':(job.doB,job.doneB,job.doFail),
        'C':(job.doC,job.doneC,job.doFail),
    }
    # ������ ������ ����� ���� (Ŭ���� �Լ�)
    cmdQ.SetCommands(cmds)
    # ������ �۾� ���� ����
    NUM_WORKERS = 5
    # �۾� ���ť
    Q = queue.Queue()
    # 3) ���� �۾� ������ ����
    for _ in range(NUM_WORKERS):
        bw = BackgroundWorker(Q)
        bw.setDaemon(True)
        bw.start()
    # 4) �׽�Ʈ�� 10���� �۾��� �۾�ť�� ����
    for _ in range(10):
        rand_cmd = cmds.keys()[random.randint(0,len(cmds)-1)]
        cmdq = cmdQ(rand_cmd,param_cmd=rand_cmd)
        Q.put(cmdq)
    # 3�ʰ� ���� �� ��� ť�� �ƹ� �۾��� ������ ����
    time.sleep(3)
    Q.join()
###############################################################################
if __name__=='__main__':
    main()