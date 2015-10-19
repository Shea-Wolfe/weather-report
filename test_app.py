import requests_mock
from current_conditions import GetConditions
from ten_day import GetTenDay
from hurricane import GetHurricane
import os

my_secret_key = os.environ['WUNDKEY']

@requests_mock.Mocker()
def test_get_conditions(m):
    with open('durhamcurrent.json') as f:
        m.get('http://api.wunderground.com/api/{}/conditions/q/27703.json'.format(my_secret_key), text=f.read())
    conditions = GetConditions(27703)
    res = conditions.run()

    assert res == 'current conditions'

@requests_mock.Mocker()
def test_get_10day(m):
    with open('durham10day.json') as f:
        m.get('http://api.wunderground.com/api/{}/forecast10day/q/27703.json'.format(my_secret_key), text=f.read())
    tenday = GetTenDay(27703)
    res = tenday.run()

    assert res == 'tenday stuff'

@requests_mock.Mocker()
def test_hurricane(m):
    with open('hurricane.json') as f:
        m.get('http://api.wunderground.com/api/{}/hurricane/view.json'.format(my_secret_key), text=f.read())
    hurricane = GetHurricane()
    res = hurricane.run()

    assert res == 'hurricane stuff'
