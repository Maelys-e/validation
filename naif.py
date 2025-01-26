import biblio as algo
import automates as prog
import fonctions as func

if __name__ == "__main__":

    print("\n--- AUTOMATE NAIF ---\n")

    program1 = prog.program_naif()
    soup1 = algo.SoupSemantics(program1)
    # print("\nSoup : ", soup1, "\n")
    graph1 = algo.RelationToGraph(soup1)


    print("\n- section critique -")
    print("P1 : A<> !(alice = c et bob = c)")

    (o, n, k) = algo.predicate_finder(graph1, func.iscritical)
    print("\nRésultats du predicate_finder :")
    print("  O - iscritical : ", o)
    print("  N - found : ", n)
    print("  K - visited : ", k)
    print("\nDonc P1 est", not o[0])


    print("\n- deadlock -")
    print("P2 : !deadlock")
    
    (o, n, k) = algo.predicate_finder(graph1, func.isdeadlock(soup1))
    print("\nRésultats du predicate_finder :")
    print("O - isdeadlock : ", o)
    print("N - found : ", n)
    print("K - visited : ", k)
    print("\nDonc P2 est", not o[0], "\n")