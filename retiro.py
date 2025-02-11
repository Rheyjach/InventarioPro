# Modulos basicos utilizados
import tkinter
import tkinter.messagebox
import tkinter.ttk
import sqlite3
from os.path import abspath,join
import sys

# Clase de ejecución de la interfaz
class retiro:
    def __init__(self):
        self.ventana=tkinter.Tk()
        self.ventana.geometry("550x550+408+109")
        self.ventana.iconbitmap(self.ruta_absoluta("imagenes/icono.ico"))
        self.ventana.resizable(width=False,height=False)
        self.ventana.title("InventarioPro")
        self.ventana.config(bg="#F8F9FA")

        #labels retiro
        self.encabezado=tkinter.Label(self.ventana,text="Retirar Cantidad de Productos",bg="#F8F9FA",font=("Arial",13,"bold"))
        self.encabezado.place(x=10,y=5)
        self.registro=tkinter.Label(self.ventana,text="Registro",bg="#F8F9FA",font=("Arial",11,"bold"))
        self.registro.place(x=10,y=30)
        self.nombredelproducto=tkinter.Label(self.ventana,text="Nombre",bg="#F8F9FA",font=("Arial",11,"bold"))
        self.nombredelproducto.place(x=160,y=30)
        self.cantidad=tkinter.Label(self.ventana,text="Cantidad",bg="#F8F9FA",font=("Arial",11,"bold"))
        self.cantidad.place(x=310,y=30)

        #label filtros 
        self.segundoencabezado=tkinter.Label(self.ventana,text="Gestion de Datos",bg="#F8F9FA",font=("Arial",13,"bold"))
        self.segundoencabezado.place(x=10,y=80)
        self.filtroregistro=tkinter.Label(self.ventana,text="Registro",bg="#F8F9FA",font=("Arial",11,"bold"))
        self.filtroregistro.place(x=10,y=105)
        self.filtronombre=tkinter.Label(self.ventana,text="Nombre",bg="#F8F9FA",font=("Arial",11,"bold"))
        self.filtronombre.place(x=10,y=140)
        self.filtrocategoria=tkinter.Label(self.ventana,text="Categoria",bg="#F8F9FA",font=("Arial",11,"bold"))
        self.filtrocategoria.place(x=10,y=175)
        self.filtroproveedor=tkinter.Label(self.ventana,text="Proveedor",bg="#F8F9FA",font=("Arial",11,"bold"))
        self.filtroproveedor.place(x=280,y=105)

        #label agregados
        self.inventario=tkinter.Label(self.ventana,text="Inventario Actual",bg="#F8F9FA",font=("Arial",15,"bold"))
        self.inventario.place(x=10,y=210)
        self.eliminarregistro=tkinter.Label(self.ventana,text="Eliminar registro",bg="#F8F9FA",font=("Arial",11,"bold"))
        self.eliminarregistro.place(x=280,y=175)
        self.mostrardatos=tkinter.Label(self.ventana,text="Mostrar todos los datos",bg="#F8F9FA",font=("Arial",11,"bold"))
        self.mostrardatos.place(x=280,y=140)
            

        #entrys retiros
        self.entryregistro=tkinter.Entry(self.ventana,font=("Arial",8),bg="white")
        self.entryregistro.place(x=10,y=55)
        self.entrynombre=tkinter.Entry(self.ventana,font=("Arial",8),bg="white")
        self.entrynombre.place(x=160,y=55)
        self.entrycantidad=tkinter.Entry(self.ventana,font=("Arial",8),bg="white")
        self.entrycantidad.place(x=310,y=55)

        #entrys filtros
        self.entryfiltroregistro=tkinter.Entry(self.ventana,font=("Arial",8),bg="white")
        self.entryfiltroregistro.place(x=85,y=105)
        self.entryfiltronombre=tkinter.Entry(self.ventana,font=("Arial",8),bg="white")
        self.entryfiltronombre.place(x=85,y=140)
        self.entryfiltrocategoria=tkinter.Entry(self.ventana,font=("Arial",8),bg="white")
        self.entryfiltrocategoria.place(x=85,y=175)
        self.entryfiltroproveedor=tkinter.Entry(self.ventana,font=("Arial",8),bg="white")
        self.entryfiltroproveedor.place(x=365,y=105)

        #entry de eliminar registro
        self.entryeliminar=tkinter.Entry(self.ventana,font=("Arial",8),bg="white",width=13)
        self.entryeliminar.place(x=405,y=175)

        #botones de retiro
        self.botonretirarproductos=tkinter.Button(self.ventana,text="Retirar",width=8,height=1,command=self.retirar)
        self.botonretirarproductos.config(bg="#EB8F15",font=("Arial",8,"bold"),bd=2,cursor="hand2",activebackground="#EB8F15")
        self.botonretirarproductos.place(x=445,y=45)
        

        #botones filtros
        self.botonfiltro1=tkinter.Button(self.ventana,text="Filtrar",width=5,height=1,command=self.buscarregistro)
        self.botonfiltro1.config(bg="#EB8F15",font=("Arial",7,"bold"),bd=2,cursor="hand2",activebackground="#EB8F15")
        self.botonfiltro1.place(x=215,y=105)
        self.botonfiltro2=tkinter.Button(self.ventana,text="Filtrar",width=5,height=1,command=self.buscarnombre)
        self.botonfiltro2.config(bg="#EB8F15",font=("Arial",7,"bold"),bd=2,cursor="hand2",activebackground="#EB8F15")
        self.botonfiltro2.place(x=215,y=140)
        self.botonfiltro3=tkinter.Button(self.ventana,text="Filtrar",width=5,height=1,command=self.buscarcategoria)
        self.botonfiltro3.config(bg="#EB8F15",font=("Arial",7,"bold"),bd=2,cursor="hand2",activebackground="#EB8F15")
        self.botonfiltro3.place(x=215,y=175)
        self.botonfiltro4=tkinter.Button(self.ventana,text="Filtrar",width=5,height=1,command=self.buscarproveedor)
        self.botonfiltro4.config(bg="#EB8F15",font=("Arial",7,"bold"),bd=2,cursor="hand2",activebackground="#EB8F15")
        self.botonfiltro4.place(x=495,y=105)

        #botones agregados
        self.botoneliminar=tkinter.Button(self.ventana,text="Eliminar",width=6,height=1,command=self.eliminar)
        self.botoneliminar.config(bg="#EB8F15",font=("Arial",7,"bold"),bd=2,cursor="hand2",activebackground="#EB8F15")
        self.botoneliminar.place(x=495,y=175)
        self.botoninicio=tkinter.Button(self.ventana,text="Inicio",width=8,height=1,command=self.inicio)
        self.botoninicio.config(bg="#EB8F15",font=("Arial",8,"bold"),bd=2,cursor="hand2",activebackground="#EB8F15")
        self.botoninicio.place(x=445,y=485)
        self.botonmostrardatoso=tkinter.Button(self.ventana,text="Mostrar",width=6,height=1,command=self.mostrartodo)
        self.botonmostrardatoso.config(bg="#EB8F15",font=("Arial",7,"bold"),bd=2,cursor="hand2",activebackground="#EB8F15")
        self.botonmostrardatoso.place(x=455,y=140)

        # pie de pagina
        self.piedepagina=tkinter.Label(self.ventana,text="© 2025 - Rheyjach Arrieta",bg="#F8F9FA",font=("Arial",10,"bold"))
        self.piedepagina.place(x=185,y=510)

        # barra menu
        self.barraMenu=tkinter.Menu(self.ventana)
        self.ventana.config(menu=self.barraMenu)
        self.barraMenu.add_command(label="Info",command=self.info)
        self.barraMenu.add_command(label="Acerca de",command=self.acercade)
        self.barraMenu.add_command(label="Salir",command=self.salir)
        
        #scroll
        self.scrollVertical=tkinter.Scrollbar(self.ventana, orient="vertical")
        self.scrollVertical.place(x=520,y=250,height=225)

        #Tabla
        self.tabla=tkinter.ttk.Treeview(self.ventana,columns=("Registro","Nombre","Cantidad","Precio Unitario","Categoria","Proveedor"),yscrollcommand=self.scrollVertical.set)
        self.tabla.config(height=10)
        self.tabla.place(x=10,y=250)
        self.tabla.heading('#1',text='Registro')
        self.tabla.heading('#2',text='Nombre')
        self.tabla.heading('#3',text='Cantidad')
        self.tabla.heading('#4',text='Precio Unitario')
        self.tabla.heading('#5',text='Categoria')
        self.tabla.heading('#6',text='Proveedor')

        self.style=tkinter.ttk.Style()
        self.style.configure("self.tabla",font=("Arial","9"))
        self.style.configure("self.tabla.heading",font=("Arial","10","bold"))

        #Desabilitar columna '#0'
        self.tabla.column('#0',width=0,stretch=tkinter.NO)

        self.tabla.column('#1',width=80,anchor="center")
        self.tabla.column('#2',width=80,anchor="center")
        self.tabla.column('#3',width=80,anchor="center")
        self.tabla.column('#4',width=90,anchor="center")
        self.tabla.column('#5',width=80,anchor="center")
        self.tabla.column('#6',width=80,anchor="center")

        #eventos de la tabla
        self.tabla.bind("<Button-1>", self.copiar_valor)

        # cooperacion entre scroll y barra
        self.scrollVertical.config(command=self.tabla.yview)

        #llamar funciones basicas de base de datos
        self.cargar()

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
    #funciones de barra de menu
    def info(self):
        tkinter.messagebox.showinfo("INFORMACION","Esta interfaz es fácil de entender, pero en caso de algún error al ingresar un dato, ella misma te guiará con avisos para que puedas utilizarla de la mejor manera."
                                     " La tabla del inventario tiene la capacidad de ensanchar sus columnas, lo que permite visualizar mejor las celdas cuando sea necesario. Además, al hacer clic izquierdo en una celda,"
                                     " es posible copiar su información para facilitar su reutilización.")
    def acercade(self):
        tkinter.messagebox.showinfo("ACERCA DE","La aplicacion fue creada por Rheyjach Arrieta Delgado con el objetivo de desarrollar un proyecto funcional")
    def salir(self):
        self.salida=tkinter.messagebox.askokcancel("SALIR","¿Desea salir de la aplicacion?")
        if self.salida == True:
            self.ventana.destroy()
    #funciones de conexion a base de datos
    def actualizar(self,registro,nombre,cantidad):
        self.conexion=sqlite3.connect("datos.db")
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM inventario")
        self.filas=self.cursor.fetchall()
        self.conexion.close()
        self.registrosActuales=[self.re[0] for self.re in self.filas]
        self.nombresActuales=[self.no[1] for self.no in self.filas]

        if registro not in self.registrosActuales and nombre not in self.nombresActuales:
            tkinter.messagebox.showinfo("AVISO","El Registro y el Nombre ingresados no se encuentran en el sistema")
        elif registro not in self.registrosActuales:
            tkinter.messagebox.showinfo("AVISO","El Registro ingresado no se encuentra en el sistema")
        elif nombre not in self.nombresActuales:
            tkinter.messagebox.showinfo("AVISO","El Nombre ingresado no pertenece a ningun producto en el sistema")
        else:
            self.conexion=sqlite3.connect("datos.db")
            self.cursor=self.conexion.cursor()
            self.cursor.execute("SELECT * FROM inventario WHERE Registro =? and Nombre=?",(registro,nombre))
            self.filaEspecifica=self.cursor.fetchall()
            self.conexion.close()
            if not self.filaEspecifica:
                tkinter.messagebox.showinfo("AVISO","El Registro y el Nombre ingresados se encuentran en el sistema, pero no hay un producto en el sistema en el que coincidan ambos.")
            else:
                self.cantidadActual=[self.ca[2] for self.ca in self.filaEspecifica]
                self.maximoPermitido=self.cantidadActual[0]
                if cantidad > self.maximoPermitido:
                    tkinter.messagebox.showinfo("AVISO",f"No se puede retirar {cantidad} porque el maximo permitido para este producto es de {self.maximoPermitido}")
                else:
                    self.cantidadActualizada=self.maximoPermitido-cantidad
                    self.conexion=sqlite3.connect("datos.db")
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute("UPDATE inventario SET Cantidad=? WHERE Registro=? and Nombre=?",(self.cantidadActualizada,registro,nombre))
                    self.conexion.commit()
                    self.conexion.close()
                    tkinter.messagebox.showinfo("EXITO",f"Se retiraron {cantidad} unidades al producto con codigo de Registro: {registro} y Nombre: {nombre}. La cantidad actualizada es de {self.cantidadActualizada}")
    def cargar(self):
        #limpiar tabla
        for self.row in self.tabla.get_children():
            self.tabla.delete(self.row)
        #consultar y cargar datos
        self.conexion=sqlite3.connect("datos.db")
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM inventario")
        self.filas=self.cursor.fetchall()
        self.conexion.close()

        for self.fila in self.filas:
            self.tabla.insert("","end",values=self.fila)
    #funciones de botones
    def inicio(self):
        from inicio import inicio
        self.ventana.destroy()
        inicio()
    def retirar(self):
        self.variableregistro=self.entryregistro.get().strip()
        self.variablenombre=self.entrynombre.get().strip()
        self.variablecantidad=self.entrycantidad.get().strip()
        if not self.variableregistro or not self.variablenombre or not self.variablecantidad:
            tkinter.messagebox.showinfo("AVISO","Los campos Registro, Nombre y Cantidad deben estar todos llenos para asegurarse de cual es el Nombre y Registro al que se le quiere modificar la cantidad")
        else:
            try:
                self.variableregistro=int(self.variableregistro)
                self.variablecantidad=int(self.variablecantidad)
                if self.variableregistro < 0 or self.variablecantidad <0:
                    tkinter.messagebox.showinfo("AVISO","los campos Registro y Cantidad tienen que ser valores numericos enteros y positivos")
                else:
                    self.actualizar(self.variableregistro,self.variablenombre,self.variablecantidad)
                    self.cargar()

            except:
                tkinter.messagebox.showinfo("AVISO","los campos Registro y Cantidad tienen que ser valores numericos enteros y positivos")    
    def buscarregistro(self):
        self.variablefiltroregistro=self.entryfiltroregistro.get().strip()
        if not self.variablefiltroregistro:
            tkinter.messagebox.showinfo("AVISO","No hay datos ingresados para filtrar por Registro")
        else:
            if not self.variablefiltroregistro.isdigit():
                tkinter.messagebox.showinfo("AVISO","Solo se permiten valores numericos enteros positivos")
            else:
                for self.row in self.tabla.get_children():
                    self.tabla.delete(self.row)

                self.conexion=sqlite3.connect("datos.db")
                self.cursor=self.conexion.cursor()
                self.cursor.execute("SELECT * FROM inventario WHERE Registro=?",(self.variablefiltroregistro,))
                self.filas=self.cursor.fetchall()
                self.conexion.close()

                for self.fila in self.filas:
                    self.tabla.insert("","end",values=self.fila)
    def buscarnombre(self):
        self.variablefiltronombre=self.entryfiltronombre.get().strip()
        if not self.variablefiltronombre:
            tkinter.messagebox.showinfo("AVISO","No hay datos ingresados para filtrar por Nombre del producto")
        else:
            for self.row in self.tabla.get_children():
                self.tabla.delete(self.row)

            self.conexion=sqlite3.connect("datos.db")
            self.cursor=self.conexion.cursor()
            self.cursor.execute("SELECT * FROM inventario WHERE Nombre=?",(self.variablefiltronombre,))
            self.filas=self.cursor.fetchall()
            self.conexion.close()

            for self.fila in self.filas:
                self.tabla.insert("","end",values=self.fila)
    def buscarcategoria(self):
        self.variablefiltrocategoria=self.entryfiltrocategoria.get().strip()
        if not self.variablefiltrocategoria:
            tkinter.messagebox.showinfo("AVISO","Estos son los registros donde no habia una Categoria establecida")
        for self.row in self.tabla.get_children():
            self.tabla.delete(self.row)

        self.conexion=sqlite3.connect("datos.db")
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM inventario WHERE Categoria=?",(self.variablefiltrocategoria,))
        self.filas=self.cursor.fetchall()
        self.conexion.close()

        for self.fila in self.filas:
            self.tabla.insert("","end",values=self.fila)
    def buscarproveedor(self):
        self.variablefiltroproveedor=self.entryfiltroproveedor.get().strip()
        if not self.variablefiltroproveedor:
            tkinter.messagebox.showinfo("AVISO","Estos son los registros donde no habia un Proveedor establecido")
        for self.row in self.tabla.get_children():
            self.tabla.delete(self.row)

        self.conexion=sqlite3.connect("datos.db")
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM inventario WHERE Proveedor=?",(self.variablefiltroproveedor,))
        self.filas=self.cursor.fetchall()
        self.conexion.close()

        for self.fila in self.filas:
            self.tabla.insert("","end",values=self.fila)
    def mostrartodo(self):
        self.cargar()
    def eliminar(self):
        self.variableeliminar=self.entryeliminar.get().strip()
        if not self.variableeliminar:
            tkinter.messagebox.showinfo("AVISO","No ha ingresado un codigo de Registro para ser eliminado")
        else:
            if not self.variableeliminar.isdigit():
                tkinter.messagebox.showinfo("AVISO","Solo se permiten valores numericos enteros positivos")
            else:
                self.conexion=sqlite3.connect("datos.db")
                self.cursor=self.conexion.cursor()
                self.cursor.execute("SELECT Registro FROM inventario")
                self.filas=self.cursor.fetchall()
                self.conexion.close()
                self.registros=[self.i[0] for self.i in self.filas]

                self.variableeliminar=int(self.variableeliminar)

                if self.variableeliminar not in self.registros:
                    tkinter.messagebox.showinfo("AVISO","El Registro ingresado no se encuentra almacenado")
                else:
                    self.conexion=sqlite3.connect("datos.db")
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute("DELETE FROM inventario where Registro=?",(self.variableeliminar,))
                    self.conexion.commit()
                    self.conexion.close()
                    tkinter.messagebox.showinfo("EXITO",f"El Registro {self.variableeliminar} fue eliminado correctamente")
                    self.cargar()
    #funcion de copiar valores de la tabla
    def copiar_valor(self,evento):
        # Obtener el item seleccionado
        self.item = self.tabla.identify_row(evento.y)
        self.column = self.tabla.identify_column(evento.x)

        if self.item and self.column:
            self.column_index = int(self.column.replace("#", "")) - 1
            self.value = self.tabla.item(self.item)["values"][self.column_index]

            # Copiar al portapapeles
            self.ventana.clipboard_clear()
            self.ventana.clipboard_append(self.value)
            self.ventana.update()
            tkinter.messagebox.showinfo("COPIADO",f"Copiado al portapapeles: {self.value}")

