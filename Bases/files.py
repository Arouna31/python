#Create file
with open('file.txt', 'x') as file:
        file.write('Je suis le premier texte du fichier')

#Read file
try:
    file = open('file.txt', 'r')
    fileContent = file.read()
    print(fileContent)
    file.close()
except FileNotFoundError:
    print('File has\'nt been create')

