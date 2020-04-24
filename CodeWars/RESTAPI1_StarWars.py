__author__ = 'cromox'

'''
1) peopleURL = "https://swapi.co/api/people/" or " http://challenges.hackajob.co/swapi/api/people/"
2) Create program to check how many times that the person appeared in the films
Eg:
- "Luke Skywalker" = 5 times
- "R2-D2" = 7 times
- "Obi-Wan Kenobi" = 6 times
- "Yoda" = 5 times
'''

import json
import urllib.request

class StarWars():

    def __init__(self, person):
        self.person = person

    def restAPIgetpeople(self, url, people):
        person = people.split(" ")[0]
        print(" URL = ", url + person)
        req = urllib.request.Request(url + people, method="GET")
        #headers = {"Content-Type": "application/json", "Accept": "application/json"} # {"Authorization": "Basic " + authKey}
        #
        #for k,v in headers.items():
        #    req.add_header(k, v)

        r = urllib.request.urlopen(req, timeout=60)

        return r.read()

    def personVsTimes(self):
        # baseURL = "https://swapi.co/api/people/"
        baseURL = "http://challenges.hackajob.co/swapi/api/people/"
        formatsearch = "?format=json&search="

        fullURL = baseURL + formatsearch

        rrest = self.restAPIgetpeople(fullURL, self.person)
        return rrest


orang = "Luke Skywalker"

starwars = StarWars(orang)
result = starwars.personVsTimes()

print(result)

##### TDD
#
#from nose.tools import assert_equals
#
#def testing(actual, expected):
#    assert_equals(actual, expected)
#
## baseURL = "https://swapi.co/api/people/"
#baseURL = "http://challenges.hackajob.co/swapi/api/people/"
#formatsearch = "?format=json&search="
#
#fullURL = baseURL + formatsearch
#
#testing(getHowManyFilms(fullURL, "Yoda"), 5)
#testing(getHowManyFilms(fullURL, "Luke Skywalker"), 5)
#testing(getHowManyFilms(fullURL, "R2-D2"), 7)
#testing(getHowManyFilms(fullURL, "Obi-Wan Kenobi"), 6)



