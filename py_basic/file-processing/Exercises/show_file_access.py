import os
from datetime import datetime

os.chdir(os.path.dirname(__file__))

last_accessed = os.path.getatime("my_files/logo.png")
last_modified = os.path.getmtime("my_files/logo.png")
last_created = os.path.getctime("my_files/logo.png")

print(last_accessed,last_modified,last_created)

print("Time last accessed is", \
    datetime.fromtimestamp(last_accessed).strftime("%c"))
print("Time last accessed is", \
    datetime.fromtimestamp(last_modified).strftime("%c"))
print("Time last accessed is", \
    datetime.fromtimestamp(last_created).strftime("%c"))
