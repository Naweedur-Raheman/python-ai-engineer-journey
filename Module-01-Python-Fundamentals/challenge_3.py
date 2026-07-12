secret_number = 7
attempts=0

while True:
     
    choice = int(input("Enter the number: "))
    attempts += 1
    
    if choice > secret_number:
        print("too high")
    elif choice < secret_number:
        print("too low")
    else:
        print("correct answer")
        break  

    if attempts == 5:
        print("💥 Game over! You ran out of guesses.")
        break