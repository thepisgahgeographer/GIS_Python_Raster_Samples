import arcpy

fc = r"C:\Users\yuri7100\Desktop\PYTS\Data\CountyData.gdb\ParcelPts"
uFields = ["SquFoot", "TaxValue", "PriceSquFt"]
sFields = ["Parcel_ID", "Owner_Name", "Phone_Number", "PriceSquFt"]
parcelList = ["Parcel_Id,Owner_Name,Phone_Number,PriceSquFt"]


with arcpy.da.UpdateCursor(fc, uFields) as cursor:
    for row in cursor:
        row[2] = row[1]/row[0]
        cursor.updateRow(row)


exp = '"PriceSquFt" <=90'

with arcpy.da.SearchCursor(fc, sFields, exp) as sCursor:
    for row in sCursor:
        rowText = "{},{},{},{}".format(row[0],row[1],row[2],row[3])
        parcelList.append(rowText)


textBody = '\n'.join(parcelList)
csvFile = open(r"C:\Users\yuri7100\Desktop\PYTS\AssessmentParcels.csv","w")
csvFile.write(textBody)
csvFile.close()
print("Script Complete")