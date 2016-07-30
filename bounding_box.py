import os
from PIL import Image
from lxml import etree as ET

rootdir = '/Users/sumukhshivakumar/Desktop/rpal/xml_file_creator/images'

for subdir, dirs, files in os.walk(rootdir):
    for d in dirs:
        # print (rootdir + '/'+ d)
        for files in os.walk(rootdir + '/'+ d):
            for x in files[-1][1:]:
                # print rootdir + '/' + d + '/' + x
                with Image.open(rootdir + '/' + d + '/' + x) as im:
                    width, height = im.size
                    # print x + ": " + str(width) + ' x ' + str(height)
                    root = ET.Element("annotation")
                    # doc = ET.SubElement(root, "doc")
                    x = os.path.splitext(x)[0]
                    ET.SubElement(root, "folder").text = x
                    tree = ET.ElementTree(root)
                    tree.write(x +".xml", pretty_print=True)
