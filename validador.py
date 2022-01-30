
def validate(opciones, eleccion):    #recibe las opciones en una lista y lo que introdujo el usuario
    # Definir validación de eleccion
    ##########################################################################
    #pass
    while eleccion not in opciones:  #mientras la eleccion no este en la lista de opciones
        eleccion = input('Opcion inválida. Ingrese una de las opciones válidas: ')

    return eleccion  #si se ingresa una opcion valida se retorna el valor de la eleccion válida

    ##########################################################################


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
