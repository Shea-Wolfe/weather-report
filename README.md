# Getting-started
* In order to run the two files you will have to run $ pip install -r requirements.txt.
* You will also need to sign up for a Weather Underground dev key (anvil level).  Find more info at http://www.wunderground.com/api.
* Once you've done this you'll need to set up your secret key in your .envrc file with echo export WUNDKEY=YourSecretKey >>.envrc
* Once you've done that enter $ nosetests to run the testing suite.
* Run $ weather.py for a simple terminal interface with the api.  Please note with a free account you may only make 10 queries per minute (and 500 per day) and each time you make a selection it is a separate query.

## Description
* weather.py is a simple python file with a few imported classes form weather_classes.py that pulls info from the Weather Underground API based on an entered US zip-code.
* test_app.py is a testing suite for weather_classes.py that is run with nosetests.
