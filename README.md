# city-weather-using-django
Simple python script to know Your city weather

## Requirements
django --2.1.7 (Check your django version type in cmd(windows): python -m django --version).<br/>
python 3.7<br/>
requests module, (*To install* pip install [requests] (https://pypi.org/project/requests/))<br/>
API-Link(Open Weather Map Api): (https://openweathermap.org/)

## How to Use API In Your Project:-
### In this project City Name is used to search to Your City Weather
1) Go to Website (https://openweathermap.org/)<br/>
2) Sign Up in this Website<br/>
3) Log in in this Website<br/>
4) Grab Your API key<br/>
5) Use Your API key in Your Project Like this--><br/>
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid= YOUR API KEY' <br/>
  *Here API returns ## Json ## File, That is useful for our Project* <br/>
  *You can add many attributes separated by # & # symbol in your API link <br/>
6) Here *units=metric* is used to convert the temparature kelvin to °C <br/>
## How to grab Json Data In Your Project-->
 ('description': r['weather'][0]['description'],)--> Grab a particular data from Json Data.<br/>

