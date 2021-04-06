import requests
from json import loads
from ._common import url_from_url_from_hash

class hitomi:
    
    def __init__(self):
        pass

    def _clear(self, l, element):
        '''
        remove all element that match the ::element:: parameter
        '''
        #pylint: disable=unused-variable
        for i in range(l.count(element)):
            l.remove(element)
        return l

    def getlist(self, tag='index', language='all', by=None, length=25):
        '''
        by default return a list of recently added content
        '''
        url = '/'.join(self._clear(['http://ltn.hitomi.la', by, '-'.join([tag, language])+'.nozomi'], None))
        req = requests.get(url)
        l = []
        for i in range(length):
            l.append(int.from_bytes(req.content[i*4:i*4+4], 'big', signed=True))
        return l

class Gallery:
    def __init__(self, ID):
        self.ID = ID

        req = requests.get('http://ltn.hitomi.la/galleries/{}.js'.format(self.ID)).text
        self.Data = loads(req[req.find('{'):-1]+'}')

        l = []
        for i in range(len(self.Data['files'])):
            _type = ''
            if self.Data['files'][i]['hasavif']:
                _type = 'avif'
            else:
                _type = 'webp'
            l.append(url_from_url_from_hash(
                self.Data['id'], self.Data['files'][i], _type, None, 'a'))
        self.ImagesUrls = l

        self.GalleryBlock = requests.get(
            'https://ltn.hitomi.la/galleryblock/{}.html'.format(id)).text

    def getImageContent(self, url):
        return requests.get(url, headers={
            'Referer': 'https://hitomi.la/reader/{}.html'.format(self.ID)
        }).content