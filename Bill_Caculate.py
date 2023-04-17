from domain.customer import customer
from domain.MeterReading import amount
numbers = []
numbers1 = []
numbers2 = []
numbers3 = []
global late_fee
late_fee = 0
global price
price = 0
def Household(count):

    # Seperate the total consumption electric for each stage
    count1 = count - 50
    count2 = count1 - 50
    count3 = count2 - 100
    count4 = count3 - 100
    count5 = count4 -100

    if count <= 0:
        amount = 0
    # If consumption electric are in 0-50kWh
    elif (count - 50) <= 0:
        amount1 = count
        amount = amount1 * 1.678
        count1 = count - 50
    # If consumption electric are in 51-100 kWh
    elif (count1 - 50) <= 0:
        amount1 = 50
        amount2 = count - 50
        count2 = count1 - 50
        amount = (amount1 * 1.678) + (amount2 * 1.734)
    # If consumption electric are in 101-200 kWh
    elif (count2 - 100) <=0:
        amount1 = 50
        amount2 = 50
        amount3 = count1 - 50
        count3 = count2 - 100
        amount = (amount1 * 1.678) + (amount2 * 1.734) + (amount3 * 2.014)
    # If consumption electric are in 201-300 kWh
    elif (count3 - 100) <= 0:
        amount1 = 50
        amount2 = 50
        amount3 = 100
        amount4 = count2 - 100
        count4 = count3 - 100
        amount = (amount1 * 1.678) + (amount2 * 1.734) + (amount3 * 2.014) +(amount4 * 2.536)
    # If consumption electric are in 300-401 kWh
    elif (count4 -100) <=0:
        amount1 = 50
        amount2 = 50
        amount3 = 100
        amount4 = 100
        amount5 = count3 - 100
        count5 = count4 -100
        amount = (amount1 * 1.678) + (amount2 * 1.734) + (amount3 * 2.014) +(amount4 * 2.536)+ (amount5 * 2.834)
    # If consumption electric are in upper 401 kWh
    else:
        # Total price
        amount1 = 50
        amount2 = 50
        amount3 = 100
        amount4 = 100
        amount5 = 100 
        amount = (amount1 * 1.678) + (amount2 * 1.734) + (amount3 * 2.014) +(amount4 * 2.536)+ (amount5 * 2.834) + (count5 * 2.927)
    
    numbers.append(amount)

def Manufacturing_industries(count):
    count1 = count - 600
    count2 = count1 - 1600
    if count <= 0:
        amount = 0
    # If consumption electric are in 0-600kWh
    elif (count - 600) <=0:
        amount1 = count
        amount = amount1 * 2.666
        count1 = count - 600
    # If consumption electric are in 601-2200 kWh
    elif (count1 - 1600) <=0:
        amount1 = 600
        amount2 = count - 600
        count2 = count1 - 1600
        amount = amount1 * 2.666 + amount2 * 2.629
    # If consumption electric are in upper from 2200 kWh
    else:
        amount1 = 600
        amount2 = 1600
        amount = amount1 * 2.666 + amount2 * 2.629 + count2 * 2.442 
    
    numbers1.append(amount)

def Administrative_offices(count):
    count1 = count - 600
    count2 = count1 - 1600
    if count <= 0:
        amount = 0
    # If consumption electric are in 0-600kWh
    elif (count - 600) <=0:
        amount1 = count
        amount = amount1 * 2.666
        count1 = count - 600
    # If consumption electric are in 601-2200 kWh
    elif (count1 - 1600) <=0:
        amount1 = 600
        amount2 = count - 600
        count2 = count1 - 1600
        amount = amount1 * 2.666 + amount2 * 2.629
    # If consumption electric are in upper from 2200 kWh
    else:
        amount1 = 600
        amount2 = 1600
        amount = amount1 * 2.666 + amount2 * 2.629 + count2 * 2.442
    
    numbers2.append(amount)


def Business(count):
    count1 = count - 600
    count2 = count1 - 1600
    if count <= 0:
        amount = 0
    # If consumption electric are in 0-600kWh
    elif (count - 600) <=0:
        amount1 = count
        amount = amount1 * 2.666
        count1 = count - 600
    # If consumption electric are in 601-2200 kWh
    elif (count1 - 1600) <=0:
        amount1 = 600
        amount2 = count - 600
        count2 = count1 - 1600
        amount = amount1 * 2.666 + amount2 * 2.629
    # If consumption electric are in upper from 2200 kWh
    else:
        amount1 = 600
        amount2 = 1600
        amount = amount1 * 2.666 + amount2 * 2.629 + count2 * 2.442
    
    numbers3.append(amount)


if customer.get_type() == "HouseHold":

    Household(amount)
    def late_fee_HouseHold():
         numbers[0]+(numbers[0]*(10/100))
         late_fee = (numbers[0]*(10/100))
         price = numbers[0]
        
elif customer.get_type() == "Administrative_offices":
    Administrative_offices(amount)
    def late_fee_Administrative_offices():
         numbers1[0]+(numbers1[0]*(10/100))
         late_fee = (numbers1[0]*(10/100))
         price = numbers1[0]
        
elif customer.get_type() == "Business":
    Business(amount)
    def late_fee_Business():
         numbers2[0]+(numbers2[0]*(10/100))
         late_fee = (numbers2[0]*(10/100))
         price = numbers2[0]
        
elif customer.get_type() == "Manufacturing_industries":
    Manufacturing_industries(amount)
    def late_fee_Manufacturing_industries():
         numbers3[0]+(numbers3[0]*(10/100))
         late_fee = (numbers3[0]*(10/100))
         price = numbers3[0]
else:
    print("Error!")
        






