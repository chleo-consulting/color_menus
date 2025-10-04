# 📥 Scripts de Téléchargement d'Images

Ce projet contient plusieurs scripts Python pour télécharger et organiser toutes les images depuis le fichier `index.html`.

## 🚀 Scripts Disponibles

### 1. `telecharger_images.py` - Script Principal
**Le script principal qui télécharge toutes les images depuis les URLs trouvées dans index.html**

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

### 2. `organiser_images.py` - Organisation par Pièce
**Script bonus pour organiser les images dans des sous-dossiers par pièce**

```bash
python3 organiser_images.py
```

**Fonctionnalités :**
- 📁 Crée des sous-dossiers pour chaque pièce
- 📁 Copie les images dans les dossiers appropriés
- 📋 Affiche la structure créée

### 3. `resume_telechargement.py` - Résumé et Statistiques
**Génère un résumé complet avec statistiques**

```bash
python3 resume_telechargement.py
```

**Fonctionnalités :**
- 📊 Statistiques complètes du téléchargement
- 📋 Répartition par pièce
- 🎯 Classification par type d'image
- 💾 Informations sur l'espace disque utilisé

## 📁 Structure des Dossiers Créés

```
/home/user/webapp/
├── images_telechargees/          # Toutes les images téléchargées
│   ├── *.jpg                     # Images avec noms explicites
│   └── metadonnees_images.txt    # Fichier de métadonnées complet
│
├── images_organisees/            # Images organisées par pièce
│   ├── Chambre_1/
│   ├── Chambre_2/
│   ├── Chambre_3/
│   ├── WC/
│   ├── Entrée_Couloir/
│   ├── Escalier/
│   ├── Salon/
│   └── Cuisine/
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
- 📊 Statistiques automatiques
- 📁 Organisation intuitive

## 🚀 Utilisation Rapide

```bash
# Télécharger toutes les images
python3 telecharger_images.py

# Organiser par pièce (optionnel)
python3 organiser_images.py

# Voir le résumé complet
python3 resume_telechargement.py
```

## 📞 Support

Les scripts gèrent automatiquement :
- Les caractères spéciaux dans les noms
- Les URLs avec ou sans extension
- La déduplication des fichiers
- La création des dossiers nécessaires
- La génération de rapports détaillés

Tous les scripts sont documentés et incluent une gestion d'erreurs robuste pour un fonctionnement fiable.