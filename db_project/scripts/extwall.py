import os 

# Read in the file
with open('extwall.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Common Brick', '1')
filedata = filedata.replace('Brick/Stone', '2')
filedata = filedata.replace('Stucco', '3')
filedata = filedata.replace('Stone', '4')
filedata = filedata.replace('Stucco Block', '5')
filedata = filedata.replace('Brick/Stucco', '6')
filedata = filedata.replace('Concrete Block', '7')
filedata = filedata.replace('Face Brick', '8')
filedata = filedata.replace('Wood Siding', '9')
filedata = filedata.replace('Aluminum', '10')
filedata = filedata.replace('Brick/Siding', '11')
filedata = filedata.replace('Vinyl Siding', '12')
filedata = filedata.replace('Stone Veneer', '13')
filedata = filedata.replace('Brick Veneer', '14')
filedata = filedata.replace('Stone/Stucco', '15')
filedata = filedata.replace('Stone/Siding', '16')
filedata = filedata.replace('Metal Siding', '17')
filedata = filedata.replace('Shingle', '18')
filedata = filedata.replace('Concrete', '19')
filedata = filedata.replace('Plywood', '20')
filedata = filedata.replace('Hardboard', '21')
filedata = filedata.replace('Default', '22')
filedata = filedata.replace('Adobe', '23')
filedata = filedata.replace('Rustic Log', '24')
filedata = filedata.replace('SPlaster', '25')
filedata = filedata.replace('3 Block', '26')
filedata = filedata.replace('Brick/3', '27')
filedata = filedata.replace('4 Veneer', '28')
filedata = filedata.replace('4/3', '29')
filedata = filedata.replace('4/Siding', '30')

# Write the file out again
with open('extwall.csv', 'w') as file:
  file.write(filedata)


