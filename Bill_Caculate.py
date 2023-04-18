from domain.customer import customer
from domain.MeterReading import amount
from main import list_user
from GUI.login import phone, password
import pandas as pd

numbers = 0
numbers1 =0 
numbers2 =0 
numbers3 =0 
global late_fee
late_fee = 0
global price
price = 0
global total
total = 0
def Household(count):

    # Seperate the total consumption electric for each stage
    count1 = count - 50
    count2 = count1 - 50
    count3 = count2 - 100
    count4 = count3 - 100
    count5 = count4 -100

    if count <= 0:
        amount_bill = 0
    # If consumption electric are in 0-50kWh
    elif (count - 50) <= 0:
        amount_bill1 = count
        amount_bill = amount_bill1 * 1678
        count1 = count - 50
    # If consumption electric are in 51-100 kWh
    elif (count1 - 50) <= 0:
        amount_bill1 = 50
        amount_bill2 = count - 50
        count2 = count1 - 50
        amount_bill = (amount_bill1 * 1678) + (amount_bill2 * 1734)
    # If consumption electric are in 101-200 kWh
    elif (count2 - 100) <=0:
        amount_bill1 = 50
        amount_bill2 = 50
        amount_bill3 = count1 - 50
        count3 = count2 - 100
        amount_bill = (amount_bill1 * 1678) + (amount_bill2 * 1734) + (amount_bill3 * 2014)
    # If consumption electric are in 201-300 kWh
    elif (count3 - 100) <= 0:
        amount_bill1 = 50
        amount_bill2 = 50
        amount_bill3 = 100
        amount_bill4 = count2 - 100
        count4 = count3 - 100
        amount_bill = (amount_bill1 * 1678) + (amount_bill2 * 1734) + (amount_bill3 * 2014) +(amount_bill4 * 2536)
    # If consumption electric are in 300-401 kWh
    elif (count4 -100) <=0:
        amount_bill1 = 50
        amount_bill2 = 50
        amount_bill3 = 100
        amount_bill4 = 100
        amount_bill5 = count3 - 100
        count5 = count4 -100
        amount_bill = (amount_bill1 * 1678) + (amount_bill2 * 1734) + (amount_bill3 * 2014) +(amount_bill4 * 2536)+ (amount_bill5 * 2834)
    # If consumption electric are in upper 401 kWh
    else:
        # Total price
        amount_bill1 = 50
        amount_bill2 = 50
        amount_bill3 = 100
        amount_bill4 = 100
        amount_bill5 = 100 
        amount_bill = (amount_bill1 * 1678) + (amount_bill2 * 1734) + (amount_bill3 * 2014) +(amount_bill4 * 2536)+ (amount_bill5 * 2834) + (count5 * 2927)
    
    numbers=amount_bill
    return float(numbers)

def Manufacturing_industries(count):
    count1 = count - 600
    count2 = count1 - 1600
    if count <= 0:
        amount_bill = 0
    # If consumption electric are in 0-600kWh
    elif (count - 600) <=0:
        amount_bill1 = count
        amount_bill = amount_bill1 * 2666
        count1 = count - 600
    # If consumption electric are in 601-2200 kWh
    elif (count1 - 1600) <=0:
        amount_bill1 = 600
        amount_bill2 = count - 600
        count2 = count1 - 1600
        amount_bill = amount_bill1 * 2666 + amount_bill2 * 2629
    # If consumption electric are in upper from 2200 kWh
    else:
        amount_bill1 = 600
        amount_bill2 = 1600
        amount_bill = amount_bill1 * 2666 + amount_bill2 * 2629 + count2 * 2442 
    
    numbers1=amount_bill
    return float(numbers1)

def Administrative_offices(count):
    count1 = count - 600
    count2 = count1 - 1600
    if count <= 0:
        amount_bill = 0
    # If consumption electric are in 0-600kWh
    elif (count - 600) <=0:
        amount_bill1 = count
        amount_bill = amount_bill1 * 2666
        count1 = count - 600
    # If consumption electric are in 601-2200 kWh
    elif (count1 - 1600) <=0:
        amount_bill1 = 600
        amount_bill2 = count - 600
        count2 = count1 - 1600
        amount_bill = amount_bill1 * 2666 + amount_bill2 * 2629
    # If consumption electric are in upper from 2200 kWh
    else:
        amount_bill1 = 600
        amount_bill2 = 1600
        amount_bill = amount_bill1 * 2666 + amount_bill2 * 2629 + count2 * 2442
    
    numbers2=amount_bill
    return float(numbers2)


def Business(count):
    count1 = count - 600
    count2 = count1 - 1600
    if count <= 0:
        amount_bill = 0
    # If consumption electric are in 0-600kWh
    elif (count - 600) <=0:
        amount_bill1 = count
        amount_bill = amount_bill1 * 2666
        count1 = count - 600
    # If consumption electric are in 601-2200 kWh
    elif (count1 - 1600) <=0:
        amount_bill1 = 600
        amount_bill2 = count - 600
        count2 = count1 - 1600
        amount_bill = amount_bill1 * 2666 + amount_bill2 * 2629
    # If consumption electric are in upper from 2200 kWh
    else:
        amount_bill1 = 600
        amount_bill2 = 1600
        amount_bill = amount_bill1 * 2666 + amount_bill2 * 2629 + count2 * 2442
    
    numbers3=amount_bill
    return float(numbers3)

for custom in list_user:
    if(custom.get_phone()==phone):
        if(custom.get_password()==password):
            customer_id = int(custom.get_id_card())

# Read data_customer to get all information of that account
data=pd.read_excel("data/data_customer.xlsx",sheet_name="filtered_data")
type_electric=data.loc[data["Identity number"]==customer_id,"Type"].values
if type_electric == "Household":

    numbers=Household(amount)
    # def late_fee_HouseHold():
    total =numbers+(numbers*(10/100))
    late_fee = (numbers*(10/100))
    price = numbers
        
elif type_electric == "Administrative office":
    numbers1=Administrative_offices(amount)
    # def late_fee_Administrative_offices():
    total = numbers1+(numbers1*(10/100))
    late_fee = (numbers1*(10/100))
    price = numbers1
        
elif type_electric == "Business":
    numbers2=Business(amount)
    # def late_fee_Business():
    total = numbers2+(numbers2*(10/100))
    late_fee = (numbers2*(10/100))
    price = numbers2
        
elif type_electric == "Manufacturing industry":
    numbers3=Manufacturing_industries(amount)
    # def late_fee_Manufacturing_industries():
    total = numbers3+(numbers3*(10/100))
    late_fee = (numbers3*(10/100))
    price = numbers3
else:
    print("Error!")
        





