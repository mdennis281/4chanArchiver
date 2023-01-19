import requests, os

HOST = 'https://a.4cdn.org/'
IMG_HOST = 'https://i.4cdn.org/'


class Web4chan:
    def __init__(self,board,**kwargs):
        self.board = board
        self.host = kwargs.get('host',HOST)
        self.base = self.host + board
        self.imgHost = kwargs.get('imgHost',IMG_HOST)
        self.imgBase = self.imgHost + board
    
    def getBoardThreads(self):
        data = self._apiGetJson('/threads')
        
        ans = []
        for page in data:
            for thread in page['threads']:
                ans.append(thread)

        return ans

    def getThreadReplies(self,threadId):
        data = self._apiGetJson(f'/thread/{threadId}')
        return data

    # make a function to download an image to a path
    def downloadImage(self,threadId,imgId,fileExt):
        savePath = f'./images/{threadId}/'
        fileName = f'{imgId}{fileExt}'
        url = f'{self.imgBase}/{imgId}{fileExt}'
        
        # make file and dir if not exist

        if not os.path.isfile(savePath+fileName):
            print(f'DOWNLOADING: {url}')
            os.makedirs(os.path.dirname(savePath), exist_ok=True)
            r = requests.get(url,allow_redirects=True)
            with open(savePath+fileName,'wb') as f:
                f.write(r.content)
    

        

    def _apiGetJson(self,uriPath):
        try:
            r = requests.get(f'{self.base}{uriPath}.json')
            return r.json()
        except:
            print(f'ERROR GETJSON: {uriPath}')
            return None
        

        


