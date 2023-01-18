import urllib.request
from youtubesearchpython import VideosSearch
import pafy
from lyricsgenius import Genius
from pydub import AudioSegment


def converttowav(file):
    m4a_file = file
    wav_file = r"audio.wav"
    track = AudioSegment.from_file(m4a_file, format='m4a')
    file_handle = track.export(wav_file, format='wav')
    print("File has been converted to wav")


def findlyric(song):
    token = "zmJkw5My6AxlLTAtTvY3OGkl8wJSxJJInPZjtavfkgKOCkvnJfTbF7xnfOLkGs2X"
    genius = Genius(token)
    songs = genius.search_song(song)
    print(songs.lyrics)
    lyrics = songs.lyrics
    text_file = open("lyric.txt", "w")
    text_file.write(lyrics)
    text_file.close()

def searchstring(name):
    query = name.replace(" ", "+")
    print(name)
    print(query)
    return query


def searchforvideo(name):
    query = searchstring(name)
    vidsearch = VideosSearch(name, limit=1)
    # print(vidsearch.result())
    data = vidsearch.result()
    for i in range(1):
        print(data['result'][i]['link'])
        html = data['result'][i]['link']
    input("Please Confirm this is the correct video (Enter to continue) ")
    video = pafy.new(html)
    bestaudio = video.getbestaudio()
    extent = bestaudio.extension
    bestaudio.download(filepath="audio." + extent, quiet=False)
    print("Audio has been downloaded")
    flenme = "audio." + extent
    converttowav(flenme)
    findlyric(name)


# def searchforvideourllib(name):
# searchstring(name) = query
# html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
# print(html.read().decode())


print("Welcome to music lyric video maker python")
song = input("Which song would you like to use?: ")
# artist = input("What is the name of the songs artist?: ")
# converttowav("C:\Users\hartf\PycharmProjects\LyricMaker\audio.m4a")
searchforvideo(song)

