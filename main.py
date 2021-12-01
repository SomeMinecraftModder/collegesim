from random import choice, randint, seed
from colorama import Fore, Back, Style

print("whaou bienvenue à collège simulator !!!")
print("v 0.3.0 version public")
a = input("whaou c'est quoi ton nom ???")
seed(a)  # can't wait for speedrun set-seed
print("erreur: ton nom est maintenant jean-pierre decrochage")

fun_name_for_day = ["souffrance", "ennuyance", "inutile", "interweb", "pipi caca prout", "je", "fun", "i like life"]
nomprof = ("enfoiré: math", "amé: français", "gégoutosaure: histoire", "pizza: science", "matasse: anglais")
qi = 120
depression = 0
jour = 0
argent = 0.
amis = 0
heure_de_colle = 0
prof_say_list = ["t'est nul!", "non mais n'importe quoi" "hein ? que veux dire le mot \"cool\" ?",
                 "non, pas de question!", "punition collective !", "vous n'aurez pas toujours une calculatrice !",
                 "ton masque !", "sortez vos affaires, les enfants !", "oui, oui, vous devez imprimer ça!",
                 "vous devez faire une belle page de présentation pour l'hivers!", "mais oui c'est très important",
                 "in english please!", "pas de produit en croix",
                 "liste die untrennbaren Partikel auf, sonst bleibe ich bei dir",
                 "Vous ête nul vout comprenez rien au DEUTSCH "]
observation = 0
sanction = False
edt = [[0, 0, 2, 1, 4], [1, 1, 4, 0], [3, 3, 1, 2], [2, 0, 4, 3, 3], [1, 2]]
name_of_day = ["Lundi", "Mardi", 'Mercredi', "Jeudi", "Vendredi", "Samedi", "Dimanche"]

