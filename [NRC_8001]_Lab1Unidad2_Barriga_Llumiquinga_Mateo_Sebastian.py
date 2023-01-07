
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

def menu_principal():
    """
    Creacion del menu de opciones con los nombre de nuestras variables para realzar los procesos
    paramtros: 
    Retorna: 
    """
    opciones={
        #todas nuestras opciones
        '1':('Area y perimetro de un rectangulo: ', Area_Perimetro_Rectangulo),
        #nombre e impresion de nuetra variable
        '2':('Calcular la expresion y=(x^z/2): ', Calcular_expresion_aritmetica),
        #nombre e impresion de nuetra variable
        '3':('Area de un Trapezoide: ', Area_trapezoide),
        #nombre e impresion de nuetra variable
        '4':('Area del cilindro: ', Area_cilindro),
        #nombre e impresion de nuetra variable
        '5':('Area de un circulo con el radio: ', Area_circulo),
        #nombre e impresion de nuetra variable
        '6':('De libras a kilos y gramos: ', De_libras_a_KilosGramos),
        #nombre e impresion de nuetra variable
        '7':('Resolver (a+b^2)/2.5: ', Resolver_expresion),
        #nombre e impresion de nuetra variable
        '8':('Saludo al usuario con su nombre: ', Saludo_con_nombre),
        #nombre e impresion de nuetra variable
        '9':('De dolares a euros y yen: ', De_dolares_a_EurosYen),
        #nombre e impresion de nuetra variable
        '10':('Resolver ((-1)k+1)/(2*k-1)((-1)^{k+1})/(2*k-1): ', Resolver_expresion2),
        #nombre e impresion de nuetra variable
        '11':('Perimetro de un rectangulo: ', Perimetro_rectangulo),
        #nombre e impresion de nuetra variable
        '12':('De centimetros a metros y kilometros: ', De_centimetros_a_MetrosKilometros),
        #nombre e impresion de nuetra variable
        '13':('De Celsius a fahrenheit y viceversa: ', De_celsius_a_Fahre),
        #nombre e impresion de nuetra variable
        '14':('Convertir de dias en anios y semanas: ', De_dias_a_AniosSemanas),
        #nombre e impresion de nuetra variable
        '15':('Hallar la potencia de cualquier numero: ', Potencia_de_cualquier_numero),
        #nombre e impresion de nuetra variable
        '16':('Area de un triangulo: ', Area_triangulo),
        #nombre e impresion de nuetra variable
        '17':('Ingresar dos numeros y resolver todas las operaciones Aritmeticas: ', Operaciones_aritmeticas),
        #nombre e impresion de nuetra variable
        '18':('Perdir al usuario su nombre y saludarlo: ', Saludo_usuario),
        #nombre e impresion de nuetra variable
        '19':('Dencidad de un objeto: ', Dencidad_objeto),
        #nombre e impresion de nuetra variable
        '20':('De RMB a dolares y pesos colombianos: ', RMB_dolares_pesos),
        #nombre e impresion de nuetra variable
        '21':('Salir', salir)
        #nombre e impresion de nuetra variable
        
    }


    generar_menu(opciones, '21')
    #llamamos a nuestra generador con el numero de opciones

def Area_Perimetro_Rectangulo():
    """
    ingreso de los parametros y resolucion del area y perimetro del tringulo mediante su formula
    paramtros: 
    Retorna: 
    """
    print('Opcion 1:')
    #impresion de el numero de opcion
    lista=[]
    #creacion de una lista 
    numero1=int(input("Ingrese la base: "))
    #creaacion de una varaible con el parametro definido a imprimir 
    lista.append(numero1)
    #guardado de la variable anterior en la lista 
    numero2=int(input("Ingrese la altura: "))
    #creaacion de una varaible con el parametro definido a imprimir 
    lista.append(numero2)
    #guardado de la variable anterior en la lista 
    print('AREA')
    #imprime mensaje area
    area=(numero1*numero2)
    #resolucion del area con los paremetros
    print(area)
    #imprime el valor del area
    print('PERIMETRO')
    #imprime mensaje de perimetro
    perimetro=(numero1+numero1+numero2+numero2)
    #guarda en una varaible la resolucion de permetro
    print(perimetro)
    #imrprime el valor de perimetro


