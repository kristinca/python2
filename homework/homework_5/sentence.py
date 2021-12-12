import tkinter as tk


class Sentence:

    def __init__(self, input_str, *args, **kwargs):
        self.input = input_str
        self.state = -1

    def __iter__(self):
        return self

    def sizeof(self, elem):
        return elem.__sizeof__()

    def words_maker(self):

        words = []
        word = ''
        for el in self.input:
            # if the character is a letter
            if 155 >= self.sizeof(bytes(ord(el))) >= 98:
                word += el
            elif word:
                words.append(word)
                word = ''

        if word:
            words.append(word)

        return words

    def __next__(self):

        self.state += 1
        t = self.words_maker()

        if self.state == len(t):
            raise StopIteration

        return t[self.state]


class MyApp(tk.Tk):
    """The app"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Sentence iterator")
        self.geometry('600x300')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.resizable(False, False)
        self.sen = Sentence('')
        self.app_data = {
            "range_elements": self.sen.words_maker()
        }

        container = tk.Frame(self)
        container.pack(side="top", fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.config(bg="#740048")

        frame = tk.Frame(self, padx=50, pady=50)
        frame.pack()

        frame1 = FrameOne(parent=container, controller=self)
        frame1.pack()


class FrameOne(tk.Frame):
    """ The only frame """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.config(bg="#740048")

        self.the_button = tk.Button(self, text='ENTER', width=10, font='Helvetica 15', bg='#af006c',
                                    borderwidth=5, command=lambda: self.show())
        self.the_button.grid(row=2, column=0, columnspan=2, pady=30)

        self.enter_from = tk.Entry(self, font='bold 12', width=50, borderwidth=5)
        self.enter_from.grid(row=0, column=0, padx=30, pady=30)

        self.i = -1
        self.label_show = tk.Label(self)

    def show(self):
        self.label_show.forget()
        self.sen1 = Sentence(self.enter_from.get())
        self.controller.app_data["range_elements"] = self.sen1.words_maker()
        self.label_show = tk.Label(self, text=self.sen1.words_maker()[0], font='bold 12', width=50, borderwidth=5,
                                   relief='sunken')
        self.label_show.grid(row=3, column=0, columnspan=5, pady=30)
        self.the_button.config(state='disabled', bg='#4e0030')
        self.every1sec()

    def every1sec(self):
        self.i += 1
        if self.i == len(self.sen1.words_maker()):
            return
        self.label_show['text'] = self.controller.app_data["range_elements"][self.i]
        self.after(1000, self.every1sec)


# def main():
#
#     a_string = 'it   786?w999 orks    2"£$ %. yaaaayyy ^^.'
#
#     some_string = Sentence(a_string)
#
#     for i in a_string:
#         print(next(some_string))

if __name__ == '__main__':
    # main()
    my_app = MyApp()
    my_app.mainloop()
