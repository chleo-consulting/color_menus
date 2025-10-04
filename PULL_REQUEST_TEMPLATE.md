# 🖼️ Scripts de Téléchargement et Organisation des Images

## 📥 Nouveaux Scripts de Téléchargement d'Images

Cette PR ajoute un système complet pour télécharger et organiser toutes les images depuis le fichier `index.html`.

### 🚀 Scripts Ajoutés

#### 1. `telecharger_images.py` - Script Principal
- ✅ Extraction automatique des URLs d'images depuis `index.html`
- ✅ Téléchargement de 18 images (10 URLs uniques) 
- ✅ Nommage intelligent: `{Pièce}_{Titre}_{ID}.jpg`
- ✅ Génération de métadonnées complètes avec traçabilité
- ✅ Gestion d'erreurs robuste et retry automatique
- ✅ Pause anti-surcharge serveur

#### 2. `organiser_images.py` - Organisation par Pièce
- 📁 Création de sous-dossiers pour chaque pièce
- 📁 Organisation automatique des images par contexte
- 📋 Affichage de la structure créée

#### 3. `resume_telechargement.py` - Statistiques
- 📊 Rapport complet avec statistiques détaillées
- 📋 Répartition par pièce et type d'image
- 💾 Informations sur l'espace disque utilisé

### 📊 Résultats

- **18 images téléchargées** avec succès (0 échec)
- **8 pièces couvertes**: Salon (5), WC (3), Escalier (3), Cuisine (2), Entrée/Couloir (2), Chambres 1-3 (1 chacune)
- **Types d'images**: Poutres (5), Sols (4), Vues (4), Papiers peints (3), Textiles (1), Autres (1)
- **Taille totale**: ~3.5 MB

### 📁 Structure Créée

```
images_telechargees/          # Toutes les images + métadonnées
images_organisees/            # Images organisées par pièce
├── Chambre_1/ 
├── Salon/                    # 5 images
├── WC/                       # 3 images
├── Escalier/                 # 3 images
└── ...                       # Autres pièces
```

### 🛠️ Fonctionnalités Techniques

- **Métadonnées complètes**: Traçabilité URL→fichier avec toutes les informations
- **Nommage intelligent**: Inclusion pièce + titre + ID unique 
- **Gestion d'erreurs**: Timeouts, retries, headers anti-blocage
- **Évitement doublons**: Vérification d'existence et nommage incrémental
- **Documentation**: README complet avec guide d'utilisation

### 🚀 Utilisation

```bash
# Télécharger toutes les images
python3 telecharger_images.py

# Organiser par pièce
python3 organiser_images.py  

# Voir statistiques
python3 resume_telechargement.py
```

### ✅ Tests Réalisés

- ✅ Téléchargement réussi de toutes les images
- ✅ Métadonnées correctement générées
- ✅ Organisation par pièce fonctionnelle 
- ✅ Statistiques et rapports précis
- ✅ Gestion d'erreurs testée
- ✅ Documentation complète

### 📋 Fichiers Ajoutés/Modifiés

- `telecharger_images.py` - Script principal de téléchargement
- `organiser_images.py` - Script d'organisation par pièce
- `resume_telechargement.py` - Script de statistiques
- `README_TELECHARGEMENT.md` - Documentation complète
- `PULL_REQUEST_TEMPLATE.md` - Template pour cette PR
- `images_telechargees/` - Dossier avec toutes les images et métadonnées
- `images_organisees/` - Dossier avec images organisées par pièce

Cette solution offre un système robuste et complet pour sauvegarder et organiser toutes les ressources images du projet de décoration Farrow & Ball.