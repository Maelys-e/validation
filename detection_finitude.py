import biblio as algo
import automates as prog
import fonctions as func
import detection_cycles as cycle

def finitude(program) :
    program_1 = program([prog.AliceBobConfigTurn(prog.w, prog.i)])
    soup_1 = algo.SoupSemantics(program_1)
    graph_1 = algo.RelationToGraph(soup_1)
    resultat_cycle = cycle.cycles(graph_1, prog.program_attente_state, func.contrainte_alice)
    r1 =  resultat_cycle[0]

    program_2 = program([prog.AliceBobConfigTurn(prog.w, prog.c)])
    soup_2 = algo.SoupSemantics(program_2)
    graph_2 = algo.RelationToGraph(soup_2)
    resultat_cycle = cycle.cycles(graph_2, prog.program_attente_state, func.contrainte_alice)
    r2 = resultat_cycle[0]

    program_3 = program([prog.AliceBobConfigTurn(prog.w, prog.w)])
    soup_3 = algo.SoupSemantics(program_3)
    graph_3 = algo.RelationToGraph(soup_3)
    resultat_cycle = cycle.cycles(graph_3, prog.program_attente_state, func.contrainte)
    r3 = resultat_cycle[0]

    program_4 = program([prog.AliceBobConfigTurn(prog.c, prog.w)])
    soup_4 = algo.SoupSemantics(program_4)
    graph_4 = algo.RelationToGraph(soup_4)
    resultat_cycle = cycle.cycles(graph_4, prog.program_attente_state, func.contrainte_bob)
    r4 = resultat_cycle[0]

    program_5 = program([prog.AliceBobConfigTurn(prog.i, prog.w)])
    soup_5 = algo.SoupSemantics(program_5)
    graph_5 = algo.RelationToGraph(soup_5)
    (o5, n5, k5) = algo.predicate_finder(graph_5, func.critical_bob)
    resultat_cycle = cycle.cycles(graph_5, prog.program_attente_state, func.contrainte_bob)
    r5 = resultat_cycle[0]

    return (not r1) and (not r2) and (not r3) and (not r4) and (not r5)
