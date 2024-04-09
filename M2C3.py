#Exercise 1
#String
name = 'Ainara'

#Number
subtotal = 52.30

#List
ingredients = ['Pepper', 'Tomato', 'Pasta', 'Onion']

#Boolean
exercise_done = True 



print(name)
print(subtotal)
print(ingredients)
print(exercise_done)


#Exercise 2
sentence = 'The real world'
first_word = sentence[0:3]

print(first_word)


#Exercise 3
ingredients = ['Pepper', 'Tomato', 'Pasta', 'Onion']
print(ingredients[0])


#Exercise 4
subtotal = 89
total = subtotal + 10
print(total)


#Exercise 5
ingredients = ['Pepper', 'Tomato', 'Pasta', 'Onion']
print(ingredients[-1])


#Exercise 6
names = 'harry,alex,susie,jared,gail,conner'
name_list = names.split(',')

print(name_list)


#Exercise 7
sentence = 'Bluey is the best kids show ever'
upper_word = sentence[0:5].upper()
new_sentence = upper_word + sentence[5:]

print(new_sentence)


#Exercise 8
age = 48
students_age = f'{age}'
print(students_age)


#Exercise 9
print('hello world')


#Además necesito que me crees una cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".

sentence = 'Hola a todo el mundo'
greeting = sentence.find('Hola')
greeting_two = sentence.index('Hola')
new_sentence = sentence.replace('Hola', 'adiós')

print(greeting)
print(greeting_two)
print(new_sentence)