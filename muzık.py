from youtube_dl import YoutubeDL


is_playing = False

music_queue = []
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
vc = ""

def search_yt(item):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try: 
            info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
        except Exception: 
            return False

    return {'source': info['formats'][0]['url'], 'title': info['title'],'thumbnail':info['thumbnail']}


m_url = music_queue


a = search_yt('doja cat you right')
print(a)    
