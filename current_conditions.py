import requests
import os
my_secret_key = os.environ['WUNDKEY']


class GetConditions:
    def __init__(self, zipcode):
        self.zipcode = zipcode

    def run(self):
        url = 'http://api.wunderground.com/api/{}/conditions/q/{}.json'.format(my_secret_key,self.zipcode)
        res = requests.get(url).json()

        current_temp = res["current_observation"]["temp_f"]
        weather = res['current_observation']['weather']
        feels_like = res['current_observation']['feelslike_f']
        return 'It is {} outside and is {} degrees but feels like {} with wind chill'.format(weather,current_temp,feels_like)

class GetHurricane:
    def run(self):
        url = 'http://api.wunderground.com/api/{}/currenthurricane/view.json'.format(my_secret_key)
        res = requests.get(url).json()

        hurricane_count = res['response']['features']['currenthurricane']
        hurricane_names = [res['currenthurricane'][x]['stormInfo']['stormName_Nice'] for x in range(hurricane_count)]
        hurricane_locations = [(res['currenthurricane'][x]['Current']['lat'], res['currenthurricane'][x]['Current']['lon']) for x in range(hurricane_count)]
        all_hurricanes =  ['Hurricane {} is named {} and is located at lattitude {} and longitude {}'.format(x+1,hurricane_names[x],hurricane_locations[x][0],hurricane_locations[x][1]) for x in range(hurricane_count)]
        return ' '.join(all_hurricanes)



class GetTenDay:
    def __init__(self, zipcode):
        self.zipcode = zipcode

    def run(self):
        url = 'http://api.wunderground.com/api/{}/forecast10day/q/{}.json'.format(my_secret_key,self.zipcode)
        res = requests.get(url).json()

        days = [res['forecast']['txt_forecast']['forecastday'][x*2]['title'] for x in range(10)]
        conditions = [res['forecast']['txt_forecast']['forecastday'][x*2]['fcttext'] for x in range(10)]
        all_days = ['{} will be {}'.format(days[x],conditions[x]) for x in range(10)]
        return '\n'.join(all_days)

class GetSunrise:
    def __init__(self, zipcode):
        self.zipcode = zipcode

    def run(self):
        url = 'http://api.wunderground.com/api/{}/astronomy/q/{}.json'.format(my_secret_key, self.zipcode)
        res = requests.get(url).json()

        sunrise = '{}:{}'.format(res['sun_phase']['sunrise']['hour'],res['sun_phase']['sunrise']['minute'])
        sunset = '{}:{}'.format(res['sun_phase']['sunset']['hour'],res['sun_phase']['sunset']['minute'])

        return 'The sun rose at {} and will set at {}'.format(sunrise,sunset)

def main():
    call = GetSunrise(27703)
    res = call.run()
    print(res)


if __name__ == '__main__':
    main()
