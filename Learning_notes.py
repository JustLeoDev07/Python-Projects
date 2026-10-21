# A string is a program of characters.
print ('Leo Major')
print ('o----')
print (' ||||')
print ('*' * 10)
# The star is a multiplicator for the string of the star by 10, similar to maths.
# The term for a string doing something such as being operated on is called an expression.

price = 10
price = 20
print (price)
# an integer is a number without a decimal point.
# variables are terms that have a value in as shown above, we can also print them.
# They are stored in the computer's memory as data.

rating = 4.9
# The number with the decimal point is called a float/floating value.

name = 'Leo'
# We can also define a value with a string (name) as shown above.

is_published = True
is_published = False
#These variables are called booleans. They are defined by true or false.
#In English these are like yes or no.
#Because python is case sensetive, you have to put true and false in capital form.

Full_name = 'John Smith'
age =  20
is_new = True
#the task here was for the scenario of storing variables for a patient in a hospital.
#John Smith is a 20 year old new patient at a hospital, as shown here in variables.

name = input('what is your name? ')
#The input command is like a TV remote with lots of buttons. You can turn it on, turn it off etc.
#Whenever we use brackets it's like pressing for a button on the remote.
#We can use input for the user to give us a value, we space the question out so that
#When it shows up in the terminal it gives room for the user to respond.
print ('hi ' + name)
#This then shows up in the terminal as what the user put into the prompt.
#We are now combining two strings together through the use of the variable and the string we've codeed in.
#The code 'print ('hi ' + name)' is an expression!
colour = input('what is your favourite colour? ')
print(name + 's favourite colour is ' + colour)
#This code uses two variables alongside strings to make a user generated sentence.

birth_year = input('birth year: ')
print(type(birth_year))
age = 2026 - int(birth_year)
print(type(age))
print (age)
#Note, you cannot subtract a string (anything in quotes) from an integer (numerical value)
#To fix this you need to use one of 3 commands: int(), bool(), or float() so that it can do the equation
#The type command is used to show what kind of variable each one is:
#birth_year is a string and age is a integer.

