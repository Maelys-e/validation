import automates as prog

def iscritical(config):
        return config.PC_alice == prog.c and config.PC_bob == prog.c

def isdeadlock(sem) : # sem c'est le graph (dit "sémantique")
    def lambda2(config) :
        return len(sem.actions(config)) == 0
    return lambda2

def true(state) :
    return True

def contrainte(state) :
    bob = not(state.PC_bob == prog.c)
    alice = not(state.PC_alice == prog.c)
    return bob and alice

def critical_alice(config) :
     return config.PC_alice == prog.c

def critical_bob(config) :
     return config.PC_bob == prog.c