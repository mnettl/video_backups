import subprocess

def get_files () -> list:
    cmd = ["ls --hide=*-* --hide=*_*"]
    files_ = subprocess.check_output (cmd, shell=True).decode()
    files = files_.split()
    return files

files = get_files()

def get_date_modified (the_file) -> str:
    cmd = ["date -r " + the_file + " +%m-%d-%Y_%H%M"]
    date_modified = subprocess.check_output (cmd, shell=True).decode()
    return date_modified.split()[0]


def rename_file (file):
    cmd = ["mv " + file + " " + get_date_modified(file) + "_" + file]
    subprocess.call (cmd, shell=True)
    

for f in files:
    rename_file(f)
    print (f)

num_files = len(files)

if (num_files == 0):
    print ("Renamed no files.")
if (num_files == 1):
    print ("Renamed 1 file.")
if (num_files > 1):
    print ("Renamed " + str(num_files) + " files.")