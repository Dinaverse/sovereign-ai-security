#!/usr/bin/env python3
import os
import numpy as np
import tritonclient.http as httpclient
from transformers import BertTokenizer
import argparse

# Configuration
TRITON_URL = "localhost:8000"
MODEL_NAME = "sid-minibert-onnx"
CATEGORIES = [
    "Address", "Bank Account", "Credit Card", "Email", "Gov ID",
    "Location", "Name", "Password", "Phone", "Secret Key"
]

def infer_line(client, tokenizer, text):
    """Envoie un texte au serveur Triton local et retourne les détections."""
    encoded = tokenizer(text, padding='max_length', truncation=True, max_length=256, return_tensors="np")
    
    input_ids = encoded['input_ids'].astype(np.int64)
    attention_mask = encoded['attention_mask'].astype(np.int64)
    token_type_ids = encoded['token_type_ids'].astype(np.int64)

    inputs = [
        httpclient.InferInput("input_ids", input_ids.shape, "INT64"),
        httpclient.InferInput("attention_mask", attention_mask.shape, "INT64"),
        httpclient.InferInput("token_type_ids", token_type_ids.shape, "INT64"),
    ]
    inputs[0].set_data_from_numpy(input_ids)
    inputs[1].set_data_from_numpy(attention_mask)
    inputs[2].set_data_from_numpy(token_type_ids)

    outputs = [httpclient.InferRequestedOutput("output")]
    response = client.infer(MODEL_NAME, inputs, outputs=outputs)
    probs = response.as_numpy("output")[0]
    
    detections = [CATEGORIES[i] for i, p in enumerate(probs) if p > 0.5]
    return detections

def main():
    parser = argparse.ArgumentParser(description="Scanner IA Pro de secrets (NVIDIA Morpheus SID)")
    parser.add_argument("path", help="Fichier ou dossier à scanner")
    args = parser.parse_args()

    print("🚀 Chargement du Tokenizer BERT...")
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    try:
        client = httpclient.InferenceServerClient(url=TRITON_URL)
        if not client.is_model_ready(MODEL_NAME):
            print(f"❌ Le modèle {MODEL_NAME} n'est pas prêt. Lancez le Docker Triton d'abord.")
            return
    except Exception as e:
        print(f"❌ Erreur de connexion au serveur local : {e}")
        return

    print(f"🚀 Scan lancé sur : {args.path}")
    for root, _, files in os.walk(args.path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        line = line.strip()
                        if len(line) < 5: continue
                        found = infer_line(client, tokenizer, line)
                        if found:
                            print(f"⚠️ [{file}] Ligne {line_num} : {', '.join(found)}")
            except Exception:
                continue

if __name__ == "__main__":
    main()
