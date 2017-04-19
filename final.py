##*librerias*
from tkinter import *
from tkinter import messagebox
from tkinter import Toplevel
import time
import threading
from threading import Thread
import os
import winsound
import random
#from datetime import datetime, date,time
#import calendar
flag_img = True
#         .............................
#......../funcion para cargar imagenes
def cargar_img(nombre):
    ruta = os.path.join("imagenes",nombre)
    imagen = PhotoImage(file =ruta)
    return imagen
#        ........
#......./sonidos
def shello():
    winsound.PlaySound('hello.wav', winsound.SND_ASYNC)
def scry():
    winsound.PlaySound('cry.wav', winsound.SND_ASYNC)
def sdance():
    winsound.PlaySound('dance.wav', winsound.SND_ASYNC)
def sgohead():
    winsound.PlaySound('gohead.wav', winsound.SND_ASYNC)
def sgoback():
    winsound.PlaySound('goback.wav', winsound.SND_ASYNC)
def sdead():
    winsound.PlaySound('dead.wav', winsound.SND_ASYNC)
def sleft():
    winsound.PlaySound('left.wav', winsound.SND_ASYNC)
def sright():
    winsound.PlaySound('righy.wav', winsound.SND_ASYNC)
def ssmile():
    winsound.PlaySound('smile.wav', winsound.SND_ASYNC)
def sfav():
    winsound.PlaySound('fav.wav', winsound.SND_ASYNC)
def sbuilt():
    winsound.PlaySound('built.wav', winsound.SND_ASYNC)
def smusic_off():
    winsound.PlaySound(None, winsound.SND_ASYNC)

#        ...............................
#......./configuracion inicial del Robot
archiv_robot = open("robot.txt", "r+")
final_linea = archiv_robot.tell()
linea1 = archiv_robot.readline()
lista = [linea1,'Eva\n','/imagenes/eva0.gif\n','10-04-2017']
archiv_robot.seek(0)
archiv_robot.writelines(lista)
archiv_robot.seek(final_linea)
print(archiv_robot.read())
#        ........................
#......./confi ventana_principal
ventana_principal = Tk()
ventana_principal.title("proyecto Robot Virtual")
ventana_principal.minsize(500,400)
ventana_principal.resizable(width = NO, height = NO)
#        ...................................
#......./contenedor principal para la imagen
contenedor_imagen = Canvas(ventana_principal, width =500,height=300, bg = "blue")
fondo1 = cargar_img("fondo1.gif")
imf1 = contenedor_imagen.create_image(250,150, image= fondo1)
contenedor_imagen.pack()

#        ........................
#......./contenedor para el shell
contenedor_shell = Canvas(ventana_principal, width=500, height=100, bg = "black")
fondo_shell = cargar_img("fondoshell.gif")
imgfs = contenedor_shell.create_image(250,50,image = fondo_shell)
contenedor_shell.place(x=0, y =300)
#.....labels....*
shell = Label(contenedor_shell, text = "Type copyright, credits or license() for more information",bg ="black", fg="white")
shell.place(x = 0,y =0)
shell1 = Label(contenedor_shell, text = ">>>", bg="black",fg="white")
shell1.place(x = 0,y = 30)
textocomandos = Entry(contenedor_shell,width=30,bg="black",fg ="white")
textocomandos.place(x= 30, y= 30)
#        ..................
#......./funcion de energia

