# cpo Odd Jumper

## Prérequis
- **Python 3**
- Librairie **pygame**
- Résolution d'écran **16/9**

## Comment Jouer
**Lancer le jeu :**
```
python3 main.py
```
**Controls en jeu :**
- q : déplacement vers la gauche
- d : déplacement vers la droite
- space : sauter
- e : interagir avec une entitée
- escape : mettre le jeu en pause durant un niveau

## Fonctionalitées

- Des menus créer depuis des fichiers json qui peuvent contenir : des boutons, des images de fonds, des images de bages grisé ou non en fonction des completions des niveaux.
- Des niveaux de type platformeur, comprennant le déplacement du joueur (gauche, droite, saut) avec des physiques de gravité et de collision calculer en delta time ainsi que des accelerations et vitesses. Le joueur peu aussi intéragire avec des entitées qui on différents comportement : item qui peu être récupéré, entitées qui "tue" et fait revenir le joueur a l'endroit de départ, entités qui parle affichant un texte souvant servant d'explication, entités qui récupère les items récupérés afin de compléter le niveau.

- Fonctionalités suplémentaire non visible : déchargement/chargement des ressources(ex : images) nécésaire pour les niveaux/menu dynamiques pour limité l'utilisation de ressources matériel (RAM).


## Compte rendu des semaines

**Semaine 1 :** 

- la fenetre de jeu est créer
- tout les fichiers et class présents dans nos diagrams uml ont été créer
- des testes pour les menu on été fait a propos des boutons

**Semaine 2 :**

- Création d'un entité depuis un fichier json
- test de déplacement grave un input clavier
- création d'une image l'affichage d'un niveau et d'un fichier pour les collision assosier au niveau 

**Semaine 3 :**
- Test d'affichage des images dans la fenêtre pygame.
- Test des sounds effect.
- Création des objets collisions depuis fichier ".json" d'une map.
- Ajouter deux méthodes de collision dans la class Collision.

**Semaine 4 :**
- Animation spritesheet faite.
- finition des collisions.
- Boucle de simulation de niveau

**Semaine 5 :**
- ajout lien du menu avec le niveau teste
- création/affichage des entité 
- ajout de possibilité que l'entité tue
- ajout de possibilité que l'entité soit ramassable
- recherche de tileset (cf lien en bas du readme) pour visuel

**Semaine 6 :**
- Finir la création des niveaux
- Finir le menu badge
- En cours de finir la dernière phase des entités


## Ressources suplémentaires

Les fichiers suplémentaires du rendu se trouve dans le dossier :  
```
./ressources_rendu/
```


## Sources : Tileset

Energie : 

- https://free-game-assets.itch.io/free-green-zone-tileset-pixel-art
- https://free-game-assets.itch.io/power-station-free-tileset-pixel-art

Poverty :
- https://free-game-assets.itch.io/free-exclusion-zone-tileset-pixel-art