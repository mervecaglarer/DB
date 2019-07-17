import os 

# Read in the file
with open('style.csv', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('3 Story', '1')
filedata = filedata.replace('4 Story', '2')
filedata = filedata.replace('2 Story', '3')
filedata = filedata.replace('2.5 Story Fin', '4')
filedata = filedata.replace('3.5 Story Fin', '5')
filedata = filedata.replace('1 Story', '6')
filedata = filedata.replace('1.5 Story Fin', '7')
filedata = filedata.replace('2.5 Story Unfin', '8')
filedata = filedata.replace('3.5 Story Unfin', '9')
filedata = filedata.replace('Default', '10')
filedata = filedata.replace('1.5 Story Unfin', '11')
filedata = filedata.replace('4.5 Story Fin', '12')
filedata = filedata.replace('Split Level', '13')
filedata = filedata.replace('Bi-Level', '14')
filedata = filedata.replace('Split Foyer', '15')
filedata = filedata.replace('Vacant', '16')
filedata = filedata.replace('Outbuildings', '17')
filedata = filedata.replace('4.5 Story Unfin', '18')


# Write the file out again
with open('style.csv', 'w') as file:
  file.write(filedata)






