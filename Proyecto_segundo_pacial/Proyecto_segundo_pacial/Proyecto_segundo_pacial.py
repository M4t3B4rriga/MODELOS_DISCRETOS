import big_o 
import timeit
import pymongo
from pymongo import MongoClient
from ingreso import Ingreso
from bson.objectid import ObjectId
from datetime import datetime
#from clase1 import Clase1



def obtener_bd():
  '''
   conceccion a mongo db
   parametros de entrada:
   ---------------------------
   parametros de salida: 
   ---------------------------
  '''
  #guardar como se llama mi base de datos
  base_de_datos="EmpresaTelefonicaConvencional"
  #concecion con mi mongo 
  client=MongoClient("localhost",27017) 
  #retorno de donde voy a tener mi mongo
  return client[base_de_datos]


def imprimir_menu(opciones):
    """
    recorre las opciones imprimiendole, mostroando un linea por iteracion
    paramtros: opciones
    Retorna: 
    """
    print('Seleccione una opcion: ')
    #imprime un mensaje
    for clave in sorted(opciones ):
        #inicia el bucle para mostrar una linea por interacion
        print(f' {clave}) {opciones[clave][0]}')
        #imprime la linea con la iteracion
def leer_opciones(opciones): 
    """
    realiza un bucle para asegurarme de que valor introducido por el usuario es valido
    paramtros: opciones
    Retorna: a
    """
    while(a :=input('Opcion: ')) not in opciones:
        # inicia el bucle con el parametro
        print('Opcionincorrecto, vuelta a intentarlo. ')
        #devuelve un mensaje diciendo que no esta dentro del intervalo
    return a
    #retorna a
def ejecutar_opcion(opcion, opciones):
    """
    recive la opcion seleccionada y el diccionario de opciones y ejecutara la accion correspondida
    paramtros: opcion, opcione
    Retorna: 
    """
    opciones[opcion][1]()
    #recive la opcion seleccionada 

def generar_menu(opciones, opcion_salida):
    """
    Ejecuta el cuerpo del bucle a excepcion si ha elegido la opcion de salir
    paramtros: opciones, opcion_salida
    Retorna: 
    """
    opcion = None 
    #en  caso de que opcion no sea correcta 
    while opcion != opcion_salida:
        #bucle para que se cree las opciones
        imprimir_menu(opciones)
        #imprecion de las opciones
        opcion=leer_opciones(opciones) 
        #ve si es valido el valor
        ejecutar_opcion(opcion, opciones) 
        #ejecuta el programa
        print()
        #imprime linea sin nada


def insertar(ingreso):
    '''
    funcion que llama a una clase para ingresar en el mongo 
    parametros:
    ingreso
    retorna: 
    Ingreso.insert_one({})
    '''
    #direccion a adonde va a guardar el porceso
    base_de_datos=obtener_bd()
    #cocneccion con mi base de datos
    Ingreso=base_de_datos.Ingreso
    #retorna todos los parametros de ingreso que esten en mi clase
    return Ingreso.insert_one({
        #redireccionamos el nombre y donde va a estar el parametro 
        "nombreDuenio":ingreso.nombreDuenio,
        #redireccionamos el nombre y donde va a estar el parametro 
        "numeroCasa":ingreso.numeroCasa,
        #redireccionamos el nombre y donde va a estar el parametro 
        "sectorCasa":ingreso.sectorCasa,
        #redireccionamos el nombre y donde va a estar el parametro 
        "planesAdicionales":ingreso.planesAdicionales,
        #redireccionamos el nombre y donde va a estar el parametro 
        "precioInstalacion":ingreso.precioInstalacion,
        #redireccionamos el nombre y donde va a estar el parametro 
        "fechaInstalacion":ingreso.fechaInstalacion,
        #redireccionamos el nombre y donde va a estar el parametro 
        "numeroTelefonico":ingreso.numeroTelefonico,
        #agregamos
        
        }).inserted_id

