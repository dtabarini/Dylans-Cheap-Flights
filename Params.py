# specify the minimum price USD
MinPrice: int = 4000

# Specify locations refer to skyscanner documentation to find Airport key
fromAirports = ["AUS-sky"]
# Houston
toAirports = ["BKK-sky"]# "CAI-sky", "CPT-sky", "SGN-sky", "HKG-sky", "BCN-sky", "TYOA-sky"]
# Paris, Cairo, Cape Town, Vietnam, Hon Kong, Barcelona, Tokyo

# Specify length of vacation, NON inclusive to the max vacation day
minVacationDays = 5
maxVacationDays = 11

# Specify week window we are looking through, NON inclusive to max week

minWeeksAway = 5
maxWeeksAway = 6

# Specify email
email = 'dtabarini@gmail.com'

differenceOfVacationDays = maxVacationDays - minVacationDays
