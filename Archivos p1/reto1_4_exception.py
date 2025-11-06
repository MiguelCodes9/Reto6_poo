def numeritos(n):
    
     lista_primer=[]
     
     for i in range(n):
          f=i+1
          try:
            n_cuenta = int(input("-------->"))
            lista_primer.append(n_cuenta)
            #En caso de que haya un valor invalido
          except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
            i -= 1  # En caso de error se repite la peticion
            continue
     print("La lista de los numeros es=",lista_primer)
     
     if len(lista_primer) < 2:
            print("Error: Se necesitan al menos 2 números para calcular sumas consecutivas")
            return None
     elemento_de_lista = lista_primer[0] + lista_primer[1] 
    
     for i in range(1, n- 1):
        suma = lista_primer[i] + lista_primer[i + 1]
        if suma > elemento_de_lista:
           elemento_de_lista = suma
     
     print("La mayor suma de numeros consecutivos es=",elemento_de_lista)
     
   
     return(elemento_de_lista)

while True:
  try:
     print("---PROGRAMA PARA EVALUAR LA MAYOR SUMA DE CONSECUTIVOS---")
     print("  Indicaciones:                                        -|")
     print("->Por favor ingresa mas de dos numeros en la lista     -|")
     print("->Pulsa cero para salir del programa                   -|")
     n_datos=int(input("Por favor ingrese el numero de datos de la lista="))
     if n_datos <2 and n_datos>0 or n_datos<0:
          print("-------INGRESA DOS DATOS O MAS------- ")
     elif n_datos==0:
         print("Programa finalizado!")
         break
     else:
         numeritos(n_datos)
         #Aqui por si es el mismo error de ingresar los numeros 
  except ValueError:
      print("Error: Debe ingresar un número entero válido")