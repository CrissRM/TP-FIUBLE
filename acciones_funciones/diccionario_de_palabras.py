import operator
from configuraciones.datos_iniciales import condiciones_iniciales

dicc_palabra = {}

def diccionario_de_palabras():
  LONG_PALABRA = condiciones_iniciales()["cantidad_letras"]
  archivo_1 = open("archivos/Cuentos.csv","r")
  archivo_2=open("archivos/La araña negra - tomo 1.csv","r")
  archivo_3=open("archivos/Las 1000 Noches y 1 Noche.csv","r")
  archivo_4=open("archivos/palabras.csv","w")
  analizador_texto(archivo_1,1,LONG_PALABRA)
  analizador_texto(archivo_2,2,LONG_PALABRA)
  analizador_texto(archivo_3,3,LONG_PALABRA)
  ordenar_palabras(archivo_4)
  archivo_1.close()
  archivo_2.close() 
  archivo_3.close()
  archivo_4.close()



def leer_Archivo(archivo):
    linea = archivo.readline()
    if linea !="":
        respuesta=linea.rstrip('\n').rstrip(',').rstrip('.').rstrip(';').rstrip('!').rstrip('¡').rstrip("?").rstrip('¿').rstrip('-').rstrip('_').rstrip('"').rstrip('*').rstrip('<<').rstrip('>>').split(' ') 
    else :
        respuesta=""
    return respuesta

def grabar_Nuevo(archivo,palabra,cantidad1,cantidad2,cantidad3):
    archivo.write(str(palabra) + ',' + str(cantidad1) +","+ str(cantidad2) +","+ str(cantidad3) +'\n')


def analizador_texto(texto,num_text,LONG):
  palabras=leer_Archivo(texto)
  while (palabras !=""):
    for palabra in palabras :
      if (palabra.isalpha()) and (palabra!="") and (len(palabra)==LONG) :
        if palabra.lower() in dicc_palabra:
          if num_text ==1:
            dicc_palabra[palabra.lower()][0]+=1
          elif num_text ==2:
            dicc_palabra[palabra.lower()][1]+=1
          else:
            dicc_palabra[palabra.lower()][2]+=1
        else:
          if num_text ==1:
            dicc_palabra.setdefault(palabra.lower(),[1,0,0])
          elif num_text ==2:
            dicc_palabra.setdefault(palabra.lower(),[0,1,0])
          else:
            dicc_palabra.setdefault(palabra.lower(),[0,0,1])
    palabras=leer_Archivo(texto)

def ordenar_palabras(archivo_4):
    palabras_ordenadas=sorted(dicc_palabra.items(),key=operator.itemgetter(0))
    for elementos in palabras_ordenadas:
      palabra=elementos[0]
      cant_1=elementos[1][0]
      cant_2=elementos[1][1]
      cant_3=elementos[1][2]
      grabar_Nuevo(archivo_4,palabra,cant_1,cant_2,cant_3)
    return palabras_ordenadas

