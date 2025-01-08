from collections import deque
import copy
import bibliotheque as algo

def parcours(roots, graph) :
    currents = copy.deepcopy(roots)
    previous = []
    while len(currents) != 0:
        i = currents[-1]
        currents.remove(i)
        previous.append(i)
        if i in graph.keys() :
            for j in graph[i] :
                if j not in previous:
                    currents.append(j)
    return previous

class DictRootedGraph :
    def __init__(self, graph, roots):
        self._data = graph
        self._roots = roots

    @property
    def roots(self) :
        return self._roots
    @property
    def neighbours(self) :
        return self._data
    
    def __str__(self):
        return f"DictRootedGraph(roots={self.roots}, graph={self.graph})"

def parcours_full(G) :
    currents = copy.deepcopy(G.roots)
    previous = []
    while len(currents) != 0:
        i = currents[-1]
        currents.remove(i)
        previous.append(i)
        if i in G.neighbours.keys() :
            for j in G.neighbours[i] :
                if j not in previous:
                    currents.append(j)
    return previous

# Correction du prof
def parcours_rapide_bfs(G) :
    Init = True
    k = set()
    F = deque()
    while (F or Init) :
        if Init :
            N = G.roots
        else :
            current = F.popleft()
            if current in G.neighbours.keys():
                N = G.neighbours[current]
        Init = False
        for n in N :
            if n not in k :
                k.add(n)
                F.append(n)
    return k

def generate_graph(roots, neighbours):
    list = copy.deepcopy(roots)
    graph = {}
    for i in list :
        k = neighbours(i)
        for j in k :
            if j not in list :
                list.append(j)
        graph[i] = k
    return graph

class Nbits :
    # On pourrait aussi implémenter une autre classe sous la forme d'une liste des Edges
    # car l'algorithme bfs est indépendant de comment on implémente le graphe
    def __init__(self, roots, N):
        self._roots = roots
        self._n = N

    @property
    def roots(self) :
        return self._roots
    def neighbours(self, S) :
        neighbours = []
        for i in range(self._n) :
            neighbours.append(S^(1<<i)) # On flippe d'1 bit vers la gauche,
                                        # mais en fait on pourrait mettre n'importe quelle fonction on s'en fout
                                        # c'est juste pour créer le graphe 
                                        # (on définit les voisins comme ceux qui n'ont qu'un bit de différence avec le noeud)
        return neighbours
    @property
    def graph(self) :
        return generate_graph(self._roots, self.neighbours)



roots = [1, 3]
graph = {1:[2,3], 2:[3,4,1], 3:[5,6]}
G = DictRootedGraph(graph, roots)
def predicate_1(n, opaque) :
    if n == opaque[0] :
        return True
    return False
opaque_1 = [4]          # On utilise des listes parce qu'on veut que la variable globale soit modifiée
def predicate_2(n, opaque) :
    if n == 4 :
        opaque[0] = True
    else :
        opaque[0] = False
    return opaque[0]
opaque_2 = [False]      # On peut mettre ce qu'on veut en opaque et s'en servir comme on veut
def predicate_3(n, opaque) :
    if n == opaque[1] :
        opaque[0] = True
    else :
        opaque[0] = False
    return opaque[0]
opaque_3 = [False, 4]   # On peut même mettre plusieurs valeurs dans la liste
def simple_predicate(n) :
    return n==4
# Le prédicat simplifié est juste une condition booléenne ici
G2 = Nbits([1], 6)
G3 = Nbits([1], 4)
def predicate_g3(n) :
    return n == 12



print ("--PARCOURS EN PROFONDEUR--")
print (parcours(roots, graph))
print ("--AVEC LA STRUCTURE DE CLASSE--")
print (parcours_full(G))
print ("--LA FONCTION DU PROF--")
print (parcours_rapide_bfs(G))
print ("--EN UTILISANT PREDICATE ET OPAQUE--")
print ("Version 1")
result = algo.parcours_bfs_predicate(G, predicate_1, opaque_1)
print ("opaque :", result[0], " n :", result[1], " k :", result[2])
print ("Version 2")
result = algo.parcours_bfs_predicate(G, predicate_2, opaque_2)
print ("opaque :", result[0], " n :", result[1], " k :", result[2])
print ("--AVEC LE PREDICATE SIMPLIFIE--")
result = algo.predicate_finder(G, simple_predicate)
print ("opaque :", result[0], " n :", result[1], " k :", result[2])
print ("--AVEC UN GRAPHE GENERE--")
print ("On cherche à obtenir 4 avec 6 bits")
result = algo.predicate_finder(G2, simple_predicate)
print ("opaque :", result[0], " n :", result[1], " k :", result[2])
print ("On cherche 12 avec 4 bits")
result = algo.predicate_finder(G3, predicate_g3)
print ("opaque :", result[0], " n :", result[1], " k :", result[2])
