# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general.

def potenciaNumero(exponente, numero):
    if exponente == 0:
        return 1
    else:
        return numero * potenciaNumero(exponente - 1,  numero)


#---------PROGRAMA PRINCIPAL------------

numeroBase = int(input("Ingrese un número: ")) 
exponente = int(input("Ingrese un exponente: "))

print(f"{numeroBase} elevado a {exponente} es igual a {potenciaNumero(exponente, numeroBase)}")

