if __name__ == '__main__':
    fichier = open('day2.txt','r')
    content = fichier.read()
    tab = [x for x in content.split('\n')]

    compteurmdp=0
    for x in tab:
        s = x.split(' ')
        position1= s[0].split('-')[0]
        position2 = s[0].split('-')[1]
        mdp = s[2]
        lettre = s[1].split(":")[0]
        compteurLettres = mdp.count(lettre)

        if mdp[position1] == lettre:
            if mdp[position2] == lettre:
                compteurmdp=compteurmdp+1
                print(compteurmdp)






