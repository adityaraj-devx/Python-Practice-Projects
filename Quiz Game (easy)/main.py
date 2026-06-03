print("Welcome to the game!")

play = input("Do you want to play? ").lower()
if play != "yes":
    quit()

print("Let's play the game :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

answer = input("Which company developed the Windows operating system? ").lower()
if answer == "microsoft":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")
    
answer = input("What is the full form of RAM? ").lower()
if answer == "random access memory":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

answer = input("What type of device is a keyboard: Input or Output? ").lower()
if answer == "input device":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")
    
answer = input("What does HTTP stand for? ").lower()
if answer == "hypertext transfer protocol":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

print(f"You answered {score} answers correctly! ")
print(f"Result: {(score * 100)/5}%. ")
    