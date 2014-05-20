'''
Created on 20-May-2014

@author: Abhinav
'''


class BaseSource(object):
    '''
    Base class that has abstraction to other source
    '''

    # End point for new source, should be override
    __endPoint = None

    def __init__(self, **kwargs):
        """
        Takes basic class wide configuration
        """

    def getWebUrls(self, **kwargs):
        """
        Abstract method and must be override
        """
        raise NotImplementedError
