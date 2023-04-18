import Bill_Caculate
from Bill_Caculate import numbers,numbers1,numbers2,numbers3
import random
from domain.customer import customer
from main import list_user
from GUI.login import phone, password
from domain.MeterReading import name, id_customer, status, types, amount
import pandas as pd
from Bill_Caculate import price,late_fee,total


global bill_status
bill_status = ""
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

for custom in list_user:
    if(custom.get_phone()==phone):
        if(custom.get_password()==password):
            customer_id = int(custom.get_id_card())

data=pd.read_excel("data/data_customer.xlsx",sheet_name="filtered_data")
type_electric=data.loc[data["Identity number"]==customer_id, "Type"].values[0]
if type_electric == "Household":
    if duedate >= payment_date:
        total = numbers
        bill_status = "Paid"
        due = f"{duedate}/3/2023"
        payment = f"{payment_date}/3/2023"
    else:
        
        bill_status = "Overdue"
        due = f"{duedate}/3/2023"
        payment = f"{payment_date}/3/2023"

            
elif type_electric == "Administrative office":
    if duedate1 >= payment_date1:
        total = numbers1
        bill_status = "Paid"
        due = f"{duedate1}/3/2023"
        payment = f"{payment_date1}/3/2023"
    else:
        
        bill_status = "Overdue"
        due = f"{duedate1}/3/2023"
        payment = f"{payment_date1}/3/2023"
    
            
elif type_electric == "Business":
    if duedate2 >= payment_date2:
        total = numbers2
        bill_status = "Paid"
        due = f"{duedate2}/3/2023"
        payment = f"{payment_date2}/3/2023"
    else:
        
        bill_status = "Overdue"
        due = f"{duedate2}/3/2023"
        payment = f"{payment_date2}/3/2023"
    
            
elif type_electric == "Manufacturing industry":
    if duedate3 >= payment_date3:
        total = numbers3
        bill_status = "Paid"
        due = f"{duedate3}/3/2023"
        payment = f"{payment_date3}/3/2023"
    else:
        
        bill_status = "Overdue"
        due = f"{duedate3}/3/2023"
        payment = f"{payment_date3}/3/2023"
            
else:
    print("Error!")

# Read data_customer to get all information of that account
data_meterreading=pd.read_excel("data/data_meterreading.xlsx",sheet_name="Total consumption")

# Write data to excel file
new_data={"Customer Code": id_customer, "Name": name, "Total consumption": amount, "Type": types, "Price": price, "Late fee amount": late_fee, "Total payment amount": total, "Due Date": due, "Payment Date": payment,  "Bill Status": ""}
df=pd.DataFrame(new_data,index=[0])
update=pd.concat([data_meterreading,df])
update.to_excel("data/data_meterreading.xlsx", index=False, sheet_name="Total consumption") 
# if type_electric == "Household":
#     Household_payment()
# elif type_electric == "Administrative offices":
#     Administrative_offices_payment()
# elif type_electric == "Business":
#     Business_payment()
# elif type_electric == "Manufacturing industries":
#     Manufacturing_industries_payment()      
