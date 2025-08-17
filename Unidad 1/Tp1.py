"""
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola mundo")

"""
"""
2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.

print("Ingresa tu nombre")
nombre=input()
print(f"¡Hola {nombre}!")
"""
"""
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.

print("Ingrese nombre")
nombre=input()
print("Ingrese apellido")
apellido=input()
print("Ingrese su edad")
edad=input()
print("Ingrese su lugar de residencia")
residencia=input()
print(f"Soy {nombre} {apellido} tengo {edad} años y soy de {residencia}")
"""
"""
4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.

print("Ingrese el radio del circulo a calcular: ")
radio = float(input())
area=3.14 * radio**2
perimetro=2 * 3.14 * radio
print(f"El area del circulo es:{area} cm y su perimetro de:{perimetro} cm ")
"""
"""
5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.

print("Ingrese cantidad de segundos a convertir: ")
segundos=int(input())
horas= float(segundos/3600)
print(f"{segundos} segundos equivale a {horas} horas")
"""
"""
6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número

print("Ingrese un numero para la tabla de multiplicar que desea: ")
num=int(input())
print(num*1)
print(num*2)
print(num*3)
print(num*4)
print(num*5)
print(num*6)
print(num*7)
print(num*8)
print(num*9)
print(num*10)
"""
"""
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Ingrese dos nùmeros enteros que no sean el nùmero 0: ")
num1=int(input())
num2=int(input())
print(f"suma {num1+num2}")
print(f"resta {num1-num2}")
print(f"multiplicacion {num1*num2}")
print(f"division {num1/num2}")
"""
"""
8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:
        𝐼𝑀𝐶 =𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

print("Ingrese su peso en kg: ")
peso=float(input())
print("Ingrese su altura en m")
altura=float(input())
imc=(peso/altura**2)
print(f" El indice de masa corporal de esta persona es de {imc}")
"""
"""
9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
        𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 x 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

print("Ingrese temperatura en celsius: ")
celsius= float(input())
farenheit= (9/5 * celsius)+32
print(f"La temperatura en farenheit es {farenheit}")
"""
"""
10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.

print("Ingrese primer numero")
n1=int(input())
print("Ingrese segundo numero")
n2=int(input())
print("Ingrese tercer numero")
n3=int(input())
promedio= float(n1+n2+n3)/3
print(f"El promedio es :{promedio}")
"""