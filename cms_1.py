from tkinter import *
import time
from tkinter import messagebox
import re

root = Tk()
root.geometry("890x580+0+0")
root.title("SIMPLE CAFE BILLING SYSTEM")

# Frames
Tops = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

# Time
localtime = time.asctime(time.localtime(time.time()))

# Header Info
lblinfo = Label(Tops, font=('aria', 30, 'bold'), text="SIMPLE CAFE BILLING MANAGEMENT SYSTEM", fg="Black", bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 20), text=localtime, fg="steel blue", anchor=W)
lblinfo.grid(row=1, column=0)

def validate_order_id(order_id):
    # Check if the order ID is valid
    pattern = r'^(?=.*[A-Z])(?=.*\d)[A-Z\d]{10}$'
    return re.match(pattern, order_id)

def validate_numeric_input(value):
    # Check if the input is a valid number
    return value.isdigit() or value == ""

def Ref():
    # Check if order ID is entered and valid
    if rand.get() == "":
        messagebox.showwarning("Input Error", "Please enter the Order ID first.")
        return

    if not validate_order_id(rand.get()):
        messagebox.showwarning("Input Error", "Order ID must be 10 characters long, contain uppercase letters and numbers only, and cannot contain special characters.")
        return

    # Validate quantities
    if not all(validate_numeric_input(q.get()) for q in [Fries, Largefries, Burger, Filet, Cheese_burger, Drinks]):
        messagebox.showwarning("Input Error", "Please enter valid numbers for item quantities.")
        return

    # Get quantities from user input
    cof = float(Fries.get() or 0)
    colfries = float(Largefries.get() or 0)
    cob = float(Burger.get() or 0)
    cofi = float(Filet.get() or 0)
    cochee = float(Cheese_burger.get() or 0)
    codr = float(Drinks.get() or 0)

    # Check if at least one item is selected
    if all(q == 0 for q in [cof, colfries, cob, cofi, cochee, codr]):
        messagebox.showwarning("Input Error", "Please select at least one item.")
        return

    costoffries = cof * 25
    costoflargefries = colfries * 40
    costofburger = cob * 35
    costoffilet = cofi * 50
    costofcheeseburger = cochee * 30
    costofdrinks = codr * 35

    total_cost = costoffries + costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks
    PayTax = total_cost * 0.33
    Ser_Charge = total_cost / 99
    OverAllCost = PayTax + total_cost + Ser_Charge

    # Set calculated values to respective fields
    Subtotal.set(f"Rs. {total_cost:.2f}")
    Tax.set(f"Rs. {PayTax:.2f}")
    Service_Charge.set(f"Rs. {Ser_Charge:.2f}")
    Total.set(f"Rs. {OverAllCost:.2f}")

def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Cheese_burger.set("")
    Drinks.set("")
    Tax.set("")
    Service_Charge.set("")
    Subtotal.set("")
    Total.set("")

# Variables
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cheese_burger = StringVar()

# Order Form
lblreference = Label(f1, font=('aria', 16, 'bold'), text="Order No.", fg="green", bd=20, anchor='w')
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, font=('ariel', 16, 'bold'), textvariable=rand, bd=6, insertwidth=6, bg="LemonChiffon", justify='right')
txtreference.grid(row=0, column=1)

lblDrinks = Label(f1, font=('aria', 16, 'bold'), text="Drinks", fg="blue", bd=10, anchor='w')
lblDrinks.grid(row=1, column=0)
txtDrinks = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="Aquamarine", justify='right')
txtDrinks.grid(row=1, column=1)

lblfries = Label(f1, font=('aria', 16, 'bold'), text="French Fries", fg="blue", bd=10, anchor='w')
lblfries.grid(row=2, column=0)
txtfries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="Aquamarine", justify='right')
txtfries.grid(row=2, column=1)

lblLargefries = Label(f1, font=('aria', 16, 'bold'), text="Lunch", fg="blue", bd=10, anchor='w')
lblLargefries.grid(row=3, column=0)
txtLargefries = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Largefries, bd=6, insertwidth=4, bg="Aquamarine", justify='right')
txtLargefries.grid(row=3, column=1)

lblburger = Label(f1, font=('aria', 16, 'bold'), text="Burger", fg="blue", bd=10, anchor='w')
lblburger.grid(row=4, column=0)
txtburger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="Aquamarine", justify='right')
txtburger.grid(row=4, column=1)

lblFilet = Label(f1, font=('aria', 16, 'bold'), text="Pizza", fg="blue", bd=10, anchor='w')
lblFilet.grid(row=5, column=0)
txtFilet = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Filet, bd=6, insertwidth=4, bg="Aquamarine", justify='right')
txtFilet.grid(row=5, column=1)

lblCheese_burger = Label(f1, font=('aria', 16, 'bold'), text="Cheese Burger", fg="blue", bd=10, anchor='w')
lblCheese_burger.grid(row=6, column=0)
txtCheese_burger = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Cheese_burger, bd=6, insertwidth=4, bg="Aquamarine", justify='right')
txtCheese_burger.grid(row=6, column=1)

# Bill Section
lblService_Charge = Label(f1, font=('aria', 16, 'bold'), text="Service Charge", fg="black", bd=10, anchor='w')
lblService_Charge.grid(row=3, column=2)
txtService_Charge = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4, bg="LightGreen", justify='right')
txtService_Charge.grid(row=3, column=3)

lblTax = Label(f1, font=('aria', 16, 'bold'), text="Tax", fg="black", bd=10, anchor='w')
lblTax.grid(row=4, column=2)
txtTax = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="LightGreen", justify='right')
txtTax.grid(row=4, column=3)

lblSubtotal = Label(f1, font=('aria', 16, 'bold'), text="Subtotal", fg="black", bd=10, anchor='w')
lblSubtotal.grid(row=5, column=2)
txtSubtotal = Entry(f1, font=('ariel', 16, 'bold'), textvariable=Subtotal, bd=6, insertwidth=4, bg="LightGreen", justify='right')
txtSubtotal.grid(row=5, column=3)

lblTotal = Label(f1, font=('aria', 16, 'bold'), text="Total", fg="green", bd=10, anchor='w')
lblTotal.grid(row=6, column=2)
txtTotal = Entry(f1, font=('aria', 16, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="LightGreen", justify='right')
txtTotal.grid(row=6, column=3)

# Buttons
btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'),
                  width=10, text="TOTAL", bg="green", command=Ref)
btnTotal.grid(row=8, column=1)

btnreset = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'),
                  width=10, text="RESET", bg="yellow", command=reset)
btnreset.grid(row=8, column=2)

btnexit = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'),
                 width=10, text="EXIT", bg="red", command=qexit)
btnexit.grid(row=8, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    
    # Original style price list layout
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=1)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=2)
    
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="French Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=2)
    
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=2)
    
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=2)
    
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=2)
    
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=2)
    
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=2)

    roo.mainloop()

btnprice = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'),
                  width=10, text="PRICE", bg="light blue", command=price)
btnprice.grid(row=8, column=0)

root.mainloop()