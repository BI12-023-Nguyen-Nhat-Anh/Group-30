from GUI import login
from domain.user import user
from domain.user import admin
import os

data=[]
list_user=[]

if os.path.exists("data/user.txt"):
    with open("data/user.txt","r") as f:
        a=f.read()
        a=a.split("\n")
        for i in range(len(a)):
            if(a[i]==''):
                a.pop(i)
            else:
                data.append(a[i].split(","))
    f.close()
    for i in range(len(data)):
        if("admin" in data[i]):
            admin_data=admin(data[i][0], data[i][1])
        else:
            k=user(data[i][0],data[i][1],data[i][2])
            list_user.append(k)

