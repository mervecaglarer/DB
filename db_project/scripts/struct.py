import os 

# Read in the file
with open('struct.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Row Inside', '1')
filedata = filedata.replace('Semi-Detached', '2')
filedata = filedata.replace('Single', '3')
filedata = filedata.replace('Row End', '4')
filedata = filedata.replace('Multi', '5')
filedata = filedata.replace('Town Inside', '6')
filedata = filedata.replace('Town End', '7')
filedata = filedata.replace('Default', '8')
filedata = filedata.replace('Vacant Land', '9')


# Write the file out again
with open('struct.csv', 'w') as file:
  file.write(filedata)


