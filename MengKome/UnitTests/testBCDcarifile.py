from os import walk as walkdir
from os.path import join as joinname

chromedatadir = 'chrome-data'

files = []
preferencesfile = 'Preferences'
for dirpath, dirname, filename in walkdir(chromedatadir):
    for file in filename:
        if file == preferencesfile:
            files.append(joinname(dirpath, file))

print('FILES = ' + str(files[0]))
# print("COOKIEFILE = " + str(cookiefile))