def Calcular_expresion_aritmetica():
    """
    ingreso de los parametros y resolucion del de la exprecion aritmetica 
    paramtros: 
    Retorna: 
    """
    print('Opcion 2:')
    #impresion de el numero de opcion
    lista=[]
    #creacion de una lista 
    numero1=int(input("Ingrese el valor de X: "))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(numero1)
    #guardado de la variable anterior en la lista 
    numero2=int(input("Ingrese el valor de Z: "))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(numero2)
    #guardado de la variable anterior en la lista 
    y=((numero1**numero2)/2)
    #guarda en una variable la resolucion de la exprecion aritmetica
    print('Resultado:', y)
    #imprime el resultado de la exprecion 




def Area_trapezoide():
    """
    ingreso de los parametros y resolucion del area del trapezoide
    paramtros: 
    Retorna: 
    """
    print('Opcion 3:')
    #impresion de el numero de opcion
    lista=[]
    #creacion de una lista 
    base1=int(input("Ingrese el valor de base1: "))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(base1)
    #guardado de la variable anterior en la lista 
    base2=int(input("Ingrese el valor de base2: "))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(base2)
    #guardado de la variable anterior en la lista 
    altura=int(input("Ingrese el valor de altura: "))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(altura)
    #guardado de la variable anterior en la lista 
    area=(0.5*(base1+base2)*altura)
    #guarda en una varible la resolucion de la ecuacion para el area del trapezoide
    print('El Area es de cm^2: ', area)
    #imprime el resultado de area
    


def Area_cilindro():
    """
    ingreso de los parametros y resolucion del area del cilidro
    paramtros: 
    Retorna: 
    """
    lista=[]
    #creacion de una lista 
    print('Opcion 4:')
     #impresion de el numero de opcion
    radio=int(input("Ingrese el valor del radio: "))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(radio)
    #guardado de la variable anterior en la lista 
    altura=int(input("Ingrese el valor de la altura: "))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(altura)
    #guardado de la variable anterior en la lista 
    area=(2*3.1416*radio*(radio+altura))
    #guarda en una variable la recolucion de la ecuacion del area del cilindro
    print('El area de un cilindro es: ', area)
    #imprime el area del cilidro


def Area_circulo():
    """
    ingreso de los parametros y resolucion del area de un circulo
    paramtros: 
    Retorna: 
    """
    print('Opcion 5:')
     #impresion de el numero de opcion
    lista=[]
    #creacion de una lista 
    radio=int(input("Ingrese el valor del radio: "))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(radio)
    #guardado de la variable anterior en la lista 
    area=(3.1416*(radio*radio))
    #guarada en una variable la resolcuion del radio de un circulo
    print('El area de un circulo es: ', area)
    #imprime el resultado del area del circulo


