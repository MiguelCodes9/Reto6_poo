#En este codigo no considero que deban existir exepciones ya que no hay que tratar tantos numero 
#que impliquen divisones por cero o algo que genere problemas , en si este codigo es robusto
def anagrama(lista):
    # Diccionario para agrupar palabras por su clave ordenada
    dic_grupos = {}
    #Este for recorre cada palabra en la lista
    for palabra in lista:
        clave = ''.join(sorted(palabra)) #Aqui cada palabra se ordena en sus letras alfabeticamente con sorted y se une con join
        #Si la clave ya existe en el diccionario, se agrega la palabra a la lista
        if clave in dic_grupos:
            dic_grupos[clave].append(palabra)
            #Si no existe, se crea una nueva entrada en el diccionario
        else:
            dic_grupos[clave] = [palabra]
    #Esta lista almacenara los grupos de anagramas encontrados
    anagramas = []
    #El for recorre los valores del diccionario
    for grupo in dic_grupos.values(): #values() devuelve las listas de palabras, es decir, los valores del diccionario
        #Si el grupo tiene mas de una palabra, es un anagrama, ya que una sola palabra no puede ser anagrama de si misma
        if len(grupo) > 1:
         anagramas.append(grupo) #Se agrega el grupo a la lista de anagramas

    #Impresion de resultados, si es un anamrgrama recorre la lista e imprime las palabras
    if anagramas:
        print("Palabras que son anagramas entre sí:")
        for grupo in anagramas:
            print(', '.join(grupo)) #join une las palabras con una coma y un espacio
    else:
        print("No se encontraron anagramas.") #Si no se encontraron anagramas
    return anagramas




#Aqui es la parte donde se pide la lista de palabras y se llama a la funcion

if __name__ == "__main__":
    texto = input("Ingrese una lista de palabras separadas por espacio: ")
    lista = texto.split() #Split divide el texto en una lista de palabras
    anagrama(lista)