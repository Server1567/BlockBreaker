#!/usr/bin/env python
# -*- coding: utf-8 -*-
# .place(x=5, y=10)
from Tkinter import *

# ----- Almacenamiento de datos | START -------------------------

box1 = ""

# ----- Almacenamiento de datos | START -------------------------

# ---------- Funciones Operacionales | START --------------------

def add1():
	one = "1"
	for i in box1:
		box1 += one
		print box1
		
def add2():
	two = "2"

def add3():
	three = "3"

def add4():
	four = "4"

def add5():
	five = "5"

def add6():
	six = "6"

def add7():
	seven = "7"

def add8():
	eight = "8"

def add9():
	nine = "9"

def add0():
	zero = "0"

def addPunto():
	point = "."

def addPI():
	PI = "3.14"


# ---------- Funciones Operacionales | END --------------------

# ______________________ ÁREA DE LÓGICA _______________________


# Método para añadir números a las variables de almacenamiento
# Al presionar una operación se guarda la primera variable y comienza la segunda
# Al presionar Igualdad(=) guarda la segunda variable y muestra el resultado de la operación

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("233x315")

canvas = Canvas(ventana, bg="white", width=233, height=50)
canvas.place(x=0, y=0)


# Botones numericos

btn1 = Button(ventana, text="1", width=6, height=3, command=add1).place(x= 0, y=95)
btn2 = Button(ventana, text="2", width=6, height=3, command=add2).place(x= 51, y=95)
btn3 = Button(ventana, text="3", width=6, height=3, command=add3).place(x= 102, y=95)
btn4 = Button(ventana, text="4", width=6, height=3, command=add4).place(x= 0, y=150)
btn5 = Button(ventana, text="5", width=6, height=3, command=add5).place(x= 51, y=150)
btn6 = Button(ventana, text="6", width=6, height=3, command=add6).place(x= 102, y=150)
btn7 = Button(ventana, text="7", width=6, height=3, command=add7).place(x= 0, y=205)
btn8 = Button(ventana, text="8", width=6, height=3, command=add8).place(x= 51, y=205)
btn9 = Button(ventana, text="9", width=6, height=3, command=add9).place(x= 102, y=205)
btn0 = Button(ventana, text="0", width=6, height=3, command=add0).place(x= 51, y=260)
btnPunto = Button(ventana, text=".", width=6, height=3, command=addPunto).place(x= 102, y=260)
btnPI = Button(ventana, text="π", width=6, height=3, command=addPI).place(x= 0, y=260)

# Botones de cálculo

btnDiv = Button(ventana, text="÷", width=10, height=3).place(x= 153, y=40)
btnMult = Button(ventana, text="×", width=10, height=3).place(x= 153, y=95)
btnMenos = Button(ventana, text="-", width=10, height=3).place(x= 153, y=150)
btn1Mas = Button(ventana, text="+", width=10, height=3).place(x= 153, y=205)
btnResult = Button(ventana, text="=", width=10, height=3).place(x= 153, y=260)

btnDel = Button(ventana, text="DEL", width=6, height=3).place(x= 102, y=40)
btnC = Button(ventana, text="C", width=6, height=3).place(x= 51, y=40)
btnCe = Button(ventana, text="CE", width=6, height=3).place(x= 0, y=40)

ventana.mainloop()
