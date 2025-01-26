import biblio as algo
import automates as prog
import fonctions as func

def finitude() :
    program_1 = prog.program_prioritaire_state([prog.AliceBobConfigTurn(prog.w, prog.i)])
    soup_1 = algo.SoupSemantics(program_1)
    graph_1 = algo.RelationToGraph(soup_1)
    (o1, n1, k1) = algo.predicate_finder(graph_1, func.critical_alice)

    program_2 = prog.program_prioritaire_state([prog.AliceBobConfigTurn(prog.w, prog.c)])
    soup_2 = algo.SoupSemantics(program_2)
    graph_2 = algo.RelationToGraph(soup_2)
    (o2, n2, k2) = algo.predicate_finder(graph_2, func.critical_alice)

    program_3 = prog.program_prioritaire_state([prog.AliceBobConfigTurn(prog.w, prog.w)])
    soup_3 = algo.SoupSemantics(program_3)
    graph_3 = algo.RelationToGraph(soup_3)
    (o3, n3, k3) = algo.predicate_finder(graph_3, func.critical_alice)
    (o3bis, n3bis, k3bis) = algo.predicate_finder(graph_3, func.critical_bob)

    program_4 = prog.program_prioritaire_state([prog.AliceBobConfigTurn(prog.c, prog.w)])
    soup_4 = algo.SoupSemantics(program_4)
    graph_4 = algo.RelationToGraph(soup_4)
    (o4, n4, k4) = algo.predicate_finder(graph_4, func.critical_bob)

    program_5 = prog.program_prioritaire_state([prog.AliceBobConfigTurn(prog.i, prog.w)])
    soup_5 = algo.SoupSemantics(program_5)
    graph_5 = algo.RelationToGraph(soup_5)
    (o5, n5, k5) = algo.predicate_finder(graph_5, func.critical_bob)

    return o1[0] and o2[0] and o3[0] and o4[0] and o5[0]
        # Ici on ne rajoute pas 'not' devant le résultat parce que, contrairement à avant, si on trouve une solution alors la propriété est vérifiée
