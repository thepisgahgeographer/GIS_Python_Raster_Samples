import arcpy

#Create a Describe object
rasDesc = arcpy.Describe(r"C:\Users\yuri7100\Desktop\raster_data\461-243-1414.tif")

if rasDesc.bandCount == 1:
    print(str(rasDesc.datasetType) + "   " + str(rasDesc.baseName))
else:
    print("This is not a 3 Band Raster Dataset")

print(str(rasDesc.bandCount) + " " + str(rasDesc.compressionType) + " " + str(rasDesc.format))

print("Raster Band Count = %s " % rasDesc.bandCount)
print("Raster Compression Type = %s" % rasDesc.compressionType)


