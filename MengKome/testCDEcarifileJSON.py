chromedatadir = "chrome-data"

import os
# import shutil
# import sys
# import ctypes
# import sqlite3

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(chromedatadir):
    for file in f:
        if file=='Cookies':
            files.append(os.path.join(r, file))

# for f in files:
#     print(f)
if len(files) >= 1:
    print(files[0])