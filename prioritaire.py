import biblio as algo
import automates as prog
import detection_cycles as cycle
import fonctions as func

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

    
    resultat_cycle = cycle.cycles(graph, prog.program_chevaleresque_state, func.contrainte)
    print("Cycles ? ", resultat_cycle[0])
    print("Cycle : ", resultat_cycle[1])

    print("\n- finitude -")
    print("P4 : (alice = w => alice = c) et (bob = w => bob = c)")

    program_1 = prog.program_prioritaire_state([prog.AliceBobConfigTurn(prog.w, prog.i)])
    soup_1 = algo.SoupSemantics(program_1)
    graph_1 = algo.RelationToGraph(soup_1)
    (o1, n1, k1) = algo.predicate_finder(graph_1, func.critical_alice)
    print("alice = w and bob = i : ", not o1[0])

    program_2 = prog.program_prioritaire_state([prog.AliceBobConfigTurn(prog.w, prog.c)])
    soup_2 = algo.SoupSemantics(program_2)
    graph_2 = algo.RelationToGraph(soup_2)
    (o2, n2, k2) = algo.predicate_finder(graph_2, func.critical_alice)
    print("alice = w and bob = c : ", not o2[0])

    program_3 = prog.program_prioritaire_state([prog.AliceBobConfigTurn(prog.w, prog.w)])
    soup_3 = algo.SoupSemantics(program_3)
    graph_3 = algo.RelationToGraph(soup_3)
    (o3, n3, k3) = algo.predicate_finder(graph_3, func.critical_alice)
    (o3bis, n3bis, k3bis) = algo.predicate_finder(graph_3, func.critical_bob)
    print("alice = w and bob = w : ", not (o3[0] or o3bis[0]))

    program_4 = prog.program_prioritaire_state([prog.AliceBobConfigTurn(prog.c, prog.w)])
    soup_4 = algo.SoupSemantics(program_4)
    graph_4 = algo.RelationToGraph(soup_4)
    (o4, n4, k4) = algo.predicate_finder(graph_4, func.critical_bob)
    print("alice = c and bob = w : ", not o4[0])

    program_5 = prog.program_prioritaire_state([prog.AliceBobConfigTurn(prog.i, prog.w)])
    soup_5 = algo.SoupSemantics(program_5)
    graph_5 = algo.RelationToGraph(soup_5)
    (o5, n5, k5) = algo.predicate_finder(graph_5, func.critical_bob)
    print("alice = i and bob = w : ", not o5[0])
