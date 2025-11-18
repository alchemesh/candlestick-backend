class Stock:
    def __init__(self, event, name):
        self.event = event
        self.name = name
        self.days = []

    def setEvent(self, event):
        self.event = event
    
    def getEvent(self):
        return self.event
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def setDays(self, days):
        self.days = days
    
    def getDays(self):
        return self.days

    def updateDays(self, day):
        self.days.append(day)

    def setPatternsFound(self, pattern):
        self.patternsFound = pattern

    def toJSON(self):
        return {"event": self.event, "name": self.name, "days": [day.to_dict() for day in self.days]}

    