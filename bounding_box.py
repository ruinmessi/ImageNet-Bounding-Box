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
                    ET.SubElement(root, "folder").text = d
                    ET.SubElement(root, "filename").text = x
                    source = ET.SubElement(root, "source")
                    ET.SubElement(source, "database").text = "ImageNet database"
                    size = ET.SubElement(root, "size")
                    ET.SubElement(size, "width").text = str(width)
                    ET.SubElement(size, "height").text = str(height)
                    ET.SubElement(size, "depth").text = '3'
                    ET.SubElement(root, "segmented").text = "0"
                    object = ET.SubElement(root, "object")
                    ET.SubElement(object, "name").text = d
                    ET.SubElement(object, "pose").text = 'Unspecified'
                    ET.SubElement(object, "truncated").text = '0'
                    ET.SubElement(object, "difficult").text = '0'
                    bndbox = ET.SubElement(object, "bndbox")
                    ET.SubElement(bndbox, "xmin").text = '0'
                    ET.SubElement(bndbox, "ymin").text = '0'
                    ET.SubElement(bndbox, "xmax").text = str(width)
                    ET.SubElement(bndbox, "ymax").text = str(height)







                    tree = ET.ElementTree(root)
                    directory = rootdir + '/boundingboxes/' + d
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    tree.write(directory + '/' + x +".xml", pretty_print=True)
                    # tree.write(x +".xml", pretty_print=True)