def obtener():
    '''
    funcion paraobtener los apramtros de mi base de datos
    parametros:
    -----------------
    retirna:
    base_de_datos.Ingreso.find()
    '''
    #cocnectamos con la base de datos 
    base_de_datos=obtener_bd()
    #recorre toda la base
    return base_de_datos.Ingreso.find() 

def actualizar(id,ingreso):
    '''
    funcion que actualiza y remplaza los parametros ya antes ingresados
    parametros: 
    id, ingreso
    retona: 
    resultado.modified_count
    '''
    #coenctamos con la base  de datos
    base_de_datos=obtener_bd()
    #agregamos los nuevos paramtros a la base  de datos
    resultado=base_de_datos.Ingreso.update_one(
        {
        #buscamos el id de la persona qeu vamos a cambiar
         '_id':ObjectId(id)   
        },
        {
            #nuevo cambio
            '$set':{
                #redireccionamos el nombre y donde va a estar el parametro
                 "nombreDuenio": ingreso.nombreDuenio,
                 #redireccionamos el nombre y donde va a estar el parametro
                 "numeroCasa":ingreso.numeroCasa,
                 #redireccionamos el nombre y donde va a estar el parametro
                 "sectorCasa":ingreso.sectorCasa,
                 #redireccionamos el nombre y donde va a estar el parametro
                 "planesAdicionales":ingreso.planesAdicionales,
                 #redireccionamos el nombre y donde va a estar el parametro
                 "precioInstalacion":ingreso.precioInstalacion,
                 #redireccionamos el nombre y donde va a estar el parametro
                 "fechaInstalacion":ingreso.fechaInstalacion,
                 #redireccionamos el nombre y donde va a estar el parametro
                 "numeroTelefonico":ingreso.numeroTelefonico,
                 
             }
        })
    #retorna y modiifca los otros datos
    return resultado.modified_count

def eliminar(id):
    '''
    proceso para eliminar datos 
    parametros:
    id
    retorna:
    resultado.deleted_count
    ''',
    #conectamos con la base de datos
    base_de_datos=obtener_bd()
    #ingresamos a la base de datos y elimina 
    resultado=base_de_datos.Ingreso.delete_one({
        #buscamos el id
        '_id':ObjectId(id)
        })
    #reorna lo borrado
    return resultado.deleted_count 

def menu_principal():
    """
    Creacion del menu de opciones con los nombre de nuestras variables para realzar los procesos
    paramtros: 
    Retorna: 
    """
    opciones={
        #todas nuestras opciones
        '1':('Ingresar datos cliente: ', datos_cliente),
        #nombre e impresion de nuetra variable
        '2':('Ver todo: ', ver_todo),
        #nombre e impresion de nuetra variable
        '3':('Actualizar: ', Actualizar),
        #nombre e impresion de nuetra variable
        '4':('Eliminar: ', Eliminar),
        #nombre e impresion de nuetra variable
        '5':('Salir', salir)
        }
    generar_menu(opciones, '5')
    #llamamos a nuestra generador con el numero de opciones
#guardamos la impresion de un menu secundario
menu = """ 
 [1] Plan mas internet, descuento de 10%  
 [2] Plan de internet por un anio mas instalacion gratis 
 [3] Plan de intenet mas un celular descuento de 50%")
 [4] Salir

 """

