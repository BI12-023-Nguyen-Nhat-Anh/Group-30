# from customer import customer
import os.path
from domain.customer import customer

class user:
    def __init__(self, identity, phone_input, password_input):
        self.__phone=phone_input
        self.__id_card=identity
        self.__password=password_input

    def get_phone(self):
        return self.__phone
    
    def add_id_card(self, new_id):
        self.__id_card=new_id

    def get_id_card(self):
        return self.__id_card
        
    def add_password(self, new_password):
        self.__password=new_password

    def get_password(self):
        return self.__password

class admin:
    def __init__(self,num,password):
        self.__id=num
        self.__password=password

    def get_id(self):
        return self.__id
    
    def get_password(self):
        return self.__password