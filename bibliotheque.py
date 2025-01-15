from collections import deque
import copy

# Correction du prof
def predicate_finder(G, predicate) :
    def check_predicate(n, opaque) :
        # Ici on utilise un prédicat beaucoup plus simple, qui dépend seulement de n
        satisfied = predicate(n)    # True si le prédicat est vérifié lors du parcours, False sinon
        opaque[1] += 1              # Compte le nombre de tours avant d'arriver à terminates
        if satisfied :
            opaque[0] = True
            opaque[2] = n           # Elément du graphe qui répond "vrai" au prédicat
        return satisfied
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
            Init = False
        else :
            current = F.popleft()
            N = G.neighbours(current)
        Init = False
        print(N)
        for n in N :
            if n.state not in k :
                k.add(n.state)
                opaque[0] = False
                terminates = predicate(n, opaque)   # opaque est un objet spécifique à la fonction predicate
                                                    # qui peut être modifié à chaque tour
                if terminates :
                    return ( opaque, n, k)   # un endroit particulier où on vérifie quelque chose avant de terminer le programme
                                             # en l'occurrence on vérifie les conditios fixées par la fonction predicate
                F.append(n)
    return (opaque, None, k)

class RelationToGraph:

    def __init__(self, relation):
        self.relation = relation
        
    def neighbours(self, state) :
        liste2 = []
        liste3 = self.relation.actions(state)
        for a in liste3 :
            targets = self.relation.execute(a, state)
            liste2.extend(targets)
        return liste2

    @property
    def roots(self) :
        return self.relation.initial()
    
    def __str__(self):
        liste = []
        for element in self.roots :
            liste.append(element.state)
        return f"Graph(roots={liste}, relation={self.relation})"

def isdeadlock(sem) : #sem c'est le graph (dit "sémantique")
        print(sem)
        def lambda2(config) :
            return len(sem.actions(config)) == 0
        return lambda2


# On va ensuite utiliser des "pieces", c'est-à-dire des couples condition-action 
# (ex : [a < 5]/a = 3). Par exemple, le programme suivant :
# x = 0
# x += 2
# x = x + 3
# Sera traduit ainsi:
# initialisation : PC = 1, x = 0
# [PC == 1] / x += 2; PC ++
# [PC == 2] / x = x + 3; PC ++
# On ajoute PC ++ à la fin afin de ne pas répéter 2 fois une même action, et de 
# pouvoir passer à l'action suivante
# On peut également utiliser plusieurs PC si on a plusieurs automates (Alice et 
# Bob par exemple donneraient PCa et PCb ou PC_alice et PC_bob)
# On mettra des fonctions à la fois comme actions et comme conditions ("gardes")

class Piece :
    def __init__(self, nom, garde, action) :
        self.nom = nom
        self.garde = garde      # une fontion
        self.behaviour = action    # une fonction aussi (on l'appelle behavious pour pas confondre mais c'est bien ce qu'on a décrit comme une action)
    
    def apply(self, config):
        self.behaviour(config)
        # Ajoutez un état explicite si nécessaire
        if not hasattr(config, 'state'):
            config.state = (config.PC, config.x)
    
    def __repr__(self):
        return f"Piece {self.nom} (garde = {self.garde}, action = {self.behaviour})"

class Soup :
    def __init__(self, start, pieces) :
        self.start = start  # l'initialisation contenant PC et éventuellement les variables du code, qu'on appelle program
        self.pieces = pieces    # une liste, mais en fait peu importe l'ordre puisque c'est PC qui gère l'ordre d'exécution
    
    def add(self, piece) :
        self.pieces.append(piece)
    def extend(self, other_pieces) :
        self.pieces += self.other_pieces
    
    #@property
    def initial(self) :
        return self.start
    
    def __repr__(self):
        return f"Soup(start = {self.start}, pieces = {self.pieces})"

class SoupConfig :
    def __init__(self, map) :
        self.map = map
    def __eq__(self, other) :
        return self.map == other.map
    def __hash__(self) :
        return 0
    # ici on gagne en vruit syntaxique sur eq et hash, mais on perd sur 
    # l'initialisation, donc on n'utilisera pas cette méthode

class SoupSemantics :
    # interpreter du programme Soup
    def __init__(self, program) :
        self.program = program  # une Soupe

    def initial(self) :
        return [self.program.start]
    
    def actions(self, config) :
        # renvoie la liste des pièces qu'on peut renvoyer à un moment donné (va vérifier la garde et donner la liste des pièces telle que la garde est vraie)
        # l'équivalent de la fonction action() dans ce qu'on a vu la semaine dernière
        def fonction_lambda(p) :
            return p.garde(config)
        kk = list(filter(fonction_lambda, self.program.pieces))
        return kk
        # on peut aussi utiliser une boucle for :
        # for p ine self.program.pieces :
        #   if p.garde(config) :
        #       actions.append(p)
        # return actions
    
    def execute(self, piece, config) :
        target = copy.deepcopy(config)
        piece.apply(target)
        #piece.behaviour(target)     # ATTENTION la pièce doit faire partie du program
        return[target]
    def __repr__(self):
        return f"Soup(start = {self.program.start}, pieces = {self.program.pieces})"

# L'exemple donné plus haut se décrirait comme ça :

class Program1Config :
    def __init__(self) :
        self.PC = 1
        self.x = 0
        self.state = (self.PC, self.x)
        
    def __eq__(self, other) :
        return self.x == other.x and self.PC == other.PC
    def __hash__(self) :
        return 0
    def __iter__(self):
        # On retourne un itérateur sur les attributs souhaités
        return iter((self.PC, self.x))

    # il faut alors générer eq et hash pour chaque programme, ce qui peut vite
    # commencer à faire beaucoup de boulot
    def __repr__(self):
        return f"Program(PC={self.PC}, x={self.x})"

def program1() :
    def action_piece_1(config) :
        config.x += 2
        config.PC += 1
        config.state = (config.PC, config.x)
    p1 = Piece("p1", lambda c : c.PC == 1, action_piece_1)
    # ATTENTION une pièce ne peut être définie que depuis l'intérieur d'un programme
    def action_piece_2(config) :
        config.x = config.x + 3
        config.PC += 1
        config.state = (config.PC, config.x)
    p2 = Piece("p2", lambda c : c.PC == 2, action_piece_2)
    soup = Soup(Program1Config(), [p1, p2])
        # on met des parenthèses car on crée une instance de Porgram1Config
    return soup

    

if __name__ == "__main__":
    program1 = program1()
    nu = program1.pieces[0].garde(Program1Config())


    soup1 = SoupSemantics(program1)
    print("\nSoup 1 : ", soup1, "\n")

    graph1 = RelationToGraph(soup1)
    r = graph1.roots
    #print ("Roots : ", r)
    
    (o, n, k) = predicate_finder(graph1, isdeadlock(soup1))
    print("O - isdeadlock : ", o)
    print("N - found : ", n)
    print("K - visited : ", k)

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
