import youtube_dl


'''
playlist.txt stores youtube linkes for a playlist to extract from it
'''
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

'''
Output example :
output.jason 
    ID:Nn7EX3zkGUo-Tittle:Introduction - CS50's Web Programming with Python and JavaScript 2020
    ID:zFZrkCIc2Oc-Tittle:HTML and CSS - Lecture 0 - CS50's Web Programming with Python and JavaScript 2020
    ID:NcoBAfJ6l2Q-Tittle:Git - Lecture 1 - CS50's Web Programming with Python and JavaScript 2020
    ID:EOLPQdVj5Ac-Tittle:Python - Lecture 2 - CS50's Web Programming with Python and JavaScript 2020
'''