def power():
    archiv_robot = open("robot.txt","r+")
    final_linea = archiv_robot.tell()
    linea1 = archiv_robot.readline()
    linea2 = float(linea1)- 1
    archiv_robot.seek(0)
    archiv_robot.writelines(str(linea2//1))
    archiv_robot.seek(final_linea)
    nuevo_contenido = archiv_robot.read()
    return(linea2)
    print(nuevo_contenido)
#      ...............
#...../funcion morir
def morir():
    label_imagen1 = Label(ventana_principal,bg ="black")
    label_imagen1.place(x=0,y =0)
    time.sleep(1)
    for i in range(13):
        imagen2 = cargar_img("eva_m" + str(i) +".gif")
        label_imagen1.config(image = imagen2)
        time.sleep(0.5)
    time.sleep(0.5)
def murio():
        em = Thread(target = morir, args=())
        em.start()
        ventana_principal.mainloop()
#        ...............
#......./funcion estatus
def hilo_energia():
    e = Thread(target = power, args = ())
    e.start()
    status_energia = power()
    label_estatus = Label(ventana_principal,text= "energia = "+str(status_energia+1),bg ="black",fg= "white")
    label_estatus.place(x=410,y =300)
    if status_energia < 20:
        messagebox.showinfo("alerta","reinicie la energia porque esta muriendo")

    if status_energia < 0:
        murio()
        messagebox.showinfo("alerta","reinicie la energia su robot acaba de morir")
        print ("murio")
#        ...........
#......./funcion reiniciar_alfinalizar las animaciones
def off():
    contenedor_imagen = Canvas(ventana_principal, width =500,height=300, bg = "black")
    fondo1 = cargar_img("fondo1.gif")
    imf1 = contenedor_imagen.create_image(250,150, image= fondo1)
    contenedor_imagen.place(x=0,y=0)
    ventana_principal.mainloop()
#      ..............
#...../funcion goright
def goright():
    label_imagen = Label(ventana_principal,bg ="black")
    label_imagen.place(x=0,y =0)
    time.sleep(1)
    for i in range(18):
        imagen2 = cargar_img("eva_izq" + str(i) +".gif")
        label_imagen.config(image = imagen2)
        time.sleep(0.2)
#       ..............
#...../funcion goleft
def goleft():
    label_imagen = Label(ventana_principal,bg ="black")
    label_imagen.place(x=0,y =0)
    time.sleep(1)
    for i in range(21):
        imagen2 = cargar_img("eva_der" + str(i) +".gif")
        label_imagen.config(image = imagen2)
        time.sleep(0.2)

#       ..............
#...../funcion gohead
def gohead():
    label_imagen = Label(ventana_principal,bg ="black")
    label_imagen.place(x=0,y =0)
    time.sleep(1)
    for i in range(12):
        imagen2 = cargar_img("eva_ad" + str(i) +".gif")
        label_imagen.config(image = imagen2)
        time.sleep(0.2)
#       ..............
#...../funcion goback
def goback():
    label_imagen = Label(ventana_principal,bg ="black")
    label_imagen.place(x=0,y =0)
    time.sleep(1)
    for i in range(10):
        imagen2 = cargar_img("eva_at" + str(i) +".gif")
        label_imagen.config(image = imagen2)
        time.sleep(0.2)
#       ..............
#...../funcion smile
def smile():
    label_imagen = Label(ventana_principal,bg ="black")
    label_imagen.place(x=0,y =0)
    time.sleep(1)
    for i in range(10):
        imagen2 = cargar_img("eva_s" + str(i) +".gif")
        label_imagen.config(image = imagen2)
        time.sleep(0.2)
#       ..............
#...../funcion cry
def cry():
    label_imagen = Label(ventana_principal,bg ="black")
    label_imagen.place(x=0,y =0)
    time.sleep(1)
    for i in range(13):
        imagen2 = cargar_img("eva_c" + str(i) +".gif")
        label_imagen.config(image = imagen2)
        time.sleep(0.2)
#       ..............
#...../funcion bailar
def dance():
    label_imagen1 = Label(ventana_principal,bg ="black")
    label_imagen1.place(x=0,y =0)
    time.sleep(1)
    for i in range(18):
        imagen2 = cargar_img("eva_b" + str(i) +".gif")
        label_imagen1.config(image = imagen2)
        time.sleep(0.2)

#       ..............
#...../funcion ejercicio
def exercise():
    label_imagen = Label(ventana_principal,bg ="black")
    label_imagen.place(x=0,y =0)
    time.sleep(1)
    for i in range(11):
        imagen2 = cargar_img("eva_g" + str(i) +".gif")
        label_imagen.config(image = imagen2)
        time.sleep(0.2)
#       ..............
#...../funcion hello
def hello():
    label_imagen = Label(ventana_principal,bg ="black")
    label_imagen.place(x=0,y =0)
    time.sleep(1)
    for i in range(13):
        imagen2 = cargar_img("eva_n" + str(i) +".gif")
        label_imagen.config(image = imagen2)
        time.sleep(0.2)
#       ..............
#...../funcion built
def built():
    label_imagen = Label(ventana_principal,bg ="black")
    label_imagen.place(x=0,y =0)
    time.sleep(1)
    for i in range(6):
        imagen2 = cargar_img("eva_h" + str(i) +".gif")
        label_imagen.config(image = imagen2)
        time.sleep(0.2)
#        .....
#......./Ventana de help
def ventana_help():
    ventana_help = Toplevel()
    ventana_help.title("help")
    ventana_help.minsize(400,500)
    ventana_help.resizable(width = NO, height = NO)
    fondo_help = Canvas(ventana_help, width =400, height =500,bg ="black")
    fonq = cargar_img("fondo_help.gif")
    Fdhp = fondo_help.create_image(250,150, image= fonq)
    fondo_help.pack()
#texto de informacion
    informacion = Label(ventana_help,text="Hola, Soy un robot virtual, para poder usarme siga las instrucciones",bg = "black",fg="yellow")
    informacion.place(x=20,y=10)
    informacion1 = Label(ventana_help,text="Instruccion1= Por favor introduzca uno de estos comandos\n *-left= El robot se mueve a la izq\n*-right= El robot se mueve a la der\n*-gohead= El robot se mueve hacia adelante\n*-goback= El robot se mueve hacia atras\n*-status= Indicacion de energia\n*-hello= El robot saluda y da su nombre\n*-built= El robot dice que dia fue creado\n*-dance= El robot baila\n*-music-on= Se reproduce la cancion favorita del robot\n*-music-off= Apaga la musica\n *-smile= El robot sonrie\n*-cry= El robot llora\n *-exercise= El robot hace ejercicios\n*-Se le puede asignar un valor de energia entre 0 y 99",bg = "black",fg="white")
    informacion1.place(x=5,y=30)
    informacion2= Label(ventana_help,text= "Instruccion2= Porfavor despues de ingresar cualquier comando \nescribir el comando: -reiniciar",bg="black",fg="white")
    informacion2.place(x=5,y=270)
    informacion3= Label(ventana_help,text= "Instruccion3= El robot cuenta con un rango de energia entre 0 y 99 \nalgunos comandos disminuyen la energia",bg="black",fg="white")
    informacion3.place(x=5,y=290)
    informacion4 = Label(ventana_help,text= "Instruccion4= Hazle algunas preguntas al robot \n*-Como te llamas?\n*-Que dia es?\n*-Que hora es?",bg="black",fg="white")
    informacion4.place(x=5,y=310)

#       ...........................
#....../boton para ingresar a help
botonHelp = Button(contenedor_shell,text ="help",command=ventana_help,bg = "black", fg = "red",  width=4, height = 1)
botonHelp.place(x=220,y = 30)
#        ...........
#......./tecla enter
def enter(event):
    co = textocomandos.get()
    #comando smile
    if co == "smile":
        s0 = Thread(target=ssmile,args=())
        s0.start()
        s = Thread(target=smile,args=())
        s.start()
    #comando cry
    elif co == "cry":
        hilo_energia()
        c0 = Thread(target=scry, args=())
        c0.start()
        c =Thread(target=cry, args=())
        c.start()
    #comando exercise
    elif co == "exercise":
        hilo_energia()
        g0 = Thread(target=exercise, args=())
        g0.start()
    #comando gohead
    elif co == "gohead":
        hilo_energia()
        g0= Thread(target = sgohead,args=())
        g0.start()
        g = Thread(target=gohead,args=())
        g.start()
    #comando goback
    elif co == "goback":
        hilo_energia()
        gb0 = Thread(target=sgoback,args=())
        gb0.start()
        gb = Thread(target=goback,args=())
        gb.start()
        off()
    #comando preguntas
    elif co == "Como te llamas?":
        hilo_energia()
        hel0 = Thread(target= shello,args=())
        hel0.start()
        hel = Thread(target =hello,args=())
        hel.start()
    elif co == "Que dia es?":
        ahora = time.strftime("%A" " %d " "%B " "%Y")
        #print("fecha y hora: ", ahora)
        messagebox.showinfo("Fecha ","Hoy es: "+ str(ahora))
    elif co == "Que hora es?":
        ahora = time.strftime("%I:%M:%S")
        messagebox.showinfo("hora","Son las :" + str(ahora))
    #comando right
    elif co == "right":
        hilo_energia()
        d0 = Thread(target=sright,args=())
        d0.start()
        d = Thread(target =goright,args=())
        d.start()
    #comando left
    elif co == "left":
        hilo_energia()
        i0 = Thread(target= sleft ,args=())
        i0.start()
        i = Thread(target = goleft,args=())
        i.start()
    #comando para volver a la imagen inicial
    elif co == "reiniciar":
        off()
    #comando built
    elif co == "built":
        bm0= Thread(target= sbuilt,args=())
        bm0.start()
        bm = Thread(target =built,args=())
        bm.start()
    #comando hello
    elif co == "hello":
        hel0 = Thread(target= shello,args=())
        hel0.start()
        hel = Thread(target =hello,args=())
        hel.start()
    #comando status
    elif co == "status":
        status_energia = power()
        messagebox.showinfo("alerta","la energia es de: "+str(status_energia))
    #comando dance
    elif co == "dance":
        hilo_energia()
        hilo_energia()
        dan0 = Thread(target= sdance,args=())
        dan0.start()
        dan = Thread(target =dance,args=())
        dan.start()
    #comando music-on
    elif co == "music-on":
        hilo_energia()
        mon = Thread(target = sfav,args=())
        mon.start()
        off()
    #comando music-off
    elif co == "music-off":
        mof = Thread(target = smusic_off,args=())
        mof.start()
        off()
    #cualquier comando diferente de los anteriores
    elif int(co) >= 0 and int(co) < 100:
        archiv_robot = open("robot.txt","r+")
        final_linea = archiv_robot.tell()
        archiv_robot.seek(0)
        x = int(co)/1
        archiv_robot.writelines(str(x))
        archiv_robot.seek(final_linea)
        print(archiv_robot.read())
    else:
        print("comando invalido")
        messagebox.showinfo("advertencia","codigo invalido\n Siga las instrucciones Porfavor")
#      ..............................
#...../configuracion de la tecla enter
textocomandos.bind('<Return>',enter)
textocomandos.focus_set()
#      ..........................
#...../menu para cerrar programa
menu = Menu(ventana_principal)
menu.add_command(label = "Cerrar", command = ventana_principal.quit)
ventana_principal.config(menu = menu)
#iniciar el loop del la ventana_principal
ventana_principal.mainloop()
