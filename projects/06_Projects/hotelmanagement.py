from tkinter import messagebox, simpledialog, Tk



rooms = { 
    1:'Joe Smith',
    2:'Bobby James',
    3:'',
    4:'',
    5:'',
    6:'Scary Larry',
    7:'',
    8:'',
    9:'Jesus Christ',
    10:''
    }

def checkin():
    print("checking in...")
    name = simpledialog.askstring(None, prompt='Please enter the first and last name of the person you are checking in',)
    days = simpledialog.askstring(None, prompt='how any days is ' + name + " staying?",)
    print(days)
    messagebox.showinfo(title=name + 's stay cost', message='Your total comes out to $' + int(days)*2)
    #fix this ^^^

def checkout():
    print("checking out...")

def checkavalable(room):
    print("checking avaliability of " + room)
    if int(room) >= 1 and int(room) <= 10:
        if rooms[int(room)] == '':
            messagebox.showinfo(title='room ' + room + ' avalibility', message= 'Room ' + room + ' is unoccupied.')
        else:
            messagebox.showinfo(title='room ' + room + ' avalibility', message= 'Room ' + room + ' is occupied by ' + rooms[int(room)])
    else:
        messagebox.showinfo(title='ERROR', message= 'Please enter a valid room number.')

choice = simpledialog.askstring(None, prompt='Welcome! Enter e to check in, enter o to check out, enter a number to view the rooms avalibility',)
if choice == 'e':
    checkin()
if choice == 'o':
    checkout()
if choice.isnumeric():
    checkavalable(choice)
else:
    messagebox.showinfo(title='ERROR', message= 'Please enter a valid command.')




