from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import *



def funktion(a):
	tabs.select(a)
	

#_________________________________Информация о гороскопе_____________________
def goroskop_():
	file=open("Ogoroskope.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box_.insert(0.0,text)
	

#_____________________________функция_овен________________________
def oven_():
	
		file=open("oven.txt", "r", encoding="utf-8-sig") #название файла
		for text in file:
			txt_box.insert(0.0,text)

#_____________________________функция_телец________________________
def telec_():
	file=open("telec.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box2.insert(0.0,text)

#_____________________________функция_близнецы________________________
def bliznece_():
	file=open("bliznece.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box3.insert(0.0,text)

#_____________________________функция_рак________________________
def rak_():
	file=open("rak.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box4.insert(0.0,text)
#_____________________________функция_лев________________________
def lev_():
	file=open("lev.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box5.insert(0.0,text)

#_____________________________функция_дева________________________
def deva_():
	file=open("deva.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box6.insert(0.0,text)

#_____________________________функция_весы________________________
def vese_():
	file=open("vese.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box7.insert(0.0,text)

#_____________________________функция_скорпион________________________
def skorpion_():
	file=open("skorpion.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box8.insert(0.0,text)

#_____________________________функция_стрелец________________________
def strelec_():
	file=open("strelec.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box9.insert(0.0,text)

#_____________________________функция_козерог________________________
def kozerog_():
	file=open("kozerog.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box10.insert(0.0,text)

#_____________________________функция_водолей________________________
def vodolei_():
	file=open("vodolei.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box11.insert(0.0,text)

#_____________________________функция_рыбы________________________
def rebe_():
	file=open("rebi.txt", "r", encoding="utf-8-sig") #название файла
	for text in file:
		txt_box12.insert(0.0,text)



#_________________________________фотографии________________
def image_car(name):
	global img
	tabs.select(0)
	img=PhotoImage(file=name).subsample(3)
	can.create_image(5,5,image=img,anchor=NW)
	




root=Tk()
root.geometry("700x300")
root.title("Гороскоп")
root.iconbitmap(r'iconocka.ico')

tabs=ttk.Notebook(root)

#_________________________________вкладки________________________
tabs=ttk.Notebook(root)
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tab5=Frame(tabs)
tab6=Frame(tabs)
tab7=Frame(tabs)
tab8=Frame(tabs)
tab9=Frame(tabs)
tab10=Frame(tabs)
tab11=Frame(tabs)
tab12=Frame(tabs)
tab13=Frame(tabs)
tab14=Frame(tabs)
tab15=Frame(tabs)
tabs.add(tab1,text="Главная")
tabs.add(tab15,text="О гороскопе")
tabs.add(tab2,text="Овен")
tabs.add(tab3,text="Телец")
tabs.add(tab4,text="Близнецы")
tabs.add(tab5,text="Рак")
tabs.add(tab6,text="Лев")
tabs.add(tab7,text="Дева")
tabs.add(tab8,text="Весы")
tabs.add(tab9,text="Скорпион")
tabs.add(tab10,text="Стрелец")
tabs.add(tab11,text="Козерог")
tabs.add(tab12,text="Водолей")
tabs.add(tab13,text="Рыбы")
tabs.pack()

#_______________________________________меню1______________________________
M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Все гороскопы",menu=m1)
m1.add_command(label="Главная", accelerator='Command+V',command=lambda:image_car("Goroskop.png"))#работает только тогда, когда выбераешь её в меню
m1.add_separator()
m1.add_command(label="Овен",command=lambda:funktion(1))
m1.add_command(label="Tелец",command=lambda:funktion(2))
m1.add_command(label="Близнецы",command=lambda:funktion(3))
m1.add_command(label="Рак",command=lambda:funktion(4))
m1.add_command(label="Лев",command=lambda:funktion(5))
m1.add_command(label="Дева",command=lambda:funktion(6))
m1.add_command(label="Весы",command=lambda:funktion(7))
m1.add_command(label="Скорпион",command=lambda:funktion(8))
m1.add_command(label="Стрелец",command=lambda:funktion(9))
m1.add_command(label="Козерог",command=lambda:funktion(10))
m1.add_command(label="Водолей",command=lambda:funktion(11))
m1.add_command(label="Рыбы",command=lambda:funktion(12))
can=Canvas(tab1,width=300,height=200)
can.pack()

#_____________________________меню_цвета______________________________
m2=Menu(M,tearoff=0)
M.add_cascade(label="Цвета",menu=m2)
m2.add_command(label="Красный",command=lambda:root.config(bg="red"))
m2.add_command(label="Оранжевый",command=lambda:root.config(bg="#FFA500"))
m2.add_command(label="Зелёный",command=lambda:root.config(bg="green"))
m2.add_command(label="Синний",command=lambda:root.config(bg="blue"))
m2.add_command(label="Светло синний",command=lambda:root.config(bg="light blue"))
m2.add_command(label="Фиолетовый", command=lambda:root.config(bg="violet"))
m2.add_command(label="Белый",command=lambda:root.config(bg="white"))

#m3=Menu(M,tearoff=0)
#M.add_cascade(label="Image",menu=m3)
#m3.add_command(label="Car",command=lambda:image_car("car.png"))
#m3.add_command(label="Car black",command=lambda:image_car("images.png"))
#m3.add_command(label="Mnogo car",command=lambda:image_car("cari.png"))

#______________________________главная______________________________
btn_open_=Button(tab15,text="Узнать о гороскопе",command=goroskop_)
txt_box_=scrolledtext.ScrolledText(tab15,width=80,height=10,bg="white")

txt_box_.grid(row=0,column=1,columnspan=3)
btn_open_.grid(row=1,column=2)

#_____________________________овен________________________
btn_open=Button(tab2,text="Узнать гороскоп на сегодня",command=oven_)

txt_box=scrolledtext.ScrolledText(tab2,width=80,height=10,bg="#FFA07A")

txt_box.grid(row=0,column=1,columnspan=3)
btn_open.grid(row=1,column=2)

#__________________________телец_______________________________
btn_open2=Button(tab3,text="Узнать гороскоп на сегодня",command=telec_)

txt_box2=scrolledtext.ScrolledText(tab3,width=80,height=10,bg="#98FB98")

txt_box2.grid(row=0,column=1,columnspan=3)
btn_open2.grid(row=1,column=2)

#__________________________близнецы_______________________________
btn_open3=Button(tab4,text="Узнать гороскоп на сегодня",command=bliznece_)

txt_box3=scrolledtext.ScrolledText(tab4,width=80,height=10,bg="#DA70D6")

txt_box3.grid(row=0,column=1,columnspan=3)
btn_open3.grid(row=1,column=2)

#__________________________рак_______________________________
btn_open4=Button(tab5,text="Узнать гороскоп на сегодня",command=rak_)

txt_box4=scrolledtext.ScrolledText(tab5,width=80,height=10,bg="#87CEFA")

txt_box4.grid(row=0,column=1,columnspan=3)
btn_open4.grid(row=1,column=2)

#__________________________лев_______________________________
btn_open5=Button(tab6,text="Узнать гороскоп на сегодня",command=lev_)

txt_box5=scrolledtext.ScrolledText(tab6,width=80,height=10,bg="#FF7F50")

txt_box5.grid(row=0,column=1,columnspan=3)
btn_open5.grid(row=1,column=2)

#__________________________дева_______________________________
btn_open6=Button(tab7,text="Узнать гороскоп на сегодня",command=deva_)

txt_box6=scrolledtext.ScrolledText(tab7,width=80,height=10,bg="#90EE90")

txt_box6.grid(row=0,column=1,columnspan=3)
btn_open6.grid(row=1,column=2)

#__________________________весы_______________________________
btn_open7=Button(tab8,text="Узнать гороскоп на сегодня",command=vese_)

txt_box7=scrolledtext.ScrolledText(tab8,width=80,height=10,bg="#D8BFD8")

txt_box7.grid(row=0,column=1,columnspan=3)
btn_open7.grid(row=1,column=2)

#__________________________скорпион_______________________________
btn_open8=Button(tab9,text="Узнать гороскоп на сегодня",command=skorpion_)

txt_box8=scrolledtext.ScrolledText(tab9,width=80,height=10,bg="#6495ED")

txt_box8.grid(row=0,column=1,columnspan=3)
btn_open8.grid(row=1,column=2)

#__________________________стрелец_______________________________
btn_open9=Button(tab10,text="Узнать гороскоп на сегодня",command=strelec_)

txt_box9=scrolledtext.ScrolledText(tab10,width=80,height=10,bg="#FFFFE0")

txt_box9.grid(row=0,column=1,columnspan=3)
btn_open9.grid(row=1,column=2)

#__________________________козерог_______________________________
btn_open10=Button(tab11,text="Узнать гороскоп на сегодня",command=kozerog_)

txt_box10=scrolledtext.ScrolledText(tab11,width=80,height=10,bg="#FAFAD2")

txt_box10.grid(row=0,column=1,columnspan=3)
btn_open10.grid(row=1,column=2)

#__________________________водолей_______________________________
btn_open11=Button(tab12,text="Узнать гороскоп на сегодня",command=vodolei_)

txt_box11=scrolledtext.ScrolledText(tab12,width=80,height=10,bg="#B0E0E6")

txt_box11.grid(row=0,column=1,columnspan=3)
btn_open11.grid(row=1,column=2)

#__________________________рыбы_______________________________
btn_open12=Button(tab13,text="Узнать гороскоп на сегодня",command=rebe_)

txt_box12=scrolledtext.ScrolledText(tab13,width=80,height=10,bg="#7FFFD4")

txt_box12.grid(row=0,column=1,columnspan=3)
btn_open12.grid(row=1,column=2)


tabs.pack(fill="both")
root.mainloop()