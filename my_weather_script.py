#!/user/bin/python
# -*- coding: utf-8 -*-
# ^ This allows you to use the degree symbol

import urllib2
import json
key = '6288250d19206179'

state_local = raw_input("What state do you live in? ")
city_local = raw_input("Ok, now what city do you live in? ")

if " " in state_local:
    s_location = state_local.replace(" ", "_")
else:
    s_location = state_local


if " " in city_local:
    c_location = city_local.replace(" ", "_")
else:
    c_location = city_local

url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/'+ s_location +'/'+ c_location +'.json'
f = urllib2.urlopen(url)
json_string = f.read()
parsed_json = json.loads(json_string)

city =  parsed_json['current_observation']['display_location']['city']
# state = parsed_json['current_observation']['display_location']['state']

weather = parsed_json['current_observation']['weather']
temp = parsed_json['current_observation']['temp_f']

print 'Today in ' +  city + ' the weather is: ' +  weather

if temp <= 40:
    print str(temp) + '° farenheit.  That is cold.'
    # degree symbol is input by shift + option + 8
else:
    print 'It\'s warming up :)'


f.close()
