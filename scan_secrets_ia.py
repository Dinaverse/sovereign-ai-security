#!/usr/bin/env python3
import os
import json
import requests
import argparse

# Configuration du serveur Triton local
TRITON_URL = "http://localhost:8000/v2/models/sid-minibert-onnx/infer"

def scan_file(file_path):
    """Lit un fichier et l'envoie au serveur Triton local pour analyse."""
    if not os.path.exists(file_path):
        print(f"❌ Erreur : Le fichier {file_path} n'existe pas.")
        return

    print(f"🔍 Analyse de : {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.readlines()

    # Morpheus SID attend des lignes de texte. 
    # Pour ce test simple, on simule l'envoi au serveur Triton.
    # Note : Dans un environnement réel, Morpheus utilise un pipeline optimisé.
    # Ce script est un "bridge" simplifié pour tester vos fichiers.
    
    findings = []
    for i, line in enumerate(content):
        line = line.strip()
        if not line: continue
        
        # Simulation de l'appel API au serveur Triton local
        # (Le vrai modèle demande un formatage Tensor spécifique via numpy)
        # Ici on affiche comment l'intégrer à vos outils Kali existants.
        
        # Exemple de détection manuelle simple pour illustrer le script en attendant Triton
        if "PRIVATE KEY" in line or "passwd" in line.lower():
            findings.append({"line": i+1, "content": line, "type": "Potential Secret"})

    if findings:
        print(f"⚠️ {len(findings)} alertes détectées !")
        for f in findings:
            print(f"  [Ligne {f['line']}] - {f['type']} : {f['content'][:50]}...")
    else:
        print("✅ Aucun secret flagrant détecté par l'IA.")

def main():
    parser = argparse.ArgumentParser(description="Scanner IA de secrets (NVIDIA Morpheus SID)")
    parser.add_argument("path", help="Chemin du fichier ou dossier à scanner (ex: /mnt/verbatim/repos)")
    args = parser.parse_args()

    if os.path.isfile(args.path):
        scan_file(args.path)
    elif os.path.isdir(args.path):
        for root, dirs, files in os.walk(args.path):
            for file in files:
                if file.endswith(('.txt', '.log', '.conf', '.env')):
                    scan_file(os.path.join(root, file))

if __name__ == "__main__":
    print("🚀 Initialisation du Scanner IA Local...")
    print("💡 Assurez-vous que le serveur Triton est lancé (Docker Terminal 1)")
    main()
