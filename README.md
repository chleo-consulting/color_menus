# 🎨 Visualisateur Couleurs Farrow & Ball - Version avec Images Intégrées

## 📋 Description du Projet
Application web élégante pour visualiser les couleurs Farrow & Ball d'un projet de décoration, organisée pièce par pièce avec des rectangles colorés interactifs et des cartes d'images. Version avec fond blanc épuré, intégration des instructions d'usage et support des images de référence par pièce.

## ✨ Fonctionnalités Principales

### 🔍 **Rectangles Colorés Agrandis**
- **Taille minimum** : 450px × 300px (3 fois plus grand que la version précédente)
- **Textes intégrés** directement dans chaque rectangle :
  - Nom de la couleur Farrow & Ball (grande typographie)
  - Localisation (murs, plafonds, étagères, etc.)
  - Code hexadécimal avec fond semi-transparent

### 🎨 **Adaptation Automatique du Texte**
- **Contraste intelligent** : Le texte s'adapte automatiquement selon la couleur de fond
- **Couleurs claires** : Texte foncé avec ombres blanches
- **Couleurs foncées** : Texte blanc avec ombres noires
- **Lisibilité optimale** sur toutes les couleurs

### 🏠 **Organisation par Pièce**
- **9 espaces distincts** avec icônes contextuelles :
  - Toutes pièces (plafonds)
  - Chambres 1, 2 et 3
  - Salle de bain, WC, Cagibi
  - Entrée/Couloir, Escalier
  - Salon et Cuisine

### 📝 **Instructions d'Usage Intégrées**
- **Nouvelle colonne Usage** du CSV intégrée dans les données
- **Instructions détaillées** affichées dans la modal pour certaines couleurs
- **Guidance précise** pour l'application (murs spécifiques, zones particulières)
- **Notes importantes** comme les alternatives de couleurs ou sous-couches

### 🖼️ **Cartes d'Images par Pièce**
- **Images de référence** intégrées pour certaines pièces
- **Cartes interactives** avec aperçu, titre et description
- **Modal détaillée** pour visualiser les images en grand format
- **Multi-images** : Plusieurs images possibles par pièce
- **Actuellement** : 16 images (Chambres 1,2,3: 1 chacune, WC: 3, Entrée/Couloir: 2, Escalier: 3, Salon: 3, Cuisine: 2)
- **Sol unifié** : Tomettes dans 4 pièces pour cohérence
- **Papier peint IVY Blue** : Salon + Escalier pour continuité verticale
- **Système extensible** pour ajouter d'autres images facilement

