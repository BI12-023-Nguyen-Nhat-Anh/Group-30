import re # The re library provides tools to use regular expressions in Python

class person:
    def __init__(self,id,name):
        self.__id=id
        self.__name=name
    
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id
        
    def get_tax(self):
        return self.__tax

class customer(person):
    def __init__(self,id,name,address,type):
        super().__init__(id,name)
        self.__address=address
        self.__type=type

    def get_address(self):
        return self.__address
    
    def add_phone(self, phone):
        self.__phone=phone

    def get_phone(self):
        return self.__phone
    
    def get_type(self):
        return self.__type

    def add_tax(self,tax):
        self.__tax=tax
    
    def get_tax(self):
        return self.__tax
