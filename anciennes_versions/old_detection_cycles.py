import anciennes_versions.bibliotheque as algo

i = "i"
w = "w"
c = "c"

class AliceBobConfig :
    def __init__(self, alice = i, bob = i) :
        self.PC_alice = alice
        self.PC_bob = bob
        self.state = (self.PC_alice, self.PC_bob)
        
    def __eq__(self, other) :
        return self.state == other.state
    def __hash__(self) :
        return 0
    def __iter__(self):
        return iter((self.PC, self.x))

    def __repr__(self):
        return f"Program(PC_alice = {self.PC_alice}, PC_bob = {self.PC_bob})"

def program_naif() :
    def action_piece_1(config) :
        config.PC_alice = c
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p1 = algo.Piece("p1", lambda conf : conf.PC_alice == conf.PC_bob, action_piece_1)
    def action_piece_2(config) :
        config.PC_alice = i
        config.PC_bob = c
        config.state = (config.PC_alice, config.PC_bob)
    p2 = algo.Piece("p2", lambda conf : conf.PC_alice == conf.PC_bob, action_piece_2)
    def action_piece_3(config) :
        config.PC_alice = c
        config.PC_bob = c
        config.state = (config.PC_alice, config.PC_bob)
    p3 = algo.Piece("p3", lambda conf : conf.PC_alice != conf.PC_bob, action_piece_3)
    def action_piece_4(config) :
        config.PC_alice = i
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p4 = algo.Piece("p4", lambda conf : conf.PC_alice != conf.PC_bob, action_piece_4)
    soup = algo.Soup(AliceBobConfig(), [p1, p2, p3, p4])
    return soup

def program_naif_state(state) :
    def action_piece_1(config) :
        config.PC_alice = c
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p1 = algo.Piece("p1", lambda conf : conf.PC_alice == conf.PC_bob, action_piece_1)
    def action_piece_2(config) :
        config.PC_alice = i
        config.PC_bob = c
        config.state = (config.PC_alice, config.PC_bob)
    p2 = algo.Piece("p2", lambda conf : conf.PC_alice == conf.PC_bob, action_piece_2)
    def action_piece_3(config) :
        config.PC_alice = c
        config.PC_bob = c
        config.state = (config.PC_alice, config.PC_bob)
    p3 = algo.Piece("p3", lambda conf : conf.PC_alice != conf.PC_bob, action_piece_3)
    def action_piece_4(config) :
        config.PC_alice = i
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p4 = algo.Piece("p4", lambda conf : conf.PC_alice != conf.PC_bob, action_piece_4)
    soup = algo.Soup(AliceBobConfig(state.PC_alice, state.PC_bob), [p1, p2, p3, p4])
    return soup

def program_chevaleresque() :
    def action_piece_1(config) :
        config.PC_alice = w
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p1 = algo.Piece("p1", lambda conf : (conf.PC_alice == i and conf.PC_bob == i) or ((conf.PC_alice == w and conf.PC_bob == w) or (conf.PC_alice == w and conf.PC_bob == c)), action_piece_1)
    def action_piece_2(config) :
        config.PC_alice = i
        config.PC_bob = w
        config.state = (config.PC_alice, config.PC_bob)
    p2 = algo.Piece("p2", lambda conf : (conf.PC_alice == i and conf.PC_bob == i) or (conf.PC_alice == c and conf.PC_bob == w), action_piece_2)
    def action_piece_3(config) :
        config.PC_alice = w
        config.PC_bob = w
        config.state = (config.PC_alice, config.PC_bob)
    p3 = algo.Piece("p3", lambda conf : (conf.PC_alice == i and conf.PC_bob == w) or (conf.PC_alice == w and conf.PC_bob == i), action_piece_3)
    def action_piece_4(config) :
        config.PC_alice = i
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p4 = algo.Piece("p4", lambda conf : (conf.PC_alice == i and conf.PC_bob == c) or (conf.PC_alice == c and conf.PC_bob == i), action_piece_4)
    def action_piece_5(config) :
        config.PC_alice = i
        config.PC_bob = c
        config.state = (config.PC_alice, config.PC_bob)
    p5 = algo.Piece("p5", lambda conf : conf.PC_alice == i and conf.PC_bob == w, action_piece_5)
    def action_piece_6(config) :
        config.PC_alice = c
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p6 = algo.Piece("p6", lambda conf : conf.PC_alice == w and conf.PC_bob == i, action_piece_6)
    def action_piece_7(config) :
        config.PC_alice = w
        config.PC_bob = c
        config.state = (config.PC_alice, config.PC_bob)
    p7 = algo.Piece("p7", lambda conf : conf.PC_alice == i and conf.PC_bob == c, action_piece_7)
    def action_piece_8(config) :
        config.PC_alice = c
        config.PC_bob = w
        config.state = (config.PC_alice, config.PC_bob)
    p8 = algo.Piece("p8", lambda conf : conf.PC_alice == c and conf.PC_bob == i, action_piece_8)
    soup = algo.Soup(AliceBobConfig(), [p1, p2, p3, p4 ,p5, p6, p7, p8])
    return soup