def datos_cliente():
   '''
   ingreso de los datos de los clientes
   paramtros:
   ---------------------
   retorna:
   ---------------------
   '''
   #imprime
   print("Insertar: ")
   #guarda la el nombre 
   nombreDuenio=input("Nombres y apellidos del cliente: ")
   #ciclo de repeticion pra validar solo letras
   while nombreDuenio.isalpha()!=True:
       #imprimir mensaje
       print("Ingrese solo letras")
       #guardamos nuevo parametro
       nombreDuenio=input("Nombres y apellidos del cliente: ")

   #ingreso de nuevo dato
   numeroCasa=input("Numero de la casa: ")
   #cliclo de repeticion para validar solo numeros
   while numeroCasa.isdigit()!=True:
       #imprime mesaje
       print("Ingrese solo numeros")
       #guarda nuevo dato
       numeroCasa=input("Numero de la casa: ")

   #ingreso de nuevo dato
   sectorCasa=input("Ingrese el sector donde vive: ")
   #cilco de repeticion de para solo letras
   while sectorCasa.isalpha()!= True:
       #imprime mensaje
       print("Ingrese solo letras")
       #guarda dato
       sectorCasa=input("Ingrese el sector donde vive: ")

   #guarda dato
   eleccion1=input("Desea agregar algun plan adicional Si=1/No=0: ")
   #ciclo de repeticion para solo letras
   while eleccion1.isdigit()!=True:
       #imprime mensaje
        print("Ingrese solo 1 o 0")
        #guarda dato
        eleccion1=input("Desea agregar algun plan adicional Si=1/No=0: ")
   #ingreso a condicion
   if eleccion1 != 1:
       #gurda dato para que no se repita
      eleccion=None 
      #entra a un blucle para ingresar al menu
      while eleccion != 4:
          #imprime el menu
          print(menu)
          #ingresa el plan
          eleccion=int(input("Elegir plan: "))
          #si fuera 1
          if eleccion == 1:
              #imprime
              print("Plan agregado: ")
              #agrega plan a base de datos
              planesAdicionales=("Plan mas internet, descuento de 10% agregado")
          #si fuera 2
          elif eleccion == 2:
              #imrpime mensaje
              print("Plan agregado: ")
              #agrega base de datos
              planesAdicionales=("Plan de internet por un anio mas instalacion gratis agregado")
          #si fuera 3
          elif eleccion == 3:
              #imprime mensaje 
              print("Plan agregado: ")
              #agrega a base de datos
              planesAdicionales=("Plan de intenet mas un celular descuento de 50% agregado")
   #caso contrario
   else:
    #agrega si no se elige ningun plan 
    planesAdicionales=("No se ingreso ningun plan adicional")

   #agrega a base de datos       
   precioInstalacion=input("Precio de instalacion es de: ")
   #siclo de repeticion para validar solo numeros
   while precioInstalacion.isdigit()!=True:
       #imprime mensaje
       print("Ingrese solo numeros")
       #gurada dato
       precioInstalacion=input("Precio de instalacion: ")

    #parametro de ingreso 
   numeroTelefonico=[7]
   #guarda numero telfonico
   numeroTelefonico=input("Nuevo numero tefelonico convencional: ")
   #condicion para validar numero
   if numeroTelefonico[0]==2:
       #imprime mensaje
           print("numero registrado")
    #caso contrario repite
   else:
       #mensaje de reingreso
           print("Ingrese de nuevo")
           #gurda el dato
           numeroTelefonico=input("Nuevo numero telefonico convencial: ")
   #vcalidacion solo numeros 
   while numeroTelefonico.isdigit()!=True:
       #mensaje
       print("Ingrese solo numeros")
       #guarad el dato
       numeroTelefonico=input("Nuevo numero telefonico convencional: ")
       #de nuevo validacion para solo 7 numeros
       if numeroTelefonico[0]!=3:
           #mesnaje
           print("numero registrado")
       #caso contrario
       else:
           #mensaje
           print("Ingrese de nuevo")
           #ingresa el dato
           numeroTelefonico=input("Nuevo numero telefonico convencial: ")

   #validacion para la fecha
   while True:
       #funcion de vlaidacion
       try:
          #gurada la entrada de la fecha
          fechaInstalacion=input("Fecha de instalacion del equipo YYYY-MM-DD: ")
          #tiene que seguir el sigueinte formato con un libreria
          datetime.strptime(fechaInstalacion,'%Y-%m-%d')
          #mesjae 
          print("fecha valida")
          #salismo del bucle si cumple
          break
       #si no es asi
       except ValueError:
           #imprime mensaje
           print("Fecha invalida Ingrese de nuevo")
   #envia los parametros de todo lo que se ingreso a mu base de datos
   ingreso=Ingreso(nombreDuenio, numeroCasa, sectorCasa,planesAdicionales,precioInstalacion,fechaInstalacion,numeroTelefonico)
   #ingresa la id
   id=insertar(ingreso)
   #impriem mesaje
   print("Los datos del cliente son: ",id)
   '''
   #funcion big_o
   lamdaCadena= lambda a:ingreso
   best, other= big_o.big_o(insertar,lamdaCadena)
   print("La complejidad es: ",best)
   '''


