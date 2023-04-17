from main import list_user
from GUI.login import phone, password
import random
import pandas as pd
from tkinter import messagebox

class MeterReading:
    def __init__(self):
        global amount
        amount=0
        # Check with which account the user is logged in to register electricity
        for custom in list_user:
            if(custom.get_phone()==phone):
                if(custom.get_password()==password):
                    self.__customer_id=int(custom.get_id_card())
                    # Read data_customer to get all information of that account
                    data=pd.read_excel("data/data_customer.xlsx",sheet_name="filtered_data")
                    data_meterreading=pd.read_excel("data/data_meterreading.xlsx",sheet_name="Total Consumtion")
                    # Take status of that account to check
                    status=data.loc[data["Identity number"]==self.__customer_id,"Status"].values[0]
                    print(f"Status: {status}")
                    if(status=="Active"):
                        # Get the data in which line has the same Customer_id as the logged in account
                        name=data.loc[data["Identity number"]==self.__customer_id,"Name"].values[0]
                        id_customer=data.loc[data["Identity number"]==self.__customer_id,"Customer Code"].values[0]
                        # Give id_customer = id_customer to have the account check variable in the get_MeterReading function because meter reading 
                        # only takes the customer code
                        self.__customer_code=id_customer
                        types=data.loc[data["Identity number"]==self.__customer_id,"Type"].values[0]
                    else:
                        # # If customers pay late fees, they will be inactive and unable to use electricity
                        messagebox.showerror("Error!","Your account is invalid due to late payment of fees")
                    # Check the types of electricity customers use and random amount of electricity
                    if(types=="Household"):
                        amount=random.randint(50,400)
                        data.to_excel("data/data_meterreading.xlsx", sheet_name="Total Consumtion",index=False)
                    elif(types=="Manufacturing industries"):
                        amount=random.randint(400,1000)
                        data.to_excel("data/data_meterreading.xlsx", sheet_name="Total Consumtion",index=False)
                    elif(types=="Business"):
                        amount=random.randint(200,700)
                        data.to_excel("data/data_meterreading.xlsx", sheet_name="Total Consumtion",index=False)
                    elif(types=="Administrative offices"):
                        amount=random.randint(200,700)
                        data.to_excel("data/data_meterreading.xlsx", sheet_name="Total Consumtion",index=False)
                    # Write data to excel file
                    new_data={"Customer Code": id_customer, "Name": name, "MeterReading": amount, "Type": types, "Status": status}
                    df=pd.DataFrame(new_data,index=[0])
                    update=pd.concat([data_meterreading,df])
                    update.to_excel("data/data_meterreading.xlsx", index=False, sheet_name="Total Consumtion")
        
    def get_customer_code(self):
        return self.__customer_code

MeterReading()
import Bill_Caculate