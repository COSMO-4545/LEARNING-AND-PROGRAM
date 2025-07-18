import random 
n = random.randint(1,100)
a = -1 
guesses = 0
while a != n:
    a = int(input("Guess the numble plz:-"))
    if a>n :
        print("the number is too high guess smaller number")
    elif(a<n):
        print("guess a larger number:- ")
    guesses += 1

print(f"your guess the correct number {n} in {guesses} attempts")