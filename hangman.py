import random

print("WELCOME TO HANGMAN GAME")
print("----------------------------------")
word=["secret","ritika","apple","ubuntu"]
randomword=random.choice(word)
print(randomword)
for x in randomword:
    print("_",end=" ")
def print_hangman(wrong):
    if wrong==0:
        print("\n+---+")
        print("     |")
        print("     |")
        print("     |")
        print("    ===")
    elif wrong==1:
        print("\n+---+")
        print("O    |")
        print("     |")
        print("     |")
        print("    ===")
    elif wrong==2:
        print("\n+---+")
        print(" O    |")
        print(" |    |")
        print("      |")
        print("    ===")
    elif wrong==3:
        print("\n+---+")
        print(" O    |")
        print("/|    |")
        print("      |")
        print("    ===")
    elif wrong==4:
        print("\n+---+")
        print(" O    |")
        print("/|\   |")
        print("      |")
        print("    ===")
    elif wrong==5:
        print("\n+---+")
        print(" O    |")
        print("/|\   |")
        print("/     |")
        print("    ===")
    elif wrong==6:
        print("\n+---+")
        print(" O    |")
        print("/|\   |")
        print("/ \   |")
        print("    ===")

def printword(guessedletters):
    counter=0
    rightletters=0
    for char in randomword:
        if char in guessedletters:
            print(randomword[counter],end=" ")
            rightletters+=1
        else:
            print(" ",end=" ")
        counter=counter+1
    return rightletters


def printlines():
    print("\r")
    for char in randomword:
        print("\u203E",end=" ")

length_of_word=len(randomword)
amount_wrong=0
current_guess_index=0
current_letters=[]
current_lettersright=0

while amount_wrong!=6 and current_lettersright!=length_of_word:
    print("\nletters guessed so far:")
    for letter in current_letters:
        print(letter,end="  ")
    letterguessd=input("guess a letter")
    if randomword[current_guess_index]==letterguessd:
        print_hangman(amount_wrong)
        current_guess_index+=1
        current_letters.append(letterguessd)
        current_lettersright=printword(current_letters)
        printlines()
    else:
        amount_wrong+=1
        current_letters.append(letterguessd)
        print_hangman(amount_wrong)
        current_lettersright=printword(current_letters)
        printlines()
print("Game is over! thank you for playing")