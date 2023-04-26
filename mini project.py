from tkinter import *
from tkinter import messagebox as m
from PIL import ImageTk, Image
import pymysql
mydb=pymysql.Connect(host="localhost",user="root",password="Sachin@2106",database="mech")
cur=mydb.cursor()
def get():
    global w2

    w3=Toplevel(w)
    w3.geometry('1366x768')
    w3.title("Report")
    load=Image.open("bg13.jpg")
    photo=ImageTk.PhotoImage(load)
    label=Label(w3,image=photo)
    label.image=photo
    label.place(x=0,y=0)

    fr=Frame(w3,bg="white",width="1100",height="600")
    fr.place(x=140,y=60)

    Label(w3,text="Your Report is Here!",font=("Times", 20,"bold"),bg="white",fg="dodgerblue").place(x=500,y=60)

    m=e7.get()
    n=e8.get()
    o=e9.get()
    p=e91.get()
    q=e92.get()
    r=e93.get()
    
    Label(w3,text="STUDENT NAME :",font=("Times", 20),bg="white",fg="black").place(x=160,y=120)
    Label(w3,text=m,font=("Times", 20,"bold"),bg="white",fg="black").place(x=390,y=120)
    Label(w3,text="CLASS :",font=("Times", 20),bg="white",fg="black").place(x=280,y=180)
    Label(w3,text=n,font=("Times", 20,"bold"),bg="white",fg="black").place(x=390,y=180)
    Label(w3,text="D-O-B :",font=("Times", 20),bg="white",fg="black").place(x=290,y=240)
    Label(w3,text=o,font=("Times", 20,"bold"),bg="white",fg="black").place(x=390,y=240)
    Label(w3,text="MOB-NO :",font=("Times", 20),bg="white",fg="black").place(x=255,y=300)
    Label(w3,text=p,font=("Times", 20,"bold"),bg="white",fg="black").place(x=390,y=300)
    Label(w3,text="REG-NO :",font=("Times", 20),bg="white",fg="black").place(x=260,y=360)
    Label(w3,text=q,font=("Times", 20,"bold"),bg="white",fg="black").place(x=390,y=360)
    Label(w3,text="ADDRESS :",font=("Times", 20),bg="white",fg="black").place(x=240,y=420)
    Label(w3,text=r,font=("Times", 20,"bold"),bg="white",fg="black").place(x=390,y=420)

    Label(w3,text="TAMIL :",font=("Times", 20),bg="white",fg="black").place(x=833,y=120)
    Label(w3,text="ENGLISH :",font=("Times", 20),bg="white",fg="black").place(x=803,y=200)
    Label(w3,text="MATHS :",font=("Times", 20),bg="white",fg="black").place(x=820,y=280)
    Label(w3,text="SCIENCE  :",font=("Times", 20),bg="white",fg="black").place(x=795,y=360)
    Label(w3,text="SOCIAL SCIENCE :",font=("Times", 20),bg="white",fg="black").place(x=700,y=440)
    Label(w3,text="Total Mark",font=("Constantia", 20,"bold"),bg="white",fg="black").place(x=950,y=80)
    Label(w3,text="Grade",font=("Constantia", 20,"bold"),bg="white",fg="black").place(x=1120,y=80)

    
    s1=int(e10.get())
    s2=int(e11.get())
    s3=int(e12.get())
    s4=int(e13.get())
    s5=int(e14.get())
    s6=int(e15.get())
    s7=int(e16.get())
    s8=int(e17.get())
    s9=int(e18.get())
    s10=int(e19.get())

    s11=int(s1+s6)
    s12=int(s2+s7)
    s13=int(s3+s8)
    s14=int(s4+s9)
    s15=int(s5+s10)
    
    Label(w3,text=s11,font=("Times",20,"bold"),bg="white",fg="black").place(x=1010,y=120)
    Label(w3,text=s12,font=("Times",20,"bold"),bg="white",fg="black").place(x=1010,y=200)
    Label(w3,text=s13,font=("Times",20,"bold"),bg="white",fg="black").place(x=1010,y=280)
    Label(w3,text=s14,font=("Times",20,"bold"),bg="white",fg="black").place(x=1010,y=360)
    Label(w3,text=s15,font=("Times",20,"bold"),bg="white",fg="black").place(x=1010,y=440)

    if s11>=90:
        Label(w3,text="O",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=120)
    elif s11>=80:
        Label(w3,text="A+",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=120)
    elif s11>=70:
        Label(w3,text="A",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=120)
    elif s11>=60:
        Label(w3,text="B",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=120)
    elif s11>=50:
        Label(w3,text="C",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=120)
    elif s11>=35:
        Label(w3,text="D",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=120)
    else:
        Label(w3,text="U",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=120)

    if s12>=90:
        Label(w3,text="O",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=200)
    elif s12>=80:
        Label(w3,text="A+",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=200)
    elif s12>=70:
        Label(w3,text="A",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=200)
    elif s12>=60:
        Label(w3,text="B",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=200)
    elif s12>=50:
        Label(w3,text="C",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=200)
    elif s12>=35:
        Label(w3,text="D",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=200)
    else:
        Label(w3,text="U",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=200)

    if s13>=90:
        Label(w3,text="O",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=280)
    elif s13>=80:
        Label(w3,text="A+",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=280)
    elif s13>=70:
        Label(w3,text="A",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=280)
    elif s13>=60:
        Label(w3,text="B",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=280)
    elif s13>=50:
        Label(w3,text="C",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=280)
    elif s13>=35:
        Label(w3,text="D",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=280)
    else:
        Label(w3,text="U",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=280)

    if s14>=90:
        Label(w3,text="O",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=360)
    elif s14>=80:
        Label(w3,text="A+",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=360)
    elif s14>=70:
        Label(w3,text="A",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=360)
    elif s14>=60:
        Label(w3,text="B",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=360)
    elif s14>=50:
        Label(w3,text="C",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=360)
    elif s14>=35:
        Label(w3,text="D",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=360)
    else:
        Label(w3,text="U",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=360)

    if s15>=90:
        Label(w3,text="O",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=440)
    elif s15>=80:
        Label(w3,text="A+",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=440)
    elif s15>=70:
        Label(w3,text="A",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=440)
    elif s15>=60:
        Label(w3,text="B",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=440)
    elif s15>=50:
        Label(w3,text="C",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=440)
    elif s15>=35:
        Label(w3,text="D",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=440)
    else:
        Label(w3,text="U",font=("Times",20,"bold"),bg="white",fg="black").place(x=1150,y=440)

    total=(s11+s12+s13+s14+s15)
    avg=(total/5)
    Label(w3,text="The Total Marks is  -",font=("Times",20,"bold"),bg="white",fg="black").place(x=470,y=500)
    Label(w3,text=total,font=("Times",20,"bold"),bg="white",fg="black").place(x=765,y=500)
    Label(w3,text="The Overall Average is -",font=("Times",20,"bold"),bg="white",fg="black").place(x=470,y=540)
    Label(w3,text=avg,font=("Times",20,"bold"),bg="white",fg="black").place(x=765,y=540)
    Label(w3,text="%",font=("Times",20,"bold"),bg="white",fg="black").place(x=820,y=540)
    Label(w3,text="The Total Grade is -",font=("Times",20,"bold"),bg="white",fg="black").place(x=470,y=580)
    if total>=450:
        Label(w3,text="A+",font=("Times",20,"bold"),bg="white",fg="black").place(x=765,y=580)
    elif total>=400:
        Label(w3,text="A",font=("Times",20,"bold"),bg="white",fg="black").place(x=765,y=580)
    elif total>=350:
        Label(w3,text="B+",font=("Times",20,"bold"),bg="white",fg="black").place(x=765,y=580)
    elif total>=300:
        Label(w3,text="B",font=("Times",20,"bold"),bg="white",fg="black").place(x=765,y=580)
    elif total>=250:
        Label(w3,text="C",font=("Times",20,"bold"),bg="white",fg="black").place(x=765,y=580)
    elif total>=200:
        Label(w3,text="D",font=("Times",20,"bold"),bg="white",fg="black").place(x=765,y=580)
    else:
        Label(w3,text="FAIL",font=("Times",20,"bold"),bg="white",fg="black").place(x=765,y=580)    