def De_libras_a_KilosGramos():
    """
    ingreso de los parametros y resolucion de la trasformacion de libras a kilos y gramos
    paramtros: 
    Retorna: 
    """
    print('Opcion 6:')
     #impresion de el numero de opcion
    lista=[]
    #creacion de una lista 
    libra=int(input('Ingrese el valor: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(libra)
    #guardado de la variable anterior en la lista 
    transformacionKilos=(libra*(1/2.2046))
    #guarada en una variable al trasformacion de libras a kilos
    transformacionGramos=(libra*(453.59/1))
    #guarda en un variable la transformacion de libras a gramos
    print('De libras a kilogramos: ', transformacionKilos)
    #imprime el resultado de los kilos
    print('De libras a gramos: ', transformacionGramos)
    #imprime la transformacion a gramos
    


def Resolver_expresion():
    """
    ingreso de los parametros y resolucion de la exprecion aritmetica 
    paramtros: 
    Retorna: 
    """
    print('Opcion 7:')
     #impresion de el numero de opcion
    lista=[]
    #creacion de una lista 
    a=int(input('Ingrese el valor de A: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(a)
    #guardado de la variable anterior en la lista 
    b=int(input('Ingrese el valor de B: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(b)
    #guardado de la variable anterior en la lista 
    resultado=((a+(b*b))/2.5)
    #guarda en una variable la ecuacion resuelta 
    print('Resultado de la Ecuacion: ', resultado)
    #imprime el resultado de la ecuacion



def Saludo_con_nombre():
    """
    ingreso del nombre y la impresion del mensaje 
    paramtros: 
    Retorna: 
    """
    print('Opcion 8:')
     #impresion de el numero de opcion
    nombre=input('Cual es tu nombre: ')
    #creaacion de una varaible con el parametro definido a imprimir
    print('Hola, ',nombre) 
    #imprime el mensaje con el nombre



def De_dolares_a_EurosYen():
    """
    ingreso de los parametros y resolucion de la trasformacion de dolar a euro y yen
    paramtros: 
    Retorna: 
    """
    print('Opcion 9:')
     #impresion de el numero de opcion
    lista=[]
    #creacion de una lista 
    dolares=float(input('Ingrese cantidad a transforma: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(dolares)
    #guardado de la variable anterior en la lista 
    euro=(dolares*0.95)
    #guarda en una variable al transformacion del euro
    yen=(dolares*130.55)
    #guarda en una variable la transformacion del yen
    print('De dolar a Euro es: ', euro) 
    #imprime el resultado del euro
    print('De dolar a Yen es: ', yen)
    #imprimer el resultado del yen



def Resolver_expresion2():
    """
    ingreso de los parametros y resolucion de la exprecion 
    paramtros: 
    Retorna: 
    """
    print('Opcion 10:')
     #impresion de el numero de opcion
    valorK=int(input('Ingresar valor de K: '))
    #creaacion de una varaible con el parametro definido a imprimir
    resultado=((((-1)*(valorK+1))/(2*(valorK-1))*((-1)**(valorK+1)))/(2*(valorK-1)))
    #guarda en una varibale el resultado de expresion 
    print('La respuesta de la expresion es: ', resultado)
    #imprime el resultado de la expresion 


def Perimetro_rectangulo():
    """
    ingreso de los parametros y resolucion del perimetro del rectagulo
    paramtros: 
    Retorna: 
    """
    print('Opcion 11:')
     #impresion de el numero de opcion
    lista=[] 
    #creacion de una lista 
    base=int(input('Ingrese la base: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(base)
    #guardado de la variable anterior en la lista 
    altura=int(input('Ingrese la altura'))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(altura)
    #guardado de la variable anterior en la lista 
    perimetro=(base+base+altura+altura)
    #guarda en una variable la suma de los lados de un rectangulo 
    print('El perimetro es: ', perimetro)
    #imprime el perimetro 


def De_centimetros_a_MetrosKilometros():
    """
    ingreso de los parametros y resolucion de la transfromacion de centimetros a metros y kilometros 
    paramtros: 
    Retorna: 
    """
    print('Opcion 12:')
     #impresion de el numero de opcion
    lista=[] 
    #creacion de una lista 
    centimetros=int(input('Ingrese la cantidad: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(centimetros)
    #guardado de la variable anterior en la lista 
    metros=(centimetros*(1/100))
    #guarda en una variable la resulucion de centimetros a metros
    kilometros=(metros*(1/1000))
    #guarda en una variable al resolucion de los metros que sacamos en laa anterior a kilometros
    print('La respuesta en metros es de: ',metros) 
    #imprime la la respuesta en metros
    print('La respuesta en kilimetros es de: ', kilometros) 
    #imprime la respuesta en kilometros 





def De_celsius_a_Fahre():
    """
    ingreso de los parametros y resolucion de la transformacion de celsius a fahrenheir y al revez 
    paramtros: 
    Retorna: 
    """
    print('Opcion 13:') 
     #impresion de el numero de opcion
    lista=[] 
    #creacion de una lista 
    celsius=(int(input('Ingrese cantidad de celsius: ')))
    #creaacion de una varaible con el parametro definido a imprimir
    fahre=(int(input('Ingrese la cantidad en Fahrenheir: ')))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(celsius) 
    #guardado de la variable anterior en la lista 
    lista.append(fahre)
    #guardado de la variable anterior en la lista 
    fahrenheir=((9/5*celsius)+32)
    #gurda en una variable la transformacion 
    resCelsius=((fahre-32)/1.8)
    #guarda en una variable la transformacion a celsius
    print('La respuesta en Fahrenheir: ', fahrenheir)
    #imprime la respuesta de fahrenheir
    print('La respuesta en Celsius: ', resCelsius)
    #imprime la respuesta de celsius 


def De_dias_a_AniosSemanas():
    """
    ingreso de los parametros y resolucion de la transformacion de dias a anios y semanas 
    paramtros: 
    Retorna: 
    """
    print('Opcion 14:') 
     #impresion de el numero de opcion
    lista=[] 
    #creacion de una lista 
    dia=int(input('Ingrese los dias: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(dia)
    #guardado de la variable anterior en la lista 
    if dia<7:
        #creacion de un condicional si es menor a 7 
        print('Los dias son: ', dia) 
        #imprimer los dias menores
    else:
        #caso contrario
        semanas=((dia*1)/7)
        #trasnformacion de dias a semanaras 
        print('las semanas son: ', semanas)
        #imprime las semanas
        anios=((dia*1)/365)
        #transformacion de dias a anios
        print('Los dias trasformados a anios son: ', anios)
        #imprimer los anios


def Potencia_de_cualquier_numero():
    """
    ingreso de los parametros y resolucion de un numero potenciado a cualquer numero
    paramtros: 
    Retorna: 
    """
    print('Opcion 15:') 
     #impresion de el numero de opcion
    lista=[] 
    #creacion de una lista 
    numero=int(input('Ingrese un numero: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(numero)
    #guardado de la variable anterior en la lista 
    potencia=int(input('Ingrese potencia: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(potencia)
    #guardado de la variable anterior en la lista 
    proceso=(numero**potencia) 
    #guarda en una variable la potencia del numero
    print('La potencia de un numero es: ', proceso) 
    #imprime la el resultado de la potencia


def Area_triangulo():
    """
    ingreso de los parametros y resolucion del area del triangulo
    paramtros: 
    Retorna: 
    """
    print('Opcion 16:') 
     #impresion de el numero de opcion
    lista=[] 
    #creacion de una lista 
    base=int(input('Ingrese la base del tringulo: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(base)
    #guardado de la variable anterior en la lista 
    altura=int(input('Ingrese la altura del tringulo: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(altura) 
    #guardado de la variable anterior en la lista 
    triangulo=((base*altura)/2)
    #resuelve el area del tringulo
    print('El area del tringulo es: ', triangulo) 
    #imprime el area del triangulo



def Operaciones_aritmeticas():
    """
    ingreso de los parametros y resolucion de la operaciones areitmetica
    paramtros: 
    Retorna: 
    """
    print('Opcion 17:') 
     #impresion de el numero de opcion
    lista=[] 
    #creacion de una lista 
    numero1=int(input('Ingrese el primer numero: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(numero1)
    #guardado de la variable anterior en la lista 
    numero2=int(input('Ingrese el segundo numero: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(numero2)
    #guardado de la variable anterior en la lista 
    suma=(numero1+numero2)
    #resolucion de la suma
    resta=(numero1-numero2)
    #resolucuon de la resta
    multiplicacion=(numero1*numero2)
    #resolucion de la multiplicacion
    division=(numero1/numero2)
    #resolucion de la division
    print('La suma es de: ', suma) 
    #imprime la respuesta de suma
    print('La resta es de: ', resta) 
    #imprime la respuesta de la resta
    print('La multiplicacion es de: ', multiplicacion)
    #imrprime la respuesta de la multiplicacion 
    print('La division es de: ', division) 
    #imrprime la respuestad e la division




def Saludo_usuario():
    """
    ingreso de los parametros e imprime el mensaje
    paramtros: 
    Retorna: 
    """
    print('Opcion 18:') 
     #impresion de el numero de opcion
    nombre=input('Ingrese su nombre: ')
    #creaacion de una varaible con el parametro definido a imprimir
    print('Hola ', nombre)
    #imprime el mesanje con su nombre



def Dencidad_objeto():
    """
    ingreso de los parametros y resolucion de la dencidad de un objeto
    paramtros: 
    Retorna: 
    """
    print('Opcion 19:') 
     #impresion de el numero de opcion
    lista=[] 
    #creacion de una lista 
    masa=int(input('Ingrese el valor de masa: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(masa)
    #guardado de la variable anterior en la lista 
    volumen=int(input('Ingrese el valor del volumen: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(volumen) 
    #guardado de la variable anterior en la lista 
    p=(masa/volumen) 
    #guarda en una variable al fromual de la dencidad 
    print('La densidad del objeto es de: ', p) 
    #imprimer el resultado de la dencidad



def RMB_dolares_pesos():
    """
    ingreso de los parametros y resolucion de la transformacion de RMB a peso colombiano
    paramtros: 
    Retorna: 
    """
    print('Opcion 20:') 
     #impresion de el numero de opcion
    lista=[] 
    #creacion de una lista 
    RMB=int(input('Ingrese la cantidad de Renminbi: '))
    #creaacion de una varaible con el parametro definido a imprimir
    lista.append(RMB)
    #guardado de la variable anterior en la lista 
    dolar=(RMB*0.15) 
    #guarda la transfromacion de rmb a dolar
    peso=(RMB*716.17) 
    #gurada la transformacion de rmb a peso
    print('El valor en Dolares es de: ', dolar) 
    #imprime la respuesta de la transformacion en dolar
    print('El valor en Peso Colombiano es de: ', peso)
    #imprime la transformacion a peso


def salir():
    """
    realiza una imprecion de un mensaje de salida
    paramtros: 
    Retorna: 
    """
    print('saliendo')
    #imprimer salida
       

if __name__=='__main__':
    """
    main del programa  
    paramtros: 
    Retorna: 
    """
    menu_principal()
    #llamada al menu del programa





