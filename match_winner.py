import random

def gagnant(a,b):
    print(f"le gagnant est : ")
    R=random.choice([a,b])
    return(R)
resultat = (gagnant("togo","burkina"))
print ( resultat)