class final():
    def welcome():
        global w2
        w2=Toplevel(w)
        w2.geometry('1366x768')
        
        load=Image.open("bg9.jpg")
        photo=ImageTk.PhotoImage(load)
        label=Label(w2,image=photo)
        label.image=photo
        label.place(x=0,y=0)
        
    
        w2.title('Welcome')

        global e7
        global e8
        global e9
        global e91
        global e92
        global e93
        global name
        global clas
        global mob
        global reg
        global reg
        global add
       
        
        global e10
        global e11
        global e12
        global e13
        global e14
        global e15
        global e16
        global e17
        global e18
        global e19

        name=StringVar()
        clas=StringVar()
        dob=StringVar()
        mob=StringVar()
        reg=StringVar()
        add=StringVar()


        
        Label(w2,text="Sucessfully Login!",font="Algerian 20",fg="white",bg="black").place(x=320,y=40)
        Label(w2,text="Enter Stutent Details below  :",font="Times 20",bg="black",fg="white").place(x=480,y=80)
        Label(w2,text="Name  :",font="Georgia 20",bg="black",fg="white").place(x=550,y=120)
        e7=Entry(w2,width=30,textvariable=name)
        e7.place(x=680,y=130)
        Label(w2,text="Class  :",font="Georgia 20",bg="black",fg="white").place(x=870,y=120)
        e8=Entry(w2,width=30,textvariable=clas)
        e8.place(x=990,y=130)
        Label(w2,text="D-O-B  :",font="Georgia 20",bg="black",fg="white").place(x=550,y=160)
        e9=Entry(w2,width=30,textvariable=dob)
        e9.place(x=680,y=170)
        Label(w2,text="Mob-No:",font="Georgia 20",bg="black",fg="white").place(x=870,y=160)
        e91=Entry(w2,width=30,textvariable=mob)
        e91.place(x=990,y=170)
        Label(w2,text="Reg.No  :",font="Georgia 20",bg="black",fg="white").place(x=550,y=200)
        e92=Entry(w2,width=30,textvariable=reg)
        e92.place(x=680,y=210)
        Label(w2,text="Address :",font="Georgia 20",bg="black",fg="white").place(x=870,y=200)
        e93=Entry(w2,width=30,textvariable=add)
        e93.place(x=990,y=210)
        
        Label(w2,text="Enter Mark Details below  :",font="Georgia 20",bg="black",fg="white").place(x=480,y=240)
        fr=Frame(w2,bg="#040405",width="820",height="370")
        fr.place(x=500,y=330)
        Label(w2,text="Subjects",font=("yu gothic ui", 20, "bold"),bg="black",fg="white").place(x=500,y=300)
        Label(w2,text="Tamil",font=("yu gothic ui", 17, "bold"),bg="black",fg="white").place(x=500,y=380)
        Label(w2,text="English",font=("yu gothic ui", 17, "bold"),bg="black",fg="white").place(x=500,y=430)
        Label(w2,text="Maths",font=("yu gothic ui", 17, "bold"),bg="black",fg="white").place(x=500,y=480)
        Label(w2,text="Science",font=("yu gothic ui", 17, "bold"),bg="black",fg="white").place(x=500,y=530)
        Label(w2,text="Social Science",font=("yu gothic ui", 17, "bold"),bg="black",fg="white").place(x=500,y=580)
        Label(w2,text="Theory Marks",font=("yu gothic ui", 18, "bold"),bg="black",fg="white").place(x=800,y=300)
        Label(w2,text="Practical Marks",font=("yu gothic ui", 18, "bold"),bg="black",fg="white").place(x=1050,y=300)
        
        e10=Entry(w2,width=5)
        e10.place(x=870,y=390)
        e11=Entry(w2,width=5)
        e11.place(x=870,y=440)
        e12=Entry(w2,width=5)
        e12.place(x=870,y=490)
        e13=Entry(w2,width=5)
        e13.place(x=870,y=540)
        e14=Entry(w2,width=5)
        e14.place(x=870,y=590)
        
        e15=Entry(w2,width=5)
        e15.place(x=1120,y=390)
        e16=Entry(w2,width=5)
        e16.place(x=1120,y=440)
        e17=Entry(w2,width=5)
        e17.place(x=1120,y=490)
        e18=Entry(w2,width=5)
        e18.place(x=1120,y=540)
        e19=Entry(w2,width=5)
        e19.place(x=1120,y=590)
        
        Button(w2,text="Report Generate",font="Times 25",width=15,height=1,bg="black",fg='white',command=get).place(x=870,y=620)
        
        
