from collections import deque

# Corresction du prof
def predicate_finder(G, predicate) :
    def check_predicate(n, opaque) :
        # Ici on utilise un prédicat beaucoup plus simple, qui dépend seulement de n
        opaque[0] = predicate(n)    # True si le prédicat est vérifié lors du parcours, False sinon
        opaque[1] += 1              # Compte le nombre de tours avant d'arriver à terminates
        if opaque[0] :
            opaque[2] = n           # Elément du graphe qui répond "vrai" au prédicat
        return predicate(n)
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
        else :
            current = F.popleft()
            N = G.neighbours(current)
        Init = False
        for n in N :
            if n not in k :
                terminates = predicate(n, opaque)   # opaque est un objet spécifique à la fonction predicate
                                                    # qui peut être modifié à chaque tour
                if terminates :
                    return ( opaque, n, k)   # un endroit particulier où on vérifie quelque chose avant de terminer le programme
                                             # en l'occurrence on vérifie les conditios fixées par la fonction predicate
                k.add(n)
                F.append(n)
    return (opaque, None, k)
