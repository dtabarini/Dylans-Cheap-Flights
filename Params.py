# specify the minimum price USD
MinPrice: int = 400

# Specify locations refer to skyscanner documentation to find Airport key
fromAirports = ["IAH-sky"]
# Houston
toAirports = ["PARI-sky", "EG-sky", "CPT-sky", "VN-sky", "HKG-sky", "BCN-sky", "TYOA-sky"]
# Paris, Egypt, Vietnam, Cape Town, Hon Kong, Barcelona, Tokyo

# Specify length of vacation, NON inclusive to the max vacation day
minVacationDays = 8
maxVacationDays = 12

# Specify week window we are looking through, NON inclusive to max week

minWeeksAway = 15
maxWeeksAway = 25

# Specify email
email = 'dtabarini@gmail.com'

# Don't worry about changing this guy
differenceOfVacationDays = maxVacationDays - minVacationDays
