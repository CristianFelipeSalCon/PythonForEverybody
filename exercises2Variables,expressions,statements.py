#NAME: Cristian Felipe Salinas
print("Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.\n\nEnter your name: Chuck\nHello Chuck")
name=input("Enter your name: ")
print(name)

print("Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.\n\nEnter Hours: 35\n\nEnter Rate: 2.75\nPay: 96.25")
hour=int(input("Enter hours: "))#aca pido un numero de horas y automaticamente convierte
#la varibale str a int
rate=float(input("Enter rate: "))
pay= rate*hour
print("hour * rate= ", pay)

payround=round(rate*hour)# here we want to see only  integers
print("hour * rate= ", payround)

print("Exercise 4: Assume that we execute the following assignment state- ments:\n\nwidth = 17height = 12.0\n\nFor each of the following expressions, write the value of the expression and the type (of the value of the expression).\n\n1. width//2\n2. width/2.0\n3. height/3\n4. 1 + 2 * 5")
width=17
height=12.0
print("width//2= ",width//2)
print("width//2.0= ",width//2.0)
print("height/3= ",height/3)
print("1+2*5= ",1+2*5)

print("Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.")
#Fórmula : (0 °C × 9/5) + 32 = 32 °F
celsius=int(input("what is the tempeture righ now in celsius?\n"))
#we must remember that input put all the variables in str, so i used int()
#in the same line so as to convert that variable in int.
fahrenheit=(celsius*9/5)+32
print("tempeture that we asked in Celsius was: ",celsius,"to Fahrenheit is: ",fahrenheit)
