from Bill_Caculate import numbers,late_fee_HouseHold,late_fee_Administrative_offices,late_fee_Business,late_fee_Manufacturing_industries
import random

# Create a dictionary to map the random number to the corresponding string value
mapping = {1: "Intime", 2: "Out of date"}

# Generate a random number between 1 and 2 (inclusive)
random_number = random.randint(1, 2)


def Household_payment():
    if random_number == 1:
        print(mapping[1],numbers[0])
        
    else:
        print(mapping[2])
        late_fee_HouseHold()
def Administrative_offices_payment():
    if random_number == 2:
        print(mapping[2])
        late_fee_Administrative_offices()
    else:
        print(mapping[1],numbers[1])
        
def Business_payment():
    if random_number == 1:
        print(mapping[1],numbers[2])
        
    else:
        print(mapping[2])
        late_fee_Business()
def Manufacturing_industries_payment():
    if random_number == 2:
        print(mapping[2])
        late_fee_Manufacturing_industries()
    else:
        print(mapping[1],numbers[3])
        


Household_payment()
Administrative_offices_payment()
Business_payment()
Manufacturing_industries_payment()



        