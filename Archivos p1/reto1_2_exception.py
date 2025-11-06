#Para este caso no considero que deba haber un error ya que es un codigo robusto , al estar el str no habrian tantos potenciales errores

def palindromo(palabra):
    #.lower() para ignorar mayusculas y minusculas lo que hace mas entendible el codigo
    
    palabra=str(palabra).lower()
    #Esto para la longitud de la palabra
    n_palabra=len(palabra)
    #Recorremos la palabra desde el inicio hasta la mitad
    #y comparamos con la letra correspondiente desde el final
    for i in range(n_palabra//2):
        if palabra[i] != palabra[n_palabra - i - 1]:
            print("No es un palindromo")
            return False #Si no es palindromo retorna falso
        else:
            print("es un palidromo")
   
    return True  


if __name__ == "__main__":
    
  palabra=str(input("Ingrese una palabra: "))
  palindromo(palabra)