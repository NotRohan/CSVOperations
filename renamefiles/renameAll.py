import os
import csv
path = '<your path>'
files = os.listdir(path)	
i = 1

for file in files:
    print(file)
    with open(path+"/"+file, 'r') as csvFile:
      print(file)
      reader = list(csv.reader(csvFile))
      name = str(reader[1][1])
      name = name[0:10]
    csvFile.close()
    os.rename(os.path.join(path, file), os.path.join(path, name+'.csv'))
    i = i+1
