import os 

# Read in the file
with open('quadrant.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('NW', '1')
filedata = filedata.replace('SW', '2')
filedata = filedata.replace('SE', '3')
filedata = filedata.replace('NE', '4')


# Write the file out again
with open('quadrant.csv', 'w') as file:
  file.write(filedata)


