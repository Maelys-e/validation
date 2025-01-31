from collections import deque
import hanoi.hanoi as hanoi
import anciennes_versions.bibliotheque as algo


g1 = hanoi.Hanoi(1)
g2 = hanoi.Hanoi(2)
g3 = hanoi.Hanoi(3)
g4 = hanoi.Hanoi(4)
g5 = hanoi.Hanoi(5)

print ("--RECHERCHE SUR LA PYRAMIDE DE HANOI--")
result = algo.predicate_finder(g1, hanoi.predicate_hanoi)
print ("opaque :", result[0], "\nn :", result[1])#, "\nk :", result[2])
result = algo.predicate_finder(g2, hanoi.predicate_hanoi)
print ("opaque :", result[0], "\nn :", result[1])#, "\nk :", result[2])
result = algo.predicate_finder(g3, hanoi.predicate_hanoi)
print ("opaque :", result[0], "\nn :", result[1])#, "\nk :", result[2])
result = algo.predicate_finder(g4, hanoi.predicate_hanoi)
print ("opaque :", result[0], "\nn :", result[1])#, "\nk :", result[2])
result = algo.predicate_finder(g5, hanoi.predicate_hanoi)
print ("opaque :", result[0], "\nn :", result[1])#, "\nk :", result[2])