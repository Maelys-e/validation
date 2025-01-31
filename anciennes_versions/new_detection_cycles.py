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

class InitRG :
    def __init__(self, G, voisins) :
        self.G = G
        self.voisins = voisins
        
    @property
    def roots(self) :
        return self.voisins
    def neighbours(self, state) :
        return self.G.neighbours(state)
    
def cycles(G, program, contrainte) :
    
    def pred(state) :
        print(state)
        if contrainte(state) :
            print("contrainte")
            voisins = G.neighbours(state)
            G_new = InitRG(G, voisins)
            def lambdal(config) :
                print("lambda")
                if config == state :
                    return True
                return False
            o, n, k = algo.predicate_finder(G_new, lambdal)
            return o[0]
        return False
    
    n = algo.predicate_finder(G, pred)
    return n


if __name__ == "__main__":

    print("\n---VERSION NAIVE---\n")

    program1 = program_naif()
    soup1 = algo.SoupSemantics(program1)
    graph1 = algo.RelationToGraph(soup1)

    def contrainte1(state) :
        return True
    resultat_cycle = cycles(graph1, program_naif_state, contrainte1)
    print("Cycles ? ", resultat_cycle[0])
    print("Cycle : ", resultat_cycle[2])

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
    print("Cycle : ", resultat_cycle[2])

