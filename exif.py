import exifread


image = open("C:\\Users\\yuri7100\\Desktop\\DJI_0424.JPG")
tags = exifread.process_file(image)
for tag in tags.keys():
       print "Key: %s, value %s" % (tag, tags[tag])

