from time import sleep
from ThreadManager.threadwrap import ThreadWrap

class ThreadManager:
    def __init__(self,maxThread,**kwargs):
        self.maxThread = maxThread
        self.delay = kwargs.get('delay',.0001)
        self.threadCount = 0
        
    def queueThread(self,**kwargs):
 
        t = ThreadWrap(target=self._startThread,threadArgs=kwargs)

        while self.threadCount >= self.maxThread:
            sleep(self.delay)
        
        
        t.start()

        return t

    def _startThread(self,threadArgs):
        fxn = threadArgs['target']
        args = threadArgs['args']

        self.threadCount += 1
        fxn(*args)
        self.threadCount -= 1

        


            


    

        

