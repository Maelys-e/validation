import biblio as algo

i = "i"
w = "w"
c = "c"
b = "bob"
a = "alice"


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
        return iter((self.PC_alice, self.PC_bob))

    def __repr__(self):
        return f"AliceBobConfig(PC_alice = {self.PC_alice}, PC_bob = {self.PC_bob})"

def program_naif_state(states) :
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
    roots = []
    for state in states :
        roots.append(AliceBobConfig(state.PC_alice, state.PC_bob))
    soup = algo.Soup(roots, [p1, p2, p3, p4])
    return soup

def program_naif() :
    state = AliceBobConfig()
    return program_naif_state([state])

def program_deadlock_state(states) :
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
    roots = []
    for state in states :
        roots.append(AliceBobConfig(state.PC_alice, state.PC_bob))
    soup = algo.Soup(roots, [p1, p2, p3, p4 ,p5, p6, p7, p8])
    return soup

def program_deadlock() :
    return program_deadlock_state([AliceBobConfig()])

def program_chevaleresque_state(states) :
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
    roots = []
    for state in states :
        roots.append(AliceBobConfig(state.PC_alice, state.PC_bob))
    soup = algo.Soup(roots, [p1, p2, p3, p4 ,p5, p6, p7, p8])
    return soup

def program_chevaleresque() :
    return program_chevaleresque_state([AliceBobConfig()])

class AliceBobConfigTurn :
    def __init__(self, alice = i, bob = i) :
        self.PC_alice = alice
        self.PC_bob = bob
        self.turn = a
        self.state = (self.PC_alice, self.PC_bob, self.turn)
        
    def __eq__(self, other) :
        return self.state == other.state
    def __hash__(self) :
        return 0
    def __iter__(self):
        return iter((self.PC_alice, self.PC_bob))

    def __repr__(self):
        return f"AliceBobConfigTurn(PC_alice = {self.PC_alice}, PC_bob = {self.PC_bob}, turn = {self.turn})"

