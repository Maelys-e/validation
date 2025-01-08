import hanoi
import copy
import bibliotheque as algo

class ParentTracer() :
    def __init__(self, n) :
        self.parents = dict()
        self.operand = n
        #list = copy.deepcopy(self.roots)
        #print ("roots : ", list)
        #for i in list :
        #    k = self.neighbours(i)
        #    for j in k :
        #        if j not in list :
        #            list.append(j)
        #    self.parents[i] = k

    @property
    def roots(self):
        rs = self.operand.roots
        for r in rs :
            self.parents[r] = [] # Liste vide qui dit qu'on est arrivés à la racine
        return rs
    
    def neighbours(self, v) :
        ns = self.operand.neighbours(v)
        for n in ns :
            print("n : ", n)
            self.parents[n] = [v] if n not in self.parents else self.parents[n]
        return ns

    @property
    def graph(self) :
        return self.parents

def getTrace(parentage, n) :
    current_state = n
    parent = ParentTracer(n)
    while parent :
        current_state = parent
        parent = parentage[current_state]
    return parent


if __name__ == "__main__":
    h = hanoi.Hanoi(3)
    parentracer = ParentTracer(h)
    (s, n, k) = algo.predicate_finder(parentracer, hanoi.predicate_hanoi)
    print ("parents : ", parentracer.parents)
    if s :
        trace = getTrace(parentracer.parents, n)
        print(trace)
