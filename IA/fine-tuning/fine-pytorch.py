from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
)

# Charger le jeu de données / dans le fichier train.txt
dataset = load_dataset("text", data_files={"train": "train.txt"})

# Charger le tokenizer et le modèle pré-entraîné  (GPT2)
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Associer le pad_token au eos_token
tokenizer.pad_token = tokenizer.eos_token


# Tokeniser les données
def tokenize_function(examples):
    return tokenizer(
        examples["text"], truncation=True, padding="max_length", max_length=128
    )


tokenized_datasets = dataset.map(
    tokenize_function, batched=True, remove_columns=["text"]
)

# Configurer les arguments d'entraînement
training_args = TrainingArguments(
    output_dir="./results",  # Dossier de sauvegarde des modèles
    evaluation_strategy="epoch",  # Évaluer après chaque époque
    learning_rate=5e-5,  # Taux d'apprentissage
    num_train_epochs=3,  # Nombre d'époques
    save_strategy="epoch",  # Sauvegarder après chaque époque
    logging_dir="./logs",  # Dossier de sauvegarde des logs
    logging_steps=10,  # Fréquence de sauvegarde des logs
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
)

# Lancer le processus d'entraînement (Fine-tuning)
trainer.train()

# Sauvegarder le modèle fine-tuné

model.save_pretrained("./my_finetuned_gpt2")
tokenizer.save_pretrained("./my_finetuned_gpt2")


# Utilisation du modèle fine-tuné


# Charger le modèle fine-tuné
model = AutoModelForCausalLM.from_pretrained("./my_finetuned_gpt2")
tokenizer = AutoTokenizer.from_pretrained("./my_finetuned_gpt2")

# Générer une réponse à une question
prompt = "Question: What is AI?\nAnswer:"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    inputs["input_ids"],
    max_length=50,
    num_return_sequences=1,
    pad_token_id=tokenizer.pad_token_id,
)

# Afficher la réponse générée
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
