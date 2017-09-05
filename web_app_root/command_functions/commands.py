import requests


def command_handler(command):

	####################
	###HELPER METHODS###
	####################
	
	def KtoC(temp):
		return str((int(temp)-273))
	
	def KtoF(temp):
		return str((1.8*(int(temp)-273)+32))

######################################################################

	def weather(city, country_code, longitude, latitude, unit):
		if longitude == 'no':
			forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&APPID=c96060f5a3df59b979d420d978f39a9d'.format(city=city, country_code=country_code)).json()
			
			city = forecast['city']['name']
			country = forecast['city']['country']
			low = forecast['list'][1]['main']['temp_min']
			high = forecast['list'][1]['main']['temp_max']
			temp = forecast['list'][1]['main']['temp']
			weather = forecast['list'][1]['weather'][0]['description']
			if unit == 'C':
				low = KtoC(low)
				high = KtoC(high)
				temp = KtoC(temp)
			if unit == 'F':
				low = KtoF(low)
				high = KtoF(high)
				temp = KtoF(temp)

			response = 'city: {city}-{country}, low: {low}{unit}, high: {high}{unit}, avg: {temp}{unit}, weather: {weather}'.format(city=city, country=country, low=low, high=high, temp=temp, weather=weather, unit=unit)
			return response
		
		
		elif city == 'no':
			forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID=c96060f5a3df59b979d420d978f39a9d'.format(lat=latititude, lon=longitude)).json()
			
			city = forecast['city']['name']
			country = forecast['city']['country']
			low = forecast['list'][1]['main']['temp_min']
			high = forecast['list'][1]['main']['temp_max']
			temp = forecast['list'][1]['main']['temp']
			weather = forecast['list'][1]['weather'][0]['description']
			if unit == 'C':
				low = KtoC(low)
				high = KtoC(high)
				temp = KtoC(temp)
			if unit == 'F':
				low = KtoF(low)
				high = KtoF(high)
				temp = KtoF(temp)

			response = 'location: {long}-{lat}, low: {low}{unit}, high: {high}{unit}, avg: {temp}{unit}, weather: {weather}'.format(long=longitude, lat=latitude, low=low, high=high, temp=temp, weather=weather, unit=unit)
			return response

	
	if command[0] == 'WEATHER':

		try:

			if any(char.isdigit() for char in command[1]) and any(char.isdigit() for char in command[2]):
				longitude = command[1]
				latitude = command[2]
				city = 'no'
				country_code = 'no'
				unit = command[3]
				response = weather(city, country_code, longitude, latitude, unit)
	
			elif str.isalpha(command[1]):
				city = command[1]
				country_code = command[2]
				longitude = 'no'
				latitude = 'no'
				unit = command[3]
				response = weather(city, country_code, longitude, latitude, unit)

		except Exception:
			response = 'incorrect format, please check your command text and try again. It should be WEATHER CITY/LONGITUTDE COUNTRYCODE/LATITUDE'
		
		return response