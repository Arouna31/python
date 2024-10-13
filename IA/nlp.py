import spacy

# Charger le modèle de langue français
nlp = spacy.load('fr_core_news_sm')


# Texte à analyser
texte = "ChatGPT est un puissant modèle de langage créé par OpenAI."

# Traiter le texte
doc = nlp(texte)

# Afficher les tokens
for token in doc:
    print(f'Token: {token.text}')
    
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# Afficher la lemmisation, ramener chaque mots à sa forme de base
for token in doc:
    print(f'Token: {token.text}, Lemme: {token.lemma_}, POS: {token.pos_}')

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# Affichage NER / Nommage de toutes les entités (personnes, lieux, organisations)
for ent in doc.ents:
    print(ent)

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

#Affichage de l'analyse syntaxique
for token in doc:
    print(f'Mot: {token.text}, Dépendance: {token.dep_}, Mot racine: {token.head.text}')