def register():
    Label(w,text="Register Sucessfully!",font="Elephant 15",bg="#040405",fg="white").place(x=750,y=635)

def verify():
    global c
    global d
    
    c=e5.get()
    d=e6.get()
    '''
    if a==c and b==d:
        final.welcome()  
    else:
       m.showerror("Warning","Incorrect id/password")
    '''
    query="select * from login_details"
    cur.execute(query)
    for i in cur:
            if i[0]==c and i[1]==d:
                    print(i[0])
                    print(i[1])
                    final.welcome()
                    break
            else:
                m.showerror("warning","incorrect username/password")

    

def Login():
    global w1
    w1=Toplevel(w)
    w1.geometry('1366x768')
    w1.title('Login')
    load=Image.open("bg2.png")
    photo=ImageTk.PhotoImage(load)
    label=Label(w1,image=photo)
    label.image=photo
    label.place(x=0,y=0)


    fr=Frame(w1,bg="black",width="400",height="600")
    fr.place(x=470,y=70)

    load=Image.open("hyy.png")
    photo=ImageTk.PhotoImage(load)
    label=Label(w1,image=photo,bg='#040405')
    label.image=photo
    label.place(x=590,y=80)

    
    var=IntVar()
    chk=Checkbutton(w1,text = "Remember me?",font=("yu gothic ui", 14, "bold"),bg="#040405",fg="white",variable=var)
    chk.place(x=480,y=380)



    global e5
    global e6
    global a
    global b

    a=e2.get()
    b=e4.get()
    query="insert into login_details values(%s,%s)"
    values=[a,b]
    cur.execute(query,values)
    mydb.commit()
    
    
    
    Label(w1,text="LOGIN",font=("yu gothic ui", 17, "bold"),fg="white",bg='black').place(x=625,y=190)
    Label(w1,text="Staff-ID  :",font=("yu gothic ui", 17, "bold"),bg="black",fg="white").place(x=480,y=240)
    e5=Entry(w1,width=40)
    e5.place(x=600,y=250)
    Label(w1,text="Password :",font=("yu gothic ui", 17, "bold"),bg="black",fg="white").place(x=480,y=330)
    e6=Entry(w1,width=40,show="*")
    e6.place(x=600,y=340)
    Label(w1,text="----------------OR----------------",font=("yu gothic ui", 17, "bold"),bg="black",fg="white").place(x=500,y=530)
    Label(w1,text="Dont't have an account?",font=("yu gothic ui", 17, "bold"),bg="black",fg="white").place(x=500,y=580)
    Button(w1,text="Sign Up",font=("yu gothic ui", 17, "bold"),bg="black",fg="orange",relief=FLAT,command=w1.destroy).place(x=755,y=570)
    Button(w1,text="Login",font="Times 25",width=15,height=1,bg="white",fg='black',activebackground="pink",command=verify).place(x=530,y=430)


