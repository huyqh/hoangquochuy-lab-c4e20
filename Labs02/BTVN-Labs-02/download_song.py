from youtube_dl import YoutubeDL
name_song = input("enter the song's name?")



options = {"default_search": "ytsearch", "max_downloads": 1}
dl = YoutubeDL(options)
dl.download([str(name_song)])
