from random import choice, randint, seed

print("whaou bienvenue à collège simulator !!!")
print("v 0.3 version public")
a = input("whaou c'est quoi ton nom ???")
seed(a)  # can't wait for speedrun set-seed
print("erreur: ton nom est maintenant jean-pierre decrochage")

fun_name_for_day = ["souffrance", "ennuyance", "inutile", "interweb", "pipi caca prout", "je", "fun", "i like life"]
nomprof = ("enfoiré: math", "amé: français", "homework: histoire")
qi = 120
depression = 0
jour = 1
heure_de_colle = 0
observation = 0
sanc = False

while 1:
    print("jour %s : %s" % (jour, choice(fun_name_for_day)))
    jour = jour + 1
    print("%s : t'est nul !" % choice(nomprof))
    thing = randint(1, 4)
    if thing == 1:
        b = randint(1, 5)
        heure_de_colle = heure_de_colle + b
        print("plus %s heure de colle !" % b)
    elif thing == 2:
        print("t'a une observation !!!!")
        observation = observation + 1
    elif thing == 3:
        print("sanction ! ta mère t'attend à ta maison !!!")
        sanc = True
    else:
        print("t'a de la chance que t'a rien !!!")
    if depression > 99:
        print("tu t'est suicidé !")
        break
    if qi < 1:
        print("t'a plus de qi ! ahahhahaha t'a oublié de respirer")
        break
    if qi > 300:
        print("t'a trop de qi ahahahha t'est mort je sais pas comment ahahhaha")
        break
    if heure_de_colle > 30 or observation > 30:
        print("t'est mort ahhahaha t'a trop d'heure de colles/observation ahhahah")
        break
    print("---bilan---")
    print("heure de colle: %s" % heure_de_colle)
    print("observation: %s" % observation)
    print("---")
    print("ancien qi : %s" % qi)
    print("ancienne depresion : %s" % depression)
    print("---")
    d = ((depression / 3) + ((int(heure_de_colle) / 5) + observation + (depression / 35)))  # mess
    if sanc:
        d = d + 15
        sanc = False
    depression = int(d)
    print("depresion: %s" % depression)
    e = qi - (depression / 25)
    qi = int(e)
    print("qi: %s" % qi)
    truc = None
    while 1:  # loop for input
        f = input("(1)travailler ou se (2)reposer ?")
        try:
            truc = int(f)
        except ValueError:
            pass
        if truc == 1:
            if randint(0, 5):
                depression = depression + randint(2, 15)
            depression = depression + randint(10, 25)
            heure_de_colle = heure_de_colle - 1
            observation = observation - 1
            qi = qi + 5
            if heure_de_colle < 1:
                heure_de_colle = 0
            if observation < 1:
                observation = 0
                break
        elif truc == 2:
            depression = depression - randint(8, 18)
            if heure_de_colle < 1:
                heurcoll = 0
            break
        else:
            print("FAIT QUELQCHOSE LOLOL MDR XDDDDDD")
            continue
    if randint(0, 1) == 1:
        print("WAOW YA DES 3ème QUI VEULE TE VOLER TON GOUTER TU FAIS QUoI XDD LOL MDR")
        while 1:
            a = input("1. donner le gouter 2. s'enfuir 3. se BATTRE #violence")
            try:
                int(a)
            except ValueError:
                print("MAIS UN CHIFFRES HAHAHAHHA MDR XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
                continue
            a = int(a)
            if a == 1:
                print("Ta donné le gouté et té pa mors #triste #collège #no #;(")
                depression = depression + 15
                break
            elif a == 2:
                if randint(0, 1) == 1:
                    print("BRAVO BRAVO !!!!!!!!!?????!!!! kgfvjbhibiu tA RéUSI")
                else:
                    print("TU Té Fé AVOIR HAHHAHAHAHAHA tê NULLE MDRRRRRRRRRRR")
                    depression = depression + 5
                break
            elif a == 3:
                if randint(1, 3) == 3:
                    print("YES KO KO KO LE 3ème EST KOOOOOOOOOOOOO KZIEUHFLBZHZULKEFUKZJNEFJZBHEYFLKIZEJHNFMIOZKNEF")
                    depression = depression - 15
                else:
                    print("ohoohohohohoh ta pa réUSSIIII MDR XDDDDDDDDDDDDDDDd")
                    depression = depression + 20
                break
    if depression < 1:  # fix negative depression
        depression = 0
    print("\n" * 1)
print("hahahah t'est mort ! bon débara !")
if randint(0, 1):
    print("tes parents ont pleuré pour toi... il te regrette !")
else:
    print("tes parents n'ont pas pleuré pour toi... il te regrette pas !")
score = (depression * 100) + (observation * 100) + (qi * 150) + heure_de_colle + (jour * 100)
print("score: %s" % score)
while 1:
    pass
