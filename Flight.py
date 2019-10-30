class Flight:
    def __init__(self):
        self.fromAP = ""
        self.toAP = ""
        self.startDate = ""
        self.startDateArrival = ""
        self.endDate = ""
        self.endDateArrival = ""
        self.price = ""
        self.link = ""

    def __str__(self):
        returnStr = "$"+ str(self.price) + " \n" + self.fromAP + " to " + self.toAP + "\n" + str(self.startDate) + " to " \
                    + str(self.endDate) + "\n" + self.link
        return returnStr
