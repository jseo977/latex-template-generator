""" Intakes a csv file of student details and outputs separate files to be processed by
    LateX to create certificate PDFs.
"""
from glob import glob
# Open the csv file above
fl = open(glob('*'+'.csv')[0], 'r')
# Extract metadata (header)
ln = fl.readline().strip()
header = ln.split(',')
# Read the data
ln = fl.readline().strip()
while ln is not '':
    # Create new .adr file using student's name
    info = ln.split(',')
    fl_s = open('std_'+info[8]+'.adr', 'w')
    for i in range(len(header)):
        fl_s.write('\def'+'\\'+header[i]+'{'+info[i]+'}'+'\n')
    fl_s.close
    ln = fl.readline().strip()
# Close the file
fl.close