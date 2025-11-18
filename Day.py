class Day:
    def __init__(self, date, open, close, high, low):
        self.date = date
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.totalMovement = high - low
        self.direction = close - open
        self.state = "Bullish"
        self.pLowerWick = 0
        self.pBody = 0
        self.pUpperWick = 0

    
    def setDate(self, date):
        self.date = date
        
    def getDate(self):
        return self.date
    
    def setOpen(self, open):
        self.open = open
        
    def getOpen(self):
        return self.open
    
    def setClose(self, close):
        self.close = close
        
    def getClose(self):
        return self.close
    
    def setHigh(self, high):
        self.high = high
        
    def getHigh(self):
        return self.high
    
    def setLow(self, low):
        self.low = low
        
    def getLow(self):
        return self.low
    
    def setTotalMovement(self, totalMovement):
        self.totalMovement = totalMovement
        
    def getTotalMovement(self):
        return self.totalMovement
    
    def setDirection(self, direction):
        self.direction = direction
        
    def getDirection(self):
        return self.direction
    
    def updateState(self):
        if self.direction < 0:
            self.state = "Bearish"

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state
    
    def setPLowerWick(self, pLowerWick):
        self.pLowerWick = pLowerWick
        
    def getPLowerWick(self):
        return self.pLowerWick
    
    def setPBody(self, pBody):
        self.pBody = pBody
        
    def getPBody(self):
        return self.pBody
    
    def setPUpperWick(self, pUpperWick):
        self.pUpperWick = pUpperWick
        
    def getPUpperWick(self):
        return self.pUpperWick
    

    def createCandleAnatomy(self):        
        if self.state == "Bearish":
            self.pLowerWick = (self.close - self.low) / self.totalMovement
            self.pBody = (self.open - self.close) / self.totalMovement
            self.pUpperWick = (self.high - self.open) / self.totalMovement
        else:
            self.pLowerWick = (self.open - self.low) / self.totalMovement
            self.pBody = (self.close - self.open) / self.totalMovement
            self.pUpperWick = (self.high - self.close) / self.totalMovement


    def to_dict(self):
            return {"date": self.date, "open": self.open, "close": self.close, "high": self.high, 
                    "low": self.low, "totalMovement": self.totalMovement, "direction": self.direction, "state": self.state,
                    "pLowerWick": self.pLowerWick, "pBody": self.pBody, "pUpperWick": self.pUpperWick}
                    
                        
                        
