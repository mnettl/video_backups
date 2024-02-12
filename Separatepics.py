import subprocess

# ls the camera pics and video (files that have underscores in the name), and add them to a list

def get_camera_pics_and_vids () -> list:
    cmd = ["ls *_*"]
    try: 
        camera_pics = subprocess.check_output(cmd, shell=True).decode().split()
    except (subprocess.CalledProcessError):
        camera_pics = []
    return camera_pics



# loop through the list and mv each of the files to the pics folder


def move_pics (filename):
    cmd = ["mv " + filename + " /mnt/c/'Documents and Settings'/monet/Desktop/pics"]
    subprocess.run(cmd, shell=True)


pics = get_camera_pics_and_vids()
numpics = len(pics)

if (numpics == 0):
    print ("There were no pics to move.")
else:
    for p in pics:
        print (p)
        move_pics (p)

    if (numpics > 1):
            print (str(numpics) + " files were moved.")
    if (numpics == 1):
            print ("1 file was moved.")

    