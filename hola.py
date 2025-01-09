from os import system  # Importa la función system del módulo os

nombre = "juan"  # Define la variable nombre con el valor "juan"
edad = 20  # Define la variable edad con el valor 20
print("Hola", nombre, "tienes", edad, "años")  # Imprime un saludo con el nombre y la edad

i = 0  # Inicializa la variable i con el valor 0
for i in range(5):  # Bucle for que itera 5 veces
    print(f"iteracion {i}")  # Imprime el número de iteración

o = 0  # Inicializa la variable o con el valor 0
while o < 5:  # Bucle while que se ejecuta mientras o sea menor que 5
    print(o)  # Imprime el valor de o
    o += 1  # Incrementa o en 1

def saludo(nombre):  # Define la función saludo que toma un parámetro nombre
    return f"Hola {nombre}"  # Retorna un saludo con el nombre

print(saludo(nombre))  # Llama a la función saludo y imprime el resultado

numeros = [1, 2, 3, 4, 5]  # Define una lista de números
nombres = ["juan", "pedro", "luis", "maria", "jose"]  # Define una lista de nombres

def pedir_indice():  # Define la función pedir_indice
    while True:  # Bucle infinito
        try:  # Intenta ejecutar el siguiente bloque de código
            indice = int(input("Ingresa un indice: "))  # Pide al usuario que ingrese un índice y lo convierte a entero
            return indice  # Retorna el índice si la conversión fue exitosa
        except ValueError:  # Si ocurre un ValueError (la conversión falló)
            print("Ingresa un numero valido")  # Imprime un mensaje de error

indice = pedir_indice()  # Llama a la función pedir_indice y guarda el resultado en la variable indice
print(numeros[indice])  # Imprime el elemento de la lista numeros en la posición indice

def pedir_nombre():  # Define la función pedir_nombre
    while True:  # Bucle infinito
        nombre = input("Ingresa un nombre: ")  # Pide al usuario que ingrese un nombre
        if nombre in nombres:  # Si el nombre está en la lista nombres
            return nombre  # Retorna el nombre
        else:  # Si el nombre no está en la lista nombres
            print("Nombre no valido")  # Imprime un mensaje de error

nombre = pedir_nombre() # Llama a la función pedir_nombre y guarda el resultado en la variable nombre
print(f"Hola {nombre}")  # Imprime un saludo con el nombre

import math

print(math.sqrt(16))  # Imprime la raíz cuadrada de 16
print(math.pi)  # Imprime el valor de pi

try:  # Intenta ejecutar el siguiente bloque de código
    resultado = 10/0
except ZeroDivisionError:
    print("No se puede dividir por cero")

#dar un numero entero y que retorne los numeros primos.  necesito que lo pida en esta funcion y no utilize las de arriba
def es_primo(numero):  # Define la función es_primo que toma un parámetro numero
    if numero < 2:  # Si el número es menor que 2
        return False  # No es primo
    for i in range(2, int(math.sqrt(numero)) + 1):  # Bucle for que itera desde 2 hasta la raíz cuadrada del número
        if numero % i == 0:  # Si el número es divisible por i
            return False  # No es primo
    return True  # Es primo