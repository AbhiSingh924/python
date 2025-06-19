import random

print("This is simple Number guessing game")
print("Here you will have 5 attempts to guess the number correctly.")

random_number = random.randint(1, 100)

attempts = 5
while attempts >= 0:
    num = int(input("Enter any Number of your choice between 1 to 100:- "))
    if attempts > 0:
        if num == random_number:
            print("Congratulation!🥳 you WON!🎊 the correct number is ", random_number)
            break
    
        elif random_number - num > 10:
            print("OPPS! the entered number id to low. Please try again.")
        
        elif num - random_number > 10:
            print("OPPS! the entered number id to High. Please try again.")
        
        else:
            print("You are too close. Please try again.")
    
    else:
        print("SORRY!😞 You are out of Attempts Please try again later.")
        
    attempts -= 1
    