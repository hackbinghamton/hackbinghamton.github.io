import tkinter as tk

class App(tk.Frame):
    '''
    A demo application.

    The App is a subclass of tk.Frame.
    tk.Frame is a widget that lets you 'pack in' other widgets.
    This way we can add in more than one widget to our application.
    '''
    def __init__(self, parent=None):
        self.parent = parent
# Attach our App to a parent widget
        super().__init__(parent)
# Set the parent widget size
        parent.geometry('500x500')
# Place our App on the screen
        self.pack()
# Add in the rest of our widgets
        self.add_hello_label()
        self.add_button()
        self.add_slider()
        self.add_counter()
        self.add_entry()

    def add_hello_label(self):
        '''
        Adds a Label to the bottom of our frame.
        '''
# We set the Label text and font here
        self.hello = tk.Label(self, text='Hello, World!', font=('Times New Roman', 20))
# This tells tkinter where to place the Label
        self.hello.pack(side='bottom')

    def add_button(self):
        '''
        Adds a Button to the top of our frame.
        '''
# We set the button text and command here
        self.change = tk.Button(self, text='Change the text', command=self.change_text)
# pack() defaults as pack(side='top')
        self.change.pack()

    def change_text(self):
        '''
        A command to change the Label's properties.
        '''

# Properties of a widget are accessed like a dictionary
        self.hello['text'] = 'This is changed text!'
        self.hello['fg'] = 'white'
        self.hello['bg'] = 'black'

    def add_slider(self):
        '''
        Adds a slider to the top of the frame.
        '''
        self.slider = tk.Scale(self,
# Define the minimum and maximum slider values
                from_=10,
                to=30,
# The default is a vertical slider
                orient=tk.HORIZONTAL,
# The command gets called every time the slider is moved
                command=self.scale_text)

# Set the sliders initial value
        self.slider.set(20)
        self.slider.pack()

    def scale_text(self, val):
        '''
        Changes the font size of our label.
        '''

# Font size is not a property of the label, so we have
# use the config() method
        self.hello.config(font=('Times New Roman', val))

    def inc(self, event):
        self.number['text'] = str(1+int(self.number['text']))

    def dec(self, event):
        self.number['text'] = str(-1+int(self.number['text']))

    def add_counter(self):
        '''
        Creates a label whose value can be updated with arrow keys'
        '''
        self.number = tk.Label(self, text='0', font=(None, 20))
        self.number.pack(side='bottom')
# Root handles keyboard entry here
        self.parent.bind('<Up>', self.inc)
        self.parent.bind('<Down>', self.dec)

    def clear_entry(self, event):
        '''
        Empties the entry box and prints out its contents
        '''
        print(self.entry.get())
        self.entry.delete(0, 'end')

    def add_entry(self):
        '''
        Creates an entry box.
        '''
        self.entry_label = tk.Label(self, text='Input')
        self.entry_label.pack(side='left')
        self.entry = tk.Entry(self, bd=5)
        self.entry.pack(side='right')
# Submit text when we hit Enter
        self.entry.bind('<Return>', self.clear_entry)


# An empty root widget to build our application from
root = tk.Tk()
# Create our app and attach it to the root
app = App(parent=root)
# Run the app
app.mainloop()
