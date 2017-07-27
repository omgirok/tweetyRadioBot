import xml.etree.ElementTree as ET

# creates a file called this_is_filename.txt in 'write' mode
# write mode is used to write to file
tree = ET.parse('Library copy.xml')
root = tree.getroot()

nav = root.find('dict')
nav = nav.find('dict')

trackDict = nav.findall('dict')
artistLib = {}

######
# generating ARTIST table
######
artist_file = open('artist_lib.sql', 'w')
# track_file = open('track_lib2.sql', 'w')

for track in trackDict:
  if track[4].text != 'Artist':
    continue
  trackName = track[3].text
  artist = track[5].text
  
  if artist not in artistLib:
    artistLib[artist] = []
    artistLib[artist].append(trackName)
  else:
    # print artist+' already in library'
    artistLib[artist].append(trackName)

  # print artist
# print artistLib['Big Sean']

for x in sorted(artistLib):
  try:
    if "'" in str(x):
      print str(x)
    else:
      artistString = str(x)
    queryString = "INSERT INTO `Music`.`Artist` (`artist_name`) VALUES ('" + artistString + "');\n"
    artist_file.write(queryString)
  except UnicodeEncodeError:
    print "error on string"


######
# generating track table
######
# for x in sorted(artistLib):
#   try:
#     if "'" in str(x):
#       print str(x)
#     else:
#       artistString = str(x)
#       for song in artistLib[x]:
#         print song
#         queryString = "INSERT INTO `Music`.`Songs` (`Artist`, `Title`) VALUES ('" + artistString + "', '" + song + "');\n"
#         track_file.write(queryString)
#   except UnicodeEncodeError:
#     print "error on string"

artist_file.close()
# track_file.close()