def ver_todo():
    '''
    funcion para mandar los parametros y ver todo lo ingresado
    parametros:
    ---------------
    retirna:
    ------------------
    '''
    #imprime mensaje
    print("Lista de clientes: ")
    #ciclo de re peticion de para todo lo ingresado en mi base de datos
    for ingreso in obtener():
        #imprimer parametro
        print("--------------------")
        #imprimer parametro
        print("Id: ",ingreso["_id"])
        #imprimer parametro
        print("nombreDuenio: ",ingreso['nombreDuenio'])
        #imprimer parametro
        print("numeroCasa: ",ingreso['numeroCasa'])
        #imprimer parametro
        print("sectorCasa: ",ingreso['sectorCasa'])
        #imprimer parametro
        print("planesAdicionales: ",ingreso['planesAdicionales'])
        #imprimer parametro
        print("precioInstalacion: ",ingreso['precioInstalacion'])
        #imprimer parametro
        print("fechaIntalacion: ",ingreso['fechaInstalacion'])
        #imprimer parametro
        print("numeroTelefonico: ",ingreso['numeroTelefonico'])
        

       



def Actualizar():
    '''
    funcion par ingreasar los nueovos parametros para actulizar los datos por si quiere algo nuevo
    parametros:
    -------------
    retorna:
    -------------
    '''
    #mesnaje
    print("Actualizar cliente: ")
    #pide id para busacr
    id=input("Dime el id: ")
    #validacion para que ingrese solo letras y numeros
    while id.isalnum()!= True:
        #mesnaje
        print("No ingrese caracteres especiales: ")
        #guarda nuevo dato
        id=input("Dime el id: ")
    #guarda parametro
    nombreDuenio=input("Nuevo Nombre del cliente: ")
    #cliclo de validacion para solo letras
    while nombreDuenio.isalpha()!=True:
        #imprime mensaje
       print("Ingrese solo letras")
       #guarda nuevo parametro
       nombreDuenio=input("Nuevo Nombre del cliente: ")
    #ingreso de parametro
    numeroCasa=input("Nuevo numero de casa: ")
    #validacion de solo nuemros
    while numeroCasa.isdigit()!=True:
        #mensaje
       print("Ingrese solo numeros")
       #reingreso si no esta valido
       numeroCasa=input("Numero de la casa: ")
   #guarda el parametro
    sectorCasa=input("Nuevo sector de la casa: ")
    #validadion de solo letras
    while sectorCasa.isalpha()!= True:
        #mensaje
       print("Ingrese solo letras")
       #gurad parametro
       sectorCasa=input("Ingrese el sector donde vive: ")
    #gurda parametro
    eleccion1=input("Desea agregar algun plan adicional Si=1/No=0: ")
    #validacion de solo letras
    while eleccion1.isdigit()!=True:
        #que re ingrese 
        print("Ingrese solo 1 o 0")
        #re ingreso
        eleccion1=input("Desea agregar algun plan adicional Si=1/No=0: ")
    # Validacion
    if eleccion1!=1:
      #guarda parametro
      eleccion=None 
      #funcion de menu hasta que sea 4 
      while eleccion != 4:
          #imprime menu secundario
          print(menu)
          #guarda la eleccion
          eleccion=int(input("Elegir plan: "))
          #ingresa al aparametro
          if eleccion == 1:
              #mensaje
              print("Plan agregado: ")
              #guarda el mesnaje 
              planesAdicionales=("Plan mas internet, descuento de 10% agregado")
          #ingresa al otro seleccionado
          elif eleccion == 2:
              #mesaje
              print("Plan agregado: ")
              #guarda el parametro 
              planesAdicionales=("Plan de internet por un anio mas instalacion gratis agregado")
          #si ingresa a este apartado
          elif eleccion == 3:
              #mensjae
              print("Plan agregado: ")
              #guarda el parametro
              planesAdicionales=("Plan de intenet mas un celular descuento de 50% agregado")
    #caso contrario 
    else:
    #guarda el otro mensaje
     planesAdicionales=("No se ingreso ningun plan adicional")

    #guarda el parametro ingresado      
    precioInstalacion=input("Precio de instalacion es de: ")
    #validacion de solo nuemros
    while precioInstalacion.isdigit()!=True:
       #mesnaje
       print("Ingrese solo numeros")
       #guarda el aprametros de re ingreso
       precioInstalacion=input("Precio de instalacion: ")

    #le damos un parametro de hasta que cantidad
    numeroTelefonico=[7]
    #guarda el parametro
    numeroTelefonico=input("Nuevo numero tefelonico convencional: ")
    #validacon para que ingrese con un numero en especifico
    if numeroTelefonico[0]==2:
           #mensaje
           print("numero registrado")
    #caso contrario
    else:
           #mensaje
           print("Ingrese de nuevo")
           #guarda el aprametro
           numeroTelefonico=input("Nuevo numero telefonico convencial: ")
    #validacoon de que sea solo numeros
    while numeroTelefonico.isdigit()!=True:
       #mensaje
       print("Ingrese solo numeros")
       numeroTelefonico=[7]
       #gurada el parametro
       numeroTelefonico=input("Nuevo numero telefonico convencional: ")
       #validacion de ingrese con un numero especifico
       if numeroTelefonico[0]!=2:
           #menaje
           print("numero registrado")
       #ccaso contrario
       else:
           #mensaje
           print("Ingrese de nuevo")
           #guarda parametro
           numeroTelefonico=input("Nuevo numero telefonico convencial: ")
    #validacion par la fecha
    while True:
        #validacion
        try:
            #ingreso de la fecha
           fechaInstalacion=input("Fecha de instalacion del equipo YYYY-MM-DD: ")
           #validacion con un formaro en especifico
           datetime.strptime(fechaInstalacion,'%Y-%m-%d')
           #mensaje
           print("Fecha valida")
           #salr del proceso
           break
        #exepto
        except ValueError:
           # mensjae 
           print("Fecha invalida Ingrese de nuevo")
    #manda todos los parametros de ingreso a mi base de datos
    ingreso= Ingreso(nombreDuenio,numeroCasa, sectorCasa,planesAdicionales, precioInstalacion, fechaInstalacion, numeroTelefonico) 
    #cactualiza los nuevo datos ingresados
    cliente_actualizado=actualizar(id,ingreso)
    #mensaje
    print("Numero de clientes actualizados: ", cliente_actualizado) 
    #funcion big_o
    '''
    lamdaCadena= lambda a:ingreso
    best, other= big_o.big_o(actualizar,lamdaCadena)
    print("La complejidad es: ",best)
    '''

def Eliminar():
    '''
    funcion para eliminar un cleinte
    parametro:
    -------------------
    retorna. 
    --------------------
    '''
    #mesaje
    print("Eliminar Ususario")
    #ingresamos el id 
    id=input("Dime el id: ")
    #contador de clientes eliminados y elimina
    clientes_eliminados=eliminar(id)
    #mensaje
    print("Numero de clientes eliminados: ", clientes_eliminados)


def salir():
    """
    realiza una imprecion de un mensaje de salida
    paramtros: 
    Retorna: 
    """
    print('saliendo')
    #imprimer salida

if __name__=="__main__":
    '''
    menu principal
    parametros:
    -----------------
    retorna:
    ---------------------
    '''
    #llama al menu pricipal
    print("EMPRESA TELEFONICA RAHALE")
    menu_principal()
  


