import random

rand_number=random.randint(1,10)
chances=5


while True:
    guess= int(input("Enter a number: "))
    chances-=1

    if chances==0:
        print("You weren't able to guess the correct number in the given chances! Try Again...")
        break
    elif guess>rand_number:
                print("Your guess is too high!")
    elif guess<rand_number:
                print("Your guess is too low!")
    else:
        if guess==rand_number:
            print("Congratulations you guessed the correct number!")
            break
                  



            
            
    

