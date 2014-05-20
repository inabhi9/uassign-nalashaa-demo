from sources import BbcNews, TheGuardian
from helper import UrlGrabber, HtmlBParser
from urlparse import urlparse
from os.path import basename

# Application configuration
GUARDIAN_API_KEY = '2ugtcs5mf3s39cgdc2c6b8pp'
BBCNEWS_API_KEY = ''
STORAGE_DIR = '/tmp'


def storeImage(source):

    for url in source.getWebUrls(query='obama') or []:
        # fetching URL content and parsing for first image
        htmlparser = HtmlBParser(None)
        htmlparser._setContentFromUrl(url)
        imgSrc = htmlparser.getFirstImageSrc()

        # fetching image
        urlgrabber = UrlGrabber(imgSrc)
        img = urlgrabber.get()

        # Storing image
        fname = basename(urlparse(imgSrc).path)
        with open('%s/%s' % (STORAGE_DIR, fname), 'w') as f:
            f.write(img)

# For Guardian
theguardian = TheGuardian(apikey=GUARDIAN_API_KEY)
storeImage(theguardian)
# For BBC new
bbcnew = BbcNews()
storeImage(bbcnew)
