from ThreadManager import ThreadManager
from web4chan import Web4chan
from time import sleep
from json import dumps as jStringify

class Cache4chan:
    def __init__(self,board):
        self.isAlive = 5000
        self.TM = ThreadManager(25)
        self.board = Web4chan(board)
        self.cache = {}

    def start(self):
        self.TM.queueThread(target=self._threadLoop,args=())

    def _threadLoop(self):
        while self.isAlive:
            currentThreads = self.board.getBoardThreads()
            
            # overwrite changes into cache
            for thread in currentThreads:
                #print(thread)
                print("THREADCOUNT:",self.TM.threadCount)
                tId = thread['no']
                existsInCache = tId in self.cache.keys()

                if existsInCache:
                    isModified = thread['last_modified'] > self.cache[tId]['modified']
                    if isModified: 
                        #self.TM.queueThread(target=self._fetchReplies,args=(tId,thread))
                        self._fetchReplies(tId,thread)
                        
                else:
                    self.cache[tId] = {
                        'modified': thread['last_modified']-1,
                        'replies': []
                    }
                    self.TM.queueThread(target=self._fetchReplies,args=(tId,thread))
                    self._fetchReplies(tId,thread)
            
            # cleanup records that no longer exist

            # for tId in self.cache.keys().sort(key = int):
            #     print(tId)

            #self.isAlive = False
            self.isAlive -= 1
        self._saveCache2File()
    
    def _fetchReplies(self, tId,thread):
        # doing twice because time will pass between now and then

        isModified = thread['last_modified'] > self.cache[tId]['modified']
        if isModified: 
            print("THREADCOUNT:",self.TM.threadCount)
            replies = self.board.getThreadReplies(tId)
            self.cache[tId]['replies'] = replies['posts']
            #print(replies)
            self.cache[tId]['modified'] = thread['last_modified']
            for reply in replies['posts']:
                if 'filename' in reply:
                    self.TM.queueThread(target=self.board.downloadImage,args=(tId,reply['tim'],reply['ext']))
    
    def _saveCache2File(self,filename='out.json'):
        with open(filename,'w') as f:
            f.write(
                jStringify(self.cache, sort_keys=True, indent=4)
            )


        

                
            





