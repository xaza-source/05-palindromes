#### Fonction secondaire


def ispalindrome(p):

    for i in range(int(len(p)/2)):
        if p[i] == p[len(p)-1-i]:
            continue
        else:
            return False
    return True

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()