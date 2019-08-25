import sqlite3
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

connection = sqlite3.connect('music.sqlite')

class ScrollBox(tkinter.Listbox):

    def __init__(self, window), **kw):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

mainWindow = tkinter.Tk()
mainWindow.title('Music DB Browser')
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ==== Labels ====
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# === Artists ===
artistLV = tkinter.Variable(mainWindow)
artistLV.set(("Choose an artist",))
artistList = tkinter.Listbox(mainWindow, listvariable=artistLV)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
artistList['yscrollcommand'] = artistScroll.set

# === Albums ListBox ===
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an album",))
albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# === Songs ListBox ===
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose a song",))
songList=tkinter.Listbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

mainWindow.mainloop()
print("Closing database connection.")
connection.close()