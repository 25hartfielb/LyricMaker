import urllib.request
from youtubesearchpython import VideosSearch
import pafy


def searchstring(name):
    query = name.replace(" ", "+")
    print(name)
    print(query)
    return query


def searchforvideo(name):
    query = searchstring(name)
    vidsearch = VideosSearch(name, limit=1)
    #print(vidsearch.result())
    data = vidsearch.result()
    for i in range(1):
        print(data['result'][i]['link'])
        html = data['result'][i]['link']
    input("Please Confirm this is the correct video (Enter to continue) ")
    video = pafy.new(html)
    bestaudio = video.getbestaudio()
    extent = bestaudio.extension
    bestaudio.download(filepath = "audio" + extent, quiet=False)


# def searchforvideourllib(name):
# searchstring(name) = query
# html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
# print(html.read().decode())


print("Welcome to music lyric video maker python")
song = input("Which song would you like to use?: ")
searchforvideo(song)
