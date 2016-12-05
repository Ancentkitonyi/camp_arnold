#we will base it on a while loop
while True:
    print("Welcome to Bootcamp!\n\nWhat do you want do?\n1.Add a skill\n2.View a list of all the skills added \n3.Indicate the skills i have studied\n4.View the skills i haven't studied\n5.See my learning progress\n6.Quit the program")


    command = input("Enter the number of the action you want to carry out:")#raw_input - python 2
    if command == "1":
        skill = (input("Enter the Skill:")).lower()
        print("added ", skill)
        break
    elif command == "2":
        print("View a list of all the skills")
    elif command == "3":
        print("skills studied")
    elif command == "4":
        print("skills not studied")
    elif command == "5":
        print("progress")
    elif command == "6":
        break
    else:
        print("You have to enter the numbers 1-6only")
