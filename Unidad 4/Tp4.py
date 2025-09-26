"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for num in range(0,101):
    print(num)
"""
"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.

entero= int(input("Ingrese un numero entero: "))
cifras= len(str(entero))
print(f"El nùmero posee:{cifras} cifras")
"""
"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores
"""
"""
num_1=int(input("Ingrese primer numero entero: "))
num_2=int(input("Ingrese segundo numero entero: "))
sumador=0
for x in range(num_1+1,num_2):
    sumador += x
print(f"La suma es = {sumador}")
"""
"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
"""
sumad=0
num=0
while True:
        num=int(input("Ingrese numeros a sumar: "))
        sumad += num
        if num == 0:
            break
print(f"La suma total es de {sumad}")
"""
"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import randint

numero=randint(0,9)
intento=0

while True:
    usuario=int(input("Adivina el numero entre 0 y 9 (Presiona 11 para salir): "))
    intento +=1
    if usuario == 11:
        print("Gracias por jugar")
        break
    
    if usuario == numero:
        print(f"Acertaste, los intentos fueron {intento}")
"""    
"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.

for x in range(100,0-1,-2):
    print(x)
"""
"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
"""
sumador=0

user=int(input("Ingrese numero entero positivo: "))

for x in range(0,user +1):
    sumador = sumador + x
print(f"El resultado de la suma desde 0 a {user} es = {sumador}")
"""
"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares=0
impares=0
negativos=0
positivos=0

for x in range(1,100 +1):
    user=int(int(input("Ingrese  numeros enteros positivos del 1 al 100: ")))
    if (user > 0):
        positivos+=1
    if(user%2==0):
        pares+=1
    if (user%2!=0):
        impares+=1
    if(user < 0):
        negativos+=1
print(f"los positivos son {positivos}\n, los pares son {pares}\n,los impares son {impares}\n, los negativos son {negativos}")
"""
"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).

total=0
media=0
for x in range (1,100 + 1):
    numeros=int(input("ingrese 100 numeros para calcular la media: "))
    total = numeros+total 
    media = total / x
print (media)
"""
"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

unidad=0
decena=0
centena=0
numero = int(input("ingrese un numero para invertir: "))
centena = numero // 100 
decena = (numero // 10) % 10
unidad = numero % 10
invertido = unidad * 100 + decena * 10 + centena

print(invertido)
"""