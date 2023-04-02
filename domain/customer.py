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

    def get_tax(self):
        self.__tax=False
        if(self.get_type()!="HouseHold"): # Only when the user chooses a different type of electricity than domestic electricity
            tax=input("Your tax number is: ")
            if re.match(r"^[0-9]{10}$", tax):   # Check if tax number have the right formula 10 digits contain from 0-9 
                self.__tax=tax
        return self.__tax
