from time import strftime, strptime, localtime, time

# print(strftime("%s", localtime()))
print(int(time()))
print(time())

# # date joined format = 'Nov. 8, 2018, 2:08 p.m.'
text1 = 'Nov. 8, 2018, 2:08 p.m.'
# text1 = 'Nov. 8, 2018, 2:08'
text1 = " ".join(text1.split(",")[:2])

print(text1)
# print(strptime(text1))
# print(strftime("%s", text1))

# timestruct = strptime(text1, "%b. %d, %Y, %I:%M")
timestruct = strptime(text1, "%b. %d %Y")
print("TEST1 = " + str(timestruct))
timeepoch = strftime('%s', localtime(timestruct))
print("TEST2 = " + str(timeepoch))

# time.strftime('%s')
# from time import time, strftime, localtime
# currentepoch = int(time())
# currentdate = strftime('%Y-%m-%d %H:%M:%S', localtime(currentepoch))
# historydate = strftime('%Y-%m-%d %H:%M:%S', localtime(historyepoch))