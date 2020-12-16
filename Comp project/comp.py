try :
    import mysql.connector
    import tkinter as tk
    import tkinter.messagebox as box
    from tkinter import *
except:
    import mysql.connector
    import tkinter as tk
    import tkinter.messagebox as box
    from tkinter import *
    
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="user123",
  database="user"
)


mycursor = mydb.cursor()


#mycursor.execute("SHOW DATABASES")
#mycursor.execute("CREATE DATABASE user")
#mycursor.execute("CREATE TABLE login (id INTEGER(255),user_name VARCHAR(255), password VARCHAR(255))")
#sql = "INSERT INTO login (user_name, password) VALUES (%s, %s)"
#val = [
    #('Peter', '1'),
    #('Amy', '2'),
    #('Hannah', '3'),
    #('Michael', '4'),
    #('Sandy', '5'),
    #('vii', '6'),  
    #]
#mycursor.executemany(sql, val)
#mydb.commit()
#mycursor.execute("CREATE TABLE blood (id INTEGER(255),full_name VARCHAR(255), user_name VARCHAR(255), password VARCHAR(255), gender VARCHAR(255), blood_type VARCHAR(255), email_id VARCHAR(255),mobile_number INTEGER(255), age VARCHAR(255), city VARCHAR(255), pincode VARCHAR(255))")



def main():
    main = tk.Tk()
    main.geometry("1920x1080")  
    main.iconbitmap(r'logo.ico')
    
    f = tk.Canvas(bg="red", height =2190 ,width =1520)
    f.grid()
    
    pic_main_lo = tk.PhotoImage(file="blood_donorlo.PNG")
    pic_main = tk.Label(f,bg = 'red',bd = '3',image = pic_main_lo)
    pic_main.place(x=0,y = 0)
    
    main.title("WELCOME TO BLOOD DONOR")
    
    btn = tk.Button(f, text = 'Login', command = login, fg = "White" ,bg="Black", width="15")
    btn.place(x=560,y=350)
    btn = tk.Button(f, text = 'signup', command = signup, fg = "White" ,bg="Black", width="15")
    btn.place(x=700,y=350)    
    
    main.mainloop()
    

