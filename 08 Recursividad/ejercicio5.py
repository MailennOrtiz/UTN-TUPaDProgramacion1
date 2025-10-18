# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed()

# devolver true si es palindromo 
# devolver false si no 

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True 
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1])

#----------PROGRAMA PRINCIPAL-----------

tieneTilde = ["á", "é", "í", "ó", "ú"]

tilde = True 

while tilde:
    cadena = input("Ingrese una palabra sin tildes: ").lower().replace(" ", "")
    
    tilde_encontrada = False

    for letra in cadena:
        if letra in tieneTilde: 
            print("La palabra no debe contener tildes. Intente nuevamente...")
            tilde_encontrada = True
    
    if not tilde_encontrada:
        print(es_palindromo(cadena))
        tilde = False  