def signup():
    global w
    w=Tk()
    w.title('signup')
    w.geometry('1366x768')
    load=Image.open("bg2.png")
    photo=ImageTk.PhotoImage(load)
    label=Label(w,image=photo)
    label.image=photo
    label.place(x=0,y=0)
        
        

    fr=Frame(w,bg="#040405",width="950",height="600")
    fr.place(x=200,y=70)

    load=Image.open("s6.png")
    photo=ImageTk.PhotoImage(load)
    label=Label(w,image=photo,bg='#040405')
    label.image=photo
    label.place(x=200,y=150)

    load=Image.open("hyy.png")
    photo=ImageTk.PhotoImage(load)
    label=Label(w,image=photo,bg='#040405')
    label.image=photo
    label.place(x=820,y=80)

    global e2
    global e4
    
    #staff=StringVar()
    #pswd=StringVar()


    var=IntVar()
    chk=Checkbutton(w,text ="Accept all terms and Conditions",variable=var,onvalue=1,offvalue=0)
    chk.place(x=720,y=530)
    chk.config(font="Times 20")
    chk.config(fg="white")
    chk.config(bg="black")


    Label(w,text="Welcome!",font="Algerian 30",bg="#040405",fg="white").place(x=320,y=100)
    Label(w,text="SIGN UP",bg="#040405",fg="white",font=("yu gothic ui", 17, "bold")).place(x=840,y=190)
    Label(w,text="Name      :",font="Times 20",bg="#040405",fg="white").place(x=720,y=240)
    e1=Entry(w,width=25).place(x=840,y=250)
    Label(w,text="Staff-ID   :",font="Times 20",bg="#040405",fg="white").place(x=720,y=300)
    e2=Entry(w,width=25)
    e2.place(x=840,y=310)
    Label(w,text="Mob-No  :",font="Times 20",bg="#040405",fg="white").place(x=720,y=360)
    e3=Entry(w,width=25).place(x=840,y=370)
    Label(w,text="Email-ID :",font="Times 20",bg="#040405",fg="white").place(x=720,y=420)
    e4=Entry(w,width=25).place(x=840,y=430)
    Label(w,text="Password :",font="Times 20",bg="#040405",fg="white").place(x=720,y=480)
    e4=Entry(w,width=25,show="*")
    e4.place(x=840,y=490)
    Button(w,text="Signup",font="Times 20",bg="white",fg='black',relief=FLAT,activebackground="pink",command=Login).place(x=880,y=580)
    Button(w,text="Register",font="Times 20",bg="white",fg='black',activebackground="pink",command=register).place(x=730,y=580)
signup()
