from abc import abstractmethod, ABC
from collections import deque
import copy


######################################
# --- Séances de décembre --- #
######################################

class RootedGraph(ABC):
    def __init__(self):
        return

    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def roots(self, roots):
        pass

    @abstractmethod
    def neighbours(self, node):
        pass

    def __hash__(self):
        return 1

class ParentTracer(RootedGraph):
    def __init__(self, operand):
        self.parents = {}
        self.operand = operand

    @property
    def roots(self):
        rs = self.operand.roots  # Hanoi node
        for r in rs:
            self.parents[r] = []
        return rs

    def neighbours(self, v):
        rs = self.operand.neighbours(v)
        for n in rs:
            if n not in self.parents:
                self.parents[n] = [v]
            elif self.parents[n] == []:
                self.parents[n] = [v]
        return rs


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


def parcours_bfs_predicate(G, predicate, opaque) :
    # print("\nG : ", G)
    Init = True
    k = set()
    F = deque()
    while (F or Init) :
        N = None
        if Init :
            N = G.roots
            Init = False
        else :
            # print("\nF : ", F)
            current = F.popleft()
            # print("current : ", current)
            N = G.neighbours(current)
        Init = False
        for n in N :
            print("n : ", n, "\nk : ", k)
            if n.state not in k :
                k.add(n.state)
                opaque[0] = False
                terminates = predicate(n, opaque)   # opaque est un objet spécifique à la fonction predicate
                                                    # qui peut être modifié à chaque tour
                print(terminates)
                if terminates :
                    return ( opaque, n, k)   # un endroit particulier où on vérifie quelque chose avant de terminer le programme
                                             # en l'occurrence on vérifie les conditios fixées par la fonction predicate
                F.append(n)
    return (opaque, None, k)


######################################
# --- Séance du 8 janvier --- #
######################################

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
    
    def __repr__(self):
        liste = []
        for element in self.roots :
            liste.append(element.state)
        return f"Graph(roots={liste}, relation={self.relation})"

def isdeadlock(sem) : # sem c'est le graph (dit "sémantique")
        def lambda2(config) :
            return len(sem.actions(config)) == 0
        return lambda2


######################################
# --- Séance du 15 janvier --- #
######################################

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
        return self.program.start
    
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


# un exemple pour générer des pièces automatiquement
class NBitsConfig :
    def __init__(self) :
        self.bits = 0 # un entier : mis à 0 comme valeur initiale (un entier de 32 bits)
    def __eq__(self, o) :
        if not isinstance(o, NBitsConfig) :
            return False
        return self.bits == o.bits
    def __hash__(self) :
        return hash(self.bits)
    def __repr__(self) :
        return f"NBitsConfig (bits = {self.bits})"
    
def create_nbits_soup(n) : # n = le nombre de bits qu'on veut bouger sur self.bits
    soup = Soup(NBitsConfig(), [])
    def flip(x) :
        def behaviour(c) :
            c.bits = c.bits^(1<<x) # on modifie des bits du nombre
        return behaviour
    for i in range(n) :
        soup.add(Piece(f'flip{i}', lambda c : True, flip(i)))
    return soup


######################################
# --- Séance du 17 janvier --- #
######################################

# Bon c'est très bien ce qu'on a fait jusque là mais il y a un problème : pour 
# détecter des boucles il nous faut encoder des automates de Büchi. En effet, 
# pour l'instant on ne peut exprimer que des propriétés locales à un état. On 
# introduit donc un automate de Büchi, dont les gardes des transitions portent 
# sur des automates extérieurs (par exemple Alice et Bob) et non sur lui-même : 
# on passe alors à une échelle globale plutôt que locale.
# On va utiliser des instances de soup (un peu modifiées) et un langage, et on 
# introduit des états de rejet (par exemple lorsqu'on arrive à la section 
# critique, l'automate de Büchi qu'on a introduit passe en état de rejet).
# il nous faut le code de la sémantique (le langage) et de l'intersecteur (qui 
# fait l'intersection entre le langage et la soup modifiée)

# --> le but est de détecter des boucles

