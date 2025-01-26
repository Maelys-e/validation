import copy
import anciennes_versions.bibliotheque as algo

def generate_graph_hanoi(roots, neighbours):
    list = copy.deepcopy(roots)
    graph = {}
    for i in list :
        k = neighbours(i)
        for j in k :
            if j not in list :
                list.append(j)
        #graph[tuple(map(tuple, i))] = k
        graph[i] = k
    return graph

class Hanoi :
    # Une classe de graphe où chaque noeud est une position possible de la tour de Hanoi
    # et où ses voisins sont les autres états accessibles depuis l'état du noeud
    # Le but est de parcourir l'intégralité du graphe, où toutes les possibilités sont représentées,
    # afin de bruteforcer la solution

    def __init__(self, N):
        self._roots = [HanoiState(list(range(N, 0, -1)), [], [])]

    def neighbours(self, s) :
        #print(s)
        i = s.state
        #print("Là", i)
        neighbours = []
        if len(i[0]) :
            gauche = i[0][-1]
        else :
            gauche = 0
        if len(i[1]) :
            milieu = i[1][-1]
        else :
            milieu = 0
        if len(i[2]) :
            droite = i[2][-1]
        else :
            droite = 0
        #print ("gauche", gauche, " milieu", milieu, " droite", droite)
        if droite < milieu and droite < gauche:
            if milieu < gauche :
                neighbours.append(HanoiState(i[0] + [milieu], i[1][:-1], i[2]))
                if droite :
                    neighbours.append(HanoiState(i[0], i[1] + [droite], i[2][:-1]))
                    neighbours.append(HanoiState(i[0] + [droite], i[1], i[2][:-1]))
                else :
                    neighbours.append(HanoiState(i[0], i[1][:-1], i[2] + [milieu]))
                    neighbours.append(HanoiState(i[0][:-1], i[1], i[2] + [gauche]))
            else :
                neighbours.append(HanoiState(i[0][:-1], i[1] + [gauche], i[2]))
                if droite :
                    neighbours.append(HanoiState(i[0] + [droite], i[1], i[2][:-1]))
                    neighbours.append(HanoiState(i[0], i[1] + [droite], i[2][:-1]))
                else :
                    neighbours.append(HanoiState(i[0], i[1][:-1], i[2] + [milieu]))
                    neighbours.append(HanoiState(i[0][:-1], i[1], i[2] + [gauche]))
        elif gauche < milieu and gauche < droite :
            if milieu < droite :
                neighbours.append(HanoiState(i[0], i[1][:-1], i[2] + [milieu]))
                if gauche :
                    neighbours.append(HanoiState(i[0][:-1], i[1] + [gauche], i[2]))
                    neighbours.append(HanoiState(i[0][:-1], i[1], i[2] + [gauche]))
                else :
                    neighbours.append(HanoiState(i[0] + [milieu], i[1][:-1], i[2]))
                    neighbours.append(HanoiState(i[0] + [droite], i[1], i[2][:-1]))
            else :
                neighbours.append(HanoiState(i[0], i[1] + [droite], i[2][:-1]))
                if gauche :
                    neighbours.append(HanoiState(i[0][:-1], i[1], i[2] + [gauche]))
                    neighbours.append(HanoiState(i[0][:-1], i[1] + [gauche], i[2]))
                else :
                    neighbours.append(HanoiState(i[0] + [milieu], i[1][:-1], i[2]))
                    neighbours.append(HanoiState(i[0] + [droite], i[1], i[2][:-1]))
        elif milieu < gauche and milieu < droite :
            if gauche < droite :
                neighbours.append(HanoiState(i[0][:-1], i[1], i[2] + [gauche]))
                if milieu :
                    neighbours.append(HanoiState(i[0], i[1][:-1], i[2] + [milieu]))
                    neighbours.append(HanoiState(i[0] + [milieu], i[1][:-1], i[2]))
                else :
                    neighbours.append(HanoiState(i[0][:-1], i[1] + [gauche], i[2]))
                    neighbours.append(HanoiState(i[0], i[1] + [droite], i[2][:-1]))
            else :
                neighbours.append(HanoiState(i[0] + [droite], i[1], i[2][:-1]))
                if milieu :
                    neighbours.append(HanoiState(i[0], i[1][:-1], i[2] + [milieu]))
                    neighbours.append(HanoiState(i[0] + [milieu], i[1][:-1], i[2]))
                else :
                    neighbours.append(HanoiState(i[0][:-1], i[1] + [gauche], i[2]))
                    neighbours.append(HanoiState(i[0], i[1] + [droite], i[2][:-1]))
        elif gauche == droite :
            neighbours.append(HanoiState(i[0], i[1][:-1], i[2] + [milieu]))
            neighbours.append(HanoiState(i[0] + [milieu], i[1][:-1], i[2]))
        elif gauche == milieu :
            neighbours.append(HanoiState(i[0], i[1] + [droite], i[2][:-1]))
            neighbours.append(HanoiState(i[0] + [droite], i[1], i[2][:-1]))
        elif milieu == droite :
            neighbours.append(HanoiState(i[0][:-1], i[1], i[2] + [gauche]))
            neighbours.append(HanoiState(i[0][:-1], i[1] + [gauche], i[2]))
        #self.state = tuple(map(tuple, i))
        return neighbours


    @property
    def roots(self) :
        return self._roots
    @property
    def graph(self) :
        return generate_graph_hanoi(self._roots, self.neighbours)
    
    def __str__(self):
        return f"Hanoi(roots={self.roots}, graph={self.graph})"
        
    
class HanoiState():

    def __init__(self, gauche, milieu, droite):
        self.state = (gauche, milieu, droite)

    def __eq__(self, other):
        if not isinstance(other, HanoiState):
            return False
        x = self.state == other.state
        return x #for i in range(len(self.neighbours)) :
            #if self.neighbours[i] != other.neighbours[i]:
                #return False
        #return True
    
    def __hash__(self):
        return hash(tuple(tuple(tour) for tour in self.state))
    
    def __iter__(self) :
        return iter(self.state)
    
    def __repr__(self):
        return f"HanoiState(state={self.state[0], self.state[1], self.state[2]})"


def predicate_hanoi(n) :
    return n.state[0] == n.state[1] # sont forcément nuls car il n'y a pas de doublons

if __name__ == "__main__":
    g4 = Hanoi(2)

    r = g4.roots
    print ("Roots : ", r)

    n = g4.neighbours(r[0])
    print ("Neighbours : ", n)

    print("Graph : ", g4)

    (o, n, k) = algo.predicate_finder(g4, predicate_hanoi)

    print("K : ", k)
    print("O : ", o)
    print("N : ", n)
