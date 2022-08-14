import youtube_dl

playlist_file = open("playlist.txt")

with open("output.json", 'a+') as output:
    for pl in playlist_file:  # iterate through each playlist in the file
        with youtube_dl.YoutubeDL() as ydl:  # open and read each playlist
            # Extract info for each playlist
            playlist_info = ydl.extract_info(pl, download=False)
            # extract_info return a dictionary
            for video in playlist_info['entries']:
                output.write('\n')
                output.write(
                    f'ID:{video.get("id")}-Tittle:{video.get("title")}')
            