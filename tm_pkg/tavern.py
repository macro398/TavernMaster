class Employee:
    def __init__(self):
        self.wage = 0
        self.name = ''
        self.happiness = 0
        
    def happiness_loss(self,loss):
        self.happiness = self.happiness - loss
  

class Tavern:
    def __init__(self):
        self.daily_income = 100
        self.gp = 0
        self.karma = 0
        
    def end_of_day(self,waitress,bard):
        atmosphere = (waitress.happiness + bard.happiness + self.karma)
        self.gp += self.daily_income * atmosphere
        print("Today you have made: ", (self.daily_income * atmosphere), "gp in sales.")
        print("Total:", self.gp,"gp")
    
    def profit(self,gp_made): 
        self.gp += gp_made