#!/usr/bin/env python3
"""
Script de résumé du téléchargement d'images
"""

import os
from collections import defaultdict
import re

def generer_resume():
    """
    Génère un résumé complet du téléchargement
    """
    meta_file = "images_telechargees/metadonnees_images.txt"
    
    if not os.path.exists(meta_file):
        print("❌ Fichier de métadonnées non trouvé!")
        return
    
    with open(meta_file, 'r', encoding='utf-8') as f:
        contenu = f.read()
    
    # Compter par pièce
    pieces_count = defaultdict(int)
    total_images = 0
    urls_uniques = set()
    
    sections = contenu.split('------------------------------')
    
    for section in sections:
        if 'Fichier:' not in section:
            continue
        
        piece_match = re.search(r'Pièce:\s*(.+)', section)
        url_match = re.search(r'URL:\s*(.+)', section)
        
        if piece_match and url_match:
            piece = piece_match.group(1).strip()
            url = url_match.group(1).strip()
            
            pieces_count[piece] += 1
            total_images += 1
            urls_uniques.add(url)
    
    # Afficher le résumé
    print("="*60)
    print("📊 RÉSUMÉ DU TÉLÉCHARGEMENT D'IMAGES")
    print("="*60)
    print(f"🏠 Total des images téléchargées: {total_images}")
    print(f"🔗 URLs uniques: {len(urls_uniques)}")
    print(f"📁 Pièces couvertes: {len(pieces_count)}")
    print()
    
    print("📋 RÉPARTITION PAR PIÈCE:")
    print("-" * 40)
    for piece, count in sorted(pieces_count.items()):
        print(f"  {piece}: {count} image(s)")
    
    print()
    print("📂 DOSSIERS CRÉÉS:")
    print("-" * 40)
    
    if os.path.exists("images_telechargees"):
        taille_totale = 0
        for fichier in os.listdir("images_telechargees"):
            if fichier.endswith(('.jpg', '.png', '.jpeg', '.webp')):
                taille = os.path.getsize(os.path.join("images_telechargees", fichier))
                taille_totale += taille
        
        print(f"  📁 images_telechargees/ - {taille_totale / (1024*1024):.1f} MB")
    
    if os.path.exists("images_organisees"):
        print(f"  📁 images_organisees/ - Organisé par pièce")
    
    print()
    print("🎯 TYPES D'IMAGES IDENTIFIÉES:")
    print("-" * 40)
    
    # Analyser les types d'images
    types_images = defaultdict(int)
    for section in sections:
        if 'Titre:' not in section:
            continue
        
        titre_match = re.search(r'Titre:\s*(.+)', section)
        if titre_match:
            titre = titre_match.group(1).strip().lower()
            
            if 'poutre' in titre:
                types_images['Poutres'] += 1
            elif 'papier' in titre or 'peint' in titre:
                types_images['Papiers peints'] += 1
            elif 'sol' in titre:
                types_images['Sols'] += 1
            elif 'vue' in titre:
                types_images['Vues générales'] += 1
            elif 'textile' in titre:
                types_images['Textiles'] += 1
            else:
                types_images['Autres'] += 1
    
    for type_img, count in sorted(types_images.items()):
        print(f"  {type_img}: {count}")
    
    print()
    print("💡 INFORMATIONS UTILES:")
    print("-" * 40)
    print("  • Toutes les images conservent leur URL d'origine dans les métadonnées")
    print("  • Les noms de fichiers incluent la pièce, le titre et l'ID unique")
    print("  • Le fichier metadonnees_images.txt contient tous les détails")
    print("  • Les images sont organisées par pièce dans images_organisees/")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    generer_resume()