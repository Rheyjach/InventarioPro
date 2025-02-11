# Modulos basicos utilizados
import tkinter
import tkinter.messagebox
import sqlite3
from os.path import join,abspath
import sys

# Clase de ejecución de la interfaz
class inicio:
    def __init__(self):
        self.ventana=tkinter.Tk()
        self.ventana.geometry("550x550+408+109")
        self.ventana.iconbitmap(self.ruta_absoluta("imagenes/icono.ico"))
        self.ventana.resizable(width=False,height=False)
        self.ventana.title("InventarioPro")
        self.ventana.config(bg="#F8F9FA")

        #imagen
        self.imagen=tkinter.PhotoImage(file=self.ruta_absoluta("imagenes/InventarioPro.png"))

        # labels
        self.imagenAplicacion=tkinter.Label(self.ventana,image=self.imagen)
        self.imagenAplicacion.config(width=250,height=250,bg="#F8F9FA")
        self.imagenAplicacion.pack(pady=15)
        self.nombreApp=tkinter.Label(self.ventana,text="InventarioPro",bg="#F8F9FA",font=("Times New Roman",20,"bold"))
        self.nombreApp.place(x=189,y=250)

        # pie de pagina
        self.piedepagina=tkinter.Label(self.ventana,text="© 2025 - Rheyjach Arrieta",bg="#F8F9FA",font=("Arial",10,"bold"))
        self.piedepagina.place(x=192,y=528)

        #botones
        self.ingresoproductos=tkinter.Button(self.ventana,text="Ingresar",width=13,height=1,command=self.ingresar)
        self.ingresoproductos.config(bg="#EB8F15",font=("Arial",10,"bold"),bd=3,cursor="hand2",activebackground="#EB8F15")
        self.ingresoproductos.place(x=217,y=295)
        self.retirarproductos=tkinter.Button(self.ventana,text="Retirar",width=13,height=1,command=self.retirar)
        self.retirarproductos.config(bg="#EB8F15",font=("Arial",10,"bold"),bd=3,cursor="hand2",activebackground="#EB8F15")
        self.retirarproductos.place(x=217,y=335)
        self.informacion=tkinter.Button(self.ventana,text="Informacion",width=13,height=1,command=self.funcioninfo)
        self.informacion.config(bg="#EB8F15",font=("Arial",10,"bold"),bd=3,cursor="hand2",activebackground="#EB8F15")
        self.informacion.place(x=217,y=375)
        self.acercade=tkinter.Button(self.ventana,text="Acerca de",width=13,height=1,command=self.funcionacercade)
        self.acercade.config(bg="#EB8F15",font=("Arial",10,"bold"),bd=3,cursor="hand2",activebackground="#EB8F15")
        self.acercade.place(x=217,y=415)
        self.salir=tkinter.Button(self.ventana,text="Salir",width=13,height=1,command=self.funcionsalir)
        self.salir.config(bg="#EB8F15",font=("Arial",10,"bold"),bd=3,cursor="hand2",activebackground="#EB8F15")
        self.salir.place(x=217,y=455)

        #llamar funcion basica de base de datos
        self.conectar()

        #Bucle de la interfaz
        self.ventana.mainloop()
    
    #funciones
    #funcion de rutas
    def ruta_absoluta(self,ruta_relativa):
        if hasattr(sys,'_MEIPASS'):
            self.ruta_base=sys._MEIPASS
        else:
            self.ruta_base=abspath(".")
        return join(self.ruta_base,ruta_relativa)

    #funciones de botones
    def ingresar(self):
        from ingreso import ingreso
        self.ventana.destroy()
        ingreso()
    def retirar(self):
        from retiro import retiro
        self.ventana.destroy()
        retiro()
    def funcioninfo(self):
        tkinter.messagebox.showinfo("Información","Esta aplicación está diseñada para gestionar tu inventario de manera eficiente. Permite ingresar productos, retirar productos y visualizar el inventario actual")
    def funcionacercade(self):
        tkinter.messagebox.showinfo("Acerca de","La aplicacion fue creada por Rheyjach Arrieta Delgado con el objetivo de desarrollar un proyecto funcional")
    def funcionsalir(self):
        self.salida=tkinter.messagebox.askokcancel("Salir","¿Desea salir de la aplicacion?")
        if self.salida == True:
            self.ventana.destroy()

    #funciones de base de datos
    def conectar(self):
        self.conexion=sqlite3.connect("datos.db")
        self.cursor=self.conexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS inventario (Registro INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT NOT NULL, Cantidad INTEGER NOT NULL, Precio REAL NOT NULL,Categoria TEXT ,Proveedor TEXT)")
        self.conexion.commit()
        self.conexion.close()

# Este script inicia la aplicación creando una instancia de la clase 'inicio'    
if __name__ == '__main__':
    ejecutar= inicio()