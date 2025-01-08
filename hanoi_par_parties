from bibliotheque import predicate_finder
import hanoi
import copy

class HanoiRelation :
    # Une classe de graphe où chaque noeud est une position possible de la tour de Hanoi
    # et où ses voisins sont les autres états accessibles depuis l'état du noeud
    # Le but est de parcourir l'intégralité du graphe, où toutes les possibilités sont représentées,
    # afin de bruteforcer la solution
    def __init__(self, N):
        self.N = N
    def initial(self):
        return [hanoi.HanoiState(list(range(self.N, 0, -1)), [], [])]
    
    def actions(self, config) :
        i = config.state
        actions = []
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
        if droite < milieu and droite < gauche:
            if milieu < gauche :
                actions.append((1, -1, 0))
                if droite :
                    actions.append((0, 1, -1))
                    actions.append((1, 0, -1))
                else :
                    actions.append((0, -1, 1))
                    actions.append((-1, 0, 1))
            else :
                actions.append((-1, 1, 0))
                if droite :
                    actions.append((1, 0, -1))
                    actions.append((0, 1, -1))
                else :
                    actions.append((0, -1, 1))
                    actions.append((-1, 0, 1))
        elif gauche < milieu and gauche < droite :
            if milieu < droite :
                actions.append((0, -1, 1))
                if gauche :
                    actions.append((-1, 1, 0))
                    actions.append((-1, 0, 1))
                else :
                    actions.append((1, -1, 0))
                    actions.append((1, 0, -1))
            else :
                actions.append((0, 1, -1))
                if gauche :
                    actions.append((-1, 0, 1))
                    actions.append((-1, 1, 0))
                else :
                    actions.append((1, -1, 0))
                    actions.append((1, 0, -1))
        elif milieu < gauche and milieu < droite :
            if gauche < droite :
                actions.append((-1, 0, 1))
                if milieu :
                    actions.append((0, -1, 1))
                    actions.append((1, -1, 0))
                else :
                    actions.append((-1, 1, 0))
                    actions.append((0, 1, -1))
            else :
                actions.append((1, 0, -1))
                if milieu :
                    actions.append((0, -1, 1))
                    actions.append((1, -1, 0))
                else :
                    actions.append((-1, 1, 0))
                    actions.append((0, 1, -1))
        elif gauche == droite :
            actions.append((0, -1, 1))
            actions.append((1, -1, 0))
        elif gauche == milieu :
            actions.append((0, 1, -1))
            actions.append((1, 0, -1))
        elif milieu == droite :
            actions.append((-1, 0, 1))
            actions.append((-1, 1, 0))
        return actions
    
    def execute(self, action, config) :
        s = copy.deepcopy(config.state)
        for i in range(3) :
            if action[i] == -1 :
                bougeur = s[i][-1]
                s[i].pop()
        #print ("SELF 1 : ", self, "fin SELF 1")
        for i in range(3) :
            if action[i] == 1 :
                s[i].append(bougeur)
        #print ("SELF 2 : ", self, "fin SELF 2")
        c = hanoi.HanoiState(s[0], s[1], s[2])
        return [c]
    
    def __str__(self):
        liste = []
        for element in self.initial() :
            liste.append(element.state)
        return f"Hanoi(initial={liste}, actions={self.actions})"



class RelationToGraph:

    def __init__(self, relation):
        print("Initialisation")
        self.relation = relation
        
    def neighbours(self, state) :
        #print("Neighbours")
        liste2 = []
        liste3 = self.relation.actions(state)
        #print("LISTE3 : ", liste3)
        for a in liste3 :
            #print ("relation6 : ", self.relation, "fin relation")
            targets = self.relation.execute(a, state)
            #print ("relation7 : ", self.relation, "fin relation")
            liste2.extend(targets)
        return liste2

    @property
    def roots(self) :
        #print ("TEST", self.relation, "FIN TEST")
        return self.relation.initial()
    
    @property
    def graph(self) :
        #print("Build graph")
        return hanoi.generate_graph_hanoi(self.relation.initial(), self.neighbours)
    
    def __str__(self):
        liste = []
        for element in self.roots :
            liste.append(element.state)
        return f"Hanoi(roots={liste}, graph={self.graph})"

if __name__ == "__main__":
    g3 = HanoiRelation(2)
    print ("Relation : ", g3)
    g4 = RelationToGraph(g3)

    r = g4.roots
    print ("Roots : ", r)

    n = g4.neighbours(r[0])
    print ("Neighbours : ", n)

    print("Graph : ", g4)

    (o, n, k) = predicate_finder(g4, lambda _: False)

    print("K : ", k)
    print("O : ", o)
    print("N : ", n)
