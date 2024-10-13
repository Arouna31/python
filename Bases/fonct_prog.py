#Convertir une liste de chaînes de caractères en majuscules
strings =  ['hakim', 'michelle', 'jean']
upperStrings = list(map(lambda string: string.upper(), strings))

print(upperStrings)

#Produire un générateur qui affiche un nombre de 1 à 5
def generator(n):
    while n < 6:
      yield n
      n += 1

for number in generator(1):
   print(number)     