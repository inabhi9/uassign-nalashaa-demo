'''
Created on 20-May-2014

@author: Abhianv
'''
import urllib2
import urllib
import json


class UrlGrabber(object):
    '''
    Handles HTTP url request via GET or POST METHOD
    '''

    def __init__(self, url, headers={}):
        self._url = url
        self._headers = headers

    def get(self, queryParams={}):
        qs = urllib.urlencode(queryParams)
        request = urllib2.Request("%s?%s" % (self._url, qs))
        response = urllib2.urlopen(request)
        self._rawResponse = response.read()
        self._responseInfo = response.info()
        if 'application/json' in self._responseInfo.getheader('Content-Type'):
            return json.loads(self._rawResponse)
        else:
            return self._rawResponse
