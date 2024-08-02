from wonderwords import RandomWord
#choosen word and pre-requisites
Choosen_word=RandomWord().word(word_min_length=7,word_max_length=7)
print(Choosen_word)
word=['_','_','_','_','_','_','_']
str=""
print(str.join(word))
count=0
print('''
 _                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                       
''')
HANGMANPICS = [
    '''
    +---+
    |   |
        |
        |
        |
        |
=========''', 
    '''
    +---+
    |   |
    O   |
        |
        |
        |
=========''', 
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========''', 
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========''', 
    '''
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
   /    |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========''']
hang_index=0
#user inputs and
#behind the scenes
while True:
        if hang_index >= 7 :
            print("bye bye 😡🤣") 
            break
        if '_' not in word: 
            print("congratulation!🫶!")
            break
        else: 
            letter=input("guess a letter: ").lower()
            isPresent=False
            for i in range(0,7):    
                if Choosen_word[i]==letter:
                    word[i]=letter
                    isPresent=True
            print(str.join(word))
            if isPresent:
                print(" \n good guess keep going😸!")
            else:
                print("not good guess \n!!")
                print(f"{HANGMANPICS[hang_index]}")
                hang_index+=1
                