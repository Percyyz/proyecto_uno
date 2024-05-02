##  1.-Escribe un programa que tome un número como entrada e imprima si es par o impar.
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

## 2.-Escribe un programa que solicite al usuario que ingrese una contraseña y luego verifique si es la contraseña correcta.
contraseña = "secreto"
input_contraseña = input("Ingrese la contraseña: ")
if input_contraseña == contraseña:
    print("Contraseña correcta. Bienvenido.")
else:
    print("Contraseña incorrecta. Inténtelo de nuevo.")

## 1.-Escribe un programa que sume todos los números en un rango dado.
suma = 0
for i in range(1, 11):
    suma += i
print("La suma de los números del 1 al 10 es:", suma)

## 2.-Escribe un programa que calcule el factorial de un número dado.
numero = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print("El factorial de", numero, "es:", factorial)