import requests
import urllib.request
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

downloaded = '0'
def download_listener(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    new_downloaded = '%.1f' % per
    global downloaded
    if new_downloaded != downloaded:
        downloaded = new_downloaded
        print ('download %s%%  %s/%s' % (downloaded, a * b, c))

def getResponse(url,headers):
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response
        return None
    except RequestException:
        return None

def getSongName(songid):
    headers = {"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",}
    url = "https://music.163.com/m/song?id={}".format(songid)
    Text = getResponse(url,headers).text
    soup = BeautifulSoup(Text,"lxml")
    title = soup.title.text
    name,*_ = title.split('-')
    return name.strip()

if __name__=='__main__':
    songid = input("Please Enter songid:")
    url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(songid)
    headers = {"user-agent":UserAgent().random}
    downurl = getResponse(url,headers).url
    SongName = getSongName(songid)
    urllib.request.urlretrieve(downurl, SongName + ".mp3",download_listener)