def login():
    
    def dialog1():  
        mycursor.execute("Select * from login")
        global username 
        username = e1.get()
        password = e2.get()
        flag = 0
        l = list(mycursor)
        for x in l:
          if ( (x[1] == username) & (x[2] == password)):
            flag = flag +1
            
        if (flag == 1):
            box.showinfo("info","You have been logged in")
            dashboard(username)
            top.destroy()
            
            
        else:
           box.showinfo("info","wrong try again")
           
    
    top = tk.Toplevel()
    top.title('WELCOME TO BLOOD DONOR Login page')
    top.geometry("1196x1080")
    top.iconbitmap(r'logo.ico')

    f = tk.Canvas(top,bg="red", height =2190 ,width =1200)
    f.grid()

    pic_main_sh = tk.PhotoImage(file="blood_donor.PNG")
    labpic = tk.Label (f,  bg = 'red',bd = '3', image = pic_main_sh)
    labpic.place(x=0,y = 0)

    label = tk.Label(f, text= "Login",fg = "White",bg = "red",width=15,font=("Courier", 35))
    label.place(x=400,y = 130)
    
    label1 = tk.Label(f,text = 'Username:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
    label1.place(x=300,y=200)
    e1 = tk.Entry(f)
    e1.place(x=620,y=213)

    label2 = tk.Label(f,text = 'Password:' ,fg="white",bg = 'red',width=20,font=("Bold", 25))
    label2.place(x=300,y=270)
    e2 = tk.Entry(f,show="*",width=30)
    e2.place(x=620,y=283)
    
    btn = tk.Button(f, text = 'Login',command = dialog1, fg = "White" ,bg="Black", width="15")
    btn.place(x=560,y=350)

    about =tk.Label(f,text = 'About us:' ,fg="white",bg = 'red',font=("Bold", 25))
    about1 =tk.Label(f,fg="white",bg = 'red',text = 'We help to donate blood in the most effective way through our portal and try our best to give the user a friendly and easy environment for blood donation procedures' , font=("Courier", 20),wraplength="1200")
    about.place (x=10,y=550)
    about1.place (x=10,y=600)
    about3 =tk.Label(f,text = 'You can contact us on: 9878956436(Moblie) or 080-2545674(land-line)' ,fg="white",bg = 'red',font=("Courier", 15))
    about3.place(x=10,y=710)

    top.mainloop()

    
def signup():

    def dialog2():
        mycursor.execute("Select * from login")
        global username
        fname = e1.get()
        username = e2.get()
        password = e3.get()
        flag = 0
        l = list(mycursor)
        for x in l:
          if ( (x[0] == username) and (x[1] == password)):
            flag = 1
            
          if ( (x[0] != username)and len (password)>2 ):
              flag = 2
              
          if ((len(username)<4) or (len(password)<=2)):
              flag = -1
              
          if (click.get() == 0 ):
              flag = 3
          
            
        if (flag == 1):
            box.showinfo("info","Sorry this User name and Password is taken")
            
        elif (flag == -1):
            box.showinfo("info","The length of user name must be minimum of 5 characters and the length of the password must be greater than 2 character")

        elif(flag == 3):
            box.showinfo("info","Please accept the terms and condition")
            
        elif (flag == 2):
            box.showinfo("info","Your have been registered")
            dashboard(username)
            top.destroy()            
       
        
    top = tk.Toplevel()
    top.geometry('1196x1080')
    top.iconbitmap(r'logo.ico')
    top.title('WELCOME TO BLOOD DONOR Sign up page')
    
    f=tk.Canvas(top,bg="red", height = 2190 ,width =1200)
    f.grid()
        
    pic_main_sh = tk.PhotoImage(file="blood_donor.PNG")
    labpic = tk.Label(f,bg = 'red',bd = '3',image = pic_main_sh)
    labpic.place(x=0,y = 0)
    pic_yes = tk.PhotoImage(file="yes.PNG")
    yes = tk.Label(f,bg = 'red',image = pic_yes)
    yes.place(x=800,y = 120)

    label = tk.Label(f, text="Register",fg = "White",bg = "red",width=15,font=("Courier", 35))
    label.place(x=350,y = 130)


    label1 = tk.Label(f, text="Full Name",width=20,font=("bold", 12))
    label1.place(x=300,y = 190)

    e1 = tk.Entry(f)
    e1.place(x=600,y = 190)

    label2 = tk.Label(f, text="User Name",width=20,font=("bold", 12))
    label2.place(x=300,y=230)

    e2 = tk.Entry(f)
    e2.place(x=600,y = 230)

    label3 = tk.Label(f, text="Password",width=20,font=("bold", 12))
    label3.place(x=300,y=270)

    e3 = tk.Entry(f)
    e3.place(x=600,y = 270)

    label4 = tk.Label(f,text="Gender",width=20,font=("bold", 12))
    label4.place(x=300,y = 310)
    var = IntVar()
    r = tk.Radiobutton(f, text="Male",font=("bold", 12),variable=var, value=1)
    r.place(x=600,y = 310)
    r1=Radiobutton(f, text="Female",font=("bold", 12),variable=var, value=2)
    r1.place(x=700,y = 310)

    label5 = tk.Label(f, text="Blood Type",width=20,font=("bold", 12))
    label5.place(x=300,y = 350)


    list1 = ['A Positive','A Negative','B Positive','B Negative','AB Positive','AB negative','O positive','O negative'];
    c=StringVar()
    droplist = OptionMenu(f,c, *list1)
    droplist.config(width=20)
    c.set('Select your Blood Type') 
    droplist.place(x=600,y = 350)

    label6 = tk.Label(f,text="Email id ",width=20,font=("bold", 12))
    label6.place(x=300,y = 390)
    e4 = tk.Entry(f,width = 35)
    e4.place(x=600,y = 390)

    label7 = tk.Label(f,text="Mobile Number",width=20,font=("bold", 12))
    label7.place(x=300,y = 430)
    e5 = tk.Entry(f,width = 15)
    e5.place(x=600,y = 430)

    label8 = tk.Label(f,text="Age",width=20,font=("bold", 12))
    label8.place(x=300,y = 470)
    e6 = tk.Entry(f,width = 25)
    e6.place(x=600,y = 470)

    label9 = tk.Label(f,text="City",width=20,font=("bold", 12))
    label9.place(x=300,y = 510)
    e7 = tk.Entry(f,width = 25)
    e7.place(x=600,y = 510)

    label10 = tk.Label(f,text="Pin code",width=20,font=("bold", 12))
    label10.place(x=300,y = 550)
    e8 = tk.Entry(f,width = 25)
    e8.place(x=600,y = 550)

    click = IntVar()
    c = tk.Checkbutton(f, text = "I Agree to all the terms and conditions", variable = click, \
                 offvalue = 0,onvalue = 1,activebackground= "white",
                 bg='red', width = 30,font=("bold", 12))
    
    c.place(x=480,y = 590)
    Button(f, text='Submit',command = dialog2 , width=20,bg='Black',fg='white').place(x=500,y = 640)

    
    about =tk.Label(f,text = 'About us:' ,fg="white",bg = 'red',font=("Bold", 18))
    about1 =tk.Label(f,fg="white",bg = 'red',text = 'We help to donate blood in the most effective way through our portal and try our best to give the user a friendly and easy environment for blood donation procedures' , font=("Courier", 15),wraplength="1200")
    about.place (x=30,y=700)
    about1.place (x=30,y=730)
    about3 =tk.Label(f,text = 'You can contact us on: 9878956436(Moblie) or 080-2545674(land-line)' ,fg="white",bg = 'red',font=("Courier", 15))
    about3.place(x=30,y=790)
    top.mainloop()



def dashboard(username):
    dashboard = tk.Toplevel()
    dashboard.geometry("1920x1080")  
    dashboard.iconbitmap(r'logo.ico')
    dashboard.title("DASHBOARD")
    f = tk.Canvas(dashboard,bg="red", height =2190 ,width =1520)
    f.grid()    

    pic_dash_lo = tk.PhotoImage(file="blood_donorlo.PNG")
    pic_dash = tk.Label(f,bg = 'black',bd = '3',image = pic_dash_lo)
    pic_dash.place(x=0,y = 0)

    label1 = tk.Label(f,relief="solid",bg = "red",width=187,height=5)
    label1.place(x=200,y = 120)

    label2 = tk.Label(f, text= "Welcome "+username[0:5]+" ;",fg = "White",bg = "red",width=27,font=("Courier", 16))
    label2.place(x=190,y = 150)
    
    label3 = tk.Label(f, text= "Dashboard",fg = "White",bg = "red",width=37,font=("Bold", 28))
    label3.place(x=440,y = 140)

    label4 = tk.Label(f,relief="solid",bg = "red",width=37,height=47)
    label4.place(x=0,y = 120)

    btn1 = tk.Button(f, text = 'to fill',fg = "black" ,activebackground="blue",bg="white", width=23,font=("Courier", 13))
    btn1.place(x=10,y=250)
    
    btn2 = tk.Button(f, text = 'to fill',fg = "black" ,bg="white", width=23,font=("Courier", 13))
    btn2.place(x=10,y=300)

    btn3 = tk.Button(f, text = 'to fill',fg = "black" ,bg="white", width=23,font=("Courier", 13))
    btn3.place(x=10,y=350)

    btn4 = tk.Button(f, text = 'to fill',fg = "black" ,bg="white", width=23,font=("Courier", 13))
    btn4.place(x=10,y=400)

    btn5 = tk.Button(f, text = 'to fill',fg = "black" ,bg="white", width=23,font=("Courier", 13))
    btn5.place(x=10,y=450)

    btn6 = tk.Button(f, text = 'to fill',fg = "black" ,bg="white", width=23,font=("Courier", 13))
    btn6.place(x=10,y=500)
 
    dashboard.mainloop()




    
#login()
#signup()   
    
main()
#dashboard("vii")


