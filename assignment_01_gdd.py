#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

in_process = True

while in_process: #used breaks in control structure to avoid having to import sys/use sys.exit() when incorrect inputs were entered/exceptions were raised

    HIGH_SCORE = 95
    
    #added float try/except for all tests in case any input is incorrect
    try:
        # Get the test scores.
        test1 = float(input('Enter the score for test 1: '))
        test2 = float(input('Enter the score for test 2: '))
        test3 = float(input('Enter the score for test 3: ')) #added test3, previously undefined
    except:
        print('Incorrect input. Please enter numerical scores only.')
        break
    # Calculate the average test score.
    average = (test1 + test2 + test3) / 3 #added parentheses for correct order of operations (PEMDAS)
    # Print the average.
    print('The average score is: ' + str(average)) #forced average to be type string, switched to concatenation style printing; personal preference bc I understand control of spaces better using +
    # If the average is a high score,
    # congratulate the user.
    if average >= HIGH_SCORE: #Python is case sensitive, fixed high_score
        print('Congratulations!')
        print('That is a great average!') #fixed indentation
    
    #Q2
    #The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
    try:
        #Get the lengths/widths.
        rect_a_l = float(input('Enter the length for rectangle a: '))
        rect_a_w = float(input('Enter the width for rectangle a: '))
        rect_b_l = float(input('Enter the length for rectangle b: '))
        rect_b_w = float(input('Enter the width for rectangle b: '))
    except:
        print('Incorrect input. Please enter numerical lengths/widths only.')
        break
    #Calculate the area for rectangle a and b
    rect_a_area = rect_a_l * rect_a_w
    rect_b_area = rect_b_l * rect_b_w
    #Print the area for rectangle a and b
    print("The area of rectangle a is: " + str(rect_a_area))
    print("The area of rectangle b is: " + str(rect_b_area))
    
    #Q3 
    #Ask a user to enter their first name and their age and assign it to the variables name and age. 
    #The variable name should be a string and the variable age should be an int.  
    name = input('Enter your first name: ')
    try:
        name = float(name) #If this works, name was invalid
        print('Incorrect input. Name must be a string, not a number.')
        break
    except:
        try:
            age = int(input('Enter your age: '))
        except:
            print('Incorrect input. Age must be an integer.')
            break
    #Using the variables name and age, print a message to the user stating something along the lines of:
    # "Happy birthday, name!  You are age years old today!"
    print('Happy birthday, ' + name + '! You are ' + str(age) + ' years old today!')
    break