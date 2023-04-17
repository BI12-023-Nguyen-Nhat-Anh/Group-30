from Bill_Caculate import numbers,numbers1,numbers2,numbers3,late_fee_HouseHold,late_fee_Administrative_offices,late_fee_Business,late_fee_Manufacturing_industries
import random
from domain.customer import customer
global total
total = 0
global status
status = ""
global due
due = ""
global payment
payment = ""
# Create a dictionary to map the random number to the corresponding string value

duedate = random.randint(5,19)
payment_date = random.randint(18,30)
duedate1 = random.randint(1,20)
payment_date1 = random.randint(15,25)
duedate2 = random.randint(20,30)
payment_date2 = random.randint(1,25)
duedate3 = random.randint(16,26)
payment_date3 = random.randint(5,29)


if customer.get_type() == "HouseHold":
    def Household_payment():
        if duedate >= payment_date:
            total = numbers[0]
            status = "Paid"
            due = f"{duedate}/3/2023"
            payment = f"{payment_date}/3/2023"
        else:
            
            total = late_fee_HouseHold()
            status = "Overdue"
            due = f"{duedate}/3/2023"
            payment = f"{payment_date}/3/2023"
            return total
elif customer.get_type() == "Administrative_offices":
    def Administrative_offices_payment():
        if duedate1 >= payment_date1:
            total = numbers1[0]
            status = "Paid"
            due = f"{duedate1}/3/2023"
            payment = f"{payment_date1}/3/2023"
        else:
            
            total = late_fee_Administrative_offices()
            status = "Overdue"
            due = f"{duedate1}/3/2023"
            payment = f"{payment_date1}/3/2023"
            return total
elif customer.get_type() == "Business":
    def Business_payment():
        if duedate2 >= payment_date2:
            total = numbers2[0]
            status = "Paid"
            due = f"{duedate2}/3/2023"
            payment = f"{payment_date2}/3/2023"
        else:
            
            total = late_fee_Business()
            status = "Overdue"
            due = f"{duedate2}/3/2023"
            payment = f"{payment_date2}/3/2023"
            return total
elif customer.get_type() == "Manufacturing_industries":
    def Manufacturing_industries_payment():
        if duedate3 >= payment_date3:
            total = numbers3[0]
            status = "Paid"
            due = f"{duedate3}/3/2023"
            payment = f"{payment_date3}/3/2023"
        else:
            
            total = late_fee_Manufacturing_industries()
            status = "Overdue"
            due = f"{duedate3}/3/2023"
            payment = f"{payment_date3}/3/2023"
            return total
else:
    print("Error!")

if customer.get_type() == "HouseHold":
    Household_payment()
elif customer.get_type() == "Administrative_offices":
    Administrative_offices_payment()
elif customer.get_type() == "Business":
    Business_payment()
elif customer.get_type() == "Manufacturing_industries":
    Manufacturing_industries_payment()



        