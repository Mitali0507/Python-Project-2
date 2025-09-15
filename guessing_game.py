from random import randint
n= randint(1,100)
a=-1
guesses=0
while (a !=n):
    guesses +=1
    a=int(input("Guess a number: "))
    if (a>n):
        print("Lower number please: ")
    elif(a<n):
         print("Higher number please: ")          
    elif(a==n):
        print(f"You have the guessed the number {n} in {guesses} attempts")          
    else:
        print("Invalid entry!")

              



