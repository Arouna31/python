from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    TFAutoModelForCausalLM,
    DataCollatorForLanguageModeling,
    create_optimizer,
)
import tensorflow as tf

# Charger le jeu de données
dataset = load_dataset("text", data_files={"train": "train.txt"})

# Charger le tokenizer et le modèle pré-entraîné (GPT-2)
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForCausalLM.from_pretrained(model_name)


# Tokeniser les données
def tokenize_function(examples):
    return tokenizer(
        examples["text"], truncation=True, padding="max_length", max_length=128
    )


tokenized_datasets = dataset.map(
    tokenize_function, batched=True, remove_columns=["text"]
)

# Préparer les données pour TensorFlow
train_dataset = tokenized_datasets["train"].to_tf_dataset(
    columns=["input_ids", "attention_mask"],
    shuffle=True,
    batch_size=8,
    collate_fn=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
)

# Configurer l'optimiseur et le programme d'entraînement
num_train_steps = len(train_dataset) * 3  # 3 époques
optimizer, schedule = create_optimizer(
    init_lr=5e-5,
    num_warmup_steps=0,
    num_train_steps=num_train_steps,
)

# Compiler le modèle avec TensorFlow
model.compile(optimizer=optimizer)

# Entraîner le modèle
model.fit(train_dataset, epochs=3)

# Sauvegarder le modèle fine-tuné
model.save_pretrained("./my_finetuned_gpt2")
tokenizer.save_pretrained("./my_finetuned_gpt2")

# Charger le modèle fine-tuné pour la génération
model = TFAutoModelForCausalLM.from_pretrained("./my_finetuned_gpt2")
tokenizer = AutoTokenizer.from_pretrained("./my_finetuned_gpt2")

# Générer une réponse
prompt = "Question: What is AI?\nAnswer:"
inputs = tokenizer(prompt, return_tensors="tf")
outputs = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=1)

# Afficher la réponse générée
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
