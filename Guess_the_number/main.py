import random

def guess_no(x):

    chances=5
    print(f"Welcome to number guess game you have to guess a no. in certain range and you have {chances} chances\
          are you ready!")
   
    random_no=random.randint(1,x)
    guess=0
    while guess!=random_no and chances!=0:
        guess=int(input(f"Guess a no. b/w 1 and {x}: "))
        
        if chances==0:
           
            break
        if guess>random_no:
            print("guess a little lower")
            chances-=1
            print(f"you still have {chances} chances left")

        elif guess==random_no:
            print("yay ! you guessed it right, Good job")
            break
        else:
            print("Guess a little higher")
            chances-=1
            print(f"you still have {chances} chances left")
    print("Sorry! u ran out of chances , better luck next time")


guess_no(30)
