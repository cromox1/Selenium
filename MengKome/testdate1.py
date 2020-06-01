from time import strftime, strptime, localtime, time, mktime

# print(strftime("%s", localtime()))
print(int(time()))
print(time())

# # date joined format = 'Nov. 8, 2018, 2:08 p.m.'
text1 = 'Nov. 8, 2018, 2:08 p.m.'
# text1 = 'June 1, 2020, 8:53 a.m.'
# text1 = 'Nov. 8, 2018, 2:08'
# text1 = " ".join(text1.split(",")[:2])
text1 = text1.replace(',','').replace('p.m.', 'pm').replace('a.m.', 'am')
text1 = " ".join(text1.split(" ")[:])

print(text1)
# print(strptime(text1))
# print(strftime("%s", text1))

# timestruct = strptime(text1, "%b. %d, %Y, %I:%M")
try:
    timestruct = strptime(text1, "%b. %d %Y %I:%M %p")
except:
    timestruct = strptime(text1, "%B %d %Y %I:%M %p")
print("TEST1 = " + str(timestruct))
# timeepoch = strftime('%s', localtime(timestruct))
timeepoch = mktime(timestruct)
print("TEST2 = " + str(timeepoch))
print("TEST3 = " + str(strftime('%Y-%m-%d %H:%M:%S', localtime(timeepoch))))

# time.strftime('%s')
# from time import time, strftime, localtime
# currentepoch = int(time())
# currentdate = strftime('%Y-%m-%d %H:%M:%S', localtime(currentepoch))
# historydate = strftime('%Y-%m-%d %H:%M:%S', localtime(historyepoch))