'''
higher-lower guessing game

'''

import random,os ,time,sys

num = 0
highscorefile = os.getcwd() + "\\\\highscore.txt"

#create file if not exist
if  not os.path.exists(highscorefile):
    with open(highscorefile, "w"):
        pass

        


def setmax(maxnum = 0):
    global num
    if maxnum == 0:
        try:
            maxnum = int(input("Enter the maxvalue: "))
            if maxnum < 2:
                print("Too low!")
                setmax()
            num = random.randint(1,maxnum)
        except:
            print("Invalid input!")
            setmax()
    else:
        num = random.randint(1,100)

def infgame():
    global num
    tries = 1
    
    setmax()
    while True:
        while True:
            try:
                guess = int(input("Please enter your guess"))
                break
            except:
                pass
        if guess == num:
            print("Congrats! You guessed my number in " + str(tries) + " guesses!")
            break
        elif guess < num:
            print("your guess is too low! number of tries: " + str(tries))
        elif guess > num:
            print("your guess is too high! number of tries: " + str(tries))
        tries+=1


def limitgame():
    global num
    tries = 1
    
    setmax(100)
    while True:
        while True:
            try:
                guess = int(input("Please enter your guess"))
                break
            except:
                pass
        
        if guess == num:
            print("Congrats! You guessed my number in " + str(tries) + " guesses!")
            break
        elif guess < num and tries < 6:
            print("your guess is too low! number of tries: " + str(tries))
        elif guess > num and tries < 6:
            print("your guess is too high! number of tries: " + str(tries))
        else:
            print("The number i was thinking of was " + str(num))
            break
        tries+=1

def highscore():
    global highscorefile
    highscores = []
    first = "NIL 999"
    second = "NIL 999"
    third = "NIL 999"
    print("high score is only for challenge mode")

    with open(highscorefile, "r") as file:
        highscores = [x for x in file.read().split("\n") if x is not ""]

    
    
    for i in highscores:
        temp = int(i.split(" ")[1])

        if temp < int(first.split(" ")[1]):
            if int(first.split(" ")[1]) < int(second.split(" ")[1]):
                second = first
            elif int(first.split(" ")[1]) < int(third.split(" ")[1]):
                third = first
            first = i
        elif temp < int(second.split(" ")[1]):
            if int(second.split(" ")[1]) < int(third.split(" ")[1]):
                third = second
            second = i
            
        elif temp < int(third.split(" ")[1]):
            third = i

    print("First: ".ljust(10) + first.split()[0].ljust(10) + " - ".ljust(5) + first.split()[1])
    print("Second: ".ljust(10)+ second.split()[0].ljust(10) + " - ".ljust(5) + second.split()[1])
    print("Third: ".ljust(10) + third.split()[0].ljust(10) + " - ".ljust(5) + third.split()[1])
    input("Enter to continue")
def challenge():
    global num
    tries = 1
    
    setmax(100)
    while True:
        while True:
            try:
                guess = int(input("Please enter your guess"))
                break
            except:
                pass
        if guess == num:
            print("Congrats! You guessed my number in " + str(tries) + " guesses!")
            break
        elif guess < num:
            print("your guess is too low! number of tries: " + str(tries))
        elif guess > num:
            print("your guess is too high! number of tries: " + str(tries))
        tries+=1
    name = input("Please enter your name: ")
    return name + " " + str(tries) + "\n"
def main():
    global highscorefile
    
    while True:
        playagn = ""
        print("[1]  guess from 1-100 in 6 tries or less")
        print("[2]  custom maxvalue ulimited tries")
        print("[3]  challenge mode 1-100 in least amount of tries")
        print("[4]  highscores")
        print("[99] exit")
        
        while True:
            try:
                choice= int(input())
                break
            except:
                print("Invalid input!")

        if choice == 99:
            playagn = "n"
            pass
        elif choice == 1:
            limitgame()
        elif choice == 2:
            infgame()
        elif choice == 3:
            score = challenge()
            with open(highscorefile, "a") as file:
                file.write(score)
        elif choice == 4:
            highscore()
            playagn = "y"
        else:
            print("Out of range!")
            time.sleep(2)
            os.system("cls")
            main()
        while playagn not in ["y","n"]:
            playagn = input("Play again? y/n").lower()

        if playagn == "y":
            time.sleep(2)
            os.system("cls")
        else:
            print("bye!")
            time.sleep(2)
            break
            

if __name__ == "__main__":
    main()
