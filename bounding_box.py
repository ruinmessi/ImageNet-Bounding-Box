import os
from PIL import Image

rootdir = '/Users/sumukhshivakumar/Desktop/rpal/xml_file_creator/images'

for subdir, dirs, files in os.walk(rootdir):
    for d in dirs:
        # print (rootdir + '/'+ d)
        for files in os.walk(rootdir + '/'+ d):
            for x in files[-1][1:]:
                # print rootdir + '/' + d + '/' + x
                with Image.open(rootdir + '/' + d + '/' + x) as im:
                    width, height = im.size
                    print x + ": " + str(width) + ' x ' + str(height)