### 📱 **Interface Moderne**
- **Fond blanc épuré** (#FFFFFF) pour une meilleure lisibilité
- **🆕 Fonds colorés par pièce** : Chaque carte utilise sa première couleur en fond (opacité 100%)
- **Design minimaliste** avec ombres portées subtiles
- **Grille mixte** : rectangles de couleurs + cartes d'images
- **Animations fluides** au survol pour tous les éléments
- **Double modal** : couleurs ET images avec contenus adaptés

## 🎯 Couleurs Traitées (23 couleurs) + 16 Images

### Couleurs Principales
- **All White** (#FBF8F4) - Plafonds de toutes les pièces
- **Wimborne White** (#F7F3E8) - Chambres 1 et 3, Salle de bain
- **School House White** (#E6DFD1) - Salon (murs principaux et sous-pentes)
- **Lime White** (#E8DEC9) - Chambre 3 et Cagibi
- **Shaded White** (#D9D2C1) - Bibliothèque TV et tablettes salon
- **Shadow White** (#DED8C6) - Murs angle cuisine côté séjour

### Couleurs d'Accent
- **Picture Gallery Red** (#A15A4D) - Dressing Chambre 1 et placard WC
- **Radicchio** (#994A50) - Fond étagères Chambre 2
- **Grove Green** (#4B5956) - Entrée, escalier et grand mur bibliothèque salon
- **Drop Cloth** (#C9BEAB) - Bibliothèque salon
- **Off-Black** (#444546) - Embrasement fenêtre cuisine

### Tons Neutres
- **Skimming Stone** (#DFD6CB) - Chambre 2 murs
- **Charleston Gray** (#9F9389) - Chambre 2 placard
- **Stony Ground** (#CEC1AD) - WC et autres murs entrée/couloir
- **Skylight** (#CCD0CD) - Cuisine (murs et plafond)

### Instructions Spécifiques Intégrées
- **Grove Green Entrée** : Application sur mur porte d'entrée et angle escalier
- **Grove Green Salon** : Grand mur bibliothèques + placards fenêtres (attention sous-couche)
- **Alternative mentionnée** : INCHYRA BLUE comme option pour le salon
- **Zones précises** : Embrasements, sous-pentes, entre poutres détaillés

## 🚀 Technologies Utilisées
- **HTML5** avec structure sémantique
- **CSS3** avec Grid, Flexbox, et effets modernes
- **JavaScript ES6+** pour l'interactivité
- **Google Fonts** (Inter) pour la typographie
- **Font Awesome** pour les icônes contextuelles

## 📐 Spécifications Techniques

### Dimensions des Rectangles
- **Taille minimum** : 450px × 300px
- **Responsive** : S'adapte automatiquement sur mobile (1 colonne)
- **Espacement** : 1.5rem entre les rectangles

### Effets Visuels
- **Hover** : Agrandissement de 5% avec ombre portée
- **Transitions** : 0.3s ease pour tous les effets
- **Glassmorphism** : Effets de transparence et flou d'arrière-plan
- **Ombres** : Ombres portées multiples pour la profondeur

### Accessibilité
- **Contraste automatique** : Texte adapté selon la couleur de fond
- **Navigation clavier** : Support Escape pour fermer la modal
- **Responsive** : Compatible mobile et desktop
- **Sémantique** : Structure HTML accessible

## 🎮 Utilisation

### Navigation
1. **Visualisation** : Les rectangles colorés affichent directement toutes les informations
2. **Détails** : Cliquer sur un rectangle pour voir la modal détaillée
3. **Fermeture** : Escape ou clic extérieur pour fermer la modal
4. **Responsive** : Utilisable sur tous les appareils

### Informations Affichées
- **Dans les rectangles** : Nom couleur + localisation + code hex
- **Modal détaillée** : Vue agrandie avec toutes les informations
- **Organisation** : Groupement logique par pièce avec icônes

## 📱 Responsive Design
- **Desktop** : Grille multi-colonnes avec rectangles 450×300px
- **Tablet** : Adaptation automatique de la grille
- **Mobile** : Une colonne avec rectangles 250px minimum

## 🔄 Améliorations de Cette Version
1. **🆕 Fonds colorés automatiques** : Chaque pièce a un fond de la première couleur (opacité 100%)
2. **Système d'images** : Ajout de cartes d'images pour certaines pièces
3. **Images multiples** : Sol, papiers peints, poutres et vues globales (WC, cuisine, entrée/escalier)
4. **Cartes interactives** : Design élégant avec aperçu, titre et description
5. **Modal d'images** : Affichage en grand format avec détails
6. **Grille adaptive** : Mélange harmonieux couleurs + images
7. **Images lazy loading** : Chargement optimisé des images
8. **Structure extensible** : Facilité d'ajout de nouvelles images par pièce
9. **Double modalité** : Fonctions séparées pour couleurs et images
10. **Vues complètes** : Photos d'aménagement + projections couleurs dans 4 espaces

## 🖼️ Images Intégrées

### Chambres - Poutres (1 image chacune)
- **Chambre 1** : Poutres apparentes + Wimborne White + Picture Gallery Red (dressing)
- **Chambre 2** : Poutres apparentes + Skimming Stone + Radicchio (étagères) + Charleston Gray (placard)
- **Chambre 3** : Poutres apparentes + Wimborne White + Lime White (placard)
- **Architecture** : Charpente traditionnelle à l'étage
- **Authenticité** : Caractère provençal dans toutes les chambres

### WC - Images (3)

#### Papier Peint
- **Référence** : LittleGreene Richmond-green-stella
- **Motif** : Floral délicat avec roses et feuillage sur fond crème
- **Style** : Romantique et vintage, tons roses poudrés et verts
- **Application** : Papier peint décoratif Little Greene

#### Sol
- **Matériau** : Tomettes en terre cuite
- **Harmonie** : Parfaite avec Stony Ground et Picture Gallery Red
- **Continuité** : Liaison avec les autres pièces

#### Vue Globale
- **Type** : Photo de l'aménagement actuel
- **Perspective** : Vue d'ensemble de l'espace WC
- **Utilité** : Visualisation avant application des finitions
- **Référence** : État actuel pour projection du rendu final

### Entrée / Couloir - Images (2)

#### Sol
- **Matériau** : Tomettes en terre cuite
- **Accueil chaleureux** : Tons terre cuite dès l'entrée
- **Harmonie** : S'accorde avec Grove Green et Stony Ground
- **Praticité** : Résistant au passage dans l'entrée

#### Vue Globale
- **Type** : Photo de l'aménagement actuel entrée/escalier
- **Perspective** : Vision d'ensemble de l'espace de circulation
- **Éléments visibles** : Escalier, garde-corps, portes, finitions
- **Utilité** : Référence pour projection des couleurs finales

### Escalier - Images (3)

#### Papier Peint
- **Référence** : IVY Blue 699 Farrow&Ball
- **Motif** : Floral délicat avec branches sur fond clair
- **Continuité** : Même papier peint que le salon
- **Harmonie** : S'accorde avec Grove Green des murs

#### Poutres
- **Matériau** : Bois naturel apparent
- **Style** : Authenticité architecturale
- **Finition** : Bois brut, grain visible
- **Continuité** : Liaison structurelle avec le salon

#### Vue Globale
- **Type** : Photo de l'escalier et circulation
- **Perspective** : Montant vers l'étage avec garde-corps
- **Architecture** : Structure escalier + aménagement actuel
- **Projection** : Base pour visualiser Grove Green + papier peint IVY Blue

### Salon - Images (3)

#### Papier Peint
- **Référence** : IVY Blue 699 Farrow&Ball
- **Motif** : Floral délicat avec branches sur fond clair
- **Style** : Vintage et romantique, tons bleu-gris
- **Application** : Papier peint décoratif pour certaines zones

#### Sol
- **Matériau** : Tomettes en terre cuite
- **Style** : Authentique et chaleureux, tons terre cuite
- **Finition** : Aspect mat naturel avec joints traditionnels
- **Harmonie** : Apporte la chaleur du sud à l'ensemble
- **Continuité** : Liaison avec entrée, WC et cuisine

#### Poutres
- **Matériau** : Bois naturel apparent
- **Architecture** : Charpente traditionnelle visible
- **Authenticité** : Caractère provençal
- **Harmonie** : Contraste chaleureux avec les couleurs murales

### Cuisine - Images (2)

#### Sol
- **Matériau** : Tomettes en terre cuite
- **Praticité** : Facile d'entretien en cuisine
- **Warmth** : Réchauffe les tons Skylight et Off-Black
- **Authenticité** : Style traditionnel provençal

#### Vue Globale
- **Type** : Photo de l'état actuel en travaux
- **Perspective** : Vue d'ensemble de l'aménagement
- **Utilité** : Visualisation de l'espace avant finitions
- **Référence** : Comparaison avant/après projet

### Comment Ajouter d'Autres Images
```javascript
// Dans roomImages, structure tableau :
'NomPièce': [
    {
        url: 'URL_image_1',
        title: 'Titre 1',
        description: 'Description 1'
    },
    {
        url: 'URL_image_2', 
        title: 'Titre 2',
        description: 'Description 2'
    }
]
```

## 💡 Fonctionnalités Usage

### Couleurs avec Instructions Spéciales
- **Grove Green Entrée** : Mur porte d'entrée + angle escalier côté entrée
- **Stony Ground Entrée** : Tous les autres murs entrée et couloir  
- **Shaded White Salon** : Bibliothèque TV + tablettes banquettes
- **Grove Green Salon** : Grand mur bibliothèques/bureau + placards fenêtres
- **Shadow White Salon** : 2 murs angle cuisine côté séjour + porte
- **Drop Cloth Salon** : 2 murs angle cuisine côté séjour + porte
- **School House White Salon** : Reste pièce (murs, sous-pentes, embrasements, entre poutres)
- **Off-Black Cuisine** : Embrasement fenêtre uniquement
- **Skylight Cuisine** : Tous murs et plafond

---

## 🎨 **Fonds Colorés par Pièce**

### Couleurs de Fond Automatiques (Opacité 100%)
- **Toutes pièces** : All White (#FBF8F4) - Fond crème doux
- **Chambre 1** : Wimborne White (#F7F3E8) - Fond blanc chaud
- **Chambre 2** : Skimming Stone (#DFD6CB) - Fond beige pierre
- **Chambre 3** : Wimborne White (#F7F3E8) - Fond blanc chaud
- **Salle de bain** : Wimborne White (#F7F3E8) - Fond blanc chaud
- **WC** : Stony Ground (#CEC1AD) - Fond beige naturel
- **Cagibi** : Lime White (#E8DEC9) - Fond blanc citron
- **Entrée/Couloir** : Grove Green (#4B5956) - Fond vert profond
- **Escalier** : Grove Green (#4B5956) - Fond vert profond  
- **Salon** : Shaded White (#D9D2C1) - Fond blanc ombré
- **Cuisine** : Off-Black (#444546) - Fond noir doux

### Avantages des Fonds Colorés
1. **Identification rapide** : Chaque pièce a son identité visuelle unique
2. **Immersion totale** : Ambiance couleur complète de chaque pièce
3. **Hiérarchie visuelle** : Couleur principale fortement mise en avant
4. **Cohérence design** : Harmonie parfaite entre fond et palette couleurs
5. **Navigation intuitive** : Reconnaissance immédiate et impact visuel fort
6. **Lisibilité préservée** : En-têtes avec fond blanc semi-transparent

---

*Projet de visualisation couleurs Farrow & Ball - Version avec fonds colorés, images intégrées et instructions d'usage*