weight_lbs = input('weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
#The program above is used to convert weight from pounds into kilograms.
#This is done through using the int function, the reason we have to do this is because
#The variable weight_lbs is a string, changing it into an integer means we can give it numerical value
#When we give it numerical value, we can then multiply, divide etc (in this case multiply it into kilograms)

Course = "python's course for begginers"
#For this variable we have to use double quotes because we cannot use single quotes twice or python won't understand it
Course = 'python for "begginers"'
#here we have the same problem because we need to use double quotes in the same scenario so we use single on the outside to fix that.
Course = ''' 
Hi john 

thank you for calling 

kind regards
HR team


'''

print(Course)
#by using triple quotes we can span multiple lines, which is useful when formatting emails in code.
Course = 'python for begginers'
print(Course[0])
#The square brackets in this print statement let us take a certain character from
#the string and show just that part, the 0 is p as all characters in the string go 0123 etc
print(Course[-2])
#If you change the number to a negative, it is the last character
print(Course[0:3])
#This line of code will print characters 0-3. It will do everything before 3, NOT 3.
print(Course[1:])
#This code will print everything from 1 onwards.
print(Course[:6])
#The difference with this is it will assume you want everything from character 6 backwards.
another = Course[:]
#Here I have set another with the value of course. Course has just a colon in the square
#brackets which means that it uses the whole string in its value,which we have assigned to another
print(another)
#printing another will show what we filtered in our course variable through the colon and square brackets.

first = 'john'
last = 'smith'
message = first + ' [' + last + '] is a coder'
print(message)
#in this code I formatted it so the square brackets are in a string and not designed for a function. This is done by
# formatting the quotes with the square brackets inside it.
first = 'john'
last = 'smith'
msg = f'{first} [{last}] is a coder'
print(msg)
#this is called an F-string (formatted string) as indicated by the 'f' before the string to indicate a mix of variable
#and string in our code and an easier way to run the previous set of code, the curly brackets are a way to swap out from
#text to variable inside of a string! pretty cool lol.

course = 'python for begginers'
print (len(course))
#The len command tells us how many characters are in the variable, which in our case can only apply to strings as they
#use characters not numerical values.
#this is good for anything to do with characters such as displaying errors for usernames etc or anything involving
#exceeding a character limit.

course = 'Python for begginers'
print(course.upper())
print(course)
print(course.lower())
#This statement is different as it is called a 'method' which is specific to strings.
#Print and len are general functions but any . function such as .upper is a method as it only works on strings.
#As you can see in the terminal when you run this program, it makes the character string uppercase!
#note that any methods create a new string and don't permanently alter the string itself.

course = 'Python for begginers'
print(course.find('P'))
#This can be used to find a specific character or set of characters in a string and it shows the value of them, for
#example, 'P' is 0 as it is the first in the sequence of the string.
print(course.find('begginers'))
#This will print where the string starts, so it starts at 11 hence when the code is ran it prints 11 in terminal.
print(course.find('p'))
#When this code is ran, the value is -1 as a lowercase 'p' does not exist in the string it is finding.

course = 'Python for begginers'
print(course.replace('begginers', 'absolute beginners'))
#Instead of using find, we used replace which is a different method and changed the characters in the string to something else
print(course.replace('P', 'J'))
#This also works with single characters.

course = 'Python for begginers'
print('python' in course)
#This creates a boolean (false) because it is case sensetive. The 'In' Function lets us see if characters are in a string.
print('Python' in course)
#This creates a true boolean because I've corrected it.
#The difference between in and find is that the 'in' method gives us a boolean and tells us yes or no, find reproduces it.

print (10 + 3)
print (10 - 3)
print (10 * 3)
#As shown above, these are the add, subtract and multiplication operators in python.
print (10 / 3)
#The Forward Slash is for divide, and it gives us a float value (decimal)
print (10 // 3)
#Adding 2 slashes gives us an integer (without a decimal)
print (10 % 3)
#This gives you the remainder of a division, not the answer. For example 3 goes 3 times into 10 and has 1 left over
# 3x3=9, 10-9=1, 1 is the remainder and is what shown in the % (modulo operator)
print (10 ** 3)
#The double astericks means to the power of, so in this case 10 to the power of 3 is 1000.
x = 10
x = x + 3
print(x)
#Python will see that we've put x as 10 before, then we're saying the new x is x add 3, so 10+3 will make the new value.
x = 10
x = x + 3
x += 3
print(x)
#This operator is the augmented operator, it functions the same as the above where we add onto the established value.
#It is for simplicity.
x = 10
x += 3
print(x)
#The above prints 13, the one above that will do 16 as it is adding 3 to the already established x, hope that doesn't
#confuse you much lol.
x = 10
x -= 3
print(x)
#We can also do it with subtraction, hence this now giving us 7.
x = 10 + 3 * 2
print(x)
#The order of operations here means that we multiply first then add it to 10 BIDMAS, giving us 16.
#The order goes as follows: Parenthesis(brackets), exponentiation(to the power), multiplication and division, addition and subtraction.
x = 10 + 3 * 2 ** 2
print(x)
#In this equation here, the answer is 22 because you would do 2 to the power of 2 which is 4, times 4 by 3 which gives 12
#then add 10 to 12 and get 22 - due to the order of operations.
x = (10 + 3) * 2 ** 2
print(x)
#In this equation here, due to the brackets it takes priority over the exponentiation, so 10+3 starts, then 2 to the power of 2.
#2 to the power of 2 is 4 and it's multiplied by 13 which gives 52.
x = (2+3) * 10 - 3
print(x)
#here the process is different because the brackets take priority, then it's multiplied and then 3 is subtracted, giving 47.

x = 2.9
print(round(x))
#the round function does exactly what it says, it rounds a float to an integer.
print(abs(-2.9))
#This function is called the absolute function (abs). It always returns a positive number.
import math
#This allows us to import all of the mathematical functions that you would find on a calculator or use in maths such as sin,cos,tan etc.
#Use this command to do any of the mathematical functions below.
print(math.ceil(2.9))
#This is a mathematical function using the math-function and we have printed the ceiling (highest value) of 2.9, which is 3.
print(math.floor(2.9))
#Floor is the opposite, it gives us the next lowest possible integer, while ceil gives us the next highest integer.

is_hot = True

if is_hot:
    print("it's a hot day")
print('enjoy your day')
#The if statement is known as a conditional, so under is_hot being true, we get it printed that it's a hot day.
#Make sure to put a colon after your if statement is finished and to keep working in the indent, if not then tab+enter!
is_hot = False
if is_hot:
    print("it's a hot day")
print('enjoy your day')
#Changing the boolean to false will negate the if-statement's condition, so the message won't be printed
is_hot = True
if is_hot:
    print("it's a hot day")
    print('drink plenty of water')
print('enjoy your day')
#You can put multiple lines of code into an if statement as shown with these two print statements.
is_hot = False
if is_hot:
    print("it's a hot day")
    print('drink plenty of water')
else:
    print("it's a cold day")
    print('wear warm clothes')
print('enjoy your day')
#The else statement is used to establish what happens if the condition isn't met, so if it isn't a warm day, then it is cold.
#and the user must be told that it isn't a warm day and that it is a cold day. so wear warm clothing.
is_hot = False
is_cold = False
if is_hot:
    print("it's a hot day")
    print('drink plenty of water')
elif is_cold:
    print("it's a cold day")
    print('wear warm clothes')
else:
    print("it's a lovely day.")
print('enjoy your day')
#As shown here we can use the elif statement (which means else if). It adds another condition to the if statement.
#If a day is warm, it doesn't nessecarily mean that it's cold so we add a variable and attach it to the conditional statement.
#Then if neither apply having a lovely day is sufficient to the user, which we use else for incase none of the above apply.

print('This house has a value of 1,000,000 dollars')
deposit = input('is your credit good or bad? ')
if deposit == 'good':
    print('You can put down a 10% deposit')
    deposit_owed = int(1000000 * 0.1)
    print(f'Your deposit is {deposit_owed} dollars')
else:
    print('You can put down a 20% deposit')
    deposit_owed = int(1000000 * 0.2)
    print(f'Your deposit is {deposit_owed} dollars')
#this is my solution to the problem of if a buyer were to buy a house for a million dollars, how would they calculate
#the downpayment based on their credit rating, so I made a deposit variable then an input statement depending on their answer
#I then used a formatted string to input said variable that is calculated based on the credit rating back to the user.
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down payment: ${down_payment}')
#This is a simpler program as it doesn't rely on as many conditionals and instead uses no user input and 2 variables with a boolean.

has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print('Eligible for Loan')
#This is an example of logical operators in use. Previously I used the if-statement, this time I am combining it with the and-statement
#. the and statement is an example of a logical operator, which is a statement that performs a function but not numerically.
has_high_income = False
has_good_credit = True
if has_high_income or has_good_credit:
    print('Eligible for Loan')
#The logical operator 'or' is used to establish 2 conditions can be fulfilled to perform the code within the if-statement.
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print('Eligible for Loan')
#The logical operator 'not' rules out a variable from a condition, meaning it has to be false for the if statement to work.
#Essentially we can agree and disagree to certain variables being banned from specific conditions, in this case if you have
#a criminal record, you should NOT be eligible for the loan even if you have a high credit score.

temperature = 30
if temperature > 30:
    print("it's a hot day")
    #The > is called a comparison operator, it means greater than when it's pointed towards something so in this case if
    #temperature is GREATER THAN 30, print it's a hot day.
else:
    print("it's not a hot day")
#because the temperature isn't higher than 30, it prints that it isnt a hot day.
temperature = 35
if temperature > 30:
    print("it's a hot day")
else:
    print("it's not a hot day")
#Because the temperature is now 35, it fulfils the conditions of the if statement to produce the message 'it's a hot day.'
#There are different comparison operators: <, >, <=, >=, !=, and ==. Note that '==' is not the same as '=', the single = means
#that we are assigning a value, we use == for comparisons.
#!= means not equal to.

#Make a program that if a name is less than 3 characters long it shows 'name must be at least 3 characters long'
#otherwise if it's more than 50 characters long: 'name can be a maximum of 50 characters', otherwise 'it looks good'.
name = 'John Smith'
if len(name) < 3:
    print('name must be at least 3 characters long')
elif len(name) > 50:
    print('name must be less than 50 characters long')
else:
    print('it looks good')
#This program was made by me to perform the task above using comparison operators, if statements and the len function.

#Make a program that asks you for your weight, you can give it in pounds or kilos. The next question asks you if it's in
#pounds or kilos and is not case sensitive. It then gives you back your weight in the other conversion.
weight = int(input('weight: '))
unit = input('(L)bs or K(g:) ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")
#this is a program that I learned which performs this task. It asks the user for their weight to store in a variable and
#makes it an integer value instead of a string (using the int function). This is so we can then use it to do calculations
#. it then asks for the unit to be in K for kilos or L for pounds, this program works through the string method .upper .
#The reason this works is because it means regardless of if the unit the user implemented was lower or uppercase, it becomes uppercase.
#which gives us an easy way to convert values. So then if it's in pounds it times it by 0.45, and if it's kilos it divides it by 0.45
#As we only have 2 conditions, we only use if or else.

i = 1
while i <= 5:
    print(i)
    i = i + 1
print('done')
#While-loops are to execute a block of code multiple times and useful for games/interactive programs.
#This loop starts the 'i' variable at 1. while is a conditional statement that constantly executes code.
#so it says aslong as i is less than or equal to 5, keep printing I. So it will go 1,2,3,4,5 and then at the end of that it will print done.
#Done is not in the conditional loop, it is automatically set to print after the loop. if you weren't to have i = i+1 then
#your code will keep executing into an infinite loop because it will never reach 5 and 1 is indefinitely less than 5.
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print('done')
#In this code here, we changed the variable being printed to a string instead (*) and for it to be timesed by the looping variable.
#What this does is when you multiply a string by a variable with a number inside it will create the same string again, so line
#by line it will go like so: * ** *** etc until it hits 5 astericks' and prints 'done'.

#This program is for a guessing number game.
secret_number = 9
#This number represents the number the player has to guess
guess_count = 0
#This variable is the amount of guesses they've used.
guess_limit = 3
#This variable sets the ceiling/limit to how many guesses they get.
while guess_count < guess_limit:
    #here it's saying when the guess count is less than the limit, perform the following loop.
    guess =int(input('guess: '))
    #this is an input statement which uses int to convert the number the user guesses into an integer for us to process
    #. it allows the user to guess what number we are thinking of.
    guess_count += 1
    #this statement means the number of guesses used increases with each guess the user has put in.
    if guess == secret_number:
        print('you won')
        break
    # here we have done an if statement which means that if they guess the correct number we tell them they've won.
    # the 'break' statement cancels a loop, so in this case when they win the code stops looping because they don't need to keep guessing.
else:
        print('Sorry, you failed.')
#I made a mistake here originally because I put the else statement in the if condition, you have to make sure it's in-line
#with the while-loop statement otherwise it prints 'sorry, you failed' after each failed guess instead of after using 3 guesses.

#This is a basic car game that I made that uses if statements, loops, variables, print statements and string methods.
command = ""
started = False
Stopped = False
#this makes our variable with no value or string to it. We also need stop and start variables to indicate warning messages.
while True:
    #while true is code for a loop, it just starts a loop without any conditions set unless we choose to give a condition to break it, or just break it.
    command = input ("> ").lower()
    #here we give user access to the variable so we can control what they see, we keep it all in lowercase or uppercase so regardless it can be filtered through our code.
    if command == "help":
        print(""" 
    start - to start the car
    stop - to stop the car 
    quit - to exit the program""")
        #I find it easiest to start coding with the order of the way I want the user to do things so it's easier to read.
        #for example here I start with using the conditional for help. It lays out all the options for the user to pick from.
    elif command == "start":
        if started:
            print('car is already started!')
        else:
            started = True
            print("car started...")
            #This is our start command, we turn the started variable to true as the car is on and print car started, the conditional
            #is if the car is already started as whenever we say start we want it to turn on regardless, we get pissy if they try starting
            #multiple times.
    elif command == "stop":
        if not started:
            print('Car is already stopped! ')
        else:
            started = False
            print("car stopped...")
        Stopped = True
        #here is the same premise, conditional for when the car is already stopped and try to stop it again, and the absolute
        #for when we tell the car to stop, it has to stop indefinitely and the variable initiates this.
    elif command == 'quit':
        break
        #this is to cancel the program.
    else:
        print("Sorry, I didn't understand that.")
        #this is for when the user gives a prompt that we don't like/the program doesn't recognise.

for item in 'python':
            print(item)
        # this is called a 'for-loop', it is a kind of loop and it is different from a while-loop. These loops take each character
        # in a string and creates a loop, so in the terminal it will look like so:
        # p
        # y
        # t
        # h
        # o
        # n

for item in ['mosh', 'john', 'sarah']:
    print(item)
        # this creates a list of names, whenever we use a list we use square brackets as it's multiple strings, so we can list each character
        # in a string-word or list individual worded strings.
for item in [1, 2, 3, 4]:
    print(item)
    # We can also do this for numbers as well!
for item in range(10):
    print(item)
        # This is an easier way to narrow it down, the range-function lets us do a list up to that number, so numbers up to and not including 10.
for item in range(5, 10):
    print(item)
        # this prints every number from 5 until 10, it doesn't include 10 as we only go to the last number not including 10, as seen above too.
for item in range(5, 10, 2):
    print(item)
        # this for-loop has a 2 without a comma which means that from 5 until 10 instead of listing every number, we list it increasing by 2 so: 5,7,9

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
    print(f'total: {total}')
        # this program is for an imaginary shopping cart, using for loops. We set the prices of each item in the trolley as 10,20,30.
        # then create a total variable at 0. in the for-loop we use an imaginary variable (price) to initiate the prices loop.
        # Total += price means that we add the value of total to price and it becomes the new total, essentially total = total + price, just simplified.

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
#this is a nested loop, essentially we've used multiple (2) for-loops to list coordinates. (0,1),(0,2) etc.
#The top loop is the outer-loop and the one below it which contains y is our inner-loop.
# The reason we see it as 0,0 , 0,1 , 0,2 is because the inner loop goes from 1-3 so 0,1,2 and then when it hits 2 the outer loop will increment to 1, then keep repeating until
#the outer loop has reached it's maximum value which in this case is the number 3.

#this is confusing so I will explain
numbers = [5, 2, 5, 2, 2]
#this specifies how many x's we want on each row to create the 'F' Shape.
for x_count in numbers:
    #The variable 'x_count' represents one number out of the list in number so x_count  =5, when this outer-loop repeats it becomes 2, 5 etc etc.
    output = ''
    #the reason we leave it as a blank string is so the values don't keep being added when we add more x's through the inner-loop.
    for count in range(x_count):
        #x_count in range tells us how many times to run the inner loop. We use count because we need a variable that isn't a number to tell
        #the program to repeat the loop in the numbers variable - if that makes sense.
        output += 'x'
        #this tells us what we're doing it to, so when we run the loop and add more x's to it, the output means x.
    print(output)
    #then we end up with the final iteration looking like this (ignore the indent, it's so it doesn't line with the #):
    # xxxxx
    # xx
    # xxxxx
    # xx
    # xx

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)
#This is another simpler way of writing the code above it without a nested loop. In Python we can multiply a string by a number to repeat it.

numbers = [1, 1, 1, 1, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
    #This nested-loop program prints an 'L' shape.

names = ['John', 'bob', 'mosh', 'Sarah', 'Mary']
#this is a list of names in square brackets and separated by commas
print(names[1])
#Because we have made a list, the number in the square brackets reflects what name we print (starting from index-0, so it prints bob)
#if we put a negative number in then we get that number from the back of the list

names = ['John', 'bob', 'mosh', 'Sarah', 'Mary']
#this is a list of names in square brackets and separated by commas
print(names[2:4])
#this prints all elements from 2 up to 4, so it will only be Mosh and Sarah, as we don't include the 4th element.

names = ['John', 'bob', 'mosh', 'Sarah', 'Mary']
names [0] = 'jon'
print(names[2:4])
#we can take an element in a list and change it like so, so john has it's h removed.

numbers = [3, 6, 2, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
#this works to find out the largest number in a random sequence. we have a list of numbers set and then max is our variable/placeholder for the sequence.
#then we create a non-conditional 'for' loop, where for each iteration if the number in the sequence is bigger than the one in the iteration then max increases.
#this sequence keeps going until the loop will break when we get the highest number in the sequence. When we print max, it will have the
#highest value number in the variable, which is 10.
#we know this works because if you put different numbers or rearrange the number 10 it still produces the highest value in the 'max' variable.

#this is called a mathematical matrix (or in Python, a 2D list), a rectangular array of numbers.
#in python we can make each number in that list have another list and have it represent items in each row.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0] [1])
#this prints a specific number in our matrix. we have chosen the first list indicated by 0 and the first character, which is 2
#(as we work from 0,1,2 etc basis in python).

matrix[0] [1] = 20
print(matrix[0] [1])
#we can also modify the values in the matrix and it will be listed here, so when we print it in the terminal, instead of 2, it is 20.

for row in matrix:
    for item in row:
        print(item)
#using this nested loop, we've used the outer to make it about our matrix and then in the inner-loop we've selected
#item to represent it, so we list the numbers in the matrix when we print into the terminal.

numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10)
print(numbers)
#this is a list-method where we can customise lists with different comands such as insert which we can choose where to insert new values and where to place them.

numbers = [5, 2, 1, 7, 4]
numbers.append(10)
print(numbers)
#this adds 10 to the sequence within the list.

numbers = [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)
#this removes a number in the list

numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)
#this clears all of the items in the list

numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)
#this removes the end number in a list.

numbers = [5, 2, 1, 7, 4]
print(numbers.index(5))
#this tells you which index the number 5 falls on, which in this case is index 0, as it is the first number in the list.

numbers = [5, 2, 1, 7, 4]
print(50 in numbers)
#this is a safe-way to generate a boolean for if a number is in a sequence, it doesn't use a list method but does the same thing.

numbers = [5, 2, 1, 7, 4]
print(numbers.count(5))
#this tells us how many times an item is in the list, with this example, 5 is in the sequence twice so it prints 2 in the terminal.

numbers = [5, 2, 1, 7, 4]
numbers.sort()
print(numbers)
#this list-method sorts the numbers in ascending order.

numbers = [5, 2, 1, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)
#this method does it in descending order as we are sorting it with the reverse method below it to indicate the opposite of ascending order.

numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)
#here we have used the copy method to copy over the list from numbers to numbers2, then after we have changed the original list and it keeps the original values in numbers2.
#which is very useful.

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
#this code works to take numbers from a list, insert them into a loop and figure out if they're duplicated or not through the if-statement and then remove any doubles.

