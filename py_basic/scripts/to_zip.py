from fileinput import filename
import sys
import os
import datetime
from zipfile import ZipFile

if len(sys.argv) != 3:
    print("""
        pack dir files to zip-file with date in name
        usage: python to_zip.py source-dir dest dir
        """)
    sys.exit(1)

def pack_dir(source_dir, archive_file):
    with ZipFile(archive_file, 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(source_dir):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                zipObj.write(filePath, os.path.basename(filePath))

source_dir = sys.argv[1]
source_dir_name = os.path.basename(source_dir)
dest_dir = sys.argv[2]
zip_filename = f"dir-{source_dir_name}-archive-date-{datetime.date.today()}.zip"
dest_path = os.path.join(dest_dir, zip_filename)

print(source_dir)
print(dest_dir)
print(zip_filename)
print(dest_path)

pack_dir(source_dir=source_dir, archive_file=dest_path)