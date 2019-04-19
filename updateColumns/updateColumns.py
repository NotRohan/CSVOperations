import os
import csv
import pandas as pd
path = '<your path>'
files = os.listdir(path)
i = 1

for file in files:
    print(file)
    f = open(path+"/"+file, 'r')
    reader = csv.reader(f)
    mylist = list(reader)
    count=0
    for row in mylist:
      count+=1
    print(count)
    f.close()
    mylist[0][1] = 'Date'
    mylist[0][3] = 'long'
    for x in range(1, count):
      mylist[x][1] = mylist[x][1][:10]
      mylist[x][3] = mylist[x][3].split(',')[0]
      mylist[x][8] = mylist[x][8].split(',')[1]
      mylist[x][7] = mylist[x][7][10:]
    my_new_list = open(path+"/"+file, 'w')   
    csv_writer = csv.writer(my_new_list)
    csv_writer.writerows(mylist)
    my_new_list.close()
    i = i+1




