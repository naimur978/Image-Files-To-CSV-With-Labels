import os
import csv

path = './train'

# Loop through path and add all files matching *.jpg to array files
with open('output.csv', 'w', newline='') as csvfile:
    files = []
    for r, d, f in os.walk(path):
        for _file in f:
            if '.jpg' in _file:
                files.append(_file)

    # Create a writer from csv module
    writer = csv.writer(csvfile, delimiter=',')
    for f in files:  # find type of file
        # cut off the number and .jpg from file, leaving only the type (this may have to be changed.)
        t = f[0:-4]

        if "cbb" in t:
            t = 0
        elif "cbsd" in t:
            t = 1
        elif "cgm" in t:
            t = 2
        elif "cmd" in t:
            t = 3
        elif "healthy" in t:
            t = 4

        writer.writerow([f, t])  # write the row to the file output.csv
