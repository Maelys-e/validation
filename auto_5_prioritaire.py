import biblio as algo
import automates as prog
import detection_cycles as cycle
import fonctions as func
import detection_finitude as finit

if __name__ == "__main__":

    print("\n--- AUTOMATE PRIORITAIRE ---\n")

    program = prog.program_prioritaire()
    soup = algo.SoupSemantics(program)
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


    print("\n- livelock -")
    print("P3 : A[] (alice = c ou bob = c)")

    
    resultat_cycle = cycle.cycles(graph, prog.program_prioritaire_state, func.contrainte)
    print("\nRésultat des cycles : ", resultat_cycle)
    print("\nDonc P3 est", not resultat_cycle[0])

    print("\n- finitude -")
    print("P4 : (alice = w => alice = c) et (bob = w => bob = c)")

    answer = finit.finitude(prog.program_prioritaire_state)
    print("\nFinalement, P4 est", answer, "\n")
