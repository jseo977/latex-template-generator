""" Reads in a source tex template and replaces elements with data from a
    csv file.
    inputs: .csv file, .tex template file
    output: many .tex files
"""

from glob import glob
import numpy as np
import os
# Open the csv file
fl = open(glob('TO_PRINT_2020'+'.csv')[0], 'r')
# Extract metadata (header)
ln = fl.readline().strip()
header = ln.split(',')
quant = np.size(header) # Number of different amounts of data
# Read the data
ln = fl.readline().strip()

# Create nested list of student data (corresponds to data in csv. file)
stddata = [] # stddata[student][specific_data]
counter = 0 # Corresponds to how many students there are
while ln is not '':
    stddata.append(ln.split(','))
    ln = fl.readline().strip()
    counter += 1
fl.close

# Open new tex file for student
for student in range(counter):
    # Gets data - Must do for each loop as we must start from first string for each student
    base = open('template' + os.sep + 'random.tex', 'r')
    fl_s = open('certificate_' + stddata[student][1]+'RANK.tex', 'w')
    ln = base.readline()
    while ln is not '':
        # Find matches in current line with data (eg if '\StudentName' is in the current line)
        for i in range(quant):
            # Replace if match is found
            if ln.find('\\' + header[i]) != -1:
                ln = ln.replace('\\' + header[i], stddata[student][i])
        fl_s.write(ln)
        ln = base.readline()
    fl_s.close
    base.close

#os.system('latexmk -pdf')



