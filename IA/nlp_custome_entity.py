import spacy
from spacy.tokens import Span

nlp = spacy.load('fr_core_news_sm')

text = "Babi est une ville de la Côte d'ivoire"

doc = nlp(text)

#Ajout d'une nouvelle entité personnalisée nom reconnue
newEntity = Span(doc, 0, 1, label="Capitale") 
doc.ents = list(doc.ents) + [newEntity]

for entity in doc.ents:
  print(entity.text, entity.label_)

print('__________________________________________')
