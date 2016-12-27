#!/usr/bin/python

# This uses the Weather Underground API

import urllib2
import json
key = '6288250d19206179' # Tutorial API key

zip = raw_input('For which zip code would you like to see the weather? ')
url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/UT/' + zip + '.json'
f = urllib2.urlopen(url)
json_string = f.read()
parsed_json = json.loads(json_string)

city =  parsed_json['current_observation']['display_location']['city']
state = parsed_json['current_observation']['display_location']['state']

weather = parsed_json['current_observation']['weather']
temp = parsed_json['current_observation']['temp_f']

print 'In the city of ' + city + ', ' +  state + ' the weather is ' +  weather.lower() + '.'
print str(temp) + ' degrees farenheit.  That is cold.'
f.close()
