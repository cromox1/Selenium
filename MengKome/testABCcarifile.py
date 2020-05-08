# chromedatadir = "chrome-data\Default"
chromedatadir = "chrome-data"

import os

# for file in os.listdir(chromedatadir):
#     if file.endswith('Preferences'):
#         print(os.path.join(chromedatadir, file))
#     else:
#         print('TAK JUMPA - DIR = ' + str(chromedatadir) +' DIR2 = ' + str(file))

# for root, dirs, files in os.walk(chromedatadir):
#     for file in files:
#         if file.endswith('Preferences'):
#             print(file)
#
# for root, dirs, files in os.walk(chromedatadir):
#     for file in files:
#         fullpath = os.path.join(root, file)
#         if os.path.splitext(fullpath)[1] == 'Preferences':
#             print(fullpath)

# the_dir = "chrome-data"
# all_txt_files = filter(lambda x: 'Preferences', os.listdir(the_dir))

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(chromedatadir):
    for file in f:
        if file=='Preferences':
            files.append(os.path.join(r, file))

for f in files:
    print(f)