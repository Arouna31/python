#Liste
elements = ['a', 'b', 3]
elements.remove(3)
elements.append('c')

print(elements)

#Dictionnaire
person = {
    'name': 'Faical',
    'age': 30,
    'job': 'Developper'
}
person['age'] = 55

print(person)

#Tuple
colorTuple = ('rouge', 'blanc', 'jaune')
#colorTuple['rouge'] = 'vert' #Les tuples sont immuables

print(colorTuple[1])

#Set/ Ensemble
nombres = {'rouge', 'rouge', 'blanc'}

print(nombres)