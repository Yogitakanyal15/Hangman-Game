#Hangman Game
import random

hangman = ['''
        +----------
        |    0
        |   /|\\
        |   / \\
        |
        |
        | 
''', '''
        +----------
        |    0
        |   /|\\
        |   /
        |
        |
        |
''',
'''
        +----------
        |    0
        |   /|\\
        |    
        |
        |
        |
''',
'''
        +----------
        |    0
        |   /|
        |   
        |
        |
        |
''',
'''
        +----------
        |    0
        |    |
        |   
        |
        |
        |
''',
'''
        +----------
        |    0
        |   
        |   
        |
        |
        |
''',
'''
        +----------
        |    
        |   
        |   
        |
        |
        |
'''
]

lst = ["apple", "boy", "cat", "egg", "fish", "girl", "hen", "ice", "jug", "lion", "monkey", "nest", "owl", "parrot", "queen",
       "rat", "sun", "toy", "umbrella", "van", "watch", "xray", "yogita", "zebra"]

ch = 1
while ch == 1:
    word = random.choice(lst)
    l = ['_'] * len(word)
    lifelines = 6
    print(l)
    print("Guess a letter in word. You have 6 lifelines. Good luck!")
    print(hangman[6])
    
    while lifelines != 0 and "_" in l:
        g = input("Enter your guess: ")
        if g in word:
            print("Right guess!")
            for i in range(len(word)):
                if word[i] == g:
                    l[i] = g
            print(l)
        else:
            lifelines -= 1
            print("Wrong guess. You now have " + str(lifelines) + " lifelines.")
            print(hangman[lifelines])
    
    if "_" not in l:
        print("You won!")
    else:
        print("You lose!")
    
    ch = int(input("Do you want to play more? (1=Yes/0=No): "))
print("Thank You!")