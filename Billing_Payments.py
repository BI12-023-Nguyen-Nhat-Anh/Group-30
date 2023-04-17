from Bill_Caculate import numbers,numbers1,numbers2,numbers3,late_fee_HouseHold,late_fee_Administrative_offices,late_fee_Business,late_fee_Manufacturing_industries
import random
from domain.customer import customer
global total
total = 0
# Create a dictionary to map the random number to the corresponding string value
mapping = {1: "Intime", 2: "Out of date"}

# Generate a random number between 1 and 2 (inclusive)
random_number = random.randint(1, 2)
random_number_1 = random.randint(1, 2)
random_number_2 = random.randint(1, 2)
random_number_3 = random.randint(1, 2)


if customer.get_type() == "HouseHold":
    def Household_payment():
        if random_number == 1:
            total = numbers[0]
        else:
            
            total = late_fee_HouseHold()
            return total
elif customer.get_type() == "Administrative_offices":
    def Administrative_offices_payment():
        if random_number_1 == 1:
            total = numbers1[0]
        else:
            
            total = late_fee_Administrative_offices()
            return total
elif customer.get_type() == "Business":
    def Business_payment():
        if random_number_2 == 1:
            total = numbers2[0]
            
        else:
            
            total = late_fee_Business()
            return total
elif customer.get_type() == "Manufacturing_industries":
    def Manufacturing_industries_payment():
        if random_number_3 == 1:
            total = numbers3[0]
        else:
            
            total = late_fee_Manufacturing_industries()
            return total
else:
    print("Error!")


Household_payment()
Administrative_offices_payment()
Business_payment()
Manufacturing_industries_payment()



        