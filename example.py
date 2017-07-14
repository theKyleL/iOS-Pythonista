import speech

words = "Pythonista is crazy cool!"  #"Hello world!"
#lang = speech.get_synthesis_languages()

#print("Synthesis languages: " + str(speech.get_synthesis_languages()) + "\n")
#print("Recognition languages: " + str(speech.get_recognition_languages()) + "\n")

#print(lang)
speech.say(words)

#while speech.is_speaking():
#	print("Speaking")

print('\n')

import qrcode

#img = qrcode.make("https://www.google.com")
#img.show()

#qr = qrcode.QRCode(
#	version=1, 
#	error_correction=qrcode.constants.ERROR_CORRECT_L,
#	box_size=10,
#	border=4)
	
#qr.add_data('some data')
#qr.make(fit=True)

#img2 = qr.make_image()

#img2.show()

dMessage = qrcode.make("I love you, babe!")
dMessage.show()

print('\n')

import location

if location.is_authorized():
	location.start_updates()
	print(location.get_location())

	address = {'Street': 'Victoria Gardens Blvd', 'City': 'Port Orange', 'Country': 'USA'}
	result = location.geocode(address)

	print("Port Orange: " + str(result))

	print("Reverse geocode: " + str(location.reverse_geocode(location.get_location())))

	location.stop_updates()
	
print('\n')

import clipboard

text = clipboard.get()
print("Clipboard Data: " + str(text))

text = clipboard.set('')
print("Clipboard Data: " + str(text))