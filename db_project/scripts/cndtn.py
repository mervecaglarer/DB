import os 

# Read in the file
with open('cndtn.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Good', '1')
filedata = filedata.replace('Very Good', '2')
filedata = filedata.replace('Average', '3')
filedata = filedata.replace('Fair', '4')
filedata = filedata.replace('Excellent', '5')
filedata = filedata.replace('Poor', '6')
filedata = filedata.replace('Default', '7')
filedata = filedata.replace('Very 1', '8')

# Write the file out again
with open('cndtn.csv', 'w') as file:
  file.write(filedata)


