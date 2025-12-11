import re


"""Module permettant de vérifier si une chaîne est un palindrome."""


def ispalindrome(p):
    """Retourne True si p est un palindrome, False sinon."""
    p = re.sub(r"[@#$%^&* !,?':-]", "", p)
    p = p.lower()
    avant = "éèêëàôîç"
    apres = "eeeeaoic"
    dictio = str.maketrans(avant, apres)
    p = p.translate(dictio)
    for i in range(len(p) // 2):
        if p[i] != p[-1 - i]:
            return False

    return True


def main():
    """Fonction principale contenant les tests."""
    # Tests de la fonction ispalindrome
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()