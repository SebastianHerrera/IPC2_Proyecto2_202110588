from typing import Literal
from empresa import Empresa
from cola import ListaSimple
from email.mime import image
from glob import glob
from re import A
from socket import NI_NUMERICHOST
import tkinter
import os 
import graphviz
import customtkinter
import webbrowser
from tkinter import RIGHT, filedialog, messagebox
from xml.dom import minidom
import os

lista = ListaSimple()

##METODOS

def show_empresa():

    nueva_ventana = tkinter.Toplevel(ventana) 
    nueva_ventana.title("Empresa")   
    ancho_cargar_archivo= 500
    alto_cargar_archivo= 600
    x_cargar_archivo = ventana.winfo_screenwidth()//2-ancho_cargar_archivo//2
    y_cargar_archivo = ventana.winfo_screenheight()//2-alto_cargar_archivo//2
    posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

    nueva_ventana.geometry(posicion)
    nueva_ventana.config(bg="#17202A")
    nueva_ventana.resizable(0,0)

def info():
    nueva_ventana = tkinter.Toplevel(ventana) 
    nueva_ventana.title("Información del Desarrollador")   
    ancho_cargar_archivo= 500
    alto_cargar_archivo= 600
    x_cargar_archivo = ventana.winfo_screenwidth()//2-ancho_cargar_archivo//2
    y_cargar_archivo = ventana.winfo_screenheight()//2-alto_cargar_archivo//2
    posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

    #LABELS
    a=150

    #IMAGEN

    #LABEL IMG

    ima = tkinter.Label(nueva_ventana, image=perfil, width=150,height=150, bg="#17202A")
    ima.place(x=125,y=105, anchor=tkinter.CENTER)

    #nombres


    nombre = tkinter.Label(nueva_ventana, text="Geovanny Sebastián", font=("Helvetica", 28, "bold"))
    nombre.config(bg="#17202A", fg="white",anchor=tkinter.W)
    nombre.place(x=40,y=50+a)

    #apellidos

    apellidos = tkinter.Label(nueva_ventana, text="Herrera Claudio", font=("Helvetica", 28, "bold"))
    apellidos.config(bg="#17202A", fg="white",anchor=tkinter.W)
    apellidos.place(x=40,y=100+a)

    #carne

    carne = tkinter.Label(nueva_ventana, text="Carné: 202110588", font=("Helvetica", 14, "bold"))
    carne.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    carne.place(x=40,y=160+a)

    #cui

    cui = tkinter.Label(nueva_ventana, text="CUI: 3556794340101", font=("Helvetica", 14, "bold"))
    cui.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    cui.place(x=40,y=195+a)

    #curso

    cui = tkinter.Label(nueva_ventana, text="Lab. Introducción a la Programación y Computación 2", font=("Helvetica", 11, "bold"))
    cui.config(bg="#17202A", fg="#B3B6B7",anchor=tkinter.W)
    cui.place(x=40,y=230+a)

    #github

    def github():
        webbrowser.open_new_tab("https://github.com/SebastianHerrera")

    button = customtkinter.CTkButton(master=nueva_ventana, text="GitHub", command=github)
    button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    nueva_ventana.geometry(posicion)
    nueva_ventana.config(bg="#17202A")
    nueva_ventana.resizable(0,0)

def cerrar():
    exit()

