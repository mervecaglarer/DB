import os 

# Read in the file
with open('roof.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Metal- Sms', '1')
filedata = filedata.replace('Built Up', '2')
filedata = filedata.replace('Neopren', '3')
filedata = filedata.replace('Comp Shingle', '4')
filedata = filedata.replace('Metal- Cpr', '5')
filedata = filedata.replace('Typical', '6')
filedata = filedata.replace('Slate', '7')
filedata = filedata.replace('Composition Ro', '8')
filedata = filedata.replace('Metal- Pre', '9')
filedata = filedata.replace('Shingle', '10')
filedata = filedata.replace('Concrete', '11')
filedata = filedata.replace('Shake', '12')
filedata = filedata.replace('Clay Tile', '13')
filedata = filedata.replace('Water Proof', '14')
filedata = filedata.replace('Concrete Tile', '15')
filedata = filedata.replace('Wood- FS', '16')


# Write the file out again
with open('roof.csv', 'w') as file:
  file.write(filedata)


