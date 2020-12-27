import random
import time
import os
def clear():
        os.system('cls')
tryAgian=True
while tryAgian==True:
    hangmanDraw = ['''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''']

    words=["turtles","flowers","typography","processor","pancake","detection","photography","keyboard"]
    
    sucsess=False
    newWord_generate=True  

    word=""
    old_word=""

    name=input("Enter your name: ")
    print(f'''Hello {name}, Welcome to HangMan!!
    you have 4 attemps to guess the word ''')
    attempts=0
    def dash(word=word):
        """ function to create random-dashed words and """ 
        dashed_word=""
        for i in word:
            randDash=random.randint(0,1)
            if randDash==0:
                dashed_word+="_"
            elif randDash==1:
                dashed_word+=i
        return dashed_word
    while newWord_generate==True:  
        word=random.choice(words)

        while old_word==word:
            word=random.choice(words) 
            """ to prevent repeating random words """
        print(word)

        dashed_word=dash(word)  
        print(dashed_word) 
        newWord=input("Want to change the Word? (press 'y' to change) :").lower()
        if newWord=="y":
            old_word=word
            newWord_generate=True
        else:newWord_generate=False

    while attempts<4:
        guess=input("Enter your guess: ")
        if word==guess:
            sucsess=True
            print("congrats, You Won!!")
            break
        else:
            print(hangmanDraw[attempts])           
            attempts+=1
            sucsess=False
    if sucsess==False:
        print("sorry wrong guess!")

    tryAgian=input("Try Again? (press 'y' to confirm) :").lower()
    if tryAgian=="y":
        clear()
        tryAgian=True
    else:
        tryAgian=False

        
    







