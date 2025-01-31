# Vérification
## Projet Alice & Bob

Le but de ce projet est de vérifier un ensemble de propriétés sur des automates Alice & Bob allant du plus simple au plus travaillé. On met ces automates sous la forme de "soupe", c'est-à-dire un ensemble désordonné de pièces qui s'emboîtent les unes dans les autres selon le chemin suivi par l'automate.
On a 4 automates : 
- l'automate naïf, le plus simple
- l'automate deadlock, où Alice et Bob se signalent lorsqu'il veulent entrer en section critique, et vérifient que personne d'autre ne s'est signalé
- l'automate chevaleresque, où Bob laisse sa place à Alice si les deux veulent entrer en section critique en même temps
- l'automate attente, où Bob entre dans un état r lorsqu'il laisse la priorité à Alice, et une fois qu'il est dans cet état il a la priorité
- l'automate prioritaire, où on intégre une variable turn qui donne la priorité une fois sur deux à Bob et une fois sur deux à Alice

## Propriétés

En ignorant le chemin trivial qui reste dans l'état initial, les 4 propriétés à vérifier sont les suivantes :

P1 : A<> !(alice = c et bob = c)  
P2 : !deadlock  
P3 : A[] (alice = c ou bob = c)  
P4 : (alice = w => alice = c) et (bob = w => bob = c)  

## Tests

On commence par tester les deux premières propriétés sur le programme naif (voir auto_1_naif.py) et le programme deadlock (voir auto_2_deadlock.py). On se rend compte que ni l'une ni l'autre ne respecte les deux propriétés.
Ensuite on teste le programme chevaleresque (voir auto_3_chevaleresque.py) sur les trois premières propriétés. Il vérifie bien les propriétés 1 et 2, mais on observe un livelock si Bob persiste à lever son drapeau. 
Puis on teste le programme attente (voir auto_4_attente.py), et on remarque qu'il respecte bien P1, P2 et P3, mais pas P4.
Enfin, le programe prioritaire (voir auto_5_prioritaire.py)

Un résumé de tous les tests peut être trouvé dans auto_nutshell.py

## Tour de Hanoi

Les fichiers de résolution du problème de la tour de Hanoi se trouvent dans le dossier hanoi. Il y a 2 méthodes de résolution :
- méthode naïve --> voir hanoi.py
- méthode soup --> voir hanoi_soup.py

Chacun de ces fichiers propose la résolution pour une tour d'Hanoi à 2, 3 et 4 étages, et il faut les laisser tourner entre 5 et 10 minutes (la version à 4 étages commence déjà à prendre beaucoup de temps, en effet la complexité de cette résolution est exponentielle du nombre d'étages).
