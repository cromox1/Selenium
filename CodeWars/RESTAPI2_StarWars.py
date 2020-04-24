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

import requests
import json

def getHowManyFilms(url, person):
    person1 = person.split(" ")[0]
    r = requests.get(url + person1)
    print("URL = ", url + person1)
    # data = json.loads(r.text)     ### ni kalau nak convert text to json
    data = r.json()              ### ni boleh terus guna sbb dah memang json format (call request format=json
    # print(data["results"][0]["films"])

    with open('outputjson.txt', 'a') as file1:
        file1.write(str(data))
        file1.close()

    return len(data["results"][0]["films"])

#### TDD

from nose.tools import assert_equals

def testing(actual, expected):
    assert_equals(actual, expected)

# baseURL = "https://swapi.co/api/people/"
baseURL = "http://challenges.hackajob.co/swapi/api/people/"
formatsearch = "?format=json&search="

fullURL = baseURL + formatsearch

testing(getHowManyFilms(fullURL, "Yoda"), 5)
#testing(getHowManyFilms(fullURL, "Luke Skywalker"), 5)
#testing(getHowManyFilms(fullURL, "R2-D2"), 7)
#testing(getHowManyFilms(fullURL, "Obi-Wan Kenobi"), 6)

