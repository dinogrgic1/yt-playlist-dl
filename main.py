import tkinter as tk

class Application(tk.Frame):
  def say_welcome(self):
    print('Welcome!')

  # example of creating a widget
  def createWidgets(self):
    self.label = tk.Label(self, anchor='w')
    self.label["text"] = 'URL:'
    self.label.grid(row=0)

    self.input = tk.Entry(self)
    self.input.grid(row=0, column=1)
    
    self.btn_search = tk.Button(self)
    self.btn_search["text"] = 'Search'
    self.btn_search.grid(row=0, column=2)


  # application initilisation function
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.pack()             # geometry-managment mechanisam
    self.createWidgets()

root = tk.Tk()
app = Application(master=root)
app.master.title('YT Playlist Download')
app.master.geometry('800x600')
app.mainloop()
root.destroy()
