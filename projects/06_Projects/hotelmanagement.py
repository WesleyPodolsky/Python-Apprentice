from tkinter import messagebox, simpledialog, Tk

clockedIn = True
fullHotel = True


rooms = { 
    1:'Joe Smith',
    2:'Bobby James',
    3:'Veris Iggma',
    4:'',
    5:'',
    6:'Scary Larry',
    7:'',
    8:'',
    9:'Jesus Christ',
    10:''
    }

def checkin():
    try:
        fullHotel = True
        for key, value in rooms.items():
            if value == '':
                fullHotel = False

        if fullHotel:
            messagebox.showinfo(None, message='Sorry! Hotel at max capacity!')
        else:
            print("checking in...")
            name = simpledialog.askstring(None, prompt='Please enter the first and last name of the person you are checking in',)
            days = simpledialog.askstring(None, prompt='how any days is ' + name + " staying?",)

            for i in range(1,len(rooms)+1):
                print(i)
                print(rooms)
                if rooms[i] == '':
                    messagebox.showinfo(None, message= name + ' owes $' + str(int(days)*150) +'.00 for thier stay, and ' + name + " will stay in room number " + str(i) + ".")
                    rooms[i]=name + "  ~ ~ ~  (Staying " + days + " days)"
                    break
    except:
        messagebox.showinfo(None, message='An error occured while checking in. Please Press OK to navigate back to home')
    


def checkout():
    try:
        print("checking out...")
        outer = simpledialog.askstring(None, prompt='Enter a room number of whom you want to check out.')
        if int(outer) <= 10 and int(outer) >= 1:
            if rooms[int(outer)] != '':
                sure = simpledialog.askstring(title='[y = yes] ~ ~ ~ [n = no]', prompt='Are you sure you want to check out ' + rooms[int(outer)] + '? [y = yes] ~ [n = no]')
                if sure == 'y':
                    messagebox.showinfo(None, message='Succesfully checked out ' + rooms[int(outer)] + '.')
                    rooms[int(outer)]=''
                elif sure == 'n':
                    messagebox.showinfo(None, message='Checkout canceled. Have a good day!')
                else:
                    messagebox.showinfo(None, message='Please enter a valid [y] or [n] answer')
                    print(sure)
        else:
            messagebox.showinfo(None, message= 'Please enter a valid room number')
    except:
        messagebox.showinfo(None, message='An error occured while checking out. Please Press OK to navigate back to home')



def checkavalable(room):
    try:
        print("checking avaliability of " + room)
        if int(room) >= 1 and int(room) <= 10:
            if rooms[int(room)] == '':
                messagebox.showinfo(title='room ' + room + ' avalibility', message= 'Room ' + room + ' is unoccupied.')
            else:
                messagebox.showinfo(title='room ' + room + ' avalibility', message= 'Room ' + room + ' is occupied by ' + rooms[int(room)])
        else:
            messagebox.showinfo(title='ERROR', message= 'Please enter a valid room number.')
    except:
        messagebox.showinfo(None, message='An error occured. Please Press OK to navigate back to home')

while clockedIn:
    choice = simpledialog.askstring(None, prompt='[c -> check in] ~ [o -> check out] ~ [number -> checks that rooom avalibility] ~ [x -> exit]',)
    if choice == 'c':
        checkin()
    elif choice == 'o':
        checkout()
    elif choice.isnumeric():
        checkavalable(choice)
    elif choice == 'x':
        clockedIn = False
    else:
        messagebox.showinfo(title='ERROR', message= 'Please enter a valid command.')




