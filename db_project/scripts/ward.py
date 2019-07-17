import os 

# Read in the file
with open('ward.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Ward 1', '1')
filedata = filedata.replace('Ward 2', '2')
filedata = filedata.replace('Ward 3', '3')
filedata = filedata.replace('Ward 4', '4')
filedata = filedata.replace('Ward 5', '5')
filedata = filedata.replace('Ward 6', '6')
filedata = filedata.replace('Ward 7', '7')
filedata = filedata.replace('Ward 8', '8')


# Write the file out again
with open('ward.csv', 'w') as file:
  file.write(filedata)






