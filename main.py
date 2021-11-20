from random import choice, randint, seed

print("whaou bienvenue à collège simulator !!!")
print("v 0.3 version public")
a = input("whaou c'est quoi ton nom ???")
seed(a)
print("erreur: ton nom est maintenant jean-pierre decrochage")

nomprof = ("enfoiré: math", "amé: français", "homework: histoire")
qi = 120
dep = 0
jour = 1
heurcolle = 0
ob = 0
sanc = False

while 1:
    print("jour %s : souffrance" % jour)
    jour = jour + 1
    print("%s : t'est nul !" % choice(nomprof))
    thing = randint(1, 4)
    if thing == 1:
        b = randint(1, 5)
        heurcolle = heurcolle + b
        print("plus %s heure de colle !" % b)
    elif thing == 2:
        print("t'a une observation !!!!")
        ob = ob + 1
    elif thing == 3:
        print("sanction ! ta mère t'attend à ta maison !!!")
        sanc = True
    else:
        print("t'a de la chance que t'a rien !!!")
    if dep > 99:
        print("tu t'est suicidé !")
        break
    if qi < 1:
        print("t'a plus de qi ! ahahhahaha t'a oublié de respirer")
        break
    if qi > 300:
        print("t'a trop de qi ahahahha t'est mort je sais pas comment ahahhaha")
        break
    if heurcolle > 30 or ob > 30:
        print("t'est mort ahhahaha t'a trop d'heure de colles/observation ahhahah")
        break
    print("---bilan---")
    print("heure de colle: %s" % heurcolle)
    print("observation: %s" % ob)
    print("---")
    print("ancien qi : %s" % qi)
    print("ancienne depresion : %s" % dep)
    print("---")
    d = ((dep/3) + ((int(heurcolle) / 5) + ob + (dep/35)))
    if sanc:
        d = d + 15
        sanc = False
    dep = int(d)
    print("depresion: %s" % dep)
    e = qi - (dep/25)
    qi = int(e)
    print("qi: %s" % qi)
    truc = None
    while 1:
        f = input("(1)travailler ou se (2)reposer ?")
        try:
            truc = int(f)
        except:
            pass
        if truc == 1:
            if randint(0, 5):
                dep = dep + randint(2, 15)
            dep = dep + randint(10, 25)
            heurcolle = heurcolle - 1
            ob = ob - 1
            qi = qi + 5
            if heurcolle < 1:
                heurcolle = 0
            if ob <1:
                ob = 0
        elif truc == 2:
            dep = dep - randint(8, 18)
            if heurcolle <1:
                heurcoll = 0
        else:
            print("FAIT QUELQCHOSE LOLOL MDR XDDDDDD")
            continue
    if dep < 1:
            dep = 0
print("hahahah t'est mort ! bon débara !")
if randint(0, 1):
    print("tes parents ont pleuré pour toi... il te regrette !")
else:
    print("tes parents n'ont pas pleuré pour toi... il te regrette pas !")
score = (dep * 100) + (ob * 100) + (qi * 150) + heurcolle + (jour*100)
print("score: %s" % score)
while 1:
    pass
