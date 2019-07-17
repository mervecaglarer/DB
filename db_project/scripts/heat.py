import os 

# Read in the file
with open('heat.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Warm Cool', '1')
filedata = filedata.replace('Hot Water Rad', '2')
filedata = filedata.replace('Forced Air', '3')
filedata = filedata.replace('Elec Base Brd', '4')
filedata = filedata.replace('Ht Pump', '5')
filedata = filedata.replace('Electric Rad', '6')
filedata = filedata.replace('Wall Furnace', '7')
filedata = filedata.replace('Water Base Brd', '8')
filedata = filedata.replace('Evp Cool', '9')
filedata = filedata.replace('Air Exchng', '10')
filedata = filedata.replace('No Data', '11')
filedata = filedata.replace('Ind Unit', '12')
filedata = filedata.replace('Gravity Furnac', '13')
filedata = filedata.replace('Air Oil', '14')

# Write the file out again
with open('heat.csv', 'w') as file:
  file.write(filedata)






