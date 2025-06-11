from transformers import pipeline

# Charger le modèle pré-entraîné de génération de texte
generator = pipeline("text-generation", model="gpt2")

# Générer une réponse
prompt = "What is the future of artificial intelligence?"
response = generator(prompt, max_length=50)
print(response[0]["generated_text"])
