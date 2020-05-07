from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import temp_db as db


class RegWindow:

    """==============================================================================================================
       =================================||| REGISTRATION WINDOW INITIALISATION|||====================================
       =============================================================================================================="""
    def __init__(self, master):
        self.master = master
        self.master.title('To be decided')
        self.master.geometry('800x780')
        self.master.resizable(0, 0)
        # '''  ------ Entry Field Variable Declaration ------  '''
        self.fn = StringVar()
        self.ln = StringVar()
        self.mob_num = IntVar()
        self.dis = StringVar()
        self.village = StringVar()
        self.block = StringVar()

        """=============================================================================================================
        ===================================||| HEADER LABEL DECLARATION |||=============================================
        ============================================================================================================="""
        label_title = Label(self.master, text='REGISTRATION', font=('corbel', 16, 'bold'), relief='solid', bg='red',
                            bd=5, fg='white')
        label_title.pack(fill=BOTH, pady=2, padx=2)

        lst_gender = ['Select', 'Male', 'Female']
        lst_cat = ['Select', 'General', 'OBC', 'SC', 'ST']

        '''=============================================================================================================
        ========================================||| REGISTRATION WINDOW |||=============================================
        ============================================================================================================='''

        '''  ======================================||| Profile Image Positioning |||================================ '''
        self.profile_img = ImageTk.PhotoImage(Image.open('index.png'))
        Label(self.master, image=self.profile_img).pack()

        '''  ==================================||| Entry Field First Name  |||=====================================  '''
        label_first_name = Label(self.master, text='First Name', font=('corbel', 16))
        label_first_name.place(x=200, y=300)
        Entry(self.master, textvar=self.fn).place(x=400, y=305)

        '''  ==================================||| Entry Field Last Name  |||======================================  '''
        Label(self.master, text='Last Name', font=('corbel', 16)).place(x=200, y=350)
        Entry(self.master, textvar=self.ln).place(x=400, y=355)

        '''  ==================================||| Dropdown Gender |||=============================================  '''
        self.gen_select = StringVar()
        Label(self.master, text='Gender', font=('corbel', 16)).place(x=200, y=400)
        input_ge = ttk.Combobox(self.master, textvar=self.gen_select, state='readonly')
        input_ge['values'] = lst_gender
        input_ge.set('Gender')
        input_ge.place(x=400, y=405)

        '''  ==================================||| Category Dropdown |||===========================================  '''
        self.cat_select = StringVar()
        Label(self.master, text='Category', font=('corbel', 16)).place(x=200, y=450)
        input_cat = ttk.Combobox(self.master, textvar=self.cat_select, state='readonly')
        input_cat['values'] = lst_cat
        input_cat.set('Category')
        input_cat.place(x=400, y=455)

        '''  ==================================||| Entry Field Mobile Number |||===================================  '''
        Label(self.master, text='Mobile Number', font=('corbel', 16)).place(x=200, y=500)
        Entry(self.master, textvar=self.mob_num).place(x=400, y=505)
        self.mob_num.set('')

        '''  ==================================||| Entry Field District |||========================================  '''
        Label(self.master, text='District*', font=('corbel', 16)).place(x=200, y=550)
        Entry(self.master, textvar=self.dis).place(x=400, y=555)

        '''  ==================================||| Entry Field Village |||=========================================  '''
        Label(self.master, text='Village', font=('corbel', 16)).place(x=200, y=600)
        Entry(self.master, textvar=self.village).place(x=400, y=605)

        '''  ==================================||| Entry Field Block |||===========================================  '''
        Label(self.master, text='Block', font=('corbel', 16)).place(x=200, y=650)
        Entry(self.master, textvar=self.block).place(x=400, y=655)

        '''  ==================================||| Submit Button Initialisation |||================================  '''
        btn_submit = Button(self.master, text='Submit', fg='white', bg='red', width='7', relief=RAISED,
                            font=('corbel', 14, 'bold'),
                            command=self.submit_information)
        btn_submit.place(x=250, y=710)

        '''  ================================||| Reset Button Initialisation |||=================================  '''
        btn_reset = Button(self.master, text='Reset', fg='white', bg='red', width='7', relief=RAISED,
                           font=('corbel', 14, 'bold'),
                           command=self.reset)
        btn_reset.place(x=370, y=710)

        '''  ================================||| Exit Button Initialisation |||==================================  '''
        btn_exit = Button(self.master, text='Quit', fg='white', bg='red', width='7', relief=RAISED,
                          font=('corbel', 14, 'bold'),
                          command=self.exit_window)
        btn_exit.place(x=490, y=710)

    '''=================================================================================================================
       ===================================||| SUBMIT BUTTON FUNCTIONALITY |||===========================================
       =============================================================================================================='''

    def submit_information(self):
        if self.blank_check():
            self.reset()
        elif len(str(self.mob_num.get())) < 10 or str(self.mob_num.get()) == '':
            messagebox.showerror('Error', 'Incorrect Mobile Number...')
            self.mob_num.set('')
        else:
            db.insert(self.fn.get() + ' ' + self.ln.get(), self.gen_select.get(), self.cat_select.get(), self.mob_num.get(), self.dis.get(),
                      self.village.get(), self.block.get())
            messagebox.showinfo('Success', 'Information saved Successfully')
            self.reset()

    '''=================================================================================================================
       ==============================================||| EXIT WINDOW |||================================================
       =============================================================================================================='''

    def exit_window(self):
        message = messagebox.askyesno('Quit', 'Are you sure, you want to Quit?')
        if message:
            exit()

    '''=================================================================================================================
       =========================================||| CHECK FOR BLANK FIELDS |||==========================================
       =============================================================================================================='''

    def blank_check(self):
        if self.fn.get() == '' or self.ln.get() == '' or self.gen_select.get() == 'Gender' or \
                self.cat_select.get() == 'Category' or self.dis.get() == '' or self.village.get() == '' or \
                self.block.get() == '':
            messagebox.showerror('Blank Fields', 'Please Enter the required information')
            return True

    '''=================================================================================================================
       =====================================||| RESET BUTTON FUNCTIONALITY |||==========================================
       =============================================================================================================='''

    def reset(self):
        self.fn.set('')
        self.ln.set('')
        self.gen_select.set('Gender')
        self.cat_select.set('Category')
        self.mob_num.set('')
        self.dis.set('')
        self.village.set('')
        self.block.set('')


