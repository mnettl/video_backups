## Video Backup Scripts

I am an avid user of Tiktok, and often download Tiktok videos to my phone for archival and reference (recipes, anyone?). Because I don't have enough space on my phone, I frequently move them off my phone and onto my computer. Once I transfer the camera roll to my computer, there are 3 console scripts that I use to wrangle the videos into archival form:

1) **Separatepics.py** - Because Tiktok saves the videos in Android's camera roll, I had to find a way to separate my personal pictures and video from Tiktok videos. This script uses Python's OS subprocess to move my personal pictures and video to another folder called "pics."

2) **renametest.py** - Sometimes in the process of transferring files, the metadata gets lost. This [makes it less annoying] by appending the date modified in front of the filename so I can keep the videos organized by date wherever I may move them.

3) **writefilescsv.py** - I keep a Notion database of all the files so that I can tag and organize them. writefilescsv.py creates a .csv file with the filename and date modified of the newly tranferred pictures so that I can import it into the database.

---

## Instructions

IMPORTANT: Make sure all 3 scripts are in the Desktop/tiktok_holding folder

1. Transfer the camera roll photos to Desktop/tiktok_holding

2. Open a WSL Ubuntu terminal and navigate to that directory

3. Run each of the scripts in order:
   
   1. ``python3 Separatepics.py``
   
   2. ``python3 renametest.py ``
   
   3. ``python3 writefilescsv.py``

4. Transfer the video files to the final folder, and run the rclone backup script

5. Open the Notion Tiktoks database, merge the ``csv.csv`` file
   
   

## Requirements

- Python 3

- Unix