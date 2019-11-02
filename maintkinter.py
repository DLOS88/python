from punto import *
from figuras import *

import sys
PYTHON_VERSION = sys.version_info.major

if PYTHON_VERSION < 3:
    try:
        import Tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo tkinter")

def win2():
    pass



class Win2:

    def __init__(self, myParent):

        self.frame = tk.Toplevel(myParent)
        self.frame.title('Geometria')
        #:wself.frame.geometry('500x500')
         
        self.label = tk.Label(self.frame, text="Calcular Area")
        self.label.grid(row=0, column=0)
        

        self.cadena1 = tk.StringVar()
        self.text1 = tk.Entry(self.frame, textvariable=self.cadena1)
        self.text1.grid(row=1,column=0)

        self.cadena2 = tk.StringVar()
        self.text2 = tk.Entry(self.frame, textvariable=self.cadena2)
        self.text2.grid(row=1,column=1)
        
        self.cadena3 = tk.StringVar()
        self.text3 = tk.Entry(self.frame, textvariable=self.cadena3)
        self.text3.grid(row=2,column=1)

        self.cadena4 = tk.StringVar()
        self.text4 = tk.Entry(self.frame, textvariable=self.cadena4)
        self.text4.grid(row=2,column=1) 
        
        self.label = tk.Label(self.frame, text="Resultado Area")
        self.label.grid(row=2,column=1) 

        self.button = tk.Button(self.frame, text="Aceptar")
        self.button.bind("<Button-1>", self.calcular)
        self.button.grid(row=2,column=1)

        self.result = tk.StringVar()
        self.text = tk.Entry(self.frame, textvariable=self.result)
        self.text.pack(side=tk.LEFT)

        self.label2 = tk.Label(self.frame, text="Resultado Perimetro")
        self.label2.pack(side=tk.LEFT)

        self.resultp = tk.StringVar()
        self.textp = tk.Entry(self.frame, textvariable=self.resultp)
        self.textp.pack(side=tk.LEFT)

        self.variable = tk.StringVar()
        radiobutton1 = tk.Radiobutton(text="Cuadrado", variable=self.variable, value=1, activebackground="#555555", activeforeground="#AAAAAA")
        radiobutton2 = tk.Radiobutton(text="Triangulo", variable=self.variable, value=2, activebackground="#555555", activeforeground="#AAAAAA")
        radiobutton3 = tk.Radiobutton(text="Rectangulo", variable=self.variable, value=3, activebackground="#555555", activeforeground="#AAAAAA")
        radiobutton4 = tk.Radiobutton(text="Circulo", variable=self.variable, value=4, activebackground="#555555", activeforeground="#AAAAAA")

        radiobutton1.pack()
        radiobutton2.pack()
        radiobutton3.pack()
        radiobutton4.pack()
        """

    def calcular(self, event):
        p1 = Punto(int(self.cadena1.get()), int(self.cadena2.get()))
        p2 = Punto(int(self.cadena3.get()), int(self.cadena4.get()))

        print(p1.x, p2.x)

        if self.variable.get()  == '1':
            cuadrado = Cuadrado(p1, p2)
            cuadrado.calcular_area()
            self.result.set(cuadrado.area)
            cuadrado.calcular_perimetro()
            self.resultp.set(cuadrado.perimetro)


        elif self.variable.get()  == '2':
            triangulo = Triangulo(p1, p2)
            triangulo.calcular_area()
            self.result.set(triangulo.area)
            triangulo.calcular_perimetro()
            self.resultp.set(triangulo.perimetro)


        elif self.variable.get()  == '3':
            rectangulo = Rectangulo(p1, p2)
            rectangulo.calcular_area()
            self.result.set(rectangulo.area)
            rectangulo.calcular_perimetro()
            self.resultp.set(rectangulo.perimetro)


        elif self.variable.get()  == '4':
            circulo = Circulo(p1, p2)
            circulo.calcular_area()
            self.result.set(circulo.area)
            circulo.calcular_perimetro()
            self.resultp.set(circulo.perimetro)



root = tk.Tk()
root.geometry('200x400')
app = Win2(root)
root.mainloop()
