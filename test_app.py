import requests_mock
from current_conditions import GetConditions, GetTenDay, GetHurricane, GetSunrise
import os

my_secret_key = os.environ['WUNDKEY']

@requests_mock.Mocker()
def test_get_conditions(m):
    with open('durhamcurrent.json') as f:
        m.get('http://api.wunderground.com/api/{}/conditions/q/27703.json'.format(my_secret_key), text=f.read())
    conditions = GetConditions(27703)
    res = conditions.run()

    assert res == 'It is Clear outside and is 55.3 degrees but feels like 55.3 with wind chill'

@requests_mock.Mocker()
def test_get_10day(m):
    with open('durham10day.json') as f:
        m.get('http://api.wunderground.com/api/{}/forecast10day/q/27703.json'.format(my_secret_key), text=f.read())
    tenday = GetTenDay(27703)
    res = tenday.run()

    assert res == '''Tuesday will be Mainly clear. Lows overnight in the upper 30s.
Wednesday will be Plentiful sunshine. High 72F. Winds light and variable.
Thursday will be Sunshine. High around 75F. Winds light and variable.
Friday will be Sunny. High 76F. Winds NNE at 5 to 10 mph.
Saturday will be Cloudy. High 67F. Winds light and variable.
Sunday will be Partly cloudy skies during the morning hours will become overcast in the afternoon. High 73F. Winds SW at 5 to 10 mph.
Monday will be Sunshine and clouds mixed. High 66F. Winds NNE at 5 to 10 mph.
Tuesday will be Except for a few afternoon clouds, mainly sunny. High 59F. Winds NE at 10 to 15 mph.
Wednesday will be Cloudy with showers. High around 60F. Winds NE at 5 to 10 mph. Chance of rain 60%.
Thursday will be Rain showers in the morning becoming more intermittent in the afternoon. High near 60F. Winds NNE at 5 to 10 mph. Chance of rain 60%.'''

@requests_mock.Mocker()
def test_hurricane(m):
    with open('hurricane.json') as f:
        m.get('http://api.wunderground.com/api/{}/currenthurricane/view.json'.format(my_secret_key), text=f.read())
    hurricane = GetHurricane()
    res = hurricane.run()

    assert res == 'Hurricane 1 is named Hurricane Olaf and is located at lattitude 9.9 and longitude -137.7'


@requests_mock.Mocker()
def test_sunrise(m):
    with open('sunrise.json') as f:
        m.get('http://api.wunderground.com/api/{}/astronomy/27703.json'.format(my_secret_key), text=f.read())
    sunrise = GetSunrise(27703)
    res = sunrise.run()

    assert res == 'The sun rose at 7:26 and will set at 18:33'
