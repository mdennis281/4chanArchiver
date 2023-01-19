import threading
from time import sleep

class ThreadWrap:
    def __init__(self,**kwargs):
        self.target = kwargs['target']
        self.args = kwargs['threadArgs']
        self.delay = kwargs.get('delay',.0001)
        self.isStarted=False
        self.thread = self._genThread()


    def _genThread(self):
        return threading.Thread(target=self.target,args=(self.args,))

    def start(self):
        self.isStarted = True
        self.thread.start()

    def join(self):
        while not self.isStarted:
            sleep(self.delay)
        return self.thread.join()