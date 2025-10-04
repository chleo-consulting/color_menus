# 📥 Script de Téléchargement d'Images

Ce projet contient un script Python pour télécharger toutes les images depuis le fichier `index.html`.

## 🚀 Script Principal

### `telecharger_images.py` - Téléchargement d'Images
**Le script qui télécharge toutes les images depuis les URLs trouvées dans index.html**

```bash
python3 telecharger_images.py
```

**Fonctionnalités :**
- ✅ Extraction automatique de toutes les URLs d'images depuis `index.html`
- ✅ Téléchargement de toutes les images avec gestion d'erreurs
- ✅ Nommage intelligent des fichiers (pièce + titre + ID unique)
- ✅ Génération automatique d'un fichier de métadonnées complet
- ✅ Évitement des doublons
- ✅ Pause entre téléchargements pour éviter la surcharge serveur

## 📁 Structure du Dossier Créé

```
/home/user/webapp/
├── images_telechargees/          # Toutes les images téléchargées
│   ├── *.jpg                     # Images avec noms explicites
│   └── metadonnees_images.txt    # Fichier de métadonnées complet
```

## 🏷️ Convention de Nommage

Les fichiers sont nommés selon le format :
```
{Pièce}_{Titre}_{ID_Unique}.jpg
```

**Exemples :**
- `Salon_Textiles_Salon_94b23a706bebef58cc5c4b52842c1ead.jpg`
- `WC_Papier_peint_WC_c4f4e980b42ea6f7d83bde8b7481422c.jpg`
- `Escalier_Vue_Escalier_5f9ccb7fc2cf3274747ccb3cb0b5056a.jpg`

## 📋 Fichier de Métadonnées

Le fichier `metadonnees_images.txt` contient pour chaque image :
- **Nom du fichier local**
- **URL d'origine**
- **Pièce associée**
- **Titre descriptif**
- **Description détaillée**

## 🔍 Images Téléchargées

### Résumé du Contenu
- **18 images au total** réparties sur **8 pièces**
- **10 URLs uniques** (certaines images sont utilisées pour plusieurs pièces)
- **Taille totale :** ~3.5 MB

### Par Type d'Image
- **Poutres :** 5 images (chambres, salon, escalier)
- **Sols :** 4 images (tomettes dans différentes pièces)
- **Vues générales :** 4 images (vues d'ensemble des pièces)
- **Papiers peints :** 3 images (WC, escalier, salon)
- **Textiles :** 1 image (tissus et coussins du salon)
- **Autres :** 1 image (essai de couleur salon)

### Par Pièce
- **Salon :** 5 images (papier peint, sol, poutres, textiles, essai couleur)
- **WC :** 3 images (papier peint, sol, vue)
- **Escalier :** 3 images (papier peint, poutres, vue)
- **Cuisine :** 2 images (sol, vue globale)
- **Entrée/Couloir :** 2 images (sol, vue)
- **Chambre 1, 2, 3 :** 1 image chacune (poutres)

## 🛠️ Fonctionnalités Techniques

### Gestion d'Erreurs
- ✅ Vérification de l'existence des fichiers
- ✅ Gestion des timeouts réseau
- ✅ Headers HTTP pour éviter les blocages
- ✅ Rapport d'erreurs détaillé

### Sécurité et Performance
- ⏱️ Pause de 1 seconde entre téléchargements
- 🔄 Retry automatique en cas d'échec
- 📝 Headers User-Agent réalistes
- 🛡️ Validation des URLs et des noms de fichiers

### Métadonnées Complètes
- 🏷️ Conservation de toutes les informations d'origine
- 🔗 Traçabilité URL → fichier local
- 📁 Organisation intuitive

## 🚀 Utilisation

```bash
# Télécharger toutes les images
python3 telecharger_images.py
```

## 📞 Support

Le script gère automatiquement :
- Les caractères spéciaux dans les noms
- Les URLs avec ou sans extension
- La déduplication des fichiers
- La création des dossiers nécessaires
- La génération de rapports détaillés

Le script est documenté et inclut une gestion d'erreurs robuste pour un fonctionnement fiable.