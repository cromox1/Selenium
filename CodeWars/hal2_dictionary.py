__author__ = 'cromox'

dict1 = {'amazon.co.uk': 89, 'doubleclick.net': 139, 'fbcdn.net': 212, 'in-addr.arpa': 384, 'google.com': 957, 'root-servers.net': 1059, 'facebook.net': 68, 'facebook.com': 525, 'google-analytics.com': 525, 'googleapis.com': 87}

#print()
#print(".items")
#print(dict1.items())
#
#print()
#print(".items - k,v")
#for k,v in dict1.items():
#    print(k, v)
#
#print()
#print(".keys")
#print(dict1.keys())
#
#print()
#print(".values")
#print(dict1.values())
#
#print()
#for k in dict1.keys():
#    print(k)
#
#print()
#for v in dict1.values():
#    print(v)

xlist = [x for x in dict1.values()]

print(xlist)