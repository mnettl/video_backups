import subprocess
import csv

# get the files and dates
def get_files () -> list:
    cmd = ["ls --ignore='writefilescsv.py' --ignore='csv.csv' --ignore='renametest.py' --ignore='Separatepics.py'"]
    files_ = subprocess.check_output (cmd, shell=True).decode()
    files = files_.split()
    return files

files = get_files()

def get_date_modified (the_file) -> str:
    cmd = ["date -r " + the_file + " +%m/%d/%Y"]
    date_modified = subprocess.check_output (cmd, shell=True).decode()
    return date_modified.split()[0]

# put the files and dates in a list
row = []
for f in files:
    date = get_date_modified (f)
    row.append ([f, date])


# write the files and dates to the csv file
with open ("csv.csv", "w", newline="") as file:
    csv_write = csv.writer (file)
    headings = csv_write.writerow (['Filename', 'Date'])
    rows = csv_write.writerows (row)

