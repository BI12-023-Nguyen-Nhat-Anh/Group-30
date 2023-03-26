hd = []
ao = []
mi = []
bs = []

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
    print(f"{amount}")
    hd.append(amount)
    

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
    print(f"{amount}")
    mi.append(amount)
    

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
    print(f"{amount}")
    ao.append(amount)

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
    print(f"{amount}")
    bs.append(amount)


# Take the value form meter_reading the consumption of electric
Household(500)
Administrative_offices(2000)
Business(1500)
Manufacturing_industries(1700)

# For the customers who does not complete in date
# Late fee
def late_fee_Household():
    for i in range(len(hd)):
        print(hd[i] * (10/100))
def late_fee_Administrative_offices():
    for i in range(len(ao)):
        print(ao[i] * (10/100))
def late_fee_Business():
    for i in range(len(bs)):
        print(bs[i] * (10/100))
def late_fee_Manufacturing_industries():
    for i in range(len(mi)):
        print(mi[i] * (10/100))
late_fee_Household()
late_fee_Administrative_offices()
late_fee_Business()
late_fee_Manufacturing_industries()
