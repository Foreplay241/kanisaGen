import tkinter as tk
from idutc import IDUTC
from texioty import TEXIOTY


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.idutc_frame = IDUTC(master=master)
        self.idutc_frame.grid(column=0, row=0)
        self.texioty_frame = TEXIOTY(master=master, IDUTC=self.idutc_frame)
        self.texioty_frame.grid(column=0, row=1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1252x800")
    root.title('KanisaGen')
    app = Application(master=root)
    app.mainloop()