def crear_empresa():
    nueva_ventana = tkinter.Toplevel(ventana) 
    nueva_ventana.title("Crear nueva empresa")   
    ancho_cargar_archivo= 1000
    alto_cargar_archivo= 600
    x_cargar_archivo = ventana.winfo_screenwidth()//2-ancho_cargar_archivo//2
    y_cargar_archivo = ventana.winfo_screenheight()//2-alto_cargar_archivo//2
    posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

    #LABELS
    a=50


    #empresa


    empresa = tkinter.Label(nueva_ventana, text="Empresa", font=("Helvetica", 32, "bold"))
    empresa.config(bg="#17202A", fg="white",anchor=tkinter.W)
    empresa.place(x=40,y=40)

    #nueva

    nueva = tkinter.Label(nueva_ventana, text="Nueva", font=("Helvetica", 22, "bold"))
    nueva.config(bg="#17202A", fg="#B3B6B7",anchor=tkinter.W)
    nueva.place(x=40,y=95)

    #Id

    Id = tkinter.Label(nueva_ventana, text="Id:", font=("Helvetica", 18, "bold"))
    Id.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    Id.place(x=40,y=160)

    ids = tkinter.IntVar()
    id_entry = customtkinter.CTkEntry(nueva_ventana,textvariable=ids,width=150, justify=tkinter.RIGHT)
    id_entry.place(x=300,y=160)

    #nombre

    nombre = tkinter.Label(nueva_ventana, text="Nombre: ", font=("Helvetica", 18, "bold"))
    nombre.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    nombre.place(x=40,y=205)

    name = tkinter.StringVar()
    nombre_entry = customtkinter.CTkEntry(nueva_ventana,textvariable=name,width=150, justify=tkinter.RIGHT)
    nombre_entry.place(x=300,y=205)

    #abreviatura

    abreviatura = tkinter.Label(nueva_ventana, text="Abreviatura: ", font=("Helvetica", 18, "bold"))
    abreviatura.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    abreviatura.place(x=40,y=250)

    abr = tkinter.StringVar()
    abreviatura_entry = customtkinter.CTkEntry(nueva_ventana,textvariable=abr,width=150, justify=tkinter.RIGHT)
    abreviatura_entry.place(x=300,y=250)

    #punto

    punto = tkinter.Label(nueva_ventana, text="Punto", font=("Helvetica", 22, "bold"))
    punto.config(bg="#17202A", fg="white",anchor=tkinter.W)
    punto.place(x=40,y=300+a)

    #atencion

    atencion = tkinter.Label(nueva_ventana, text="de Atención", font=("Helvetica", 18, "bold"))
    atencion.config(bg="#17202A", fg="#B3B6B7",anchor=tkinter.W)
    atencion.place(x=40,y=330+a)

    #Id

    id_punto = tkinter.Label(nueva_ventana, text="Id:", font=("Helvetica", 12, "bold"))
    id_punto.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    id_punto.place(x=40,y=380+a)

    ids_punto = tkinter.IntVar()
    id_punto = customtkinter.CTkEntry(nueva_ventana,textvariable=ids_punto,width=150,height=15 ,justify=tkinter.RIGHT)
    id_punto.place(x=300,y=380+a)

    #nombre

    nombre_punto = tkinter.Label(nueva_ventana, text="Nombre: ", font=("Helvetica", 12, "bold"))
    nombre_punto.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    nombre_punto.place(x=40,y=410+a)

    name_punto = tkinter.StringVar()
    name_punto_entry = customtkinter.CTkEntry(nueva_ventana,textvariable=name_punto,width=150, height=15 ,justify=tkinter.RIGHT)
    name_punto_entry.place(x=300,y=410+a)

    #direccion

    direccion = tkinter.Label(nueva_ventana, text="Dirección: ", font=("Helvetica", 12, "bold"))
    direccion.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    direccion.place(x=40,y=440+a)

    address = tkinter.StringVar()
    address_entry = customtkinter.CTkEntry(nueva_ventana,textvariable=address,width=150,height=15 , justify=tkinter.RIGHT)
    address_entry.place(x=300,y=440+a)

    #escritorio

    escritorio = tkinter.Label(nueva_ventana, text="Escritorio", font=("Helvetica", 22, "bold"))
    escritorio.config(bg="#17202A", fg="white",anchor=tkinter.W)
    escritorio.place(x=600,y=40)

    #servicio

    servicio = tkinter.Label(nueva_ventana, text="de Servicio", font=("Helvetica", 18, "bold"))
    servicio.config(bg="#17202A", fg="#B3B6B7",anchor=tkinter.W)
    servicio.place(x=600,y=70)

    #Id

    id_escritorio = tkinter.Label(nueva_ventana, text="Id:", font=("Helvetica", 12, "bold"))
    id_escritorio.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    id_escritorio.place(x=600,y=120)

    ids_escritorio = tkinter.IntVar()
    id_escritorio_entry = customtkinter.CTkEntry(nueva_ventana,textvariable=ids_escritorio,width=150,height=15 ,justify=tkinter.RIGHT)
    id_escritorio_entry.place(x=760,y=120)

    #identificacion

    identificacion_escritorio = tkinter.Label(nueva_ventana, text="Identificación: ", font=("Helvetica", 12, "bold"))
    identificacion_escritorio.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    identificacion_escritorio.place(x=600,y=150)

    identificacion = tkinter.StringVar()
    identificacion_entry = customtkinter.CTkEntry(nueva_ventana,textvariable=identificacion,width=150, height=15 ,justify=tkinter.RIGHT)
    identificacion_entry.place(x=760,y=150)
    
    #encargado

    encargado = tkinter.Label(nueva_ventana, text="Encargado: ", font=("Helvetica", 12, "bold"))
    encargado.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    encargado.place(x=600,y=180)

    encarg = tkinter.StringVar()
    encarg_entry = customtkinter.CTkEntry(nueva_ventana,textvariable=encarg,width=150,height=15 , justify=tkinter.RIGHT)
    encarg_entry.place(x=760,y=180)

    #transaccion

    escritorio = tkinter.Label(nueva_ventana, text="Transacción", font=("Helvetica", 22, "bold"))
    escritorio.config(bg="#17202A", fg="white",anchor=tkinter.W)
    escritorio.place(x=600,y=220+a)

    #nueva

    servicio = tkinter.Label(nueva_ventana, text="Nueva", font=("Helvetica", 18, "bold"))
    servicio.config(bg="#17202A", fg="#B3B6B7",anchor=tkinter.W)
    servicio.place(x=600,y=250+a)

    #Id

    id_transaccion = tkinter.Label(nueva_ventana, text="Id:", font=("Helvetica", 12, "bold"))
    id_transaccion.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    id_transaccion.place(x=600,y=300+a)

    ids_transaccion = tkinter.IntVar()
    id_transaccion = customtkinter.CTkEntry(nueva_ventana,textvariable=ids_transaccion,width=150,height=15 ,justify=tkinter.RIGHT)
    id_transaccion.place(x=760,y=300+a)

    #transaccion

    nombre_transaccion = tkinter.Label(nueva_ventana, text="Transacción: ", font=("Helvetica", 12, "bold"))
    nombre_transaccion.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    nombre_transaccion.place(x=600,y=330+a)

    nombre_trans = tkinter.StringVar()
    nombre_trans_entry = customtkinter.CTkEntry(nueva_ventana,textvariable=nombre_trans,width=150, height=15 ,justify=tkinter.RIGHT)
    nombre_trans_entry.place(x=760,y=330+a)
    
    #tiempo

    encargado = tkinter.Label(nueva_ventana, text="Tiempo: ", font=("Helvetica", 12, "bold"))
    encargado.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    encargado.place(x=600,y=360+a)

    encarg = tkinter.IntVar()
    time_entry = customtkinter.CTkEntry(nueva_ventana,textvariable=encarg,width=150,height=15 , justify=tkinter.RIGHT)
    time_entry.place(x=760,y=360+a)

    def agregar_empresa():
        
        nombre_empresa = nombre_entry.get()
        id_empresa = id_entry.get()
        global ab_empresa
        ab_empresa = abreviatura_entry.get()
        print("EL id es: "+str(id_empresa)+" el nombre es "+str(nombre_empresa)+" y su abreviastura es "+ab_empresa)
        file = open("C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Proyecto 2/Empresas/"+ab_empresa+".txt", "w")
        file.write("Nombre de Empresa: "+nombre_empresa + os.linesep)
        file.write("Id de Empresa: "+id_empresa+ os.linesep)
        file.write("Abreviatura de Empresa: "+ab_empresa+ os.linesep)
        file.close()
        lista.agregarUltimo("","Co")
        messagebox.showinfo(message="Empresa agregada correctamente.", title="Agregada correctamente")
    
    def agregar_punto_de_atencion():
        try:
            id_punto_atencion = ids_punto.get()
            nombre_punto_atencion = name_punto_entry.get()
            direccion_punto = address_entry.get()

            print("EL id es: "+str(id_punto_atencion)+" el nombre es "+str(nombre_punto_atencion)+" y su abreviastura es "+direccion_punto)
            file = open("C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Proyecto 2/Empresas/"+ab_empresa+".txt", "a")
            file.write("ID del Punto de Atención: "+str(id_punto_atencion) + os.linesep)
            file.write("Nombre del Punto de Atención: "+nombre_punto_atencion+ os.linesep)
            file.write("Dirección del Punto de Atención: "+direccion_punto+ os.linesep)
            file.close()
            messagebox.showinfo(message="Punto de atención agregado correctamente.", title="Agregado correctamente")

        except:
            messagebox.showerror(message="No se ha agregado una empresa aún, agrega una empresa primero para poder utilizar esta opción.", title="Ha ocurrido un error")

    def agregar_escritorio_de_servicio():
        try:
            nombre_escritorio = identificacion_entry.get()
            id_escritorio = id_escritorio_entry.get()
            direccion_punto = address_entry.get()

            file = open("C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Proyecto 2/Empresas/"+ab_empresa+".txt", "a")
            file.write("ID del Escritorio: "+str(id_escritorio) + os.linesep)
            file.write("Nombre del Escritorio: "+nombre_escritorio+ os.linesep)
            file.write("Dirección del Escritorio: "+direccion_punto+ os.linesep)
            file.close()
            messagebox.showinfo(message="Escritorio de servicio agregado correctamente.", title="Agregado correctamente")

        except:
            messagebox.showerror(message="No se ha agregado una empresa aún, agrega una empresa primero para poder utilizar esta opción.", title="Ha ocurrido un error")

    def agregar_transaccion():
        try:
            id_trans = id_transaccion.get()
            name_trans = nombre_trans_entry.get()
            tiempo_entry = time_entry.get()

            file = open("C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Proyecto 2/Empresas/"+ab_empresa+".txt", "a")
            file.write("ID de la Transacción: "+str(id_trans) + os.linesep)
            file.write("Nombre de la transacción: "+name_trans+ os.linesep)
            file.write("Tiempo de la transacción: "+str(tiempo_entry)+ os.linesep)
            file.close()
            messagebox.showinfo(message="Transacción agregada correctamente.", title="Agregada correctamente")

        except:
            messagebox.showerror(message="No se ha agregado una empresa aún, agrega una empresa primero para poder utilizar esta opción.", title="Ha ocurrido un error")

    button = customtkinter.CTkButton(master=nueva_ventana, text="Agregar", command=agregar_empresa, width=100)
    button.place(x=400, y=310, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=nueva_ventana, text="Agregar", command=agregar_punto_de_atencion, width=100)
    button.place(x=400, y=540, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=nueva_ventana, text="Agregar", command=agregar_escritorio_de_servicio, width=100)
    button.place(x=860, y=230, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=nueva_ventana, text="Agregar", command=agregar_transaccion, width=100)
    button.place(x=860, y=460, anchor=tkinter.CENTER)

    nueva_ventana.geometry(posicion)
    nueva_ventana.config(bg="#17202A")
    nueva_ventana.resizable(0,0)

