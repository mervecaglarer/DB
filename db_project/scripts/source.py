import os 

# Read in the file
with open('source.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('Residential', '1')
filedata = filedata.replace('Condominium', '2')



# Write the file out again
with open('source.csv', 'w') as file:
  file.write(filedata)


