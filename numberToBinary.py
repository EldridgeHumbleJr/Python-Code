#Author: Eldridge Humble Jr.
#Date: 02/01/2021
#Purpose: The purpose of this program is to convert a number between 1 and 255 to
#it 8 bit binary equivalent. Each line of code in the program is explained in
#comments in bottom section of this document in the section titled Code Explainations.

choice = None
exitException = 0
withinRange = 0
while choice != "q":
    while exitException == 0 :
         try:
             number = int(input("Input a number between 1 and 255"))
             while withinRange == 0:
                if number < 256 and number > -1:
                    withinRange = 1
                else:
                    number = int(input("That number is not in between 1 and 255.Input a number between 1 and 255"))
             exitException = 1
         except:
            print("That is not a number")


    #number = int(input("Input a number between 1 and 255:"))
    numberCopy = number
    binaryList  = ["0", "0", "0", "0", "0", "0", "0", "0"]

    if number > 127:
        binaryList[0] = "1"
        number = number -128

    if number > 63:
        binaryList[1] = "1"
        number = number - 64

    if number > 31:
        binaryList[2] = "1"
        number = number - 32
        
    if number > 15:
        binaryList[3] = "1"
        number = number - 16

    if number > 7:
        binaryList[4] = "1"
        number = number - 8

    if number > 3:
        binaryList[5] = "1"
        number = number - 4

    if number > 2:
        binaryList[6] = "1"
        number = number - 2

    if number > 0:
        binaryList[7] = "1"
        number = number - 1

    binaryOutput = ''.join(binaryList)
    print("The binary equivolent of the number " + str(numberCopy) + " is " +binaryOutput + ".")
    exitException = 0
    withinRange = 0


    choice = input("Press the letter q to quit or any other key to perform another calculation. ")
    if choice == "q":
        print("The program has ended")

