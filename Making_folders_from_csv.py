import csv
import os
import re

i_csvFile = 'C:\\'
path = 'C:\\'


with open(i_csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row[0] + ' ' + row[1])
        dirName = row[0] + ' ' + row[1]
        dirName = re.sub('[^A-Za-z0-9]+', ' ', dirName)
        try:
            os.mkdir(path + dirName)
            print("Directory " , dirName ,  " Created ")
        except FileExistsError:
            print("Directory " , dirName ,  " already exists")
