import os 

# Read in the file
with open('intwall.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Hardwood', '1')
filedata = filedata.replace('Wood Floor', '2')
filedata = filedata.replace('Hardwood/Carp', '3')
filedata = filedata.replace('Carpet', '4')
filedata = filedata.replace('Lt Concrete', '5')
filedata = filedata.replace('Vinyl Comp', '6')
filedata = filedata.replace('Ceramic Tile', '7')
filedata = filedata.replace('Default', '8')
filedata = filedata.replace('Terrazo', '9')
filedata = filedata.replace('Parquet', '10')
filedata = filedata.replace('Vinyl Sheet', '11')
filedata = filedata.replace('Resiliant', '12')
filedata = filedata.replace('1/Carp', '13')


# Write the file out again
with open('intwall.csv', 'w') as file:
  file.write(filedata)


