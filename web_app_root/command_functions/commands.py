import requests

def command_handler(command):

	def weather(city, country_code):
		forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&APPID=c96060f5a3df59b979d420d978f39a9d'.format(city=city, country_code=country_code)).json()
		low = forecast['list'][1]['main']['temp_min']
		high = forecast['list'][1]['main']['temp_max']
		temp = forecast['list'][1]['main']['temp']
		weather = forecast['list'][1]['weather'][0]['description']
		response = 'low: {low}K, high: {high}K, avg: {temp}K, weather: {weather}'.format(low=low, high=high, temp=temp, weather=weather)
		return response
	if command[0] == 'WEATHER':
			city = command[1]
			country_code = command[2]
			response = weather(city, country_code)
			return response