# Vérification
## Projet Alice & Bob

Le but de ce projet est de vérifier un ensemble de propriétés sur des automates Alice & Bob allant du plus simple au plus travaillé. On met ces automates sous la forme de "soupe", c'est-à-dire un ensemble désordonné de pièces qui s'emboîtent les unes dans les autres selon le chemin suivi par l'automate.
On a 4 automates : 
- l'automate naïf, le plus simple
- l'automate deadlock, où Alice et Bob se signalent lorsqu'il veulent entrer en section critique, et vérifient que personne d'autre ne s'est signalé
- l'automate chevaleresque, où Bob laisse sa place à Alice si les deux veulent entrer en section critique en même temps
- l'automate prioritaire, où on intégre une variable turn qui donne la priorité une fois sur deux à Bob et une fois sur deux à Alice

## Propriétés

En ignorant le chemin trivial qui reste dans l'état initial, les 4 propriétés à vérifier sont les suivantes :

P1 : A<> !(alice = c et bob = c)
P2 : !deadlock
P3 : A[] (alice = c ou bob = c)
P4 : (alice = w => alice = c) et (bob = w => bob = c)

## Tests

On commence par tester les deux premières propriétés sur le programme naif (voir naif.py) et le programme deadlock (voir deadlock.py). On se rend compte que ni l'une ni l'autre ne respecte les deux propriétés.
Ensuite on teste le programme chevaleresque (voir chevaleresque.py) sur les trois premières propriétés. Il vérifie bien les propriétés 1 et 2, mais on observe un livelock si Bob persiste à lever son drapeau.
Enfin, le programe prioritaire (voir prioritaire.py)

Un résumé de tous les tests peut être trouvé dans nutshell.py

