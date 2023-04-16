from main import list_user
from GUI.login import phone, password
from openpyxl.utils.dataframe import dataframe_to_rows
import openpyxl
import random
import pandas as pd
from tkinter import messagebox

class MeterReading:
    def __init__(self):
        # write=pd.ExcelWriter("data/data_meterreading.xlsx", engine="openpyxl")
        for custom in list_user:
            if(custom.get_phone()==phone):
                if(custom.get_password()==password):
                    self.__customer_id=int(custom.get_id_card())
                    print(f"Customer id={self.__customer_id}")
                    data=pd.read_excel("data/data_customer.xlsx",sheet_name="filtered_data")
                    data_meterreading=pd.read_excel("data/data_meterreading.xlsx",sheet_name="MeterReading")
                    # write=pd.ExcelWriter("data/data.xlsx",engine="openpyxl")
                    status=data.loc[data["Identity number"]==self.__customer_id,"Status"].values[0]
                    if(status=="Active"):
                        name=data.loc[data["Identity number"]==self.__customer_id,"Name"].values[0]
                        id_customer=data.loc[data["Identity number"]==self.__customer_id,"Customer Code"].values[0]
                        self.__customer_code=id_customer
                        type=data.loc[data["Identity number"]==self.__customer_id,"Type"].values[0]
                    else:
                        messagebox.showerror("Error!","Your account is invalid due to late payment of fees")

                    new_data={"Customer Code": id_customer, "Name": name, "MeterReading": "","Type": type, "Status": status}
                    df=pd.DataFrame(new_data,index=[0])
                    update=pd.concat([data_meterreading,df])
                    update.to_excel("data/data_meterreading.xlsx", index=False, sheet_name="MeterReading")

    def set_MeterReading(self):
        # Random amount of electricity used by the customer 
        data=pd.read_excel("data/data_meterreading.xlsx",sheet_name="MeterReading")
        type=data.loc[data["Customer Code"]==self.__customer_code, "Type"].values[0]
        if(type=="Household"):
            data.loc[data["Customer Code"]==self.__customer_code, "MeterReading"]=random.randint(50,400)
            data.to_excel("data/data_meterreading.xlsx", sheet_name="MeterReading",index=False)
        elif(type=="Manufacturing industries"):
            data.loc[data["Customer Code"]==self.__customer_code, "MeterReading"]=random.randint(400,1000)
            data.to_excel("data/data_meterreading.xlsx", sheet_name="MeterReading",index=False)
        elif(type=="Business"):
            data.loc[data["Customer Code"]==self.__customer_code, "MeterReading"]=random.randint(200,700)
            data.to_excel("data/data_meterreading.xlsx", sheet_name="MeterReading",index=False)
        elif(type=="Administrative offices"):
            data.loc[data["Customer Code"]==self.__customer_code, "MeterReading"]=random.randint(200,700)
            data.to_excel("data/data_meterreading.xlsx", sheet_name="MeterReading",index=False)

    def get_MeterReading(self):
        # Take the data by the CustomerID in the data_customer file
        data=pd.read_excel("data/data_customer.xlsx",sheet_name="filtered_data")
        user_data=data.loc[data["Customer Code"]==self.__self.__customer_id, "MeterReading"].values[0]
        

k=MeterReading()
k.set_MeterReading()