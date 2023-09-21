
print("Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.")
import math
import random

for i in range(10):
    x=random.random()
    print(x)
for i in range(10):
    x=random.random()
    print(x)
for i in range(10):
    x=random.random()
    print(x)

print("Exercise 6: Rewrite your pay computation with time-and-a-half for over- time and create a function called computepay which takes two parameters (hours and rate).\n\nEnter Hours: 45\nEnter Rate: 10\nPay: 475.0")
def pago(hora,rate):
    if hora>40:
        horasextra=hora-40
        pago=(40*rate)+1.5*(horasextra*rate)
        return pago
    else:
        return hora*rate
print(pago(45,10))

def salario(hours, rate):
    if hours<40:
        salary=hours*rate
        return salary
    elif hours>40:
        horasextra=hours-40
        salary=(40*rate)+1.5*(horasextra*rate)
        return salary

x=salario(100,10)
print(x)

print("Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.\n\nScore  Grade \n>= 0.9  A\n>= 0.8  B\n>= 0.7  C\n>= 0.6  D\n<0.6  F\n\nEnter score: 0.95\nA\nEnter score: perfect\nBad score\nEnter score: 10.0\nBad score\nEnter score: 0.75\nC\nEnter score: 0.5\nF")
#this is a Void variable.
def nota(resultado):
    try:
        resultado=float(resultado)
        if resultado>=0 and resultado<=1:
            if resultado>=0.9:
                print("A")
            elif resultado>=0.8:
                print("B")
            elif resultado>=0.7:
                print("C")
            elif resultado>=0.6:
                print("D")
            elif resultado<0.6:
                print("F")
        if resultado<0 or resultado>1:
            print("intervalo incorrecto")
    except:
        print("debe ser un valor")



#this is a frutful variable
def grade(nota):
    try:
        nota=float(nota)
        if nota>=0 and nota<=1:
            if nota>=0.9:
                a="A"
                return a
            if nota>=0.8:
                b="B"
                return b
            elif nota>=0.7:
                c="C"
                return c
            elif nota>=0.6:
                d="D"
                return d
            elif nota <0.6:
                f="F"
                return f
        if nota<0 or nota>1:
            t="el valor es incorrecto"
            return t
    except:
        z="el resultado debe ser un digito"
        return z


# forma mas facil de hacer.
def grade(nota):
    try:
        nota=float(nota)
        if nota>=0 and nota <=1:
            if nota>=0.9:
                return "A"
            if nota>=0.8:
                return "B"
            if nota>=0.7:
                return "C"
            if nota>=0.6:
                return "D"
            if nota<0.6:
                return "F"
        if nota<0 or nota>1:
            return "El valor esta fuera del rango"
    except:
        return "Debe digitar un numero del intervalo de [0-1]"
x=grade(1)
print(x)
