import random
#word list
words = ['apple', 'banana', 'aupp', 'nak', 'shortking']
#ramdomly select a word from the list
word = random.choice(words)
#number of chances
chances = 5
#empty list to store the guessed letters
print("guess the word")
guessed = ["_"] * len(word)
print(" ".join(guessed))
#loop to run the game
while chances > 0 and "_" in guessed:
    #taking input from the user
    Letter = input("Enter a letter: ")
    print("You havr", chances, "chances left")
    #checking if the letter is in the word
    if guessed.count(Letter) == 0 and Letter in word:
        for i in range(len(word)):
            if word[i] == Letter:
                guessed[i] = Letter
        print(" ".join(guessed))
        if guessed in word:
            print("You won")
            break
    else:
        chances -= 1
        print(" ".join(guessed))
        print("Try again")
        if chances == 0:
            print("You lost")
            break
        print("Enter a Letter: ", end="", flush=True)