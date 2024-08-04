import random

def difference(no):
    if number>no:
        dist=number-no
        if dist>=5:
            print("too low")
        else:
            print("you are close")
    else:
        dist=no-number
        if dist>=5:
            print("too high")
        else:
            print("you are close")




print("!welcome")
print('''
        _    _    _    _    _
 / \  / \  / \  / \  / \
( G )( u )( e )( s )( s )
 \_/  \_/  \_/  \_/  \_/
  _    _    _
 / \  / \  / \
( t )( h )( e )
 \_/  \_/  \_/
  _    _    _    _    _    _
 / \  / \  / \  / \  / \  / \
( N )( u )( m )( b )( e )( r )
 \_/  \_/  \_/  \_/  \_/  \_/

      ''')
isContinue=True
while isContinue:
    number=round(random.random()*100)
    diff=input("choose the difficulty level \n1.easy\n2.mid\n4.hard:\n")
    if diff=='hard':
        attempt=5
        while attempt>=1:
            guessed_no=int(input("guess the number: "))
            if guessed_no==number:
                print(f"your guess is correct🫶.number is{number}")
                break
            else:
                attempt-=1
                print(f"you have {attempt} attempts left")
                difference(guessed_no)
        else:
            print(f"you loose😾.The number is{number}")
    elif diff=='mid':
        attempt=7
        while attempt>=1:
            guessed_no=int(input("guess the number: "))
            if guessed_no==number:
                print(f"your guess is correct🫶.number is{number}")
                break
            else:
                attempt-=1
                print(f"you have {attempt} attempts left")
                difference(guessed_no)
        else:
            print(f"you loose😾!!number is{number}")
    elif diff=='easy':
        attempt=10
        isContinue=True
        while attempt>=1:
            guessed_no=int(input("guess the number: "))
            if guessed_no==number:
                print(f"your guess is correct🫶.number is{number}")
                break
            else:
                attempt-=1
                print(f"you have {attempt} attempts left")
                difference(guessed_no)
        else:
            print(f"you loose😡.number is{number}")
    else:
        print("invalid input😡")
    play=input("\nyou want to play again(y/n): ")
    if play=='n':
        isContinue=False