def program_prioritaire_state(states) :
    def action_piece_1(config) :
        config.PC_alice = w
        config.PC_bob = i
        config.turn = b
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p1 = algo.Piece("p1", lambda conf : 
            ((conf.PC_alice == i and conf.PC_bob == i) and conf.turn == b), action_piece_1)
    def action_piece_1bis(config) :
        config.PC_alice = w
        config.PC_bob = i
        config.turn = a
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p1bis = algo.Piece("p1bis", lambda conf : 
            (((conf.PC_alice == i and conf.PC_bob == i) and conf.turn == a) or ((conf.PC_alice == w and conf.PC_bob == c) and conf.turn == b)) or (conf.PC_alice == w and conf.PC_bob == c and (conf.turn == a)), action_piece_1bis)
    def action_piece_2(config) :
        config.PC_alice = i
        config.PC_bob = w
        config.turn = b
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p2 = algo.Piece("p2", lambda conf : 
            (((conf.PC_alice == i and conf.PC_bob == i) and conf.turn == b) or ((conf.PC_alice == c and conf.PC_bob == w) and conf.turn == a)) or (conf.turn == b and (conf.PC_alice == c and conf.PC_bob == w)), action_piece_2)
    def action_piece_2bis(config) :
        config.PC_alice = i
        config.PC_bob = w
        config.turn = a
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p2bis = algo.Piece("p2bis", lambda conf : 
            (conf.PC_alice == i and conf.PC_bob == i) and conf.turn == a, action_piece_2bis)
    def action_piece_3(config) :
        config.PC_alice = w
        config.PC_bob = w
        config.turn = b
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p3 = algo.Piece("p3", lambda conf : 
            (conf.turn == b and(conf.PC_alice == i and conf.PC_bob == w) or (conf.PC_alice == w and conf.PC_bob == i)), action_piece_3)
    def action_piece_3bis(config) :
        config.PC_alice = w
        config.PC_bob = w
        config.turn = a
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p3bis = algo.Piece("p3bis", lambda conf : 
            (conf.turn == a and (conf.PC_alice == i and conf.PC_bob == w) or (conf.PC_alice == w and conf.PC_bob == i)), action_piece_3bis)
    def action_piece_4(config) :
        config.PC_alice = i
        config.PC_bob = i
        config.turn = b
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p4 = algo.Piece("p4", lambda conf : 
            (conf.turn == b and (conf.PC_alice == i and conf.PC_bob == c)) or (conf.turn == a and(conf.PC_alice == c and conf.PC_bob == i)), action_piece_4)
    def action_piece_4bis(config) :
        config.PC_alice = i
        config.PC_bob = i
        config.turn = a
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p4bis = algo.Piece("p4bis", lambda conf : 
            (conf.turn == b and (conf.PC_alice == i and conf.PC_bob == c)) or (conf.turn == a and(conf.PC_alice == c and conf.PC_bob == i)), action_piece_4bis)
    def action_piece_5(config) :
        config.PC_alice = i
        config.PC_bob = c
        config.turn = b
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p5 = algo.Piece("p5", lambda conf : 
            conf.turn == b and (conf.PC_alice == i and conf.PC_bob == w), action_piece_5)
    def action_piece_5bis(config) :
        config.PC_alice = i
        config.PC_bob = c
        config.turn = a
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p5bis = algo.Piece("p5bis", lambda conf : 
            conf.turn == a and (conf.PC_alice == i and conf.PC_bob == w), action_piece_5bis)
    def action_piece_6(config) :
        config.PC_alice = c
        config.PC_bob = i
        config.turn = b
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p6 = algo.Piece("p6", lambda conf : 
            conf.turn == b and (conf.PC_alice == w and conf.PC_bob == i), action_piece_6)
    def action_piece_6bis(config) :
        config.PC_alice = c
        config.PC_bob = i
        config.turn = a
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p6bis = algo.Piece("p6bis", lambda conf : 
            conf.turn == a and (conf.PC_alice == w and conf.PC_bob == i), action_piece_6bis)
    def action_piece_7(config) :
        config.PC_alice = w
        config.PC_bob = c
        config.turn = b
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p7 = algo.Piece("p7", lambda conf : 
            (conf.turn == b and (conf.PC_alice == i and conf.PC_bob == c)) or (conf.turn == b and (conf.PC_alice == w and conf.PC_bob == w)), action_piece_7)
    def action_piece_7bis(config) :
        config.PC_alice = w
        config.PC_bob = c
        config.turn = a
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p7bis = algo.Piece("p7bis", lambda conf : 
            conf.turn == a and (conf.PC_alice == i and conf.PC_bob == c), action_piece_7bis)
    def action_piece_8(config) :
        config.PC_alice = c
        config.PC_bob = w
        config.turn = b
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p8 = algo.Piece("p8", lambda conf : 
            conf.turn == b and (conf.PC_alice == c and conf.PC_bob == i), action_piece_8)
    def action_piece_8bis(config) :
        config.PC_alice = c
        config.PC_bob = w
        config.turn = a
        config.state = (config.PC_alice, config.PC_bob, config.turn)
    p8bis = algo.Piece("p8bis", lambda conf : 
            (conf.turn == a and (conf.PC_alice == c and conf.PC_bob == i)) or (conf.turn == a and (conf.PC_alice == w and conf.PC_bob == w)), action_piece_8bis)
    roots = []
    for state in states :
        roots.append(AliceBobConfigTurn(state.PC_alice, state.PC_bob))
    soup = algo.Soup(roots, [p1, p1bis, p2, p2bis, p3, p3bis, p4, p4bis,p5, p5bis, p6, p6bis, p7, p7bis, p8, p8bis])
    return soup

def program_prioritaire() :
    return program_prioritaire_state([AliceBobConfigTurn()])