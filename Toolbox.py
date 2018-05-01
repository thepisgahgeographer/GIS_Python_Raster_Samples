import arcpy
import laspy
import os, sys, matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Read_LAS_Header"
        self.description = "This script tool crawls through a raw .las file and writes out that info to a .txt file"
        self.canRunInBackground = False

    def getParameterInfo(self):
        
        input_LAS = arcpy.Parameter(
            displayName = "Input LAS File",
            name = "File",
            datatype = "DEFile",
            parameterType = "Required"
        )

        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return





#Specify a variable to store the file object
inputLas = arcpy.GetParameterAsText(0)


print("Header Fields Are:")
#Read and print all of the input header fields
headerformat = inputLas.header.header_format
for spec in headerformat:
    print(spec.name)


#Create a Format variable and store the Header Object
Format = inputLas.header

print("Software ID is:" + str(Format.software_id))

print("GUID is:" + str(Format.guid))

print("Date of Capture is:" + str(Format.date))

print("Point Record Count is:" + str(Format.point_records_count))

print("GPS Time is:" + str(Format.gps_time_type))

print("Point Return Count is:" + str(Format.point_return_count))

print("Header min is (XYZ):" + str(Format.min))

print("Header max is (XYZ):" + str(Format.max))

print("Scale is:" + str(Format.scale))

print("Input Format is:" + str(Format.file_signature))



print("ASCII specified field names:")
#User the Point Format method to Capture what individual point fields are avaliable in the Raw Point Data
pointFormat = inputLas.point_format
for spec in pointFormat:
    print(spec.name)


print("Grab the first and last 3 point XYZ:")
coordinates = np.vstack((inputLas.x, inputLas.y, inputLas.z)).transpose()
print(coordinates)


#Use the File Object to Return Information about the Raw Points
print ("Intensity is:" + str(inputLas.intensity))

print ("Point Source ID is:" + str(inputLas.pt_src_id))

print("Raw Classification is:" + str(inputLas.raw_classification))

print("X Value is:" + str(inputLas.x))

print("Y Value is:" + str(inputLas.y))

print("Z Value is:" + str(inputLas.z))

print("Flag Byte Value is:" + str(inputLas.flag_byte))

print("User Data Value is:" + str(inputLas.user_data))

fig, ax = plt.subplots()

plt.hist(inputLas.z)
plt.title("Range of Z values")
ax.set_xlabel("Elevation Values")
ax.set_ylabel("Number of Returns")
plt.show()