"""
Section: Code Explainations.

#The choice variable is initialized. The choice variable will determine whether the user wants to
#end the program or run it again.
choice = None
#The exit exception variable is initialized. The exitException variable is a switch that ensures
#that the users inout is an integer
exitException = 0

#The withinRange variable is initialized. The withinRange variable ensures that the users input
#is between 1 and 255.
withinRange = 0

#This while loop determines when the program ends. At the end of an iteration
#of the loop the user will be prompted to enter "q" to end the program. If the
#user enters "q" the loop is terminated along with the program. If the
#user presses and other button the loop is executed again.
while choice != "q":

    
    #This loop ensures that the user input is an integer since it is what is required be used in the calculations of this program.
    while exitException == 0:
         try:
            #The following line of code is what prompts the user for a numeric input.
            #The input is stored in a variable to be used in the programs calculations. It is also store
            #as a integer data type, which is require to proceed with the execution of the program.
            number = int(input("Input a number between 1 and 255"))

            #The following while loop ensures that the user input is a number between 1 and 255.
            #The withinRange variable was set to 0 at the start of the program, there the loop is entered.
            while withinRange == 0:
                #If the users input is between 1 and 255 the withinRange variable is set to 1. Upon the next iteration
                #of the loop the test of whether withinRange == 0 fails, the loops is exited, and the program continues.
                if number < 256 and number > -1:
                    #The users input was in between 1 and 255, so the value of withinRange is set to 1.
                    withinRange = 1
                #If the users input was not between 1 and 255 the user is continuously prompted to enter a number
                #between 1 and 255 until they do.
                else:
                    number = int(input("That number is not in between 1 and 255.Input a number between 1 and 255"))
            
            #The following exitException variable is used as a switch to allow the program to continue if the
            #users input has passed the test of being an integer. When this while loop iterates again, it test whether
            #or not exitException == 0. Since the users input was an integer, and the value of exitException was changed to 1,
            #then the while loop test of exitException == 0 fails and the program continues.
            exitException = 1
         except:
             #If the user input is not a number, then the user is given a
            #message and the user is prompted again to enter an integer.
            print("That is not a number") 
    
    #A copy of the value of the number variable is made to be used as output at the end of
    #the program. The reason a copy is made is because the output at the end of the program that
    #reflects the user initial input must remain the same. Since the number variable is used in the calculations
    #of the program it changes.
    numberCopy = number

    #The binaryList variable stores a list of 8 elements that each represent a bit of a byte of binary. Each element
    #contains the string value of "0", and collectively represent the number zero. The value of these element will be changed
    #to the string value of "1" depending on the users numeric input.
    binaryList  = ["0", "0", "0", "0", "0", "0", "0", "0"]


    #The following series of if statements determine which of the elements in the binaryList list will be
    #changed to "1" based on the users numeric input. For simplicity, the logic of the following code works
    #this way. If the user enters the number 129 the first test that the program will make is whether or not the user
    #input is greater than 127, which it is. Because the users input is greater that 127 the code block in the first if statement
    #will execute. 
    if number > 127:
        #The following line of code will change the value of the first element in the binaryList list from "0" to "1".
        #Continuing with the example above, the users input of 129 passes the test of being greater than 127. Therefore the
        #value of the binaryList list is changes to ["1", "0", "0", "0", "0", "0", "0", "0"] which is equal to 128
        binaryList[0] = "1"
        #Since the value is the first bit in a byte of binary is worth 128, then the 128 is subtracted from the users input of
        #129 leaving 1
        number = number -128
    #The remainder of the users input is 1 which does not pass the test of the next 6 if statements, so their respective code block
    #are ignored
    if number > 63:
        binaryList[1] = "1"
        number = number - 64

    if number > 31:
        binaryList[2] = "1"
        number = number - 32
        
    if number > 15:
        binaryList[3] = "1"
        number = number - 16

    if number > 7:
        binaryList[4] = "1"
        number = number - 8

    if number > 3:
        binaryList[5] = "1"
        number = number - 4

    if number > 2:
        binaryList[6] = "1"
        number = number - 2
    #The remainder of the users input is 1, which does pass the test for the following code block. As a result, its code block is executed.
    if number > 0:
        #The following line of code converts the seventh element in the binaryList list from a "0" to a "1"
        #Follow the example from above, the value of binaryList is now ["1", "0", "0", "0", "0", "0", "0", "1"] which is equal to 129.
        binaryList[7] = "1"
        #Since the value of the final bit of a byte of binary is worth 1 the 1 is subtracted from the remainder of the users input, leaving 0
        number = number - 1

    #The following line of code converts the value of the binaryList variable from a list to a string. In other words, it converts
    #["1", "0", "0", "0", "0", "0", "0", "1"] into 10000001.
    binaryOutput = ''.join(binaryList)

    #The next line of code echo's the number of the users initial input and its binary counterpart.
    print("The binary equivolent of the number " + str(numberCopy) + " is " +binaryOutput + ".")

    #The value off the exitException variable is reset to zero so that if the user runs th program again, then the program knows to
    #test the users input to determined if it is an integer.
    exitException = 0
    #The value off the withinRange variable is reset to zero so that if the user runs the program again, then the program knows to
    #test the users input to determined if it is between 1 and 255.
    withinRange = 0


    #The following line of code prompts the user to enter the letter "q" if they want to quit the program or any other key
    #to run the program again. The users input is stored in the choice variable to be used as a test in the following if statement
    #to decide if the program should be ended. The value of the choice variable is also used in the previous while loop to determine if the
    #program should be executed again.
    choice = input("Press the letter q to quit or any other key to perform another calculation ")

    #The following if statement decides if the program should be terminated depending on what the user entered in the previous prompt.
    #If the user entered the letter "q" then the program ends.
    if choice == "q":

        #If the user entered the letter "q" to quit then they are notified that the program has ended.
        print("The program has ended")

"""








