# UTN-TUPaDProgramacion1
Trabajo Practico de P1 uso de Git a traves de GitHub y GitHub Desktop

#1) Crea un programa que imprima el mensaje: "Hola Mundo!".
nombre = input("Hola Mundo!")
print("nombre")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado
nombre = input(" Ingrese su nombre: ")
print(f" Hola {nombre}.")

#3) Crea un programa que pida al usuario nombre, apellido, edad y lugar de residencia e imprima en pantalla una oracion con todos los datos ingresados
nombre = input(" Ingrese su nombre ")
apellido = input(" Ingrese su apellido ")
edad = input(" Ingrese su edad ")
lugar_de_residencia = input(" Ingrese su luigar de residencia ")
print (f"Soy {nombre} {apellido} tengo {edad} años y vivo en {lugar_de_residencia}") 


#4) Crea un programa que pida al usuario el radio de un circulo e imprima por pantalla su area y su perimetro 
radio = float(input(" Por favor ingrese el Radio del Circulo "))
area = radio*radio * 3.14159
perimetro = radio*2 * 3.14159
print (f" El area es {area} y el perimetro es {perimetro} ")

#5) Crea un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuantas horas equivale
segundos = float(input(" Ingrese los segundos para saber Horas "))
hora = segundos / 3600 
print (f"El resultado en horas es, {hora} ")

#6) Crea un programa que pida al usuario un nunmero e imprima por pantalla la tabla de multiplicar de dicho numero 
num = int(input(" Ingrese el numero para multiplicar "))
print("El resultado es: ")
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

#7) Crea un programa que pida al usuario dos numero enteros distintos de 0 y muestre por pantalla el resultado de sumarlos restarlos mutiplicarlos y dividirlos
num1 = int(input("Ingrese el primer numero "))
num2 = int(input("Ingrese el segundo numero "))
print("El resultado de la suma es: ", num1+num2)
print("El resultado de la resta es: ", num1-num2)
print("El resultado de la multiplicacion es: ", num1*num2)
print("El resultado de la division es ", num1/num2)

#8) Crea un programa que pida al usuario su altura y su peso e imprima por pantalla su IMC 
peso = float(input("Ingrese su Peso en Kilos "))
altura = float(input("Ingrese su altura en Metros "))
IMC = peso / (altura**2)
print("Su Indice de Masa Corporal es:", IMC)

#9) Crea un programa que pida al usuario una temperatura en Grados Celsius e imprima por pantalla su equivalente en Fahrenheit
temp = float(input("Ingrese la Temperatura en Celsius "))
temp_final = temp + 32 
print("La Temperatura en Fahrenheit es: ", temp_final)

#10) Crea un programa que pida al usuario 3 numeros e imprima por pantalla el promedio de dichos numero 
num1 = int(input("Ingrese el primer numero "))
num2 = int(input("Ingrese el segundo numero "))
num3 = int(input("Ingrese el tercer numero "))
prom = (num1 + num2 + num3) / 3 
print("El promedio es: ", prom)