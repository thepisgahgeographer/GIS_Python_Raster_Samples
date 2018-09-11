import arcpy

#Create a Describe object
rasDesc = arcpy.Describe(r"")

if rasDesc.bandCount == 3:
    print(rasDesc.datasetType + rasDesc.baseName)
else:
    print("This is not a 3 Band Raster Dataset")

print(rasDesc.bandCount + " " + rasDesc.compressionType + " " + rasDesc.format)

print("Raster Band Count = %s " % rasDesc.bandCount)
print("Raster Compression Type = %s" % rasDesc.compressionType)


