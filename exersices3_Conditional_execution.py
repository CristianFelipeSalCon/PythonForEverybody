print("Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.\n\nEnter Hours: 45\nEnter Rate: 10\nPay: 475.0")

hournormal=40
rate=10
extratime=45
leftover=extratime-40
paid=hournormal*rate+(1.5*(leftover)*rate)
print("hournormal=40\nrate=10\nextratime=45\nleftover=extratime-40\npaid=hournormal*rate+1.5*(leftover)*rate","paid: ",paid)
# another form to do this point.
leftover=None
paid=None
rate=None
hournormal=None
workt=float(input("text your work hours: "))
if workt<=40:
    rate=10
    print("paid: ", workt*rate)
else:# here i did a nested condition
    if workt>40:
        rate=10
        hournormal=40
        leftover=workt-40
        paid=hournormal*rate+1.5*leftover*rate
        print("paid: ",paid)
print("Exercise 2: Rewrite your pay program using try and except so that\nyour program handles non-numeric input gracefully by printing a message\nand exiting the program. The following shows two executions of the\nprogram:\n\nEnter Hours: 20\nEnter Rate: nine\nError, please enter numeric input\nEnter Hours: forty\nError, please enter numeric input\n")

leftover=None
paid=None
rate=None
hournormal=None


try:
    workt=float(input("text your work hours: "))
except:
    print("Ypu have written a non-numeric")

if workt<=40: # we can see that if we put a str in workt
#we dont get an error here because whole conditions are false.
    rate=10
    print("paid: ", workt*rate)
else:
    rate=10
    hournormal=40
    leftover=workt-40
    paid=hournormal*rate+1.5*leftover*rate
    print("paid: ",paid)

print(" Exercise 3: Write a program to prompt for a score between 0.0 and\n1.0. If the score is out of range, print an error message.\nIf the score is between 0.0 and 1.0, print a grade using the following table:\n\nScore  Grade\n>= 0.9  A\n>= 0.8  B\n>= 0.7  C\n>= 0.6  D\n<0.6  F\n\nEnter score: 0.95\nA\n\nEnter score: perfect\nBad score\n\nEnter score: 10.0\nBad score\n\nEnter score: 0.75\nC\n\nEnter score: 0.5\nF\n\nRun the program repeatedly as shown above to test the various different values for\ninput.")

note=input("What your score was:  ")
try:
    note=float(note)
    if note>=0.9 and note <=1:
        print("A")
    elif note >=0.8 and note <0.9:
        print("B")
    elif note >=0.7 and note <= 0.8:
        print("C")
    elif note >= 0.6 and note <= 0.7:
        print("D")
    elif note>=0 and note < 0.6:
        print("F")
    elif note>1 or note<0:
        print("your score must be aimd 0-1")
except:
    print("Error, please enter numeric")

print("otra manera de hacerlo")

score=input("What is your score?\n")
try:
    score=float(score)
    if score>=0 and score<=1:
            #we have done a nested condition
        if score>=0.9:
            print("Your grade was A")
        elif score>=0.8:
            print("your socre was B")
        elif score>=0.7:
            print("Your score was C")
        elif score>=0.6:
            print("Your score was D")
        elif score < 0.6:
            print("Your score was F")
    else:
        print("Bad score")
except:
     print("Digit a number, please")
