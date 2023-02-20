
#importamos librerias necesarias para la intefaz grafica
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def agenteInteligente(comienzo_estados, estados):
    costo=0
    for clave in estados:
        if int(estados[clave])==comienzo_estados[clave]:
            costo=costo 
        else: 
            if int(estados[clave])==1:
               estados[clave]=='0'
            else: 
                estados[clave]='1'
            costo+=1
    
    #print('Costo es ',costo) 
    #print('Estado de la afinacion',str(estados))
    messagebox.showinfo(message='Afinacion Completada con Exito.',title='Afinado')
    #cambiamos de estado para modificar el texto
    trv.config(state='normal')
    #eliminamos los elementos del texto
    trv.delete("1.0","end")
    #volmemos a modificar el estado
    trv.config(state='disabled')
    #mandamos informacion del estado que esta pasando con sus costos
    messagebox.showinfo(message="El Costo de energia utilizado fue de {}".format(costo),title='Proceso Finalizados')
    #mostramos resutados por el porgrama
    afinarGuitarraPrograma(estados)

def afinarGuitarraPrograma(estados):
    """
    Funcion que permite cambiar estados y mostrar en nuestro programa los estados

    Parametro
    -------------------------------
    Estados de las cuerdas: estados

    Retorna
    -----------------------------
    No retorna ningun valor
    """
    #Arreglo de estados en el programa 
    arregloEstados=[combobox_1,combobox_2,combobox_3,combobox_4,combobox_5,combobox_6]
    i=0
    #recorremos los estados ya afinados
    for  clave in estados:
        #recorremos el estado deseado
        arregloEstados[i].set(estados[clave])
        i+=1
   
def encerar():
    """
    Funcion que permite encerar los datos encontrados 

    Parametros
    --------------------------------
    ningun parametros

    Retorna 
    --------------------------------
    No retorna ningun valor
    """
    #setea cada elemento a 0 nuevamente
    combobox_1.set('')
    combobox_2.set('')
    combobox_3.set('')
    combobox_4.set('')
    combobox_5.set('')
    combobox_6.set('')
def strCuerdas(diccionario):
    """
    Funcion que devuelve un strign con las cuerdas y sus estados

    Parametro
    --------------------------------------
    Diccionario con los estados:diccionario

    Retorna
    -------------------------------------
    Retorna un String con estados 
    """
    strDatos=""
    i=1
    for dato in diccionario:
        if int (diccionario[dato])==0:
            strDatos+="Cuerda {}: {}\n".format(i,diccionario[dato])
        i+=1
    return strDatos
def comprobar(diccionario):
    """
    Funcion que permite comprobar si existe algun elemento vacio en mi programa

    Parametro
    ----------------------------------
    Diccionario con todos los estados:diccionario

    Retorna
    ---------------------------------
    True or False: si todos los datos son correctos
    """
    #recorre cada elemento de la lista
   
    for elemento in diccionario:
        #comprueba los elementos que no esten vacios
        if diccionario[elemento]=='':
            return False
    #retorna verdadero si los datos estan completos
    return True

def click():
    """
    Funcion realiza la accion al precionar el boton afinar

    Parametros
    ------------------------------
    Ningun Parametro

    Retorna
    ------------------------------
    No retorna ningun valor 
    """
    #Creamos un diccionario con los datos que nos devuelve nuestro programa
    listaEstados = {}
    #Designamos cada elemento 
    listaEstados['Cuerda_1']=combobox_1.get()
    listaEstados['Cuerda_2']=combobox_2.get()
    listaEstados['Cuerda_3']=combobox_3.get()
    listaEstados['Cuerda_4']=combobox_4.get()
    listaEstados['Cuerda_5']=combobox_5.get()
    listaEstados['Cuerda_6']=combobox_6.get()
    #Estado a llegar al afinar
    afinador={'Cuerda_1':1, 'Cuerda_2':1, 'Cuerda_3':1, 'Cuerda_4':1, 'Cuerda_5':1,'Cuerda_6':1}
    #comprobamos si existe datos completos para realizar la accion de afinar 
    if comprobar(listaEstados):
        #transformamos los estados en estring para el usuario
        strLista=strCuerdas(listaEstados)
        #modificacion de estado para editar textos
        trv.config(state="normal")
        #aumento de informacion
        trv.insert(tk.END,'Cuedas Desafinadas \n')
        #insetmos lo que esta pasando en el programa
        trv.insert(tk.END,strLista)
        #encerar()
        trv.insert(tk.END,'Afinando\n')
        trv.insert(tk.END,'Espere...\n')
        trv.config(state="disabled")
        #afinamos nuestras cuerdas
        agenteInteligente(afinador,listaEstados)
    else:
        #mandamos informacion de que nos falta mas datos
        messagebox.showerror(message='Datos Incompletos. Revise si todos los cuerdos están seleccionados.',title='Datos Faltantes')

def cuerdaN(nombre,row,column,rowC,columnC):
    """
    Funcion para crear comboboxs  con su label

    Parametros
    --------------------------------
    nombre de la cuerda:nombre
    columna donde se ubica:column
    fila donde se encuentra:row
    Ubicacio de la fila del comboboxs:rowC
    Ubicacion columna del combobox:columnC

    Retorna
    ---------------------------------
    Label y un combobox
    """
    #crea el label con la infromacion de la cuerda
    cuerda=Label(frame1,text=nombre,fg='black',font=('Times New Roman',18))
    #nos ubicamos con el grid
    cuerda.grid(pady=10,row=row,column=column)
    #creamos el combobox
    combobox=ttk.Combobox(frame1,values=['0','1'], width=5 ,state="readonly")
    #ubicamos el combobox
    combobox.grid(padx=30,row=rowC,column=columnC,sticky=W)
    return cuerda,combobox

if __name__=='__main__':
    #cremaos las pantallas
    pantalla= Tk()
    pantalla['bg']='white'
    #cremoas el frame donde estaran las cuerdas
    frame1=LabelFrame(pantalla,text='Afinador')
    frame1.pack(fill="both",expand="yes",padx=20,pady=15)
    #creamos el frame para mostrar infromacion que realiza el programa
    frame2=LabelFrame(pantalla,text='Guitarra')
    frame2.pack(fill="both",expand="yes",padx=20,pady=15)
    #Creamos el titulo de la ventana
    pantalla.title('Afinador de Cuerdas Inteligente')
    #creamos la pantalla
    pantalla.geometry("470x400")
    #creamos cuerdas para nuestro programa
    cuerda_1,combobox_1=cuerdaN('Cuerda 1',0,0,0,1)
    cuerda_2,combobox_2=cuerdaN('Cuerda 2',1,0,1,1)
    cuerda_3,combobox_3=cuerdaN('Cuerda 3',2,0,2,1)
    cuerda_4,combobox_4=cuerdaN('Cuerda 4',0,3,0,4)
    cuerda_5,combobox_5=cuerdaN('Cuerda 5',1,3,1,4)
    cuerda_6,combobox_6=cuerdaN('Cuerda 6',2,3,2,4)
    #creamos un boton parque afine nuestras cuerdas 
    boton=Button(frame1,text='Afinar!!' ,command=click)
    #ubicamos usando grid nuestro boton
    boton.grid(padx=10, pady=10, row=7, column=0, columnspan=6,sticky=S+N+E+W)
    #mostrara la informacion del programa
    trv=tk.Text(frame2, width=52,height=15)
    trv.pack()
    pantalla.mainloop()



    