import bibliotheque as algo
import copy
from collections import deque

w = "w"
i = "i"
c = "c"

class AliceBobConfig :
    # l'équivalent de HanoiState
    def __init__(self, a = i, b = i):
        self.a = a
        self.b = b
        self.state = (a, b)
    
    def __repr__(self):
        return f"(Alice = {self.a}, Bob = {self.b})"

class AliceBobRelation :
    def initial(self):
        return [AliceBobConfig(i, i)]
    
    def execute(self, action, config) :
        if action[0] :
            a = action[0]
            b = config.b
        else :
            a = config.a
            b = action[1]
        c = AliceBobConfig(a, b)
        return [c]
    
    def __repr__(self):
        liste = []
        for element in self.initial() :
            liste.append(element.state)
        return f"Alice&Bob(initial={liste})"
    
class AliceBobNaif(AliceBobRelation) :
    
    def actions(self, config) :
        a = config.a
        b = config.b
        list = []
        if a == i :
            list.append((c, 0))
        elif a == c :
            list.append((i, 0))
        if b == i :
            list.append((0, c))
        elif b == c :
            list.append((0, i))
        return list
    
class AliceBob2(AliceBobRelation) :
    # On introduit un état WAIT pour gérer la section critique
    # et respecter le propriété P1 : !(self.a == c and self.b == c)
    
    def actions(self, config) :
        a = config.a
        b = config.b
        list = []
        if a == i :
            list.append((w, 0))
        elif a == w and b == i :
            list.append((c, 0))
        elif a == c :
            list.append((i, 0))
        if b == i :
            list.append((0, w))
        elif b == w and a == i :
            list.append((0, c))
        elif b == c :
            list.append((0, i))
        return list
    
class AliceBob3(AliceBobRelation) :
    # On ajoute la reddition de Bob
    # pour respecter la propriété P2 : !deadlock
 
    def actions(self, config) :
        a = config.a
        b = config.b
        list = []
        if a == i :
            list.append((w, 0))
        elif a == w and b == i :
            list.append((c, 0))
        elif a == c :
            list.append((i, 0))
        if b == i :
            list.append((0, w))
        elif b == w and a == i :
            list.append((0, c))
        elif b == w and a == w :
            list.append((0, i))
        elif b == c :
            list.append((0, i))
        return list
       

   
if __name__ == "__main__":

    def lambda1(config):
        return config.a == c and config.b == c

    print("\n---VERSION NAIVE---\n")

    g1 = AliceBobNaif()
    print ("Relation 1 : ", g1)
    g4 = algo.RelationToGraph(g1)
    r = g4.roots
    print ("Roots : ", r)
    n = g4.neighbours(r[0])
    print ("Neighbours : ", n)
    visited_configs = set()
    def lambda2(config):
        if config.state in visited_configs:
            return True
        visited_configs.add(config.state)
        actions = g1.actions(config)
        return len(actions) == 0

    visited_configs = set()
    print("\n-Lambda1-")
    (o, n, k) = algo.predicate_finder(g4, lambda1)
    print("O : ", o)
    print("N : ", n)
    print("K : ", k)
    print("\n-Lambda2-")
    (o, n, k) = algo.predicate_finder(g4, lambda2)
    print("O : ", o)
    print("N : ", n)
    print("K : ", k)
    
    print("\n---VERSION DEADLOCK---\n")

    g2 = AliceBob2()
    print ("Relation 2 : ", g2)
    g5 = algo.RelationToGraph(g2)
    r = g5.roots
    print ("Roots : ", r)
    n = g5.neighbours(r[0])
    print ("Neighbours : ", n)
    visited_configs = set()
    def lambda2(config):
        if config.state in visited_configs:
            return True
        # devrait pouvoir être enlevé
        visited_configs.add(config.state)
        actions = g2.actions(config)
        return len(actions) == 0
    print("\n-Lambda1-")
    (o, n, k) = algo.predicate_finder(g5, lambda1)
    print("O : ", o)
    print("N : ", n)
    print("K : ", k)
    print("\n-Lambda2-")
    (o, n, k) = algo.predicate_finder(g5, lambda2)
    print("O : ", o)
    print("N : ", n)
    print("K : ", k)
    
    print("\n---VERSION CHEVALERESQUE---\n")

    g3 = AliceBob3()
    print ("Relation 3 : ", g3)
    g6 = algo.RelationToGraph(g3)
    r = g6.roots
    print ("Roots : ", r)
    n = g6.neighbours(r[0])
    print ("Neighbours : ", n)
    visited_configs = set()
    def lambda2(config):
        if config.state in visited_configs:
            return True
        # devrait pouvoir être enlevé aussi
        visited_configs.add(config.state)
        actions = g3.actions(config)
        return len(actions) == 0
    print("\n-Lambda1--")
    (o, n, k) = algo.predicate_finder(g6, lambda1)
    print("O : ", o)
    print("N : ", n)
    print("K : ", k)
    print("\n-Lambda2-")
    (o, n, k) = algo.predicate_finder(g6, lambda2)
    print("O : ", o)
    print("N : ", n)
    print("K : ", k)


    print("\n---VERSION DU PROF : LAMBDA2 POUR LES 2 DERNIERES VERSIONS---\n")

    print("\n-Version 2-")
    print ("Relation : ", g2)
    r = g5.roots
    print ("Roots : ", r)
    n = g5.neighbours(r[0])
    print ("Neighbours : ", n)

    (o, n, k) = algo.predicate_finder(g5, algo.isdeadlock(g2))
    # ici on a appelé avec la sémantique g3 en argument, 
    # ce qui éite de définir un lambda2 différent pour chaque graphe, 
    # et on pourrait la mettre en bibliothèque (le test du deadlock 
    # peut ainsi se faire sur n'importe quel système)
    print("(O) - Is deadlock ? : ", o)
    print("(N) - For what configuration ? : ", n)
    print("(K) - Visited configurations : ", k)

    print("\n-Version 3-")
    print ("Relation : ", g3)
    r = g6.roots
    print ("Roots : ", r)
    n = g6.neighbours(r[0])
    print ("Neighbours : ", n)

    (o, n, k) = algo.predicate_finder(g6, algo.isdeadlock(g3))
    # ici on a appelé avec la sémantique g3 en argument, 
    # ce qui éite de définir un lambda2 différent pour chaque graphe, 
    # et on pourrait la mettre en bibliothèque (le test du deadlock 
    # peut ainsi se faire sur n'importe quel système)
    print("(O) - Is deadlock ? : ", o)
    print("(N) - For what configuration ? : ", n)
    print("(K) - Visited configurations : ", k)
