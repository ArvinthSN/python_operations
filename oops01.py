import datetime

class eligible:
    def __init__(self,name,dob):
        self.name =  name
        self.dob =dob

    def calculate(self):
        today = datetime.date.today()
        age = today.year - self.dob.year
        if (age >= 18):
            print(f"{self.name} is eligible to vote this age is {age}")
        else :
            print(f"{self.name} is note eligible to vote {age}")
obj = eligible("arvinth",datetime.date(2005,2,5))
obj.calculate()