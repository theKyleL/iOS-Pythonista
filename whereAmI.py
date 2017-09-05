# Audible location identifier
__author__ = ‘Kyle Latino’

 
# Sometimes you need to tell someone your location but you don’t know it..
# Perhaps you can’t share your location via tech but you need someone to find you.
# NOTE: This is not meant to be relied on in emergencies!!!
# Use it to verify or narrow down your location... Maybe order pizza.
# 


import location
import speech
import time

if not location.is_authorized():
	text = ‘Location services must be active!’
	print(text)
	speech.say(text)
	sys.exit()


def getLocation():
	currentLocation = location.reverse_geocode(location.get_location())
	return currentLocation[0]

			
error = ‘Unable to determine location’
try:
	location.start_updates()
	
	# allow location data to settle before returning
	while True:
		temp = getLocation()
		time.sleep(1)
		currentLocation = getLocation()
		if temp == currentLocation:
			break
	
	street = currentLocation.get(‘Street’)
	city = currentLocation.get(‘City’)
	state = currentLocation.get(‘State’)
	youAreHere = (‘Your current location is: ‘ + street + ‘, ‘ + city + ‘, ‘  + state)
	speech.say(youAreHere)
	print(youAreHere)
	location.stop_updates()
except:
	print(error)
	speech.say(error)