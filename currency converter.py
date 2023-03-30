from tkinter import *
import customtkinter
import requests

root = customtkinter.CTk()

customtkinter.set_appearance_mode("System")


root.geometry("500x400+500+200")
root.resizable(0,0)
root.configure(bg="white")


def convert_currency():
    source = from_menu.get()
    destination = to_menu.get()
    amount = amount_enter.get()
    result = requests.get(f'https://v6.exchangerate-api.com/v6/{"460daa49cfdff1b748f7c8ee"}/pair/{source}/{destination}/{amount}').json()
    converted_result = result['conversion_result']
    formatted_result = f'{amount} {source} = {converted_result} {destination}'
    result_label.configure(text=formatted_result)



top_label = customtkinter.CTkLabel(root,text="Currency Converter",font=("arial",35,"bold"),)
top_label.pack()

from_label = customtkinter.CTkLabel(root,text="FROM: ")
from_label.place(x=10,y=70)

to_label = customtkinter.CTkLabel(root,text="TO: ")
to_label.place(x=120,y=70)


currency_rates = ["USD","GEL","EUR","GBP"]
variable1 =StringVar()
variable2 =StringVar()

from_menu = customtkinter.CTkComboBox(root,variable=variable1,values=currency_rates,font=("arial",12),width=80,dropdown_font=("arial",12))
from_menu.set("USD")
from_menu.place(x=10,y=90)

to_menu = customtkinter.CTkComboBox(root,variable=variable2,width=80,values=currency_rates,font=("airal",12),dropdown_font=("arial",12))
to_menu.set("GEL")
to_menu.place(x=120,y=90)



amount_label = customtkinter.CTkLabel(root,text="Enter Amount: ",font=("Arial",22))
amount_label.place(x=10,y=120)

amount_enter = customtkinter.CTkEntry(root,font=('arial',25,'bold'),justify=CENTER,width=300,corner_radius=65)
amount_enter.place(x=5,y=150)

result_label = customtkinter.CTkLabel(root,text="AMOUNT: ",font=("poppins",22,"bold"))
result_label.place(x=10,y=195)


convert_button = customtkinter.CTkButton(root,text="Convert",font=("Poppins",25,"bold"),corner_radius=70,command=convert_currency)
convert_button.place(x=320,y=150)






root.mainloop()