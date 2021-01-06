'''
Modules needed:
requests
json
# Python program to find current  
# weather details of any city 
# using openweathermap api
'''
# import required modules 
import requests,json

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name =input("Enter city name: ")

# Enter your API key here
api_Key="7e9be8a2da32272524f371793624df7f"

# complete_url variable to store 
# complete url address 
url = base_url+"q="+city_name+"&appid="+api_Key
print(url)

# get method of requests module 
# return response object 
response = requests.get(url)

# json method of response object  
# convert json format data into 
# python format data 
resp_py_format = response.json()
print(resp_py_format)

# Now resp_py_format contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if resp_py_format['cod'] != 404:
    
    # store the value of "main" 
    # key in variable
    main_value = resp_py_format['main']

    current_temp = main_value['temp']

    current_press = main_value['pressure']

    current_humid = main_value['humidity']

     # store the value corresponding  
    # to the "description" key at  
    # the 0th index
    weather_desc = resp_py_format['weather'][0]['description']
    print(weather_desc)

    print("*******************************************\nTemperature (in Kelvin unit)= " + str(current_temp)+
          "\natmospheric pressure (in hPa unit) = "+ str(current_press)+
          "\nhumidity (in percentage) = "+str(current_humid)+
          "\ndescription = " + str(weather_desc))
else:
    print(f"City {city_name} not found")
