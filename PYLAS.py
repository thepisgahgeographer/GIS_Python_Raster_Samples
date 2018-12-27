import pylas

lasFile = pylas.read(r"C:\points.las")
print(lasFile.header.point_count, lasFile.header.generating_software, lasFile.header.z_max, lasFile.header.creation_year)
print(lasFile.header)