def empresas():
    nueva_ventana = tkinter.Toplevel(ventana) 
    nueva_ventana.title("Empresas")   
    ancho_cargar_archivo= 800
    alto_cargar_archivo= 500
    x_cargar_archivo = ventana.winfo_screenwidth()//2-ancho_cargar_archivo//2
    y_cargar_archivo = ventana.winfo_screenheight()//2-alto_cargar_archivo//2
    posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)
    nueva_ventana.geometry(posicion)
    
    #label_empresa

    empresa = tkinter.Label(nueva_ventana, text="Empresas", font=("Helvetica", 32, "bold"),width=100)
    empresa.config(bg="#17202A", fg="white",anchor=tkinter.W)
    empresa.place(x=300,rely=0.1)

    button = customtkinter.CTkButton(master=nueva_ventana, text="Crear empresa", command=crear_empresa, border_width=3, border_color="#B3B6B7" ,fg_color="#CB4335", hover_color="#943126")
    button.place(relx=0.88, rely=0.92, anchor=tkinter.CENTER)

    lista = os.listdir("C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Proyecto 2/Empresas")
    print("Existen "+str(len(lista))+" archivos")
    largo = len(lista)
    for i in range(largo):
        string = lista[i]
        characters = ".txt"
        for x in range(len(characters)):
         string = string.replace(characters[x],"")
        label = customtkinter.CTkButton(nueva_ventana,text=string,width=100, command=show_empresa)
        label.place(x=(125*i)+100,y=150)
        



    nueva_ventana.config(bg="#17202A")
    nueva_ventana.resizable(0,0)

