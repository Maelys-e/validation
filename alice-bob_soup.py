import bibliotheque as algo

i = "i"
w = "w"
c = "c"

class AliceBobConfig :
    def __init__(self) :
        self.PC_alice = i
        self.PC_bob = i
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

def program_deadlock() :
    def action_piece_1(config) :
        config.PC_alice = w
        config.PC_bob = i
        config.state = (config.PC_alice, config.PC_bob)
    p1 = algo.Piece("p1", lambda conf : (conf.PC_alice == i and conf.PC_bob == i) or (conf.PC_alice == w and conf.PC_bob == c), action_piece_1)
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

    

if __name__ == "__main__":

    print("\n---VERSION NAIVE---\n")

    program1 = program_naif()
    soup1 = algo.SoupSemantics(program1)
    print("\nSoup : ", soup1, "\n")
    graph1 = algo.RelationToGraph(soup1)

    print("-deadlock-")
    
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
    print("K - visited : ", k)


    print("\n---VERSION DEADLOCK---\n")

    program1 = program_deadlock()
    soup1 = algo.SoupSemantics(program1)
    print("\nSoup : ", soup1, "\n")
    graph1 = algo.RelationToGraph(soup1)

    print("-deadlock-")
    
    (o, n, k) = algo.predicate_finder(graph1, algo.isdeadlock(soup1))
    print("O - isdeadlock : ", o)
    print("N - found : ", n)
    print("K - visited : ", k)

    print("-section critique-")

    (o, n, k) = algo.predicate_finder(graph1, lambda1)
    print("O - iscritical : ", o)
    print("N - found : ", n)
    print("K - visited : ", k)


    print("\n---VERSION CHEVALERESQUE---\n")

    program1 = program_chevaleresque()
    soup1 = algo.SoupSemantics(program1)
    print("\nSoup : ", soup1, "\n")
    graph1 = algo.RelationToGraph(soup1)

    print("-deadlock-")
    
    (o, n, k) = algo.predicate_finder(graph1, algo.isdeadlock(soup1))
    print("O - isdeadlock : ", o)
    print("N - found : ", n)
    print("K - visited : ", k)

    print("-section critique-")

    (o, n, k) = algo.predicate_finder(graph1, lambda1)
    print("O - iscritical : ", o)
    print("N - found : ", n)
    print("K - visited : ", k)