while 1:
    print(Fore.BLACK)
    print(Back.WHITE + "jour %s : %s" % (jour, choice(fun_name_for_day)))
    print("Jour de la semaine: %s" % name_of_day[jour % 7])
    print(Style.RESET_ALL)
    jour = jour + 1
    if not (jour % 7 == 6 or jour % 7 == 0):
        if randint(0, 2) == 1:
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
                        print("YES KO KO KO LE 3ème EST KOOOOOOOOOOOOO KZIEUHFLBZHZULKEFUKZJNEFJZBHEYFKIZEJHNFMIOZKNEF")
                        depression = depression - 15
                    else:
                        print("ohoohohohohoh ta pa réUSSIIII MDR XDDDDDDDDDDDDDDDd")
                        depression = depression + 20
                    break
        current_day_number = jour % 7 - 1
        edt_current = edt[current_day_number]
        current_hour = 0
        for x in edt_current:
            if current_hour % 2 == 1:
                print("WAOW c'ESt L'eur DE lA RéCRéatIoN Les EnfAntS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                while 1:
                    no = input("1. socialiser 2.voler des truc #illégale 3.explorer pour de l'argent")
                    try:
                        yesnt = int(no)
                    except ValueError:
                        print("choisi un chifre sinön ons teu *chiffre* des heur deu coll!!!???!?💩💩💩💩💩💩💩💩💩💩💩💩💩")
                        continue
                    if yesnt == 1:
                        print("")
                    elif yesnt == 2:
                        pass
                    elif yesnt == 3:
                        pass
                    else:
                        print("un chiffr entr 1 et troix :!!!!!!!!!?? :))))))))))))))))")
                        continue
            print("%s : %s" % (nomprof[x], choice(prof_say_list)))
            thing = randint(1, 10)
            if thing == 1:
                b = randint(1, 5)
                heure_de_colle = heure_de_colle + b
                print(Fore.RED + "plus %s heure de colle !" % b)
                print(Style.RESET_ALL)
            elif thing == 2:
                print(Fore.RED + "t'a une observation !!!!")
                print(Style.RESET_ALL)
                observation = observation + 1
            elif thing == 3:
                print(Fore.RED + "sanction ! ta mère t'attend à ta maison !!!")
                print(Style.RESET_ALL)
                sanction = True
            else:
                print(Fore.LIGHTGREEN_EX + "t'a de la chance que t'a rien !!!")
                print(Style.RESET_ALL)
            while 1:
                yes = input("1. suivre les cours de l'éducation national™® 2. ne rien faire 3. tiago (bêta)")
                try:
                    truc = int(yes)
                except ValueError:
                    print(":|")
                    continue
                if truc == 1:
                    print("waow tU SUI LE COUR INCROYABLE")
                    depression = depression + 2
                    qi = qi + 17
                    break
                elif truc == 2:
                    print("Oh NOn Tu A RiEn FaIT OMG :o :OOOOOO COMMENT #prof #education #mince")
                    if randint(0, 1) == 1:
                        print("OOHOHOHOHO LA PRoF A reMARQUé QUE TA rIeN FAit #prof")
                        depression = depression + 3
                    else:
                        print("la prof n'a rien remarqué !!!!!! omg #hashtag")
                        depression = depression - 5
                    break
                elif truc == 3:
                    depression = depression - 5
                    qi = qi - 7
                    while 1:
                        abc = input("choisi ton arme: 1.boulettes de papier 2. ciseaux dans la gorge 3. compas")
                        try:
                            zxy = int(abc)
                        except ValueError:
                            print("AHAHHAHA CHOISI UNE ARME AHAHAH XDDDD LOL MDR LOL LUL prout hahahahahahah")
                            continue
                        if zxy == 1:
                            if randint(0, 1):
                                print("la boulette de papier attaint le prof!")
                                depression = depression - 14
                            else:
                                print("la boulette de papier n'a pas attaint le prof! #sad")
                                depression = depression + 5
                            break
                        elif zxy == 2:
                            if randint(0, 1):
                                print("LE PROF EST MORT !!!!! #mort #ché #khoul #bienfé")
                            else:
                                print("oHohO lA ProF ä eSquiVé le cIsEAux !!!!11!1!11!1! tA UNE SANctiOn !!!!!!!!????")
                                sanction = True
                            break
                        elif zxy == 3:
                            if randint(0, 1):
                                print("LE PROF EST MORT !!!!! #mort #ché #khoul #bienfé")
                            else:
                                print("oHohO lA ProF ä eSquiVé le CompA !!!!11!1!11!1! tA UNE SANctiOn !!!!!!!!????")
                                sanction = True
                            break
                        else:
                            print("AHHAHAHAHHAHAHAHAHHAAHHAHH MAIS UN TRUC §!!!!!!!!!!!!!!!!!!!!!!!!!")
                            continue
                    break
                else:
                    print(":|")
                    continue
            current_hour = current_hour + 1
        while 1:  # loop for input
            f = input("(1)travailler ou se (2)reposer ?")
            try:
                truc = int(f)
                break
            except ValueError:
                print("FAIT QUELQCHOSE LOLOL MDR XDDDDDD")
        if truc == 1:
            depression = depression + 15 + randint(0, 5)
            heure_de_colle = heure_de_colle - 1
            observation = observation - 1
            qi = qi + 5
            if heure_de_colle < 1:
                heure_de_colle = 0
            if observation < 1:
                observation = 0
        elif truc == 2:
            depression = depression - randint(8, 20)
            if heure_de_colle < 1:
                heurcoll = 0
        if depression < 1:  # fix negative depression
            depression = 0
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
        if amis < 1:
            amis = 0
        print("---bilan---")
        print("heure de colle: %s" % heure_de_colle)
        print("observation: %s" % observation)
        print("---")
        print("ancien qi : %s" % qi)
        print("ancienne depresion : %s" % depression)
        print("---")
        d = (depression + ((int(heure_de_colle) / 5) + observation + (depression / 35)))  # mess
        if sanction:
            d = d + 15
            sanction = False
        depression = int(d)
        e = qi - (depression / 25)
        qi = int(e)
        print("depression: %s" % depression)
        print("qi: %s" % qi)
        print("amis: %s" % amis)
        truc = None
    garbage = input("appuie sur entrer pour terminer la journé")
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