'''==================================================================================================================
   =============================================||| LOGIN WINDOW |||=================================================
   =================================================================================================================='''


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry('700x600')
        self.master.resizable(0, 0)

        self.username = StringVar()
        self.password = StringVar()
        """=============================================================================================================
        =======================================||| HEADER LABEL DECLARATION |||=========================================
        ============================================================================================================="""
        label_title = Label(self.master, text='LOGIN', font=('corbel', 16, 'bold'), relief='solid', bg='red',
                            bd=5, fg='white')
        label_title.pack(fill=BOTH, pady=2, padx=2)

        self.profile_img = ImageTk.PhotoImage(Image.open('index.png'))
        Label(self.master, image=self.profile_img).pack()

        '''  ==================================||| Entry Field Username |||========================================  '''
        Label(self.master, text='Username', font=('corbel', 15)).place(x=200, y=250)
        Entry(self.master, textvar=self.username, bd=3).place(x=350, y=255)

        '''  ==================================||| Entry Field Password |||========================================  '''
        Label(self.master, text='Password', font=('corbel', 15)).place(x=200, y=300)
        Entry(self.master, textvar=self.password, bd=3).place(x=350, y=305)

        '''  =================================||| Login Button Initialisation |||==================================  '''
        btn_login = Button(self.master, text='Login', fg='white', bg='red', width='7', relief=RAISED,
                           font=('corbel', 16, 'bold'),
                           command=self.auth)
        btn_login.place(x=220, y=380)

        '''  =============================||| Registration Button Initialisation |||===============================  '''
        btn_registration = Button(self.master, text='Registration', fg='white', bg='red', width='10', relief=RAISED,
                                  font=('corbel',
                                        16, 'bold'), command=self.reg_window)
        btn_registration.place(x=350, y=380)

    def reg_window(self):
        reg = Toplevel()
        RegWindow(reg)

    def auth(self):
        if self.username.get() == 'anurag' and self.password.get() == '12345':
            messagebox.showinfo('Success', 'Login Successful')
        else:
            messagebox.showerror('Invalid User', 'Wrong Credential')
            self.username.set('')
            self.password.set('')


root = Tk()
app = LoginWindow(root)
root.mainloop()
