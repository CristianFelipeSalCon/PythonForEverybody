#Name: Cristian Felipe Salinas Contreras
print("Exercise 1: Write a program to read through a file and print the contents of the file (line by line) are all in upper case. Executing the program will look as follows:")
mboxshort=open("mbox-short.txt")
mboxshort=mboxshort.read()
mboxshort=mboxshort.upper()
print(mboxshort)

mboxshort=open("mbox-short.txt")
mbox=open("mbox.txt")

for i in mbox:
    i=i.upper()
    print(f"{i}")

#we are asking how many lines there are in this file.
mboxshort=open("mbox-short.txt")
count=0
for i in mboxshort:
    count+=1
    
print(f"Numero de lineas: {count}")
#we are asking how many characters there are in this file.
mboxshort=open("mbox-short.txt")
lista=[]
for i in mboxshort:
    lista.extend(i) 
    
print(f"what is the weight of lista?: {len(lista)}")


#Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, 
#they add a harmless Easter Egg to their program. Modify the program that prompts 
# the user for the file name so that it prints a funny message when the user types 
# in the exact file name “na na boo boo”. The program should behave normally for 
# all other files which exist and don’t exist. Here is a sample execution of the 
# program:

#in this loop we are going to ask how many character, and line there are:
#and we are going to set all characters to Upper.
while True:
    lista=[]
    count=0
    filename=input("What kind of file you are interested in?")
    try:
        if filename=="Done":
            break

        file=open(filename)
        
        #1) upper
        for i in file:
            i=i.upper()
            count+=1
            print(f"{i}")
        file=open(filename)
        for i in file:
            lista.extend(i)
            

        print(f"Numero de lineas: {count},what is the weight of lista?: {len(lista)}")

        
    except:
        print("This file does not exist.")
