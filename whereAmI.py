# Audible location identifier written in pythonista
# By: Kyle Latino
# 
# Sometimes you need to tell someone your location but you don’t know it..
# Perhaps you can’t share your location via tech but you need someone to find you.
# NOTE: This is not meant to be relied on in emergencies!!!
# Use it to verify or narrow down your location... Maybe order pizza.
#


import location
import speech

if not location.is_authorized():
	print('Location services must be active!')
	sys.exit()
	
address = 'location not yet found'

location.start_updates()
currentLocation = location.reverse_geocode(location.get_location())
currentLocation = currentLocation[0]
print(currentLocation)

#streetNum = currentLocation.get('SubThoroughfare')
street = currentLocation.get('Street')
city = currentLocation.get('City')
state = currentLocation.get('State')
speech.say('Your current location is: ' + street + city + state)
