from tkinter import *
import sqlpage

run = sqlpage.connecting()

class stage:
    def to_register(self):
        self.register_data=[done.new_email.get(),done.new_password.get()]

        run.q1.execute('insert into employee_login(email,passwd) value(%s,%s)', self.register_data)
        run.connection.commit()

    def window(self):
        self.registerpage = Tk()
        self.registerpage.title('register page')
        self.registerpage.geometry('350x350')

        self.new_email = StringVar()
        self.new_password = StringVar()

        Label(self.registerpage, text='REGISTER PAGE').grid(row=0, column=3, columnspan=4)

        Label(self.registerpage, text='enter email').grid(row=1, column=3,sticky='E')
        Entry(self.registerpage, textvariable= self.new_email).grid(row=1, column=4, columnspan=3)

        
        Label(self.registerpage, text='enter password').grid(row=2, column=3)
        Entry(self.registerpage, textvariable= self.new_password).grid(row=2, column=4, columnspan=3)

        Button(self.registerpage, text= 'register',background='pink', command = lambda:[done.to_register(),self.registerpage.destroy()]).grid(row=3,column=6, columnspan=2)
        self.registerpage.mainloop()

        # print('try login again')

done = stage()

