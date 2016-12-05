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
def reader(self,name):
    numbers = list()
    # Open the input text file for reading
    name= raw_input('Enter Your Name')
    dataFile = open(name + ".txt",'r')

    for eachLine in dataFile:
    # setup a temporay variable
        tmpStr = ''

        for char in eachLine:

            if char.isdigit():
                # if it is a number add it to the tmpStr
                tmpStr += char

            elif char == ',' and tmpStr != '':
                numbers.append(int(tmpStr))
                tmpStr = ''
        # if the tmpStr contains a number add it to the
        # numbers list.
        if tmpStr.isdigit():
            numbers.append(int(tmpStr))
    # Print the number list
    print numbers
    # Close the input data file.
    dataFile.close()

    # 2) Uses the string function split to line from the file
    # into a list of substrings
    numbers = list()
    dataFile = open(name + ".txt", 'r')

    for eachLine in dataFile:

        substrs = eachLine.split(',',eachLine.count(','))

        for strVar in substrs:
            if strVar.isdigit():
                numbers.append(int(strVar))

    print numbers

    dataFile.close()
def writer(self,*args):
    aList = [1, 1, 1, 4,6, 5, 6, 7, 8, 9, 10,
    'one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight', 'nine', 'ten']
    dataFile = open(name + ".txt", 'w')
    for eachitem in aList:
        dataFile.write(str(eachitem)+'\n')

    dataFile.close()
