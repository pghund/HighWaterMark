
class Filing:
    d={}
    def __init__(self, year,month, day, fund):
        self.year=year
        self.month=month
        self.day=day
        self.fund=fund

    def addToD(self,name, amt):
        self.d[name]=amt
    
