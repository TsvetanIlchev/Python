import pickle
#
# imelda = ('More Mayhem',
#           'Imelda May',
#           '2011',
#           ((1, "Track1",),
#            (2, "Track2",),
#            (3, "Track3")))
#
# with open("imelda.pickle", 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)

with open("imelda.pickle", 'rb') as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, tracks = imelda2

print(album)
print(artist)
print(year)
for track in tracks:
    track_number, track_title = track
    print(track_number, track_title)