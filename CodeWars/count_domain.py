__author__ = 'cromox'

def count_domains(domains, min_hits):
    # print(domains)
    listdomain = domains.replace("\t", " ").split("\n")

    #key = [ x.split(" ")[0] for x in listdomain]
    #value = [ x.split(" ")[-1] for x in listdomain]
    #domainkv = dict(list(zip(key, value)))

    dom = list(set([x.split(" ")[0].split(".")[-2] if len(x.split(" ")[0].split(".")[-2]) <= 4 else x.split(" ")[0].split(".")[-1] for x in listdomain]))

    domainkv = {}
    for i in range(len(listdomain)):
        listdom = [x for x in dom if x in listdomain[i].split(" ")[0]]
        if domainname(listdomain[i].split(" ")[0], listdom) in domainkv:
            domainkv[domainname(listdomain[i].split(" ")[0], listdom)] += int(listdomain[i].split(" ")[-1])
        else:
            domainkv[domainname(listdomain[i].split(" ")[0], listdom)] = int(listdomain[i].split(" ")[-1])
        # print(listdom, domainname(listdomain[i].split(" ")[0], listdom))

    print(domainkv)
    result = {}
    for kk, vv in domainkv.items():
        if vv > min_hits:
            result[kk] = vv
    sorted_keys = sorted(result, key=result.get, reverse=True)
    print(sorted_keys)
    text = ""
    for r in sorted_keys:
        text = text + r + " ("+ str(result[r]) + ")\n"
    text = text[:-1]
    return text

def domainname(site, listdom):
    lsite = len(site)
    dom = ""
    for iname in listdom:
        if len(site.replace(iname, "")) < lsite:
            lsite = len(site.replace(iname, ""))
            dom = iname
    dname = site.split(dom)
    dname = dname[0].split(".")[-2] + "." + dom + dname[1]
    return dname

#print(domainname("edge-mqtt.facebook.com.my", ['co', 'com']))
#print(domainname("amazon.co.jp", ['co', 'com']))
#print(domainname("edge-mqtt.facebook.com", ['co', 'com']))
#print(domainname("edge-mqtt.facebook.net", ['net']))
##print(domainname("in-addr.arpa", ['']))

## TDD

domains_list = '''\
*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212
*.in-addr.arpa    384
*.l.google.com    317
1.client-channel.google.com    110
6.client-channel.google.com    45
a.root-servers.net    1059
apis.google.com    43
clients4.google.com    71
clients6.google.com    81
connect.facebook.net    68
edge-mqtt.facebook.com    56
graph.facebook.com    150
mail.google.com    128
mqtt-mini.facebook.com    47
ssl.google-analytics.com    398
star-mini.c10r.facebook.com    46
staticxx.facebook.com    48
www.facebook.com    178
www.google.com    162
www.google-analytics.com    127
www.googleapis.com    87'''

from nose.tools import assert_equals

def testing(actual, expected):
    assert_equals(actual, expected)

#testing(count_domains(domains_list, 500), '''\
#root-servers.net (1059)
#google.com (957)
#facebook.com (525)
#google-analytics.com (525)''')
#testing(count_domains(domains_list, 1000), 'root-servers.net (1059)')

print()
print(count_domains(domains_list, 500))
print()
print(count_domains(domains_list, 1000))
print()
print(count_domains(domains_list, 200))
print()