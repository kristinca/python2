import tkinter as tk


class MyRange:

    def __init__(self, number_start, number_end, *args, **kwargs):
        self.number_start = number_start
        self.number_end = number_end

        self.state = self.number_start
        self.list1 = [i for i in range(self.number_start, self.number_end + 1)]

    def __iter__(self):
        return self

    def __next__(self):
        temp_state = self.state

        if self.state > self.number_end:
            raise StopIteration

        self.state += 1
        return temp_state


class MyApp(tk.Tk):
    """The app"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("My Range iterator")
        self.geometry('400x300')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.resizable(False, False)
        self.myrang = MyRange(0,1)
        self.app_data = {
            "range_elements": self.myrang.list1
        }

        container = tk.Frame(self)
        container.pack(side="top", fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.config(bg="#0D5176")

        frame = tk.Frame(self, padx=50, pady=50)
        frame.pack()

        frame1 = FrameOne(parent=container, controller=self)
        frame1.pack()


class FrameOne(tk.Frame):
    """ The only frame """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.config(bg="#0D5176")

        self.enter_label = tk.Label(self, text='START', width=7, font='Helvetica 15',
                                    bg='#0D98BA', borderwidth=5, relief='raised')
        self.enter_label.grid(row=0, column=0, pady=30)

        self.enter_from = tk.Entry(self, width=12, borderwidth=5)
        self.enter_from.grid(row=1, column=0, padx=30)

        self.to_label = tk.Label(self, text='END', width=7, font='Helvetica 15',
                                 bg='#0D98BA', borderwidth=5, relief='raised')
        self.to_label.grid(row=0, column=1, pady=30)

        self.enter_to = tk.Entry(self, width=12, borderwidth=5)
        self.enter_to.grid(row=1, column=1, padx=30)

        the_button = tk.Button(self, text='ENTER', width=10, font='Helvetica 15', bg='#0D98BA',
                               borderwidth=5, command=lambda: self.show())
        the_button.grid(row=2, column=0, columnspan=2, pady=30)

        self.i = -1
        self.label_show = tk.Label(self)


    def show(self):
        self.label_show.destroy()
        self.myrang1 = MyRange(int(self.enter_from.get()), int(self.enter_to.get()))
        self.controller.app_data["range_elements"] = self.myrang1.list1
        self.label_show = tk.Label(self, text=self.myrang1.list1[0], font='bold 12')
        self.label_show.grid(row=3, column=0, columnspan=2, pady=10)
        self.every1sec()


    def every1sec(self):
        self.i += 1
        if self.i == len(self.myrang1.list1):
            return
        self.label_show['text'] = self.controller.app_data["range_elements"][self.i]
        self.after(1000, self.every1sec)


# def main():
#     myrang = MyRange(2, 8)
#     for i in myrang:
#         print(i)

if __name__ == '__main__':
    # main()
    my_app = MyApp()
    my_app.mainloop()
