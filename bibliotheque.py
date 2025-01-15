from collections import deque

# Correction du prof
def predicate_finder(G, predicate) :
    def check_predicate(n, opaque) :
        # Ici on utilise un prédicat beaucoup plus simple, qui dépend seulement de n
        satisfied = predicate(n)    # True si le prédicat est vérifié lors du parcours, False sinon
        opaque[1] += 1              # Compte le nombre de tours avant d'arriver à terminates
        if satisfied :
            opaque[0] = True
            opaque[2] = n           # Elément du graphe qui répond "vrai" au prédicat
        return satisfied
    return parcours_bfs_predicate(G, check_predicate, [False, 0, None])

# Correction du prof
def parcours_bfs_predicate(G, predicate, opaque) :
    Init = True
    k = set()
    F = deque()
    while (F or Init) :
        N = None
        if Init :
            N = G.roots
            Init = False
        else :
            current = F.popleft()
            N = G.neighbours(current)
        Init = False
        for n in N :
            if n.state not in k :
                k.add(n.state)
                opaque[0] = False
                terminates = predicate(n, opaque)   # opaque est un objet spécifique à la fonction predicate
                                                    # qui peut être modifié à chaque tour
                if terminates :
                    return ( opaque, n, k)   # un endroit particulier où on vérifie quelque chose avant de terminer le programme
                                             # en l'occurrence on vérifie les conditios fixées par la fonction predicate
                F.append(n)
    return (opaque, None, k)

class RelationToGraph:

    def __init__(self, relation):
        self.relation = relation
        
    def neighbours(self, state) :
        liste2 = []
        liste3 = self.relation.actions(state)
        for a in liste3 :
            targets = self.relation.execute(a, state)
            liste2.extend(targets)
        return liste2

    @property
    def roots(self) :
        return self.relation.initial()
    
    def __str__(self):
        liste = []
        for element in self.roots :
            liste.append(element.state)
        return f"Graph(roots={liste}, relation={self.relation})"

def isdeadlock(sem) : #sem c'est le graph
        def lambda2(config) :
            return len(sem.actions(config)) == 0
        return lambda2
