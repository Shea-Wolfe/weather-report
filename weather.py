from weather_class import GetConditions, GetTenDay, GetHurricane, GetSunrise, GetAlerts
import re


def weather_app(zipcode):
    while True:
        selection = input('''Welcome to your weather app for zip-code {}.
        Enter [1] for current conditions.
        Enter [2] for sunrise and sunset times.
        Enter [3] for a ten-day forecast.
        Enter [4] for any active alerts.
        Enter [5] to see any active hurricanes worldwide.
        Enter [q] to quit\n\n> '''.format(zipcode))
        if re.match(r'[1-5q]{1}$', selection):
            if selection == '1':
                print(GetConditions(zipcode).run())
                print('-------------------------------------------------')
            elif selection == '2':
                print(GetSunrise(zipcode).run())
                print('-------------------------------------------------')
            elif selection == '3':
                print(GetTenDay(zipcode).run())
                print('-------------------------------------------------')
            elif selection == '4':
                print(GetAlerts(zipcode).run())
                print('-------------------------------------------------')
            elif selection == '5':
                print(GetHurricane.run())
                print('-------------------------------------------------')
            else:
                break
        else:
            print('That is not a valid choice\n')
            return weather_app(zipcode)



def main():
    zipcode = input('please input a 5 digit US zip-code\n\n> ')
    if re.match(r'\d{5}$', zipcode):
        return weather_app(zipcode)
    else:
        print('That is not a valid US zip-code.  5 digit version please\n')
        return main()

if __name__ == '__main__':
    main()
