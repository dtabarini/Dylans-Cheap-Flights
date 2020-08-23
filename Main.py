import Params
import Exceptions
import time
import datetime
import smtplib
import SensitiveInformation
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from math import trunc
from APIFunctions import checkFlights
from typing import List
from Flight import Flight

def dateToString(inputDate):
    return inputDate.strftime("%Y-%m-%d")


foutput = open("output.txt", "a+")


x = 0
start_time = time.time()
now = datetime.datetime.now()
totalLowPriceFlights: List[Flight] = []
for fromAirport in Params.fromAirports:
    for toAirport in Params.toAirports:
        currentDate = now + datetime.timedelta(weeks=Params.minWeeksAway)

        while currentDate != now + datetime.timedelta(weeks=Params.maxWeeksAway):

            for i in range(Params.differenceOfVacationDays):
                continue_loop = True
                while continue_loop:
                    try:
                        print(toAirport)
                        x = x + 1
                        tempLowPriceFlights = checkFlights(dateToString(currentDate), fromAirport,
                                                           dateToString(currentDate + datetime.timedelta(
                                                               days=Params.minVacationDays + i)), toAirport)
                        totalLowPriceFlights.extend(tempLowPriceFlights)
                        continue_loop = False

                    except Exceptions.TooManyAcessTrys:
                        time.sleep(5)
                    except Exceptions.OtherError as e:
                        print("ERROR %d DETECTED %s, %s - %d days, to: %s---- %s\n" % (e.value,
                        dateToString(currentDate), fromAirport, Params.minVacationDays + i, toAirport, e.response)
                              )
                        foutput.write("ERROR %d DETECTED %s, %s - %d days, to: %s---- %s\n" % (e.value,
                        dateToString(currentDate), fromAirport, Params.minVacationDays + i, toAirport, e.response))
                        continue_loop = False

            currentDate += datetime.timedelta(days=1)

if len(totalLowPriceFlights) > 0: 
    f = open("emailDraft.txt", "w+")
    f.write("Hey look, we found some cheap flights for you!\n")
    f.write("\n\n")
    for fl in totalLowPriceFlights:
        f.write(fl.__str__())
        f.write("\n\n")

    log = open("emailDraft.txt")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('developerdylan77', SensitiveInformation.EMAIL_PASSWORD)

    attachment = MIMEText(log.read())  # create a message
    log.close()

    msg = MIMEMultipart('alternative')
    msg['From'] = 'developerdylan77@gmail.com'
    msg['To'] = Params.email
    msg['Subject'] = "FLIGHTS FLIGHTS FLIGHTS"
    msg.attach(attachment)

    server.send_message(msg)
    del msg

#log runtime
foutput.write("%s SUCCESS- Runtime: %d hours %d minutes, %d seconds\n" % (dateToString(now),(trunc(int((time.time() - start_time)))) / 3600,
                                                                ((trunc(int((time.time() - start_time)))) % 3600)/ 60,
                                                                ((trunc(int((time.time() - start_time)))) % 3600)
                                                                % 60))
foutput.close()


