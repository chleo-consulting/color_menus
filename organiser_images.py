#!/usr/bin/env python3
"""
Script bonus pour organiser les images téléchargées par pièce
"""

import os
import shutil
from pathlib import Path
import re

def organiser_par_piece():
    """
    Organise les images dans des sous-dossiers par pièce
    """
    dossier_images = "images_telechargees"
    dossier_organise = "images_organisees"
    
    if not os.path.exists(dossier_images):
        print(f"❌ Dossier {dossier_images} non trouvé!")
        return
    
    # Créer le dossier de destination
    Path(dossier_organise).mkdir(exist_ok=True)
    
    # Lire le fichier de métadonnées
    meta_file = os.path.join(dossier_images, "metadonnees_images.txt")
    if not os.path.exists(meta_file):
        print("❌ Fichier de métadonnées non trouvé!")
        return
    
    with open(meta_file, 'r', encoding='utf-8') as f:
        contenu = f.read()
    
    # Parser les métadonnées
    sections = contenu.split('------------------------------')
    
    for section in sections:
        if 'Fichier:' not in section:
            continue
        
        # Extraire les informations
        fichier_match = re.search(r'Fichier:\s*(.+)', section)
        piece_match = re.search(r'Pièce:\s*(.+)', section)
        
        if fichier_match and piece_match:
            nom_fichier = fichier_match.group(1).strip()
            nom_piece = piece_match.group(1).strip()
            
            # Nettoyer le nom de la pièce pour le dossier
            nom_dossier = re.sub(r'[^\w\s-]', '', nom_piece)
            nom_dossier = re.sub(r'\s+', '_', nom_dossier).strip('_')
            
            # Créer le sous-dossier
            sous_dossier = os.path.join(dossier_organise, nom_dossier)
            Path(sous_dossier).mkdir(exist_ok=True)
            
            # Copier l'image
            source = os.path.join(dossier_images, nom_fichier)
            destination = os.path.join(sous_dossier, nom_fichier)
            
            if os.path.exists(source):
                shutil.copy2(source, destination)
                print(f"📁 {nom_fichier} → {nom_dossier}/")
            else:
                print(f"⚠️  Fichier non trouvé: {source}")
    
    # Copier aussi le fichier de métadonnées
    shutil.copy2(meta_file, os.path.join(dossier_organise, "metadonnees_images.txt"))
    
    print(f"\n✅ Images organisées dans {dossier_organise}/")
    
    # Afficher la structure
    print("\n📂 Structure créée :")
    for root, dirs, files in os.walk(dossier_organise):
        level = root.replace(dossier_organise, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            if file.endswith(('.jpg', '.png', '.jpeg', '.webp')):
                print(f"{subindent}{file}")

if __name__ == "__main__":
    organiser_par_piece()