"""     
class RootedDependentRelation :
    def __init__(self, program) :
        self.program = program

    @abstractmethod
    def initial(self) :
        pass
    @abstractmethod
    def actions(self, input, config) :
        pass
    @abstractmethod
    def execute(self, a, input, config) :
        pass

class SoupDependantSemantics (RootedDependentRelation):

    def initial(self) :
        return [self.program.start]
    def actions(self, input, config) :
        def lambdak(p) :
            return p.garde(input, config) # pour rappel garde est une fonction (avec retour booléen) de notre choix
        retour = list(filter(lambdak, self.program.pieces))
        return retour
    def execute(self, piece, config) :
        target = copy.deepcopy(config)
        print(piece)
        piece.behaviour(target) # et behaviour est une fonction de notre choix
        return [target]

    def __repr__(self) :
        return f"SoupDependantSemantics (program = {self.program})"

class Stutter(object) :
    def __new__(cls) :
        if not hasattr(cls, 'instance'):
            cls.instance = super
    
class Step :
    def __init__(self, lc, rc) :
        self.rc = rc
        self.lc = lc
    @property
    def state(self) :
        return (self.lc, self.rc)
    
    def __iter__(self):
        return iter((self.rc, self.lc))
    
    def __repr__(self) :
        return f"Step (lhs = {self.lc}, rhs = {self.rc})"
    
class StepIntersectionSemantics :
    def __init__(self, lefthand_side, righthand_side) :
        self.lhs = lefthand_side
        self.rhs = righthand_side
        # les deux côtés entrant dans l'intersection

    def initial(self) :
        configs = []
        for lc in self.lhs.initial() :
            for rc in self.rhs.initial() :
                configs.append(Step(lc, rc))
        return configs
    
    def actions(self, config) :
        print("\n##HERE##\n")
        print("config : ", config)
        sync_actions = []
        l_c, r_c = config.lc, config.rc
        print("self.lhs : ", self.lhs)
        left_actions = self.lhs.actions(l_c)
        # vu qu'on travaille à gauche, on utilise la configuration de "gauche"
        n_actions = len(left_actions) # "nombre d'actions productives", la liste des actions utiles (aka "qui produisent des choses")
        print("left_actions : ", left_actions)
        print("len(left(actions)) : ", n_actions)
        for l_a in left_actions :
            left_targets = self.rhs.execute(l_a, l_c)
            # ici je suis pas sûre de ce que j'ai fait, j'ai supposé que r_c était la actual config
            if len(left_targets) == 0 :
                n_actions -= 1
            print("\nBOUCLE SUR LEFT_TARGETS")
            for l_t in left_targets :
                l_step = (l_c, l_a, l_t)
                print("\nl_step : ", l_step)
                print("\nr_c : ", r_c)
                print("\nself : ", self)
                # jusque là on a calculé un pas à gauche
                right_actions = self.rhs.actions(l_step, r_c)
                print("\n ACTION1 : ", right_actions)
                # on passe l'entrée dans la sémantique à droite pour avancer d'un pas à droite
                def lambdak(r_a) :
                    return (l_step, r_a)
                sync_actions.append(Step(right_actions, l_c))
                # là on a fini les actions synchrones
        if n_actions == 0 :
            # pour vérifier l'absence de deadlock
            l_step = (l_c, Stutter(), l_t)
            right_actions = self.rhs.actions(l_step, r_c)
            print("\n ACTION : ", right_actions)
            def lambdal(r_a) :
                return (l_step, r_a)
            sync_actions.extends(map(lambdal, right_actions))
        print("RETOUR : ", sync_actions)
        return sync_actions
    
    def execute(self, action, config) :
        l_step, r_a = action
        l_c, r_c = config.lc, config.rc
        print("r_a : ", r_a)
        right_targets = self.rhs.execute(r_a[0], r_c)
        l_cx, l_a, l_t = l_step # ici l_cx c'est pareil que le l_c d'avant
        def lambdam(r_t) :
            return (l_t, r_t)
        targets = map(lambdam, right_targets)
        return list(targets)

    def __repr__(self) :
        return f"StepIntersectionSemantics (lhs = {self.lhs}, rhs = {self.rhs})"

 """
    

if __name__ == "__main__":

    print("--- VERSION DU 15/01/2025 (DITE 'SOUPE') ---")

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

    print("--- VERSION DU 17/01/2025 (FINALE) ---")

"""     
    class ConfP1 :
        def __init__(self) :
            self.PC = 0

        @property
        def state(self) :
            return self.PC

        def __hash__(self):
            return hash(self.PC)
        def __eq__(self, other) :
            return self.PC == other.PC
        def __repr__(self) :
            return f"ConfP1 (PC = {self.PC})"
    
    def nbits_has_3_even() :
        # détecte s'il existe un chemin qui a 3 nombres pairs
        def lambdao(step, conf) :
            (source_config, a, target_config) = step
            return (source_config.bits % 2) == 0
        def p1a(conf) :
            conf.PC += 1
            return conf.PC
        p1 = Piece("even", lambdao, p1a)
        def lambdap(step, conf) :
            (source_config, a, target_config) = step
            return (source_config.bits % 2) != 0
        def p2a(conf) :
            return conf.PC
        p2 = Piece("not even", lambdap, p2a)
        soup = Soup(ConfP1(), [p1, p2])
        def lambdaq(conf) :
            return conf.PC == 3
        return (soup, lambdaq)
    
    S = create_nbits_soup(5)
    (p, accept) = nbits_has_3_even()
    ss = SoupSemantics(S)
    sp = SoupDependantSemantics(p)
    s_inter = StepIntersectionSemantics(ss, sp)
    print(s_inter)
    rrzrg = RelationToGraph(s_inter)
    print("G :", rrzrg)
    pt = ParentTracer(rrzrg)    # renvoie  le parcours de graphe qui est solution (pour hanoi par exemple)
    def lambdan(conf) :
        l_c, r_c = conf.lc, conf.rc
        return accept(r_c)
    (s, n, c), k = predicate_finder(rrzrg, lambdan)
    pt.get_trace(n)
    print("Résultat") """
