import random

# creation
ALPHABET_LOWER = 'azertyuiopqsdfghjklmwxcvbn'
ALPHABET_UPPER = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
NUMBERS = '1234567890'
SYMBOLS ='?%*$#€&!/'

def gen_psw(size,maj,nb,sy):
    psw = ''

    # logic of repartition, add extra
    if nb == 'y':
        for _ in range(round(size*0.25)):
            print("Add numbers.")
            psw += random.choice(NUMBERS)
    if sy == 'y':
        for _ in range(round(size*0.1)):
            print("Add symbols.")
            psw += random.choice(SYMBOLS)
    if capital == 'y':
        for _ in range(round(size*0.3)):
            print("Add capital letters.")
            psw += random.choice(ALPHABET_UPPER)

    # add letters
    while len(psw) < size:
        psw += random.choice(ALPHABET_LOWER)

    # mix the password
    psw_list = list(psw)
    random.shuffle(psw_list)
    psw = ''.join(psw_list)

    return psw

def requestValidation(message):
    while True:
        answer = input(message).lower().strip()
        if answer in ['y', 'n', 'yes', 'no']:
            return answer
        print("Error : Make sure to answer with 'y' (yes) or 'n' (no)")

if __name__ == "__main__":
    print("=== PASSWORD GENERATOR ===")
    
    # ask the parameters to the user
    while True:
        try:
            size = int(input("Password lenght (e.g. : 12) : "))
            if size < 7:
                if size <= 0 : 
                    print("The lenght must be positive !")
                    continue
                print("Too short password, choose at least 7.")
                continue
            break
        except ValueError:
            print("Make sure you enter numbers.")

    capital = requestValidation("Do you want to include capital letters? (y/n) : ")
    nb = requestValidation("Do you want to include numbers? (y/n) : ")
    sym = requestValidation("Do you want to include symbols ? (y/n) : ")

    
    resultat = gen_psw(size, capital, nb, sym)

    print("\n------------------------------")
    print(f"Ton mot de passe généré : {resultat}")
    print("------------------------------")