from urllib import request
from bs4 import BeautifulSoup


def getWeather():
    url="https://tianqi.moji.com/weather/china/shanghai/shanghai"
    htmlData = request.urlopen(url).read().decode('utf-8')
    # print(htmlData)
    soup = BeautifulSoup(htmlData, 'html.parser')
    #print(soup)
    weather = soup.find('meta',attrs={'name':"description"})
    wtxt =  weather.get_attribute_list("content")[0]
    # print(wtxt)
    return wtxt

def getSHYQ():
    url="https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner&city=%E4%B8%8A%E6%B5%B7-%E4%B8%8A%E6%B5%B7"
    htmlData = request.urlopen(url).read().decode('utf-8')
    # print(htmlData)
    soup = BeautifulSoup(htmlData, 'html.parser')
    print(soup)
    # weather = soup.find('meta',attrs={'name':"description"})
    # wtxt =  weather.get_attribute_list("content")[0]
    # # print(wtxt)
    # return wtxt