#Name of Program: studentMarkCalculations.py
#Purpose of Program: Finds the mean, median, and mode of numbers
#Author of the Program: Ryan Medina
#Date Programmed: 09/04/2026

marks = [] #Create an empty list to add student marks

#Create a function for the user to enter student marks. Reuse this function for the user enter a new set of numbers
def student_marks():
    # Create while loop for the user to enter marks until the user types "done"
    while True:

        user = input("Enter a Student Mark: ")  #User will input an integer (e.g., 70, 75, 85)

        #IF the user types "done", then exit the loop immediately to prevent crashing
        if str(user.lower()) == "done": break

        try: #Run this code to handle errors if they occur
            s_mark = int(user) #Convert the string into an integer.
            marks.append(s_mark) #ADD the student marks into the list by converting the string to integer
        except ValueError: #Runs if a ValueError occurs (e.g., invalid number input)
            print("Invalid input. Please enter a number only.") #Run the print statement onto the terminal

student_marks() #Call the function to enter the student marks on the terminal window

print(marks) #Output the marks list onto the terminal window for calculations

#Re-prompt the user UNTIL there's more than or equal to 2 numbers before exiting the loop
while True:
    if(len(marks) >= 2): #if the list size is more than or equal to 2
        break #Exit the  loop to present the menu
    else: #otherwise if the length is less than or equal to 2
        print("Add at least two numbers") #Print out a message on the terminal window
        student_marks() #The function is reused to enter more student marks

#Create a function to calculate the mean of an list of numbers
def calculate_mean():
    sum = 0 #Accumulator variable to find the total integers inside an array

    #For in loop to find the total sum of the array
    for integer in marks:
        sum += integer #Get the current sum and add the integer to it, and store the result back to sum. This updates the sum every time

    mean = sum / len(marks) #Divide the total sum of the array by the length of the array to get the mean

    return mean #Output the mean onto the terminal window

#Create a function to calculate the median of an list of numbers
def calculate_median():
    marks.sort() #Sort the array in ascending order from smallest to largest to see the middle value

    #Find the median IF array length is an ODD number
    if len(marks) % 2 == 1:
        median = (len(marks) + 1) / 2 #Calculate the middle number if the array length is ODD
        return marks[int(median) -1] #Use marks[int(median) -1] to get the element inside the array, -1 is used because the index starts at 0

    #Find the median IF array length is an EVEN number
    if len(marks) % 2 == 0:
        median_ = (marks[int(len(marks) / 2) - 1] + marks[int(len(marks) / 2 + 1) - 1]) / 2  #Use the median formula for nth is even. marks[index] grabs the elements. -1 is used because the index starts at 0
        return median_

#Create a function to calculate the mode of an list of numbers
def calculate_mode():
    marks.sort()  #Sort the array in ascending order from smallest to largest to see the most common number

    dict = {}  # Create a dictionary to store key/value pair

    #Loop over the array to get each elements
    for num in marks:
        dict[num] = dict.get(num, 0) + 1 #Add key/value pair content inside the dictionary with value as number of occurances from the same numbers

    max_frequency = max(dict.values()) #Get the max frequency from the dictionary using max() and values() method

    #Create a List Comprehension to loop over the dictionary to check if the value matches the max frequency and return the mode
    mode = [key for key, value in dict.items() if value == max_frequency]
    return mode[0] if len(mode) == 1 else "No mode"

#Create a function to calculate the Standard Deviation Population (SD)
def standard_deviation():
    total = 0 #Accumlator variable

    #Loop over the list to get each value starting from first element to  last element
    for j in range(0, len(marks)):
        total += (marks[j] - calculate_mean()) ** 2 #Substract the mean -> square it - > SUM all the results from the accumulator (total)

    return (total / len(marks)) ** 0.5 #Square root of the SD. 0.5 is 1/2, then it's used to find square root from x^1/n = n√x (fractional exponent rule)

#Create a function to calculate the Skewness of the list (marks)
def skewness():
    return 3 * (calculate_mean() - calculate_median()) / standard_deviation() #Use Pearson’s second coefficient of skewness formula

#Create While loop to repeatedly display the menu until the user exits
while True:
    # Create a function to utput a menu of choice onto the terminal window before the user inputs a number of choice
    def choice():
        print("\nPress 1 Print the mean of the numbers")
        print("\nPress 2 Print the median of the numbers")
        print("\nPress 3 Print the mode of the numbers")
        print("\nPress 4 to Go back and enter a NEW set of numbers")
        print("\nPress 5 to Exit the application ")
        print("\nPress 6 Print out the Skewness value")

    choice()  #Call the function to output the user choices onoto the terminal window

    choice = int(input("\nEnter your choice: "))  #The user should enter a choice of 1, 2, 3, 4, or 5

    if choice == 1: #The user types 1 to become True
        print(calculate_mean()) #Print out the calculated mean from the function
        break #Exit the loop immediately

    elif choice == 2: #The user types 2 to become True
        print(calculate_median()) #Print out the calculated median from the function
        break #Exit the loop immediately

    elif choice == 3: #The user types 3 to become True
        print(calculate_mode()) #Print out the calculated mode from the function
        break #Exit the loop immediately

    elif choice == 4: #The user types 4 to Enter a new set of numbers
        marks.clear() #Remove every single element from the list
        student_marks() #The function is called back to enter more student marks
        print(marks) #Print out the new set of numbers in mark list

    elif choice == 5: #The user types 5 to become True
        exit() #Stops the entire program immediately

    elif choice == 6: #The user types 6 to become True
        print(skewness()) #Call the function to print out the skewness value
        break #Exit the loop immediately

