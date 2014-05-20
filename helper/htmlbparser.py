'''
Created on 20-May-2014

@author: Abhinav
'''
from BeautifulSoup import BeautifulSoup
from urlgrabber import UrlGrabber


class HtmlBParser(object):
    '''
    Html parser using beautifulsoup
    '''

    def __init__(self, content):
        '''
        :param str content: HTML content to be parsed
        '''
        self._htmlContent = content

    def _setContentFromUrl(self, url):
        """
        Fetching content from url and set it to self._content

        :param str url: URL to be fetched
        """
        urlgrabber = UrlGrabber(url)
        self._htmlContent = urlgrabber.get()

    def getFirstImageSrc(self):
        soup = BeautifulSoup(self._htmlContent)
        try:
            return soup.find('img').get('src')
        except (IndexError, KeyError, TypeError):
            return None
