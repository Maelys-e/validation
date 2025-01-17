import bibliotheque as algo

i = "i"
w = "w"
c = "c"

class HanoiConfig :
    def __init__(self, n) :
        self.PC_gauche = list(range(n, 0, -1))
        self.PC_milieu = []
        self.PC_droite = []
        self.state = (tuple(self.PC_gauche), tuple(self.PC_milieu), tuple(self.PC_droite))
        
    def __eq__(self, other) :
        return self.state == other.state
    def __hash__(self) :
        return hash(self.state)
    def __iter__(self):
        return iter((self.PC, self.x))
    
    def state_update(self) :
        self.state = (tuple(self.PC_gauche), tuple(self.PC_milieu), tuple(self.PC_droite))

    def __repr__(self):
        return f"Hanoi(gauche = {self.PC_gauche}, milieu = {self.PC_milieu}, droite = {self.PC_droite})"



def program_hanoi(n) :
    
    def deplacement_gauchedroite(config) :
        deplace = config.PC_gauche[-1]
        config.PC_gauche.remove(deplace)
        config.PC_droite.append(deplace)
        config.state_update()
    def condition1(conf) :
        if len(conf.PC_gauche) :
            if len(conf.PC_droite) :
                return conf.PC_gauche[-1] < conf.PC_droite[-1]
            return True
        return False
    p1 = algo.Piece("gauche-droite", condition1, deplacement_gauchedroite)

    def deplacement_gauchemilieu(config) :
        deplace = config.PC_gauche[-1]
        config.PC_gauche.remove(deplace)
        config.PC_milieu.append(deplace)
        config.state_update()
    def condition2(conf) :
        if len(conf.PC_gauche) :
            if len(conf.PC_milieu) :
                return conf.PC_gauche[-1] < conf.PC_milieu[-1]
            return True
        return False
    p2 = algo.Piece("gauche-milieu", condition2, deplacement_gauchemilieu)

    def deplacement_milieudroite(config) :
        deplace = config.PC_milieu[-1]
        config.PC_milieu.remove(deplace)
        config.PC_droite.append(deplace)
        config.state_update()
    def condition3(conf) :
        if len(conf.PC_milieu) :
            if len(conf.PC_droite) :
                return conf.PC_milieu[-1] < conf.PC_droite[-1]
            return True
        return False
    p3 = algo.Piece("milieu-droite", condition3, deplacement_milieudroite)

    def deplacement_milieugauche(config) :
        deplace = config.PC_milieu[-1]
        config.PC_milieu.remove(deplace)
        config.PC_gauche.append(deplace)
        config.state_update()
    def condition4(conf) :
        if len(conf.PC_milieu) :
            if len(conf.PC_gauche) :
                return conf.PC_milieu[-1] < conf.PC_gauche[-1]
            return True
        return False
    p4 = algo.Piece("milieu-gauche", condition4, deplacement_milieugauche)

    def deplacement_droitegauche(config) :
        deplace = config.PC_droite[-1]
        config.PC_droite.remove(deplace)
        config.PC_gauche.append(deplace)
        config.state_update()
    def condition5(conf) :
        if len(conf.PC_droite) :
            if len(conf.PC_gauche) :
                return conf.PC_droite[-1] < conf.PC_gauche[-1]
            return True
        return False
    p5 = algo.Piece("droite-gauche", condition5, deplacement_droitegauche)

    def deplacement_droitemilieu(config) :
        deplace = config.PC_droite[-1]
        config.PC_droite.remove(deplace)
        config.PC_milieu.append(deplace)
        config.state_update()
    def condition6(conf) :
        if len(conf.PC_droite) :
            if len(conf.PC_milieu) :
                return conf.PC_droite[-1] < conf.PC_milieu[-1]
            return True
        return False
    p6 = algo.Piece("droite-milieu", condition6, deplacement_droitemilieu)

    soup = algo.Soup(HanoiConfig(n), [p1, p2, p3, p4, p5, p6])
    return soup




    

if __name__ == "__main__":

    def lambda1(config):
        return config.state[0] == config.state[1]
        # si ils sont égaux alors les 2 sont vides, et toutes les pièces sont à droite


    print("\n---HANOI 2---\n")

    program1 = program_hanoi(2)
    soup1 = algo.SoupSemantics(program1)
    #print("\nSoup : ", soup1, "\n")
    graph1 = algo.RelationToGraph(soup1)

    (o, n, k) = algo.predicate_finder(graph1, lambda1)
    print("O - has a solution : ", o)
    print("N - final state : ", n)
    print("K - visited : ", k)

    print("\n---HANOI 3---\n")

    program1 = program_hanoi(3)
    soup1 = algo.SoupSemantics(program1)
    #print("\nSoup : ", soup1, "\n")
    graph1 = algo.RelationToGraph(soup1)

    (o, n, k) = algo.predicate_finder(graph1, lambda1)
    print("O - has a solution : ", o)
    print("N - final state : ", n)
    print("K - visited : ", k)

    print("\n---HANOI 4---\n")

    program1 = program_hanoi(4)
    soup1 = algo.SoupSemantics(program1)
    #print("\nSoup : ", soup1, "\n")
    graph1 = algo.RelationToGraph(soup1)

    (o, n, k) = algo.predicate_finder(graph1, lambda1)
    print("O - has a solution : ", o)
    print("N - final state : ", n)
    print("K - visited : ", k)

    print("\n---HANOI 5---\n")

    program1 = program_hanoi(5)
    soup1 = algo.SoupSemantics(program1)
    #print("\nSoup : ", soup1, "\n")
    graph1 = algo.RelationToGraph(soup1)

    (o, n, k) = algo.predicate_finder(graph1, lambda1)
    print("O - has a solution : ", o)
    print("N - final state : ", n)
    print("K - visited : ", k)
