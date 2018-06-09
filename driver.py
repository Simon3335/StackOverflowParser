import tkinter as tk # Provide window to display content
from tkinter import messagebox

import transcript as ts # Get the library to parse the content
import console # Log actions

console.log(console.R, 'Running interfase')


class MainWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        
        self.pack() # Show MainWindow
        self.widgets() # Create function for the widgets

    def widgets(self):
        
        console.log(console.L, 'Loading ID label and entry')

        self.room_id = tk.Label()
        self.room_id['text'] = "ID:"
        self.room_id['bg'] = "white"
        self.room_id['font'] = ("Courier", 20, "bold")
        self.room_id.pack(side=tk.LEFT)
        
        self.search = tk.Text()
        self.search['width'] = 10
        self.search['height'] = 1
        self.search['font'] = ("Courier", 30)
        self.search.pack(side=tk.LEFT)

        console.log(console.S, 'Loaded ID label and entry')
        console.log(console.L, 'Loading day label and entry')

        self.room_day = tk.Label()
        self.room_day['text'] = "Day:"
        self.room_day['bg'] = "white"
        self.room_day['font'] = ("Courier", 20, "bold")
        self.room_day.pack(side=tk.LEFT)

        self.day = tk.Text()
        self.day['width'] = 2
        self.day['height'] = 1
        self.day['font'] = ("Courier", 30)
        self.day.pack(side=tk.LEFT)

        console.log(console.S, 'Loaded day label and entry')
        console.log(console.L, 'Loading month label and entry')

        self.room_month = tk.Label()
        self.room_month['text'] = "Month:"
        self.room_month['bg'] = "white"
        self.room_month['font'] = ("Courier", 20, "bold")
        self.room_month.pack(side=tk.LEFT)

        self.month = tk.Text()
        self.month['width'] = 2
        self.month['height'] = 1
        self.month['font'] = ("Courier", 30)
        self.month.pack(side=tk.LEFT)

        console.log(console.S, 'Loaded month label and entry')
        console.log(console.L, 'Loading year label and entry')

        self.room_year = tk.Label()
        self.room_year['text'] = "Year:"
        self.room_year['bg'] = "white"
        self.room_year['font'] = ("Courier", 20, "bold")
        self.room_year.pack(side=tk.LEFT)

        self.year = tk.Text()
        self.year['width'] = 4
        self.year['height'] = 1
        self.year['font'] = ("Courier", 30)
        self.year.pack(side=tk.LEFT)

        console.log(console.S, 'Loaded year label and entry')
        console.log(console.L, 'Loading search icon')

        self.search_ico = tk.PhotoImage(file="elements/search.png")

        console.log(console.S, 'Loaded search icon')
        console.log(console.L, 'Loading search button')
        
        self.get = tk.Button()
        self.get['image'] = self.search_ico
        self.get['height'] = 40
        self.get['width'] = 40
        self.get['border'] = 0
        self.get['command'] = self.recieve
        self.get.pack(side=tk.LEFT)

        console.log(console.S, 'Loaded search button')

        self.display = tk.Text()

    def recieve(self):

        year = self.year.get('1.0', tk.END).strip('\n')
        month = self.month.get('1.0', tk.END).strip('\n')
        day = self.day.get('1.0', tk.END).strip('\n')
        id_ = self.search.get('1.0', tk.END).strip('\n')

        if id_ == '':
            messagebox.showerror('Fatal Error', 'Please enter an ID')
            console.log(console.E, 'Invalid ID entered')

        else:
            try: id_ = int(id_)
            except ValueError:
                messagebox.showerror('Fatal Error', 'ID must be an integer')
                console.log(console.E, 'ID not an integer')

        if day != '' and month != '' and year != '' and id_ != '':
            try: day = int(day)
            except ValueError:
                messagebox.showerror('Fatal Error', 'Day must be an integer between 1 and 7')
                console.log(console.E, 'Day not an integer')

            try: month = int(month)
            except ValueError:
                messagebox.showerror('Fatal Error', 'Month must be an integer between 1 and 31/30/29')
                console.log(console.E, 'Month not an integer')

            try: year = int(year)
            except ValueError:
                messagebox.showerror('Fatal Error', 'Year must be an integer')
                console.log(console.E, 'Year not an integer')

            room_request = ts.Room(id_, year=year, month=month, day=day)
            self.process(room_request)

        else:
            room_request = ts.Room(id_)
            self.process(room_request)

    def process(self, room_request):

        text = b''
        for message in room_request.messages():
            text += message + b'\n\n'
        
        
        self.display.insert(tk.END, text.decode('utf-8'))
        self.display.config(state=tk.DISABLED)
        self.display.pack(side=tk.BOTTOM)

        self.scroll = tk.Scrollbar()
        
        

root = tk.Tk()
root.configure(background="white") # Set background window as white
root.title('Stack Overflow Chat')

app = MainWindow(master=root) # Pass root to MainWindow
app.mainloop() # Call MainWindow's mainloop
