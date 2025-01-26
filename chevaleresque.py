import biblio as algo
import automates as prog
import detection_cycles as cycle
import fonctions as func

if __name__ == "__main__":

    print("\n--- AUTOMATE CHEVALERESQUE ---\n")

    program = prog.program_chevaleresque()
    soup = algo.SoupSemantics(program)
    # print("\nSoup : ", soup1, "\n")
    graph = algo.RelationToGraph(soup)


    print("\n- section critique -")
    print("P1 : A<> !(alice = c et bob = c)")

    (o, n, k) = algo.predicate_finder(graph, func.iscritical)
    print("\nRésultats du predicate_finder :")
    print("  O - iscritical : ", o)
    print("  N - found : ", n)
    print("  K - visited : ", k)
    print("\nDonc P1 est", not o[0])


    print("\n- deadlock -")
    print("P2 : !deadlock")
    
    (o, n, k) = algo.predicate_finder(graph, func.isdeadlock(soup))
    print("\nRésultats du predicate_finder :")
    print("O - isdeadlock : ", o)
    print("N - found : ", n)
    print("K - visited : ", k)
    print("\nDonc P2 est", not o[0], "\n")


    print("\n livelock")
    print("P3 : A[] (alice = c ou bob = c)")

    
    resultat_cycle = cycle.cycles(graph, prog.program_chevaleresque_state, func.contrainte)
    print("Cycles ? ", resultat_cycle[0])
    print("Cycle : ", resultat_cycle[1])
    