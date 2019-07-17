import os 

# Read in the file
with open('grade.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Very Good', '1')
filedata = filedata.replace('Above Average', '2')
filedata = filedata.replace('Good Quality', '3')
filedata = filedata.replace('Excellent', '4')
filedata = filedata.replace('Average', '5')
filedata = filedata.replace('Superior', '6')
filedata = filedata.replace('Fair Quality', '7')
filedata = filedata.replace('Exceptional-D', '8')
filedata = filedata.replace('Exceptional-C', '9')
filedata = filedata.replace('Low Quality', '10')
filedata = filedata.replace('Exceptional-A', '11')
filedata = filedata.replace('Exceptional-B', '12')
filedata = filedata.replace('No Data', '13')

# Write the file out again
with open('grade.csv', 'w') as file:
  file.write(filedata)


