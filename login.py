# program to permit registered users login into a system
#create a database and a table - 'employee_login'  
'''run the program'''
#now table will hold details of already registered emails
'''comments the lines 11-14 and run the program further however many times needed'''



import sqlpage
run = sqlpage.connecting()


run.q1.execute('create table employee_login(email varchar(50), passwd varchar(50))')
data = [('abc@gmail.com','abc123'),('def@gmail.com','def456'),('ghi@gmail.com','ghi789')]
run.q1.executemany("insert into employee_login(email,passwd) values(%s,%s)",data)
run.connection.commit()


class process1:
    def first(self):
        self.login = email.get()
        self.pwd = password.get()

    def ex(self):    
        run.q1.execute(f'select * from employee_login where email="{obj1.login}" ')
        self.choose = run.q1.fetchone()

    def done(self):   
        if obj1.choose != None:
            if obj1.pwd == obj1.choose[1]:
                print('login successfull')
            else:
                print('wrong password')
        else:
            print('no account registered')
            print('do you want to register?')
            x=input('yes/no??\n').lower()

            if x == 'yes':
                import registering
                registering.done.window()
                print('registered')
                exit()

        run.q1.execute('drop table employee_login')    
        exit()

obj1 = process1()


from tkinter import *

loginpage = Tk()
loginpage.title('login page')
loginpage.geometry('350x200')

email = StringVar()
password = StringVar()

Label(loginpage, text='LOGIN PAGE').grid(row=0, column=3, columnspan=4)

Label(loginpage, text='enter email').grid(row=1, column=3,sticky='E')
Entry(loginpage, textvariable= email).grid(row=1, column=4, columnspan=3)

Label(loginpage, text='enter password').grid(row=2, column=3)
Entry(loginpage, textvariable= password).grid(row=2, column=4, columnspan=3)

def work():
    obj1.first()
    obj1.ex()
    obj1.done()

Button(loginpage, text= 'proceed', command=lambda:[loginpage.destroy(),work()], background='lightblue').grid(row=3,column=6, columnspan=2)

loginpage.mainloop()