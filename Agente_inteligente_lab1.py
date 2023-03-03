
def ingreso_de_datos(goal_state):
    """
    Se reliaza el ingreso de los datos en esta funcion y se los guarda en un diccionario 

    Parametros: goal_state

    Retorna: viaATratar
    """
    #creamos un diccionario 
    aux=0
    viaATratar={}
    #realizamos un ciclo for para el ingreso de cada uno de los estados de las vias
    for comprobar in goal_state:
        #guardamos los datos del valor que lo pongamos 
        estado=input('Ingrese 1 si esta ocuada la via {} o 0 si no esta ocuada la via: \n'.format(comprobar))
        #validacion para que solo sea numeros
        while estado.isdigit()!= True:
            #impresion de un mensaje
            print("El dato no es un numero")
            #se guarda de nuevo por la repeticion
            estado=input('Ingrese 1 si esta ocupada la via {} o 0 si no esta ocupada la via: \n'.format(comprobar))
        #condicion de que si el valor es 1 o 0 para guardarlo
        if int(estado)==1 or int(estado)==0:
            #guardamos en el diccionario
            viaATratar[comprobar]=int(estado)
        #caso contrario
        else:
            #ciclo de repeticion para validacion si se ingresa otro numero
            while estado!=True:
                #mensaje de ingreso incorrecto
                print("Ingreso no correcto, ingrese de nuevo\n")
                #ingresa de nuevo el valor
                estado=input('Ingrese 1 si esta ocupada la via {} o 0 si no esta ocupada la via: \n'.format(comprobar))
                #ciclo de validacion 
                while estado.isdigit()!=True:
                    #imprimos mensaje 
                    print("El dato no es un numero")
                    #se guarda de nuevo por la repeticion de la validacion
                    estado=input('Ingrese 1 si esta ocupada la via {} o 0 si no esta ocupada la via: \n'.format(comprobar))
                    #si el estado es 1 o 0 guardara el resultado
                if int(estado)==1 or int(estado)==0:
                    #guadamos verdadero en caso de que si sea verdadero
                    estado=True
                    #se guarda el dato
                    viaATratar[comprobar]=int(estado)
                    #caso contrario 
                else:
                    #si se ingresa otro numero vamos a mandar un falso para que se repita el proceso de ingreso de la via que se ingreso incorrectamente 
                    estado=False
    #retornamos los valores del diccionario
    return viaATratar 

def agenteInteligente(comienzo_estados, estados):
    """
    Se reliaza nos ayuda a comprobar los valores si la via esta habilitada o no 

    Parametros: comienzo_estado, estado

    Retorna:
    -----------------------------------
    """
    #creamos un contador para los valores del costo 
    costo=0
    #ciclo de peticion para pasar por cada cuerda
    for clave in estados:
        #validacion de que los valores son iguales los que debe de tener las cuerdas
        if estados[clave]==comienzo_estados[clave]:
            #mismo costo
            costo=costo 
        #caso contrario
        else: 
            #caso contrario si el valor de 1 guardaremos el valor de 0 si la condicion no es la misma que la del principio
            if estados[clave]==1:
                #guardamos el valor
               estados[clave]=0
            #caso contrario 
            else: 
                #el valor se guardara con 1 
                estados[clave]=1
            # aumentamos el valor de costo 
            costo+=1
    #imprimimos el valor del costp
    print('Costo es ',costo) 
    #imprimimos el etado que esta cada una de las vias
    print('Estado de la via',str(estados))


if __name__=='__main__':
    #valores que debe de tener cada una de las cuerdas
    goal_state={'Quito':0, 'Chone':1, 'Lorena':1, 'Pilaton':0,'Abraham Calazacon':1,'Luis albeto valencia':0}
    #llamamos al parametro de ingreso de datos
    estados=ingreso_de_datos(goal_state)
    #imprimimos los esatdos de las vias
    print('Via a tratar:', estados)
    #imprimimos como debe de estar las vias 
    print('Via obtenida: ', goal_state)
    #las vias habilitadas o las que no
    agenteInteligente(goal_state,estados)