numbers = (1, 2, 3)
#This is a tuple, we use normal brackets and is how we distinguish them from lists. These are immutable, meaning they cannot be changed or modified.
#We can only get info from a tuple
print(numbers[0])

coordinates = (1, 2, 3)
coordinates[0] * coordinates[1] * coordinates [2]
#This is about unpacking. We have used a tuple and then made a lengthy formula above so instead we store them in variables
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
#like so then we can just x * y * z, we can achieve the same result but far less with unpacking
x, y, z = coordinates
#this code here is identicle to the code on lines 4-6 but very simplified.
print(x, y, z)
#When Python gets the statement it will assign the first variable and assign it to the first variable in the tuple, and then do the same with other variables.
coordinates = [1, 2, 3]
x, y, z = coordinates
print(x, y, z)
#We can also use this with a list, not JUST a tuple.

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
#This is called a dictionary. A dictionary is where we can define key variables under one variable if they all correlate.#
#In this scenario we use a customer and then their details such as name, age, verification can all be placed under here.
#The keys(variables in the dictionary) have to be unique, but they can be assigned booleans, lists, strings, values - anything.
print(customer["name"])
#Here I printed the variable into the terminal, to specify what I want to show then I use square brackets as if a number in a list or tuple
#and put the variable in with speech marks.
print(customer.get("birthdate"))
#This is how we get variables that don't exist. The 'get' method is used to retrieve variables that do or don't exist.
#If you used print(customer["birthdate"]), it will print an error - whereas .get will print 'none'. 'None' represents the
#absence of a key/variable/value in the terminal.
#REMEMBER! When doing it with a new variable, use normal brackets, NOT square brackets! Or it will show an error in the terminal.
print(customer.get("birthdate", "Jan 1 1980"))
#We can make a value within this statement as seen above if we want to though. This will print Jan 1 1980 in the terminal.
#Note that this just makes the value on the spot, it does NOT store it in the dictionary, it temporarily adds it.
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])
#This will store it in your dictionary by using the = operator and changing the statement from above.
customer["name"] = "jack Smith"
print(customer["name"])
#Even though we have it in a dictionary, we can change the keys inside in our code later on for whatever reason.

