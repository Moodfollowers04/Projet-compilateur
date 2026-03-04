# Projet Compilateur L3Lang

Ce projet a pour but de créer un compilateur pour un langage simplifié de type Pascal appelé **L3Lang**.

## Étapes du projet

1. **Interpréteur** : Un programme qui peut lire et exécuter un code intermédiaire appelé P-Code (comme une petite machine virtuelle).
2. **Analyseur lexical et syntaxique** : Un programme qui lit le texte du programme en L3Lang et vérifie si la syntaxe est correcte.
3. **Analyse sémantique** : On vérifie si les variables sont bien déclarées, et on gère la table des symboles pour connaître tous les noms utilisés.
4. **Génération de code** : Le compilateur transforme le programme L3Lang en instructions P-Code, qui peuvent être exécutées par l’interpréteur.

## Utilisation

- Le projet est écrit en **Python**.
- Pour lancer l’exécution :  
  ```bash
  python interpreter_mach.py
  ```
- Pour compiler un fichier source (ex : `exemple.l3`) :  
  ```bash
  python main_compilateur.py exemple.l3
  ```
  Cela va produire un fichier de code intermédiaire qui pourra être lancé par l’interpréteur.

## Contenu du dépôt

- `interpreter_mach.py` : exécute les instructions P-Code.
- `main_compilateur.py` : le programme principal du compilateur.
- Autres fichiers nécessaires à l’analyseur et à la génération de code.

## Explications

- Le projet suit les étapes classiques d’un compilateur : lire un texte, le vérifier (analyse lexicale et syntaxique), le comprendre (sémantique), puis le transformer en instructions simples (P-Code).
- Le tout a été développé en Python, qui est simple à utiliser et permet de bien manipuler le texte et les fichiers.

## Auteur

- [Moodfollowers04](https://github.com/Moodfollowers04)

-

Ce README est volontairement simplifié. Plus de détails techniques sont disponibles dans les commentaires du code exigé par l’enseignant.
