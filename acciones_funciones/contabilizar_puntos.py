from acciones_funciones.msg_puntos_parciales import msg_puntos_parciales

def contabilizar_puntos(contador_credito,ganador_parcial,turno,dicc_jugadores,ronda_terminada,textos): 
    """
    """
    if contador_credito == 0:
        puntos=50
    elif contador_credito==1:
        puntos =40
    elif contador_credito==2:
        puntos =30
    elif contador_credito==3:
        puntos =20
    elif contador_credito==4:
        puntos =10
    else:
        puntos = -100
    
    if not ganador_parcial:
        
        for key in dicc_jugadores:
            if key == turno:
                dicc_jugadores[key][0] += puntos 
            else:
                dicc_jugadores[key][0] += puntos+50
    
    else:
        
        for key in dicc_jugadores:
            if key == turno:
                dicc_jugadores[key][0] += puntos
            else:
                dicc_jugadores[key][0] += -puntos
    
    msg_puntos_parciales(puntos,ronda_terminada,dicc_jugadores,textos)

    
    return dicc_jugadores