phone = input("phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}
#I originally overthought this program when making it so don't overcomplicate it lmao.
#This code is for a program that lets you type a number in for a phone number and it will translate it into a word.
#I was trying to automate it by using len, str etc when the solution is much simpler.
#Instead I made an input variable for phone, then did a dictionary to map each numbered-string to their worded copy.
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
    # The for-loop takes every character in the phone variable,
    # assigns it to ch, and runs the code inside the loop.

    # The output variable starts as an empty string using "".
    # This lets us build up the final result as the loop runs.

    # Say the first digit in phone was "2".
    # It gets assigned to ch during the first iteration.

    # It goes to digits_mapping.get(ch, "!"), which looks for
    # the current value of ch ("2") in the dictionary.
    # It finds "2" and returns "Two".

    # The + " " adds a space after the word.

    # The += means whatever word gets found in that iteration
    # gets added onto the existing output.
    #it's the same as saying output = output + Three.

    # So if the next digit is "3", the previous word "Two"
    # is still kept, and "Three" gets added afterwards.
    # example: output = output + Three , The result is "Two Three"

    # The "!" in .get() is a fallback if the digit isn't
    # found in the dictionary.
    #For example if we typed 9 in there when 9 isn't defined.
print(output)

message = input(">")
words = message.split(" ")
print(words)
#The split method splits a string, so if you typed 'good morning sunshine', it creates 3 strings for each word.
emojis = {
     ":)": "😀",
     ":(": "😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
#This program is very similar to the program in my dictionaries section but I have used a dictionary to transcribe emojis instead.
#It uses a for loop to map a variable for an iteration of the split words variable to run through the loop. the loop runs through
#each character and lets a word come through and continues the loop unless an emoji comes out then it transcribes it with the dictionary for emojis.
#The reason we have an output variable is so we can print the new statement and there is a set of " at the end so there is a space between each word in the iteration.
#or itwouldlooklikethisinstead

def greet_user():
    print("Hi there!")
    print("Welcome aboard")
#This is called a function and we use it to group code so it looks simpler to us and we don't have to write out all the whole thing and it look confusing.
#We use 'def' to define the function and then type the name of the function as specific as we can, then (): after it, the code in the function is indented.

print("start")
greet_user()
print("finish")
#This block of code will print the function above inbetween the two print statements as we have already defined the function.
#If we put the function before the definition then it comes up with an error.

def greet_user(first_name):
    print(f"Hi {first_name} !")
    print("Welcome aboard")
#In this function we have put a parameter in the definition. A parameter is a variable inside of a function's brackets.
#What this will do is it gives us a free variable which we can change each time we use the function.
#In programming the parameter is the name we give to the variable in a function and the value we give to it when we use the
#function in practise is called the argument.
#For example: in a ham sandwich, sandwich is the parameter and ham is the argument.


print("start")
greet_user("john")
greet_user("Mary")
print("finish")
#As shown here we have changed the 'name' parameter in the function to John so it will print "Hi John!" in the terminal.
#Name is whatever we choose it to be each time we use the function. I also changed it again to prove my point.

def greet_users(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")

print("start")
greet_users("john", "Smith")
print("finish")
#Here we have changed it to have two parameters, a first and a last name and now we have two arguments alongside it: John and Smith.



