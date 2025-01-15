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

def program_hanoi() :
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


class NBitsConfig :
    def __init__(self) :
        self.bits = 0
    def __eq__(self, o) :
        if not isinstance(o, NBitsConfig) :
            return False
        return self.bits == o.bits
    def __hash__(self) :
        return hash(self.bits)
    
def create_nbits_soup(n) :
    soup = Soup(NBitsConfig())
    def flip(x) :
        def behaviour(c) :
            c.bits = c.bits^(1<<x)
        return behaviour
    for i in range(n) :
        soup.add(Piece(f'flip{i}', lambda c : True, flip(i)))
    return soup
# devraient être utiles pour hanoi

    

if __name__ == "__main__":

    def lambda1(config):
        return config.PC_alice == c and config.PC_bob == c


    print("\n---HANOI---\n")

    program1 = program_hanoi()
    soup1 = algo.SoupSemantics(program1)
    print("\nSoup : ", soup1, "\n")
    graph1 = algo.RelationToGraph(soup1)

    print("-section critique-")

    (o, n, k) = algo.predicate_finder(graph1, lambda1)
    print("O - iscritical : ", o)
    print("N - found : ", n)
    print("K - visited : ", k)