def abrir_archivo():
    doc = minidom.parse(filename)
    lista_de_empresas = doc.getElementsByTagName("empresa")
    for empresas in lista_de_empresas:
        sid = empresas.getAttribute("id")
        nombre = empresas.getElementsByTagName("nombre")[0]
        abreviatura = empresas.getElementsByTagName("abreviatura")[0]
        lista.agregarUltimo(str(sid),str(nombre.firstChild.data),(abreviatura.firstChild.data))
    lista.recorrido()   

def cargar_configuracion():
    global filename
    try:
        filename = filedialog.askopenfilename(initialdir = "C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Proyecto 2/Archivos de Entrada"
        , title = "Seleccione un Archivo de Entrada", filetypes = (("Archivos de Datos","*.XML*"),("all files","*.*")))
        print(filename)
        global nombre_archivo
        nombre_archivo = str(os.path.basename(filename))
        print("Archivo cargado '"+nombre_archivo+"'")
        ##TRATAR DE LEER LA CONFIGURACIÓN
        try:
            abrir_archivo()

        except:
            messagebox.showerror(message="El archivo no ha sido cargado correctamente :(", title="Ha ocurrido un error")
    except:
        messagebox.showerror(message="El archivo no ha sido cargado correctamente :(", title="Ha ocurrido un error")

