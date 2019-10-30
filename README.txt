Dylan's flight scanner

OVERVIEW:
This is a flight scanner that scanners for a flight to any specified location and will send an email once a flight is
found within that range. It's intended purpose would be to run once a day until it finds a price drop for a trip.

TO USE:
In Params.py set date range, minimum price, fromAirport(s), toAirport(s). In order to find the from airport and to airports
you will have to refer to the Skyscanner documentation to get the quiery code for the airport. For example I need to put in AUS-sky
to represent Austin–Bergstrom International Airport.

Once parameters are set. Simply run the Main.py and an email should be sent containing information and a link. For Mac users crontab is a good resource to
use to set up to run everyday

To check if it is running correctly, check "output.txt" for errors relating to API. This will update each time script is run.
It will also give the run time of each script