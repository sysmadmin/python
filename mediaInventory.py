# Retrieve Media inventory on localhost

import os

home = os.path.expanduser('~')
mediaLocations = [home + '/Movies', home + '/TV']
mediaListName = 'Media List.txt'

if not os.path.exists(os.path.join(home, mediaListName)):
    open((os.path.join(home, mediaListName)), 'w')
else:
    open((os.path.join(home, mediaListName)), 'w').truncate()

mediaList = open((os.path.join(home, mediaListName)), 'a')

for location in mediaLocations:
    mediaList.write("\n" + os.path.basename(location) + "\n\n")
    for item in os.listdir(location):
        mediaList.write("%s\n" % item)

mediaList.close()
