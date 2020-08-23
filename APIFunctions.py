from typing import List
import requests
import json
from Flight import Flight
import Params
import SensitiveInformation
from Exceptions import TooManyAcessTrys
from Exceptions import OtherError

def checkFlights(outBoundDate, outBoundLocation, inBoundDate, inBoundLocation):
    usedItineraryMap = set()
    return_list: List[Flight] = []
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"
    payload = "inboundDate=" + inBoundDate + "&cabinClass=economy&children=0&infants=0&country=US&currency=USD&locale=en-US&originPlace=" + outBoundLocation + "&destinationPlace=" + inBoundLocation + "&outboundDate=" + outBoundDate + "&adults=1"
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': SensitiveInformation.API_PASSWORD,
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    lowFLightsList: list
    if response:

        fullKey = response.headers["Location"]
        key = fullKey[-36:]
        url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/" + key
        querystring = {"sortType": "price", "sortOrder": "asc", "pageIndex": "0", "pageSize": "10"}

        headers = {
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
            'x-rapidapi-key': SensitiveInformation.API_PASSWORD
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        if response:
            responseDict = json.loads(response.text)
    
            if "Itineraries" in responseDict:
                queryDict = responseDict["Query"]
                itineraryList = responseDict["Itineraries"]
                index = -1
                for itineraryDict in itineraryList:
                    index += 1
                    priceList = itineraryDict["PricingOptions"]
                    for priceOptionDict in priceList:
                        price = priceOptionDict["Price"]
                        if int(price) < Params.MinPrice:
                            if not (index in usedItineraryMap):
                                usedItineraryMap.add(index)
                                flight = Flight()
                                flight.price = price
                                flight.link = priceOptionDict["DeeplinkUrl"]
                                legsList = responseDict["Legs"]
                                for leg in legsList:
                                    if leg["Id"] == itineraryDict["OutboundLegId"]:
                                        flight.startDate = leg["Departure"]
                                        flight.startDateArrival = leg["Arrival"]

                                    if leg["Id"] == itineraryDict["InboundLegId"]:
                                        flight.endDate = leg["Departure"]
                                        flight.endDateArrival = leg["Arrival"]
                                queryDict = responseDict["Query"]
                                originID = queryDict["OriginPlace"]
                                destID = queryDict["DestinationPlace"]
                                placesList = responseDict["Places"]
                                for place in placesList:
                                    if place["Id"] == int(originID):
                                        flight.fromAP = place["Name"]
                                    if place["Id"] == int(destID):
                                        flight.toAP = place["Name"]

                                return_list.append(flight)
                        else:
                            return return_list`
        else:
            raise OtherError(response.status_code, response.text)
        return return_list

    else:
        if str(response.status_code) == "429":
            raise TooManyAcessTrys
        else:
            raise OtherError(response.status_code, response.text)


