from tkinter import *
import requests, json
from PIL import ImageTk,Image

root = Tk()
root.geometry('1366x768')
root.title("Live Train Status")
root.config(bg='pink')

img = ImageTk.PhotoImage(Image.open('rail-701x394.jpg'))
panel = Label(root,image=img,bg='pink')
panel.place(x=701,y=394)

lable_0 = Label(root,text="Live Train Status",width = 20,font=("bold",15),fg='brown',bg='pink')
lable_0.place(x=90,y=83)

lable_1 = Label(root,text="Train Number : ",width = 20,font=("bold",10),fg='black',bg='pink')
lable_1.place(x=60,y=130)
numbers = StringVar()
entry_1 = Entry(root,textvariable=numbers)
entry_1.place(x=200,y=130)
numbers.set("Ex : 12056")

lable_2 = Label(root,text="Today's Date : ",width = 20,font=("bold",10),fg='black',bg='pink')
lable_2.place(x=60,y=160)
dates = StringVar()
entry_2 = Entry(root,textvariable=dates)
entry_2.place(x=200,y=160)
dates.set("Ex : 01-07-2018")


def live():
    api_key = "qhx3wzhx26"
    base_url = "https://api.railwayapi.com/v2/live/train/"
    train_number = entry_1.get()
    current_date = entry_2.get()
    complete_url = base_url + train_number + "/date/" + current_date + "/apikey/" + api_key + "/"

    response_ob = requests.get(complete_url)
    result = response_ob.json()


    if result["response_code"] == 200:


        train_name = result["train"]["name"]
        y = result["route"]
        source_station = y[0]["station"]["name"]
        destination_station = y[len(y) - 1]["station"]["name"]
        position = result["position"]
        lable_3.configure(text=str(train_name))
        lable_4.configure(text=str(source_station))
        lable_5.configure(text=str(destination_station))
        lable_6.configure(text=str(position))
    else:
        lable_3.configure(text="Error")
        lable_4.configure(text="Error")
        lable_5.configure(text="Error")
        lable_6.configure(text="Error")



lable_3 = Label(root,text="...",width = 30,font=("bold",8),fg='black',bg='pink')
lable_3.place(x=110,y=240)
lable_4 = Label(root,text="...",width = 30,font=("bold",8),fg='black',bg='pink')
lable_4.place(x=110,y=260)
lable_5 = Label(root,text="...",width = 30,font=("bold",8),fg='black',bg='pink')
lable_5.place(x=110,y=280)
lable_6 = Label(root,text="...",width = 50,font=("bold",8),fg='black',bg='pink')
lable_6.place(x=50,y=300)

lable_7 = Label(root,text="Indian Railway",width = 20,font=("bold",8),fg='black',bg='pink')
lable_7.place(x=140,y=340)
lable_8 = Label(root,text="Developed by Shreekant Gosavi",width = 30,font=("bold",8),fg='black',bg='pink')
lable_8.place(x=110,y=360)

Button(root,text="Show",width=20,bg='brown',fg='white',command=live).place(x=130,y=200)

mainloop()
