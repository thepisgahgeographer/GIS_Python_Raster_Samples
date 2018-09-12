#import modules
import arcpy, csv
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(103501)
print("Modules imported and environments set.")

#variables
outageXY = r""
outConvexHull = r""
outputJoin = r""
serviceAreas = r""
print("Variables are set.")

#Append coordinates from csv in a list
outageCoords = []
csvFile = open(outageXY)
csvReader = csv.reader(csvFile)
next(csvReader)
for row in csvReader:
    outageCoords.append(row)

#Create a multipoint geometry object from list of coordinates
#Takes outageCoords and * splits the list into comma sep. values to be passed to the Point Class Constructor Method
outagePoints = (arcpy.Multipoint(arcpy.Array([arcpy.Point(*coords) for coords in
outageCoords])))
print("Geometry object created.")


#Create outage boundary using convex hull


#Use Spatial Join to identify affected areas
arcpy.SpatialJoin_analysis(serviceAreas,outagePoints,outputJoin)
print("Spatial join finished.")

#Search join output
sFields = ['Join_Count', 'ServArNu']
exp = '"Join_Count" = 1'
print("Affected service areas")
with arcpy.da.SearchCursor(outputJoin,sFields,exp) as sCursor:
    for row in sCursor:
        print("Service Area: {}".format(row[1]))

print("Analysis complete.")
