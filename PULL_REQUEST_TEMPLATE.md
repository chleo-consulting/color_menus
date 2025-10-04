# 🖼️ Script de Téléchargement des Images

## 📥 Nouveau Script de Téléchargement d'Images

Cette PR ajoute un script pour télécharger toutes les images depuis le fichier `index.html`.

### 🚀 Script Ajouté

#### `telecharger_images.py` - Script de Téléchargement
- ✅ Extraction automatique des URLs d'images depuis `index.html`
- ✅ Téléchargement de 18 images (10 URLs uniques) 
- ✅ Nommage intelligent: `{Pièce}_{Titre}_{ID}.jpg`
- ✅ Génération de métadonnées complètes avec traçabilité
- ✅ Gestion d'erreurs robuste et retry automatique
- ✅ Pause anti-surcharge serveur

### 📊 Résultats

- **18 images téléchargées** avec succès (0 échec)
- **8 pièces couvertes**: Salon (5), WC (3), Escalier (3), Cuisine (2), Entrée/Couloir (2), Chambres 1-3 (1 chacune)
- **Types d'images**: Poutres (5), Sols (4), Vues (4), Papiers peints (3), Textiles (1), Autres (1)
- **Taille totale**: ~3.5 MB

### 📁 Structure Créée

```
images_telechargees/          # Toutes les images + métadonnées
├── *.jpg                     # 18 images avec noms explicites
└── metadonnees_images.txt    # Fichier de métadonnées complet
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
```

### ✅ Tests Réalisés

- ✅ Téléchargement réussi de toutes les images
- ✅ Métadonnées correctement générées
- ✅ Gestion d'erreurs testée
- ✅ Documentation complète

### 📋 Fichiers Ajoutés

- `telecharger_images.py` - Script de téléchargement
- `README_TELECHARGEMENT.md` - Documentation complète
- `PULL_REQUEST_TEMPLATE.md` - Template pour cette PR
- `images_telechargees/` - Dossier avec toutes les images et métadonnées (18 images)

Cette solution offre un script robuste pour sauvegarder toutes les ressources images du projet de décoration Farrow & Ball.