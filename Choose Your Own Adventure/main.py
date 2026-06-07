name = input("Enter your name: ")

print(f"Welcome {name} to this adventure!")

print("You arrive at the gates of an abandoned city.")
print('''You have two paths:
1. Enter the city through the main gate
2. Sneak in through a tunnel
''')

answer = input("Type 'gate' for 1st path or 'tunnel' for 2nd path: ").lower()

if answer == 'gate':
    print("The guards' statues suddenly come to life.")
    print('''Do you::
1. Fight the stone guards
2. Hide behind a broken wall
''')
    
    answer = input("Type 'fight' to fight the stone guards or 'hide' to hide behind the wall: ").lower()

    if answer == "fight":
        print("The guards are powerful.")
        print('''Do you::
1. Use your sword
2. Use magic
''')
        
        answer = input("Type 'sword' to use sword or 'magic' to use magic: ").lower()

        if answer == 'sword':
            print("You defeat the guards but get injured.")
        elif answer == 'magic':
            print("You destroy the guards and proceed safely.")
        else:
            print("Not a valid option. You Lose :(")
        
    elif answer == 'hide':
        print("The guards pass by, but you hear strange noises from the palace.")
        print("You arrived at palace.")
    
    else:
        print("Not a valid option. You Lose :(")

elif answer == 'tunnel':
    print('The tunnel is dark and filled with spiders.')
    print('''Do you::
1. Run through quickly
2. Move carefully
''')
    
    answer = input("Type 'run' to move quickly or 'carefully' to move carefully: ").lower()

    if answer == 'run':
        print("You fall into a pit and lose.")
    elif answer == 'carefully':
        print("You avoid the spiders and reach the palace basement.")
    else:
        print("Not a valid option. You Lose :(")
else:
    print("Not a valid option. You Lose :(")

print("Thank you for playing", name)