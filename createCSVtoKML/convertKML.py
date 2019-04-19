import os
import csv
path = '<your path>'
files = os.listdir(path)	
i = 1

for file in files:
    data = csv.reader(open(path+'/'+file), delimiter = ',')
    data.next()
    #Open the file to be written.
    f = open(file.replace("csv","")+'kml', 'w')
    #Writing the kml file.
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    f.write("<kml xmlns='http://www.opengis.net/kml/2.2'>\n")
    f.write("<Document>\n")
    f.write("   <name>" + file.replace("csv","") + 'kml' +"</name>\n")
    f.write("   <Style id='blueLine'>\n")
    f.write("     <LineStyle>\n")
    f.write("       <color>FFFF00</color>\n")
    f.write("       <width>2</width>\n")
    f.write("     </LineStyle>\n")
    f.write("   </Style>\n")
    f.write("   <Placemark>\n")
    f.write("       <name>" +file.replace("csv","")+'kml'+ "</name>\n") 
    f.write("       <styleUrl>#blueLine</styleUrl>\n")
    f.write("       <LineString>\n")
    f.write("       <altitudeMode>relative</altitudeMode>\n")
    f.write("       <coordinates>\n")
    for row in data:	
        f.write(str(row[8]) + "," + str(row[3]) + "," + str(row[4])+"\n")
    f.write("</coordinates>\n")
    f.write("</LineString>\n")
    f.write("</Placemark>\n")
    f.write("</Document>\n")
    f.write("</kml>\n")
    f.close()
    print(i)
    i = i+1