def program_chevaleresque_state(state) :
    def action_piece_1(config) :
        config.PC_alice = w
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p1 = algo.Piece("p1", lambda conf : (conf.PC_alice == i and conf.PC_bob == i) or ((conf.PC_alice == w and conf.PC_bob == w) or (conf.PC_alice == w and conf.PC_bob == c)), action_piece_1)
    def action_piece_2(config) :
        config.PC_alice = i
        config.PC_bob = w
        config.state = (config.PC_alice, config.PC_bob)
    p2 = algo.Piece("p2", lambda conf : (conf.PC_alice == i and conf.PC_bob == i) or (conf.PC_alice == c and conf.PC_bob == w), action_piece_2)
    def action_piece_3(config) :
        config.PC_alice = w
        config.PC_bob = w
        config.state = (config.PC_alice, config.PC_bob)
    p3 = algo.Piece("p3", lambda conf : (conf.PC_alice == i and conf.PC_bob == w) or (conf.PC_alice == w and conf.PC_bob == i), action_piece_3)
    def action_piece_4(config) :
        config.PC_alice = i
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p4 = algo.Piece("p4", lambda conf : (conf.PC_alice == i and conf.PC_bob == c) or (conf.PC_alice == c and conf.PC_bob == i), action_piece_4)
    def action_piece_5(config) :
        config.PC_alice = i
        config.PC_bob = c
        config.state = (config.PC_alice, config.PC_bob)
    p5 = algo.Piece("p5", lambda conf : conf.PC_alice == i and conf.PC_bob == w, action_piece_5)
    def action_piece_6(config) :
        config.PC_alice = c
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p6 = algo.Piece("p6", lambda conf : conf.PC_alice == w and conf.PC_bob == i, action_piece_6)
    def action_piece_7(config) :
        config.PC_alice = w
        config.PC_bob = c
        config.state = (config.PC_alice, config.PC_bob)
    p7 = algo.Piece("p7", lambda conf : conf.PC_alice == i and conf.PC_bob == c, action_piece_7)
    def action_piece_8(config) :
        config.PC_alice = c
        config.PC_bob = w
        config.state = (config.PC_alice, config.PC_bob)
    p8 = algo.Piece("p8", lambda conf : conf.PC_alice == c and conf.PC_bob == i, action_piece_8)
    soup = algo.Soup(AliceBobConfig(state.PC_alice, state.PC_bob), [p1, p2, p3, p4 ,p5, p6, p7, p8])
    return soup

    

def cycles(G, program, contrainte) :
    # On commence par faire la liste des états
    liste_etats = G.roots

    # Ensuite on prend chaque état (on touche pas encore aux états d'acceptation)
    for state in liste_etats :
        # On fait la liste des voisins
        voisins = G.neighbours(state)
        print("state : ", state)
        print("voisins : ", voisins)
        for voisin in voisins :
            if voisin != state :
                print("voisin : ", voisin)
                print(G.neighbours(voisin))
                print(G.neighbours(G.neighbours(voisin)[0]))
                # On crée un programme qui commence à chaque voisin de cet état
                program1 = program(voisin)
                    # on ne prend pas G.relation.program parce que là ça dépend de l'état
                soup1 = algo.SoupSemantics(program1)
                graph1 = algo.RelationToGraph(soup1)
                print("roots : ", graph1.roots)
                # On définit le prédicate qui cherche la présence de state en partant de 
                def predicate(config) :
                    if config == state and contrainte(state) :
                        return True
                    return False
                # On chercher la présence de state
                (o, n, k) = algo.predicate_finder(graph1, predicate)
                # Si on a trouvé state, alors on a un cycle et on sort :
                if o[0] :
                    tuple_voisin = (voisin.PC_alice, voisin.PC_bob)
                    k.add(tuple_voisin)
                    return (True , k)    
                        # on rajoute voisin au début, car k ne contient que les états atteints depuis voisin, donc pas voisin lui-même  
    # Sinon on sort en disant qu'on a rien trouvé
    return (False, None)


if __name__ == "__main__":

    print("\n---VERSION NAIVE---\n")

    program1 = program_naif()
    soup1 = algo.SoupSemantics(program1)
    graph1 = algo.RelationToGraph(soup1)

    def contrainte1(state) :
        return True
    resultat_cycle = cycles(graph1, program_naif_state, contrainte1)
    print("Cycles ? ", resultat_cycle[0])
    print("Cycle : ", resultat_cycle[1])

    print("\n--- VERSION CHEVALERESQUE ---\n")

    program2 = program_chevaleresque()
    soup2 = algo.SoupSemantics(program2)
    graph2 = algo.RelationToGraph(soup2)

    def contrainte2(state) :
        bob = not(state.PC_bob == c)
        alice = not(state.PC_alice == c)
        return bob and alice
    resultat_cycle = cycles(graph2, program_chevaleresque_state, contrainte2)
    print("Cycles ? ", resultat_cycle[0])
    print("Cycle : ", resultat_cycle[1])



    """ print("-deadlock-")
    
    (o, n, k) = algo.predicate_finder(graph1, algo.isdeadlock(soup1))
    print("O - isdeadlock : ", o)
    print("N - found : ", n)
    print("K - visited : ", k)

    print("-section critique-")

    def lambda1(config):
        return config.PC_alice == c and config.PC_bob == c

    (o, n, k) = algo.predicate_finder(graph1, lambda1)
    print("O - iscritical : ", o)
    print("N - found : ", n)
    print("K - visited : ", k) """

