import tkinter
from tkinter import messagebox



class MyGui:

    
    def __init__(self):

        self.main_window = tkinter.Tk()


        self.main_window.wm_title('Mini Calculator')



        self.frm_label = tkinter.Frame(self.main_window)
        self.lbl_header = tkinter.Label(self.frm_label, text='Mini Calculator', font=('Arial', 32))
        self.lbl_header.pack(side='top', pady=[20, 0])
        self.frm_label.pack()


        self.frm_input1 = tkinter.Frame(self.main_window)


        self.ety_value1 = tkinter.Entry(self.frm_input1, font=('Arial', 22), width=5)
        self.ety_value1.pack(side='left')


        self.btn_add = tkinter.Button(self.frm_input1, text='+', font=('Arial', 22), width=3,
                                      command=self.btn_add_click)
        self.btn_add.pack(side='left', padx=20, pady=10)


        self.btn_multiply = tkinter.Button(self.frm_input1, text='X', font=('Arial', 22), width=3,
                                           command=self.btn_multiply_click)
        self.btn_multiply.pack(side='left')

        self.frm_input1.pack()


        self.frm_input2 = tkinter.Frame(self.main_window)


        self.ety_value2 = tkinter.Entry(self.frm_input2, font=('Arial', 22), width=5)
        self.ety_value2.pack(side='left')


        self.btn_subtract = tkinter.Button(self.frm_input2, text='-', font=('Arial', 22), width=3,
                                           command=self.btn_subtract_click)
        self.btn_subtract.pack(side='left', padx=20, pady=10)


        self.btn_divide = tkinter.Button(self.frm_input2, text='/', font=('Arial', 22), width=3,
                                         command=self.btn_divide_click)
        self.btn_divide.pack(side='left')

        self.frm_input2.pack()


        self.frm_output = tkinter.Frame(self.main_window)


        self.txt_result = tkinter.Text(self.frm_output, state='disabled', width=40, height=20, font=('Arial', 12))
        self.txt_result.pack(side='left', padx=20)

        self.frm_output.pack()


        self.frm_bottom = tkinter.Frame(self.main_window)


        self.btn_clear = tkinter.Button(self.frm_bottom, text='Clear', font=('Arial', 12), command=self.btn_clear_click)
        self.btn_clear.pack(side='left', padx=10, pady=20)


        self.btn_about = tkinter.Button(self.frm_bottom, text='About', font=('Arial', 12), command=self.btn_about_click)
        self.btn_about.pack(side='left', padx=10, pady=20)

        self.frm_bottom.pack()


        self.ety_value1.focus()


        tkinter.mainloop()


    def btn_add_click(self):


        if not self.validate_numbers():
            return


        value1 = float(self.ety_value1.get())
        value2 = float(self.ety_value2.get())
        answer = value1 + value2
        message = str(value1) + ' plus ' + str(value2) + ' equals ' + str(answer) + '\n'


        self.txt_result.configure(state='normal')
        self.txt_result.insert('0.0', message)
        self.txt_result.configure(state='disabled')


    def btn_subtract_click(self):


        if not self.validate_numbers():
            return


        value1 = float(self.ety_value1.get())
        value2 = float(self.ety_value2.get())
        answer = value1 - value2
        message = str(value1) + ' minus ' + str(value2) + ' equals ' + str(answer) + '\n'


        self.txt_result.configure(state='normal')
        self.txt_result.insert('0.0', message)
        self.txt_result.configure(state='disabled')


    def btn_multiply_click(self):


        if not self.validate_numbers():
            return


        value1 = float(self.ety_value1.get())
        value2 = float(self.ety_value2.get())
        answer = value1 * value2
        message = str(value1) + ' times ' + str(value2) + ' equals ' + str(answer) + '\n'


        self.txt_result.configure(state='normal')
        self.txt_result.insert('0.0', message)
        self.txt_result.configure(state='disabled')


    def btn_divide_click(self):


        if not self.validate_numbers():
            return


        value1 = float(self.ety_value1.get())
        value2 = float(self.ety_value2.get())


        if value2 == 0:
            tkinter.messagebox.showerror('Error', 'Can not divide a number by zero')
            self.ety_value2.focus()
            return


        answer = value1 / value2
        message = str(value1) + ' divided by ' + str(value2) + ' equals ' + str(answer) + '\n'


        self.txt_result.configure(state='normal')
        self.txt_result.insert('0.0', message)
        self.txt_result.configure(state='disabled')


    def btn_about_click(self):

        tkinter.messagebox.showinfo('About', 'Mini Calculator\n\n(c)2017 College of DuPage\nAll Rights Reserved')


    def btn_clear_click(self):

        self.ety_value1.delete(0, 'end')
        self.ety_value2.delete(0, 'end')
        self.txt_result.configure(state='normal')
        self.txt_result.delete('0.0', 'end')
        self.txt_result.configure(state='disabled')


    def validate_numbers(self):


        if not self.is_float(self.ety_value1.get()):
            tkinter.messagebox.showerror('Error', 'The first value must be a valid number')
            self.ety_value1.focus()
            return False


        if not self.is_float(self.ety_value2.get()):
            tkinter.messagebox.showerror('Error', 'The second value must be a valid number')
            self.ety_value2.focus()
            return False

        return True

    @staticmethod
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False



myGui = MyGui()
