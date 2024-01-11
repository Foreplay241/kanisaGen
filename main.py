import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1252x800")
    root.title('KanisaGen')
    app = Application(master=root)
    app.mainloop()
    