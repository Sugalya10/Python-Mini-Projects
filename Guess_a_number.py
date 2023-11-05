import random
print("Guessing a number")
#getting the maximum or minimum range
x=int(input("Enter the range:"))
#random number
random_number=random.randint(x,20)
def number():
    num=0
    #num=0 is a dummy variable for the further usage in the loop.
    while num!=random_number:
        num=int(input("Enter your guess: "))
        #never use "continue" if you are using conditional statements afterwards.
        if num>20 or num<x:
            print("OOPSIE! Your number is out of the given range!")
        elif num==random_number:
            print(f"Bravo!.. You guessed it right..{random_number} is the right numeral!")
        elif num<random_number:
            print("Ummm...Try a little higher please!")
        elif num>random_number:
            print("Nah... Smaller value helps!")
        
number()
