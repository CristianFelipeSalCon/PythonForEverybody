#Cristian Felipe Salinas Conteras
print("Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.")

nombre=None
count=0
total=0

while True:
    nombre=input("> Digite numero o <done> cuando termine: ")
    try:
        nombre=float(nombre)
        count=count+1
        total=nombre+total
        print("count= ",count)
        print("total= ",total)
    except:
        if nombre=="done":
            break
        print("You wrote a wrong letter")
print("Total: ",total,"Count: ",count,"average: ",total/count)

print("Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.")
nombre=None
mini=None
maxi=None
while True:
    nombre=input("> Digite numero o <done> cuando termine: ")
    try:
        nombre=float(nombre)
        if mini is None or nombre<mini:
            mini=nombre
        elif maxi is None or nombre>maxi:
            maxi=nombre
    except:
        if nombre=="done":
            break
        print("You wrote a wrong letter")
print("Minimo: ",mini,"Maximo: ", maxi)
