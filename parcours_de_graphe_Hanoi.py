from collections import deque
import hanoi as hanoi
import bibliotheque as algo


g1 = hanoi.Hanoi(1)
g2 = hanoi.Hanoi(2)
g3 = hanoi.Hanoi(3)
g4 = hanoi.Hanoi(4)
g5 = hanoi.Hanoi(5)
def predicate_hanoi(n) :
    return n.state[0] == n.state[1] # sont forcément nuls car il n'y a pas de doublons

print ("--RECHERCHE SUR LA PYRAMIDE DE HANOI--")
result = algo.predicate_finder(g1, predicate_hanoi)
print ("opaque :", result[0], "\nn :", result[1])#, "\nk :", result[2])
result = algo.predicate_finder(g2, predicate_hanoi)
print ("opaque :", result[0], "\nn :", result[1])#, "\nk :", result[2])
result = algo.predicate_finder(g3, predicate_hanoi)
print ("opaque :", result[0], "\nn :", result[1])#, "\nk :", result[2])
result = algo.predicate_finder(g4, predicate_hanoi)
print ("opaque :", result[0], "\nn :", result[1])#, "\nk :", result[2])
result = algo.predicate_finder(g5, predicate_hanoi)
print ("opaque :", result[0], "\nn :", result[1])#, "\nk :", result[2])