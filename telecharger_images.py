#!/usr/bin/env python3
"""
Script pour télécharger toutes les images depuis les URLs du fichier index.html
"""

import requests
import os
import re
import time
from urllib.parse import urlparse, unquote
from pathlib import Path

def extraire_urls_images(fichier_html):
    """
    Extrait toutes les URLs d'images du fichier HTML
    """
    with open(fichier_html, 'r', encoding='utf-8') as f:
        contenu = f.read()
    
    # Pattern pour extraire les URLs d'images dans l'objet roomImages
    pattern = r"url:\s*['\"]([^'\"]+)['\"]"
    urls = re.findall(pattern, contenu)
    
    return urls

def nettoyer_nom_fichier(url, titre=""):
    """
    Crée un nom de fichier propre à partir de l'URL et du titre
    """
    # Extraire l'extension de l'URL
    parsed_url = urlparse(url)
    path = parsed_url.path
    
    # Déterminer l'extension
    extension = ".jpg"  # Par défaut
    if path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
        extension = os.path.splitext(path)[1].lower()
    
    # Créer un nom de fichier basé sur l'ID de l'URL ou le titre
    if "base64_upload" in url:
        # Extraire l'ID unique de l'URL
        id_match = re.search(r'/([a-f0-9]{32})$', parsed_url.path)
        if id_match:
            nom_base = id_match.group(1)
        else:
            nom_base = os.path.basename(parsed_url.path) or "image"
    elif "genspark" in url:
        # Extraire l'ID de l'URL GenSpark
        id_match = re.search(r'/([a-f0-9-]{36})$', parsed_url.path)
        if id_match:
            nom_base = id_match.group(1)
        else:
            nom_base = os.path.basename(parsed_url.path) or "image_genspark"
    else:
        nom_base = os.path.basename(parsed_url.path) or "image"
    
    # Ajouter le titre si fourni
    if titre:
        titre_propre = re.sub(r'[^\w\s-]', '', titre).strip()
        titre_propre = re.sub(r'\s+', '_', titre_propre)
        if titre_propre:
            nom_base = f"{titre_propre}_{nom_base}"
    
    return f"{nom_base}{extension}"

def telecharger_image(url, dossier_destination, nom_fichier):
    """
    Télécharge une image depuis une URL
    """
    try:
        print(f"Téléchargement de {url}...")
        
        # Headers pour éviter les blocages
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        chemin_complet = os.path.join(dossier_destination, nom_fichier)
        
        with open(chemin_complet, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ Image sauvegardée : {chemin_complet}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors du téléchargement de {url}: {e}")
        return False
    except Exception as e:
        print(f"❌ Erreur inattendue pour {url}: {e}")
        return False

def extraire_infos_images(fichier_html):
    """
    Extrait les informations complètes des images (URL, titre, description, pièce)
    """
    with open(fichier_html, 'r', encoding='utf-8') as f:
        contenu = f.read()
    
    images_info = []
    
    # Pattern pour extraire les objets d'images avec leurs métadonnées
    pattern_room = r"'([^']+)':\s*\[(.*?)\]"
    matches_rooms = re.findall(pattern_room, contenu, re.DOTALL)
    
    for piece, images_content in matches_rooms:
        # Pattern pour extraire chaque image dans une pièce
        pattern_image = r"\{\s*url:\s*['\"]([^'\"]+)['\"],\s*title:\s*['\"]([^'\"]*)['\"],\s*description:\s*['\"]([^'\"]*)['\"]"
        images_matches = re.findall(pattern_image, images_content)
        
        for url, title, description in images_matches:
            images_info.append({
                'url': url,
                'title': title,
                'description': description,
                'piece': piece
            })
    
    return images_info

def main():
    fichier_html = "index.html"
    dossier_images = "images_telechargees"
    
    # Vérifier que le fichier HTML existe
    if not os.path.exists(fichier_html):
        print(f"❌ Fichier {fichier_html} non trouvé!")
        return
    
    # Créer le dossier de destination
    Path(dossier_images).mkdir(exist_ok=True)
    print(f"📁 Dossier de destination : {dossier_images}")
    
    # Extraire les informations des images
    images_info = extraire_infos_images(fichier_html)
    
    if not images_info:
        print("❌ Aucune image trouvée dans le fichier HTML!")
        return
    
    print(f"🔍 {len(images_info)} images trouvées")
    
    # Créer un fichier de métadonnées
    with open(os.path.join(dossier_images, "metadonnees_images.txt"), 'w', encoding='utf-8') as meta_file:
        meta_file.write("Métadonnées des images téléchargées\n")
        meta_file.write("="*50 + "\n\n")
    
    # Télécharger chaque image
    succes = 0
    echecs = 0
    
    for i, image_info in enumerate(images_info, 1):
        url = image_info['url']
        title = image_info['title']
        description = image_info['description']
        piece = image_info['piece']
        
        print(f"\n[{i}/{len(images_info)}] Traitement de l'image:")
        print(f"  Pièce: {piece}")
        print(f"  Titre: {title}")
        print(f"  Description: {description}")
        
        # Créer un nom de fichier unique
        nom_fichier = nettoyer_nom_fichier(url, f"{piece}_{title}")
        
        # Éviter les doublons
        compteur = 1
        nom_original = nom_fichier
        while os.path.exists(os.path.join(dossier_images, nom_fichier)):
            nom_base, extension = os.path.splitext(nom_original)
            nom_fichier = f"{nom_base}_{compteur}{extension}"
            compteur += 1
        
        # Télécharger l'image
        if telecharger_image(url, dossier_images, nom_fichier):
            succes += 1
            
            # Ajouter les métadonnées
            with open(os.path.join(dossier_images, "metadonnees_images.txt"), 'a', encoding='utf-8') as meta_file:
                meta_file.write(f"Fichier: {nom_fichier}\n")
                meta_file.write(f"URL: {url}\n")
                meta_file.write(f"Pièce: {piece}\n")
                meta_file.write(f"Titre: {title}\n")
                meta_file.write(f"Description: {description}\n")
                meta_file.write("-" * 30 + "\n\n")
        else:
            echecs += 1
        
        # Pause pour éviter de surcharger les serveurs
        time.sleep(1)
    
    print("\n" + "="*60)
    print(f"📊 RÉSUMÉ:")
    print(f"  ✅ Images téléchargées avec succès: {succes}")
    print(f"  ❌ Échecs: {echecs}")
    print(f"  📁 Dossier: {os.path.abspath(dossier_images)}")
    print(f"  📄 Métadonnées: {os.path.join(dossier_images, 'metadonnees_images.txt')}")

if __name__ == "__main__":
    main()