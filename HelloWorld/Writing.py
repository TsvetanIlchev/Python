# tracklist = "More Mayhem", "Imelda May", "2011", (
#     (1, "Track1"), (2, "Track2"), (3, "Track3"), (4, "Track4"))
#
# with open("imelda3.txt", 'w') as tracklist_file:
#     print(tracklist, file=tracklist_file)

with open("imelda3.txt", 'r') as tracklist_file:
    contents = tracklist_file.readline()

tracklist = eval(contents)

print(tracklist)

title, artist, year, tracks = tracklist
print(title)
print(artist)
print(year)



