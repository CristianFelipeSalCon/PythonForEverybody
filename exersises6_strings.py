#Exercise 1: Write a while loop that starts at the last character in the string 
#and works its way backwards to the first character in the string, printing each
#letter on a separate line, except backwards.

fruit="Banana"
# B A N A N A
#-6-5-4-3-2-1
index=-len(fruit)
while index<0:
    letter=fruit[index]
    print(f"la posicion de indice es {index} y su letra es: { letter}")
    index+=1

for i in fruit:
    print(i)

#Exercise 3: Encapsulate this code in a function named count, and generalize 
# it so that it accepts the string and the letter as arguments.        
def count(letra,palabra):
    conteo=0
    for i in palabra:
        if i==letra:
            conteo+=1 
    return f"La letra deseada fue {letra} y aparecio : {conteo} veces"
busca=count(letra="n",palabra="banana")
print(busca)

#Exercise 4: There is a string method called count that is similar to the function 
# in the previous exercise. Read the documentation of this method at:
#https://docs.python.org/library/stdtypes.html#string-methods
#Write an invocation that counts the number of times the letter a occurs in “banana”.

word="banana"
#.count() tells us how many a letter or words appers in the variable, also
#there is a 2 argument, we can set where we want to start to search
print(word.count("a"))# for example here we wanto to know how many times a appers in 
#word
print(word.count("a",2))#and here we want to search how many times a appers in world 
#since in 2 position.

#Parsing strings

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')#we want to know where @ is located.
print(atpos)

#Exercise 5: Take the following Python code that stores a string:
#str = 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after the colon 
# character and then use the float function to convert the extracted string into
#  a floating point number.
str = 'X-DSPAM-Confidence:0.8475'
print(str.find(":"))
str=float(str[19:])
print(str,type(str))

#Exercise 6: Read the documentation of the string methods at
#  https://docs.python.org/library/stdtypes.html#string-methods 

# You might want to experiment with some of them to make sure you 
# understand how they work. strip and replace are particularly useful.
#The documentation uses a syntax that might be confusing. For example, 
# #in find(sub[, start[, end]]), the brackets indicate optional arguments.
#  So sub is required, but start is optional, and if you include start, 
# then end is optional.

#str.replace(old, new[, count])
#Return a copy of the string with all occurrences of substring old replaced 
# by new. If the optional argument count is given, only the first count 
# occurrences are replaced.

hola="te amo"
print(hola.replace("amo","odio"))#we have replace amo to odio.
print(hola.replace("a","pppo"[3:])) #we have replace all a to the letter that is in 3 position.
print(hola.replace("a","pppo"[2:]) )#we have replace all a to all the letters that are in 2 position until the end.

#str.lstrip([chars])
#Return a copy of the string with leading characters removed. 
# The chars argument is a string specifying the set of characters to be removed.
#  If omitted or None, the chars argument defaults to removing whitespace. 
# The chars argument is not a prefix; rather, all combinations of its values are 
# stripped:

#'   spacious   '.lstrip() if there is nothing in its arguments, all left spaces are going to  be remobed
#'spacious   '
print('www.example.com.lstrip("cmowz.")','www.example.com'.lstrip('cmowz.'))
# it remove all the characteres  that have on its left enven the <. > but there is not space.
#'example.com'
print("'   spacious   '.lstrip()",'   spacious   '.lstrip())

" hola como estas?".lstrip(" h")#we remobe space and h.

" hola. como estas?".lstrip(" phal")#we remove space an h,but not a but we know that there is 
#one a there, so why can we not remobe it?

" hola. como estas?".lstrip("  plha.ocsem ")#we have remobed space,and all leter that are in its argument.
#but as we can see there is even a space in the right argument, it means that has to check
#if there other words or letter that match with the letter are in argument, so as to remobe them too.

'Arthur: three!'.lstrip('Arthur: ')#there a space include in its argument
#so it can remobe letters in other words.

#str.rstrip([chars])
#Return a copy of the string with trailing characters removed. 
# The chars argument is a string specifying the set of characters to be removed. 
'   spacious   '.rstrip()# If omitted or None, the chars argument defaults 
#to removing right whitespace. 
# The chars argument is not a suffix; rather,
#  all combinations of its values are stripped:

'mississippi'.rstrip('ipz')#.rstrip("ipz") remove as a loop, rstrip starts on the right
# of the sentence, so it is going to ask what is the first right string, the first
#is i, and i is in its arguments so it is removed,the next variable is p, and it is removed
# twoice, and after is i again and it is removed, but the next variable is s, and we dont
# have s in rstrip argument so this function stops here. 

#'mississ'

'Monty Python'.rstrip(' Python')#there is a space on the left, it means that can remove
#the letters that are in other words and if the letter are in rstring arguments match.
#'M'

#See str.removesuffix() for a method that will remove a single suffix string 
# rather than all of a set of characters. For example:
#romevesuffix()remove only the word that match, no each letter.
print('Monty Python'.removesuffix(' Python'))
print("holo como estas".removesuffix("estas"))
print("holo como estas".removesuffix("esta"))# the word there is in argument does not
#match with any string, so we could not remove anything.
