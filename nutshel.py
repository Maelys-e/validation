import biblio as algo
import automates as prog
import fonctions as func
import detection_cycles as cycle

if __name__ == "__main__":

    print("\n--- AUTOMATE NAIF ---\n")

    program1 = prog.program_naif()
    soup1 = algo.SoupSemantics(program1)
    graph1 = algo.RelationToGraph(soup1)

    (o, n, k) = algo.predicate_finder(graph1, func.iscritical)
    print("P1 : ", not o[0])
    
    (o, n, k) = algo.predicate_finder(graph1, func.isdeadlock(soup1))
    print("P2 : ", not o[0])


    print("\n--- AUTOMATE DEADLOCK ---\n")

    program1 = prog.program_deadlock()
    soup1 = algo.SoupSemantics(program1)
    graph1 = algo.RelationToGraph(soup1)

    (o, n, k) = algo.predicate_finder(graph1, func.iscritical)
    print("P1 : ", not o[0])
    
    (o, n, k) = algo.predicate_finder(graph1, func.isdeadlock(soup1))
    print("P2 : ", not o[0])


    print("\n--- AUTOMATE CHEVALERESQUE ---\n")

    program = prog.program_chevaleresque()
    soup = algo.SoupSemantics(program)
    graph = algo.RelationToGraph(soup)

    (o, n, k) = algo.predicate_finder(graph, func.iscritical)
    print("P1 : ", not o[0])
    
    (o, n, k) = algo.predicate_finder(graph, func.isdeadlock(soup))
    print("P2 : ", not o[0])

    
    resultat_cycle = cycle.cycles(graph, prog.program_chevaleresque_state, func.contrainte)
    print("P3 : ", not resultat_cycle[0])


    print("\n--- AUTOMATE PRIORITAIRE ---\n")

    program = prog.program_prioritaire()
    soup = algo.SoupSemantics(program)
    graph = algo.RelationToGraph(soup)

    (o, n, k) = algo.predicate_finder(graph, func.iscritical)
    print("P1 : ", not o[0])

    (o, n, k) = algo.predicate_finder(graph, func.isdeadlock(soup))
    print("P2 : ", not o[0])


    resultat_cycle = cycle.cycles(graph, prog.program_chevaleresque_state, func.contrainte)
    print("P3 : ", not resultat_cycle[0])
    
    
    print("P4 :  ?\n")