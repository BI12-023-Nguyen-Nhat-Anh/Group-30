import re # The re library provides tools to use regular expressions in Python

class person:
    def __init__(self,id,name,tax):
        self.__id=id
        self.__name=name
        if not re.match(r"^[0-9]{10}$", tax):   # Check if tax number have the right formula 10 digits contain from 0-9 
            self.__tax=False
        else:
            self.__tax=tax
    
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id
        
    def get_tax(self):
        return self.__tax

class customer(person):
    def __init__(self,id,name,address,phone_number,email,tax,type):
        super().__init__(id,name,tax)
        self.__address=address

        if not re.match(r"^[0-9]{10}$", phone_number):    # Similar to tax number check if phone_number has the right formula
            self.__phone_number=False
        else:
            self.__phone_number=phone_number

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):    # Similar to tax number check the formula of email
            self.__email=False
        else:
            self.__email=email

        self.__type=type

    def get_address(self):
        return self.__address
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_email(self):
        return self.__email
    
    def get_type(self):
        return self.__type