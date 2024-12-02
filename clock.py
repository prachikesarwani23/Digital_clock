from tkinter import *
import datetime

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime("%I")
    mi=time.strftime("%M")
    sec=time.strftime("%S")
    am=time.strftime("%p")

    date=time.strftime("%d")
    month=time.strftime("%m")
    year=time.strftime("%y")
    day=time.strftime("%a")

    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_hr.after(200,date_time)





clk=Tk()
clk.title("  ***********Digital Clock***********")
clk.geometry("1000x500")
clk.config(bg="black")

#time

lab_frame=Label(clk,text="Digital Clock",font=("Time New Roman",23,"bold"),bg="black",fg="light blue")
lab_frame.place(x=380,y=1,height=50,width=300)

lab_hr=Label(clk,text="00",font=("Time New Roman",50,"bold"),bg="white",fg="black")
lab_hr.place(x=120,y=40,height=110,width=100)
lab_hr_txt=Label(clk,text="Hour",font=("Time New Roman",25,"bold"),bg="black",fg="white")
lab_hr_txt.place(x=115,y=190,height=30,width=100)
lab_hr_sign=Label(clk,text=":",font=("Time New Roman",35,"bold"),bg="black",fg="white")
lab_hr_sign.place(x=230,y=80,height=30,width=100)


lab_min=Label(clk,text="00",font=("Time New Roman",50,"bold"),bg="white",fg="black")
lab_min.place(x=340,y=40,height=110,width=100)
lab_min_txt=Label(clk,text="Min.",font=("Time New Roman",25,"bold"),bg="black",fg="white")
lab_min_txt.place(x=330,y=150,height=110,width=100)
lab_min_sign=Label(clk,text=":",font=("Time New Roman",35,"bold"),bg="black",fg="white")
lab_min_sign.place(x=450,y=80,height=30,width=100)


lab_sec=Label(clk,text="00",font=("Time New Roman",50,"bold"),bg="white",fg="black")
lab_sec.place(x=560,y=40,height=110,width=100)
lab_sec_txt=Label(clk,text="Sec.",font=("Time New Roman",25,"bold"),bg="black",fg="white")
lab_sec_txt.place(x=550,y=150,height=110,width=100)
lab_sec_sign=Label(clk,text=":",font=("Time New Roman",35,"bold"),bg="black",fg="white")
lab_sec_sign.place(x=670,y=80,height=30,width=100)



lab_am=Label(clk,text="00",font=("Time New Roman",50,"bold"),bg="white",fg="black")
lab_am.place(x=780,y=40,height=110,width=100)
lab_am_txt=Label(clk,text="AM/PM",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_am_txt.place(x=780,y=150,height=110,width=100)


#date
lab_date=Label(clk,text="00",font=("Time New Roman",50,"bold"),bg="white",fg="black")
lab_date.place(x=120,y=300,height=110,width=100)
lab_date_txt=Label(clk,text="Date",font=("Time New Roman",25,"bold"),bg="black",fg="white")
lab_date_txt.place(x=115,y=450,height=30,width=100)
lab_date_sign=Label(clk,text=":",font=("Time New Roman",35,"bold"),bg="black",fg="white")
lab_date_sign.place(x=230,y=330,height=30,width=100)

lab_mon=Label(clk,text="00",font=("Time New Roman",50,"bold"),bg="white",fg="black")
lab_mon.place(x=336,y=300,height=110,width=100)
lab_mon_txt=Label(clk,text="Month",font=("Time New Roman",25,"bold"),bg="black",fg="white")
lab_mon_txt.place(x=330,y=410,height=110,width=100)
lab_mon_sign=Label(clk,text=":",font=("Time New Roman",35,"bold"),bg="black",fg="white")
lab_mon_sign.place(x=450,y=330,height=30,width=100)

lab_year=Label(clk,text="00",font=("Time New Roman",50,"bold"),bg="white",fg="black")
lab_year.place(x=557,y=300,height=110,width=100)
lab_year_txt=Label(clk,text="Year",font=("Time New Roman",25,"bold"),bg="black",fg="white")
lab_year_txt.place(x=550,y=410,height=110,width=100)
lab_year_sign=Label(clk,text=":",font=("Time New Roman",35,"bold"),bg="black",fg="white")
lab_year_sign.place(x=670,y=330,height=30,width=100)

lab_day=Label(clk,text="00",font=("Time New Roman",50,"bold"),bg="white",fg="black")
lab_day.place(x=780,y=300,height=110,width=100)
lab_day_txt=Label(clk,text="Day",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_day_txt.place(x=780,y=412,height=110,width=100)




date_time()
clk.mainloop()