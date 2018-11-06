from tkinter import *
from algo import *

#creating main window
root=Tk()
root.title("Distances")
width=1000
height=700
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x= screen_width/2- width/2
y= screen_height/2-height/2
root.geometry("%dx%d+%d+%d" % (width,height,x,y))

#labels
l1=Label(root, text="choose start point")
l1.place(x=100,y=100)
l2=Label(root, text="choose end point")
l2.place(x=300,y=100)
l3=Label(root, text="DAA Project", font=" 40,Bold")
l3.place(x=200,y=35)
l4= Label(root,text="Enter time")
l4.place(x=100,y=200)
l5=Label(root,text=":")
l5.place(x=210,y=200)
l6=Label(root,text="Sortest Path: ")
l6.place(x=60,y=350)
l7=Label(root,text="Distance: ")
l7.place(x=60,y=370)
l8=Label(root,text="Time: ")
l8.place(x=60,y=390)

#dropdown menu
start_var= StringVar(root)
end_var=StringVar(root)
time_var=StringVar(root)

#initializing dictionaries
places= {"amer fort":1,
         "city palace":2,
         "nahargarh fort":3,
         "bapu bazaar":4,
         "hawa mahal":5,
         "jantar mantar":6,
         "jal mahal":7,
         "albert hall museum":8,
         "jaigarh fort":9,
         "chokhi dhani":10,
         "rajmandir cinema":11,
         "birla mandir":12,
         "rambagh palace":13,
         "central park":14}
speed_factor={"00":10,
              "1":10,
              "2":10,
              "3":10,
              "4":10,
              "5":10,
              "6":20,
              "7":20,
              "8":10,
              "9":10,
              "10":10,
              "11":10,
              "12":10,
              "13":5,
              "14":5,
              "15":5,
              "16":3,
              "17":3,
              "18":-3,
              "19":-3,
              "20":-5,
              "21":-5,
              "22":20,
              "23":20}
start_drop = OptionMenu(root,start_var, *places)
start_drop.place(x=100,y=130)
end_drop = OptionMenu(root,end_var, *places)
end_drop.place(x=300,y=130)

#entries
e1=Entry(root,width=2)
e1.place(x=190,y=200)
e2=Entry(root,width=2)
e2.place(x=215,y=200)

#setvar function

def set_var():

    start=start_var.get()
    end=end_var.get()
    hour=e1.get()
    minute=e2.get()
    start_ver=places.get(start)
    start_ver=start_ver-1
    end_ver=places.get(end)
    end_ver=end_ver-1
    h=speed_factor.get(hour)
    solution,distancegraph,t=generate_timegraph(start_ver,end_ver,h)

    sum=0
    for i in range(len(solution)-1):
        sum=sum+(distancegraph[int(solution[i])][int(solution[i+1])])
    keyss = list(places.keys())
    sol=[]
    for i in range(len(solution)):
        sol.append(keyss[int(solution[i])])



    t=t*60

    t = float("{0:.2f}".format(t))
    path_text= Text(root,height=1,width=120)
    for i in range(len(sol)):
        path_text.insert(END,sol[i]+"-->","-->")

    path_text.place(x=150,y=350)
    l9=Label(root,text=sum)
    l9.place(x=130,y=370)
    l10=Label(root,text=t)
    l10.place(x=130,y=390)
    l11=Label(root,text="km")
    l11.place(x=180,y=370)
    l12=Label(root,text="minutes")
    l12.place(x=180,y=390)

         #buttons
b1=Button(root,text="Go",command=set_var)
b1.place(x=215,y=250)

root.mainloop()