##VENTANA

ventana = tkinter.Tk()
ventana.title("Práctica 1")
ventana.resizable(0,0)
ventana.iconbitmap("C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab Lenguajes Formales y de Programación/Práctica 1/Programa/logo.ico")
ventana.config(bg="#17202A")



##FRAME

frame = tkinter.Frame(ventana, width=800, height=500)
ancho_frame= 800
alto_frame= 500
x_frame = ventana.winfo_screenwidth()//2-ancho_frame//2
y_frame = ventana.winfo_screenheight()//2-alto_frame//2
posicion=str(ancho_frame)+"x"+str(alto_frame)+"+"+str(x_frame)+"+"+str(y_frame)
ventana.geometry(posicion)
frame.config(bg="#17202A")

#LABEL IMG
logo = tkinter.PhotoImage(file="C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Proyecto 2/logo.png")
img = tkinter.Label(frame, image=logo, width=375,height=250, bg="#17202A")
img.place(relx=0.5,y=140, anchor=tkinter.CENTER)

perfil = tkinter.PhotoImage(file="C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Proyecto 2/perfil.png")

frame.pack()

##BOTONES DEL FRAME

#BOTON ORDENES

button = customtkinter.CTkButton(master=frame, text="Empresas", command=empresas)
button.place(relx=0.5, rely=0.60, anchor=tkinter.CENTER)


#BOTON INFO DEL DESARROLLADOR

button = customtkinter.CTkButton(master=frame, text="Información del Desarrollador", command=info)
button.place(relx=0.5, rely=0.70, anchor=tkinter.CENTER)

#BOTON CERRAR

button = customtkinter.CTkButton(master=frame, text="Cerrar", command=cerrar)
button.place(relx=0.5, rely=0.80, anchor=tkinter.CENTER)

#BOTON CARGAR ARCHIVO DE CONFIGURACIÓN

button = customtkinter.CTkButton(master=frame, text="Cargar Archivo", command=cargar_configuracion, border_width=3, border_color="#B3B6B7" ,fg_color="#CB4335", hover_color="#943126")
button.place(relx=0.88, rely=0.92, anchor=tkinter.CENTER)

##MAINLOOP

ventana.mainloop()