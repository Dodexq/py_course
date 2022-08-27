import os

def spaces2dashes():
    for dirpath, dirnames, filenames in os.walk('my_files'):
        for fname in filenames:
            if ' ' in fname:
                oldname = dirpath + '/' + fname
                newname = dirpath + '/' + fname.replace(' ', '-')
                print("Replacing", oldname, "with", newname)
                os.rename(oldname, newname)

def dashes2spaces():
    for dirpath, dirnames, filenames in os.walk('my_files'):
        for fname in filenames:
            if '-' in fname:
                oldname = dirpath + '/' + fname
                newname = dirpath + '/' + fname.replace('-', ' ')
                print("Replacing", oldname, "with", newname)
                os.rename(oldname, newname)

spaces2dashes()