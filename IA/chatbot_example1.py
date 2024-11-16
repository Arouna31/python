import spacy

nlp = spacy.load("fr_core_news_sm")


def chatbot_response(message: str) -> str:
    doc = nlp(message)

    if "réserver" or "reserver" in [token.lemma_ for token in doc]:
        destination: str = None
        for ent in doc.ents:
            if ent.label_ == "LOC":  # GPE : lieux géographique (villes, pays)
                destination = ent.text
                break
        if destination:
            return f"Je peux vous aider à reserver un vol pour {destination}."
        else:
            return "Pour quelle destination voulez vous réserver un vol ?"
    else:
        return "je ne suis pas sûr de comprendre. Pouvez-vous reformuler ?"


user_input = "Je veux faire une réservation de vol pour Abidjan."
reponse = chatbot_response(user_input)
print(reponse)
