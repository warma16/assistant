from QQMusicAPI import QQMusic
import requests
inf=0
def w_in(c):
    with open('music.m4a','wb') as f:
        f.write(c)    
def search_song(songname):
    music_list=QQMusic.search(songname)
    music=music_list.data
    song=music[inf]
    try:
        resp = requests.get(song.song_url(), headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'})
        if resp.status_code == 200:
            w_in(resp.content)    
            return '开始播放'                       
        else:
            return '无法播放'               
    except:
        return '无法播放'
    w_in(resp.content)
def next_song():
    inf=inf+1
    try:
        try:
            song=music[inf]
        except KeyError:
            if music_list.cursor_page < music_list.page_size:
                music_list=music_list.next_page()
                music=music_list.data
                inf=0
                song=music[inf]
                
        resp = requests.get(song.song_url(), headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'})
        if resp.status_code == 200:
            w_in(resp.content)    
            return '开始播放'                       
        else:
            return '无法播放'               
    except:
        return '无法播放'
def back_song():
    inf=inf-1
    if inf < 0:
        return '无法播放'
    try:
        try:
            song=music[inf]
        except KeyError:
            music_list=music_list.prev_page()
            music=music_list.data
            inf=len(music)-1
            song=music[inf]
                
        resp = requests.get(song.song_url(), headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'})
        if resp.status_code == 200:
            w_in(resp.content)    
            return '开始播放'                       
        else:
            return '无法播放'               
    except:
        return '无法播放'