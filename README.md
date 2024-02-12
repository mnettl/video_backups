## Video Backup Scripts

Here are 3 console scripts I use to put Tiktok videos in archival form:

1) **Separatepics.py** - Because Tiktok saves the videos in Android's camera roll, I had to find a way to separate my personal pictures and video from Tiktok videos. This script uses Python's OS subprocess to move my personal pictures and video to another folder called "pics."

2) **renametest.py** - Appends the date modified in front of the filename so that the videos can be searched and organized by date.

3) **writefilescsv.py** - I keep a Notion database of all the files so that I can tag and organize them. ``writefilescsv.py`` creates a .csv file with the filename and date modified of the newly tranferred pictures so that I can import it into the database.

---

## Instructions

IMPORTANT: Make sure all 3 scripts are in the same folder. I'll call it tiktok_holding

1. Transfer the camera roll photos to tiktok_holding folder

2. Open a bash terminal in that directory

3. Run each of the scripts in order:
   
   1. ``python3 Separatepics.py``
   
   2. ``python3 renametest.py ``
   
   3. ``python3 writefilescsv.py``

4. Use the notion_csv_addpages script to merge csv.csv with the Notion database (https://github.com/mnettl/notion_csv_addpages)
   
5. Transfer the video files to their final directory

## Requirements

- Python 3

- Unix
