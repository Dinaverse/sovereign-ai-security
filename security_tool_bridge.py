import os
import time
import subprocess
import shutil

# Dossiers surveillés (sur votre disque Verbatim)
INPUT_DIR = "/mnt/verbatim/data_in"
OUTPUT_DIR = "/mnt/verbatim/intelligence_out"

def process_file(file_path):
    print(f"🚀 Détection de nouvelle donnée : {file_path}")
    
    # 1. Si c'est une image (provenant de CamPhish) -> Analyse DeepStream
    if file_path.endswith(('.jpg', '.png')):
        print("🔍 Analyse IA : Détection de visages/objets via DeepStream...")
        # Lancement du container DeepStream
        subprocess.run(["docker", "run", "--rm", "--gpus", "all", "-v", f"{file_path}:/data/img.jpg", "nvcr.io/nvidia/deepstream:6.2-triton", "python3", "detect.py"])
        
    # 2. Si c'est un log/JSON (provenant de Ashok/Hound) -> Analyse cyBERT
    elif file_path.endswith(('.json', '.log')):
        print("🔍 Analyse IA : Analyse de menaces via cyBERT...")
        # Lancement du container Morpheus cyBERT
        subprocess.run(["docker", "run", "--rm", "--gpus", "all", "-v", f"{file_path}:/data/log.json", "nvcr.io/nvidia/morpheus/morpheus-models:sid-minibert-onnx", "python3", "analyze.py"])

    print(f"✅ Analyse terminée pour {file_path}")
    # Déplacement vers le dossier de sortie
    shutil.move(file_path, os.path.join(OUTPUT_DIR, os.path.basename(file_path)))

def main():
    # S'assurer que les dossiers existent
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("🛰️ Bridge IA activé. Surveillance de /mnt/verbatim/data_in...")
    try:
        while True:
            for file in os.listdir(INPUT_DIR):
                if file.startswith('.'): continue
                full_path = os.path.join(INPUT_DIR, file)
                process_file(full_path)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n🛑 Bridge IA arrêté.")

if __name__ == "__main__":
    main()
