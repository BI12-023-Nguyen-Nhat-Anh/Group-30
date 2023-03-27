from domain.customer import customer
import datetime
import pytz

tz=pytz.timezone("Asia/Ho_Chi_Minh") # Set timezone to Asia TP Ho Chi Minh

class electricitycomsumption:
    def __init__(self,id):
        self.__id=id
        self.__customer_id=customer.customer.get_id()
        self.__date=datetime.date.today().strftime("%A,%d %B %Y") # Variable date follows day month year format
        self.__time=datetime.datetime.now(tz).strftime("%H:%M") # Similar to date, variable time follows the format
        # self.__consumption_amount=

    def get_id(self):
        return self.__id
    
    def get_date(self):
        return self.__date
    
    def get_time(self):
        return self.__time