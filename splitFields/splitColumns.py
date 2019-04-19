import os
import csv
import pandas as pd
path = '<your path>'
files = os.listdir(path)
i = 1

for file in files:
    print(file)
    csv_input = pd.read_csv(path+"/"+file)
    csv_input['Time'] = csv_input['UTC']
    csv_input['lat'] = csv_input['Position']
    csv_input.to_csv(path+"/"+file, index=False)
    i = i+1
