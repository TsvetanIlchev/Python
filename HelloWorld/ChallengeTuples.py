imelda = "More Mayhem", "Imelda May", 2011, (
    (1 , "Track1"), (2, "Track2"), (3, "Track3"), (4, "Track4"))

artist, album, year, tracks = imelda
print("Artist name: {}\n".format(artist), "Album name: {}\n".format(album), "Year: {}\n".format(year))
for song in tracks:
    trackNumber, title = song
    print("\tTrack number {}, Title {}".format(trackNumber, song))
# print(tracks[0], tracks[1], tracks[2], tracks[3])