import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
    #pass
    print(f''' {enunciado[0]}

    a. {alternativas[0][0]}
    b. {alternativas[1][0]}
    c. {alternativas[2][0]}
    d. {alternativas[3][0]}''')

    
    
    ###############################################################
    return
    
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4