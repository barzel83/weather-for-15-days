#! python3
# quickWeather.py - Prints the current weather for a location from the command line.

import json, requests, sys

# Compute location from command line arguments.

hours = ' '.join(sys.argv[1:2])
location = ' '.join(sys.argv[2:])    
outputFile = open('weather_in_Ramat_Gan.txt', 'w')

# Cities coordinates.
coordinates = {'Ramat Gan':['32.083','34.817'],
               'Moscow':['55.617','37.751'],
               'London':['51.495','0.0'],
               'Eilat':['29.554','34.952'],
               'Almaty':['43.229','76.855'],
               'Alma Ata':['43.229','76.855'],
               'Alma-Ata':['43.229','76.855'],
               'Singapur':['1.356','103.823'],
               'Krasnodar':['45.042','38.999'],
               'Haifa':['32.777','35.0184']
               }

shirota = str(coordinates[location][0])
dolgota = str(coordinates[location][1])


# Download the JSON data from tomorrow.io's API

url =f"https://api.weather.com/v3/wx/forecast/hourly/15day?apiKey=e1f10a1e78da46f5b10a1e78da96f525&geocode={shirota}%2C{dolgota}&units=m&language=en-US&format=json"  

  
response = requests.get(url)
response.raise_for_status()

#Load JSON data into a Python variable.
weatherData = json.loads(response.text)

print('\n')
print('Current weather in %s:' % (location))


outputFile.write('Current weather in %s:')
outputFile.close()


#Print weather descriptions.
for i in range(int(hours)):
   cloudCover = weatherData['wxPhraseLong'][i]
   dayOfWeek = weatherData['dayOfWeek'][i]
   DewPoint = weatherData['temperatureDewPoint'][i]
   Time = weatherData['validTimeLocal'][i][11:16]
   Humidity = weatherData['relativeHumidity'][i]
   CurrentTemperature = weatherData['temperature'][i]
   UVindex = weatherData['uvIndex'][i]
   print('Date: ', weatherData['validTimeLocal'][i][8:10],'-', weatherData['validTimeLocal'][i][5:7],'-',weatherData['validTimeLocal'][i][:4], 'Local time: ', Time)
   print('Day of week: ', dayOfWeek)
   print('Current Temperature: ', CurrentTemperature,'ºC')
   print('DewPoint: ', DewPoint, 'ºC')
   print('Relative Humidity: ', Humidity, '%')
   print('cloudCover: ', cloudCover)
   print('UVindex: ', UVindex)
   HeatLoad = (CurrentTemperature+DewPoint)/2
   print('Heat load: ', HeatLoad)
   print('\n')
   ###Heat Load calculation
   for i in range(2): 
       if HeatLoad>28:
           print('Heat load level: 4')
       elif HeatLoad>26:
           print('Heat load level: 3')
       elif HeatLoad==26:
           print('Heat load level: 2-3')
       elif HeatLoad>24:
           print('Heat load level: 2')
       elif HeatLoad==24:
           print('Heat load level: 1-2')
       elif HeatLoad>22:
           print('Heat load level: 1')
       else:
           print('Прохлада - это здорово!')
   print('\n')




