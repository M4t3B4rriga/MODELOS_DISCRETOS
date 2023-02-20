


def ingreso_de_datos(afinador):
    """
    Se reliaza el ingreso de los datos en esta funcion y se los guarda en una 

    Parametros: afinador

    Retorna: afinadorATratar
    """
    #creamos un diccionario 
    afinaATratar={}
    #realizamos un ciclo for para el ingreso de cada cuerda
    for afinar in afinador:
        #guardamos los datos del valor que lo pongamos 
        estado=input('Ingrese 1 si esta afinada la cuerda {} o 0 si esta desafinada: \n'.format(afinar))
        #validacion para que solo sea numerosagetme
        while estado.isdigit()!= True:
            #impresion de un mensaje
            print("El dato no es un numero")
            #se guarda de nuevo por la repeticion
            estado=input('Ingrese 1 si esta afinada la cuerda {} o 0 si esta desafinada: \n'.format(afinar))
        #condicion de que si el valor es 1 o 0 para guardarlo
        if int(estado)==1 or int(estado)==0:
            afinaATratar[afinar]=int(estado)
        #caso contrario
        else:
            #mensaje de lo que pasa si no es valor correcto
            print("Ingreso no correcto, la cuerda estara desafinada\n")
            #guadamos el valor de 0
            afinaATratar[afinar]=0
    #retornamos los valores del diccionario
    return afinaATratar 

def agenteInteligente(comienzo_estados, estados):
    """
    Se reliaza nos ayuda a comprobar los valores si la guitarra esta afinada o no 

    Parametros: comienzo_estado, estado

    Retorna:
    -----------------------------------
    """
    #creamos un contador para los valores del costo de cada afinada
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
            # aumentamos el valor de costo por la afinacion
            costo+=1
    #imprimimos el valor del costp
    print('Costo es ',costo) 
    #imprimimos el etado que esta cada uno de las cuerdas
    print('Estado de la afinacion',str(estados))


if __name__=='__main__':
    #valores que debe de tener cada una de las cuerdas
    afinador={'Cuerda1':1, 'Cuerda2':1, 'Cuerda3':1, 'Cuerda4':1, 'Cuerda5':1,'Cuerda6':1}
    #llamamos al parametro de ingreso de datos
    estados=ingreso_de_datos(afinador)
    #imprimimos los esatdos de la cuerdas
    print('Afinacion a tratar:', estados)
    #imprimimos como debe de estar las cuerdas 
    print('Afinacion obtenida: ', afinador)
    #afinamos las cuerdas
    agenteInteligente(afinador,estados)
