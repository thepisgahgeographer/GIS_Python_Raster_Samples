import arcpy

arcpy.env.workspace = r"C:\Users\yuri7100\Desktop\PYTS\Data\CountyData.gdb"
outWorkspace = r"C:\Users\yuri7100\Desktop\test_data\test.gdb"

fcList = arcpy.ListFeatureClasses("", "Point")
for fc in fcList:
    outputFC = "{}\{}".format(outWorkspace,fc)
    arcpy.CopyFeatures_management(fc, outputFC)
    print("{} copied".format(fc))


#
#print(fc_list)
#print("Number of Feature Classes %s" % len(fc_list))


