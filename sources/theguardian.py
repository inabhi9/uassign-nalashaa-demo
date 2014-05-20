'''
Created on 20-May-2014

@author: Abhinav
'''
from base import BaseSource
from helper import UrlGrabber


class TheGuardian(BaseSource):
    '''
    The SDK of Guardain
    '''

    __endPoint = "http://content.guardianapis.com"

    def __init__(self, **kwargs):
        '''
        Constructor
        '''

        self._apiKey = kwargs.get('apikey')

    def _search(self, query):
        urlgrabber = UrlGrabber('%s/search' % self.__endPoint)
        response = urlgrabber.get({'q': query, 'format': 'json',
                                   'api-key': self._apiKey}) or {}
        return response.get('response')

    def getWebUrls(self, **kargs):
        """
        It uses search end point for getting urls

        :param str query: Query string to be searched
        :retval generator: it yields the url generator
        """

        resposne = self._search(kargs.get('query'))
        if resposne == None:
            return None

        results = resposne.get('results')

        # iterating result and yielding urls
        return [result.get('webUrl') for result in results]
