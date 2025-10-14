booleans.py<br>
Create two boolean variables: is_student and is_employed, then print them.<br>
Use the and operator to check if both are true and print the result.<br>
Use the or operator to check if at least one is true and print the result.<br>
Output<br>
True False<br>
False<br>
True<br>

<img src="Images/boolean.png" alt="Output Screenshot" width="300">

number.py<br>
Create a variable age and assign it as an integer.<br>
Print the value of age.<br>
Create a variable height as a float and print it.<br>
Calculate age_in_days by multiplying age by 365 and print it.<br>
Divide age by 7, store the result in result, and print it.<br>
Output<br>
18<br>
1.64<br>
6570<br>
2.5714285714285716<br>

<img src="Images/number.png" alt="Output Screenshot" width="300">

string.py<br>
Create a variable name with full name as a string and print it.<br>
Use string concatenation to make a greeting message and print it.<br>
Use an f-string to make the same greeting message and print it.<br>
Find the length of name using len() and print it.<br>
Output<br>
Pema Rinzin Deolkar<br>
Kuzuzangpo, Pema Rinzin Deolkar!<br>
Kuzuangpo, Pema Rinzin Deolkar!<br>
19<br>

<img src="Images/string.png" alt="Output Screenshot" width="250">

type_conversion.py<br>
Convert age to a string and concatenate it with another message, then print it.<br>
Convert a numeric string "18" to an integer and print it.<br>
Try converting a non-numeric string to an integer and handle the error with a try-except block.<br>
Output<br>
I am 18 years old.<br>
18<br>
Error: invalid literal for int() with base 10: 'KUZU'<br>

<img src="Images/type_conversion.png" alt="Output Screenshot" width="400">

DATA STRUCTURES<br>

dictionaries.py<br>
Create a dictionary with name, age, height, and student status, then print it.<br>
Add a key "favorite_color" to the dictionary and print it again.<br>
Try to access a non-existing key and handle the KeyError using a try-except block.<br>
Output<br>
{'name': 'Pema Rinzin Deolkar', 'age': 18, 'height': 1.64, 'is_student': True}<br>
{'name': 'Pema Rinzin Deolkar', 'age': 18, 'height': 1.64, 'is_student': True, 'favorite_color': 'White'}<br>
Error: 'weight'<br>

<img src="Images/dict.png" alt="Output Screenshot" width="400">

lists.py<br>
Create a list of favorite fruits and print it.<br>
Add another fruit to the list using append() and print again.<br>
Access the second fruit in the list by index and print it.<br>
Output<br>
['blueberry', 'peach', 'mango', 'grape']<br>
['blueberry', 'peach', 'mango', 'grape', 'watermelon']<br>
peach<br>

<img src="Images/list.png" alt="Output Screenshot" width="400">

OPERATORS

arithematics.py<br>
Create two variables, a and b, and assign them 15 and 4, then print both.<br>
Perform the four basic arithmetic operations between a and b, and print the result of each.<br>
Use the modulus operator to get the remainder of a divided by b, and print it.<br>
Use the exponentiation operator to calculate a raised to the power of b, and print the result.<br>
Use floor division to divide a by b, and print the result.<br>
Output<br>
a = 15, b = 4<br>
Addition: 19<br>
Subtraction: 11<br>
Multiplication: 60<br>
Division: 3.75<br>
Modulus: 3<br>
Floor Division: 3<br>

<img src="Images/arthi.png" alt="Output Screenshot" width="200">

assignment.py<br>
Create a variable x with the value 10 and print it.<br>
Increase x by 5 using += and print the new value.<br>
Decrease x by 3 using -= and print the new value.<br>
Multiply x by 2 using *= and print the result.<br>
Divide x by 4 using /=, and print the value.<br>
Output<br>
Initial x: 10<br>
After x += 5: 15<br>
After x -= 3: 12<br>
After x *= 2: 24<br>
After x /= 4: 6.0<br>

<img src="Images/assignment.png" alt="Output Screenshot" width="200">

comparison.py<br>
Create two variables, a and b, with values 10 and 5, then print both.<br>
Use comparison operators to compare a and b, printing the result of each comparison.<br>
Create a variable c with value 10 and compare it to a, printing the result.<br>
Output<br>
a = 10, b = 5<br>
a == b: False<br>
a != b: True<br>
a > b: True<br>
a < b: False<br>
a >= b: True<br>
a <= b: False<br>
a == c: True<br>

<img src="Images/comparision.png" alt="Output Screenshot" width="200">

logical.py<br>
Create two boolean variables, x and y, assign them to True and False, and print both.<br>
Use the and operator with x and y, and print the result.<br>
Use the or operator with x and y, and print the result.<br>
Use the not operator with both x and y, and print each result.<br>
Output<br>
x = True, y = False<br>
x and y: False<br>
x or y: True<br>
not x: False<br>
not y: True<br>

<img src="Images/logical.png" alt="Output Screenshot" width="200">

CONTROL STRUCTURE

break_continue.py<br>
Use a while loop with a break statement to print numbers starting at 0 and ending before 5, then print "Loop ended."<br>
Write a for loop that uses continue to skip printing even numbers from 1 to 5, printing only odd numbers.<br>
Write a for loop to search for a specific number in a list, print a message for each non-match, and stop the loop once found, printing a found message.<br>
Implement a number guessing game using a while loop; prompt the user to guess a random secret number between 1 and 10, give hints if the guess is too high or low, count attempts, and break when the guess is correct, printing the attempt count.<br>
Use a for-else loop inside a function to check if a number is prime; print whether the number is prime or not.<br>
Output<br>
0<br>
1<br>
2<br>
3<br>
4<br>
Loop ended<br>
1<br>
3<br>
5<br>
Not 8...<br>
Not 8...<br>
Not 8...<br>
Not 8...<br>
Found 8!<br>
Guess the number (1-10): 7<br>
Too high. Try again.<br>
Guess the number (1-10): 5<br>
tashi delek! You guessed it in 2 attempts.<br>
17 is prime.<br>

<img src="Images/break&continue.png" alt="Output Screenshot" width="300"> <br>

conditionals.py<br>
Create an if-else statement that checks if a number is positive; print "The number is positive." if true, otherwise print "The number is non-positive."<br>
Extend the if-else to include zero as a separate case using elif, printing whether the number is positive, negative, or zero.<br>
Write a program that assigns a letter grade from a numerical score using if-elif-else conditions: A for >= 90, B for >= 80, C for >= 70, D for >= 60, otherwise F; then print the grade.<br>
Use a ternary operator to check whether a number is even or odd and print the result.<br>
Implement a simple calculator using if-elif-else statements to perform addition, subtraction, multiplication, or division based on an operator variable; handle division by zero and invalid operators appropriately; print the result.<br>
Output<br>
The number is positive.<br>
The number is positive.<br>
The number is zero.<br>
Your grade is: A<br>
The number is odd.<br>
Result: 15<br>

<img src="Images/conditional.png" alt="Output Screenshot" width="200"><br>

loops.py<br>
Write a for loop to print numbers from 1 through 5.<br>
Use a while loop to print numbers from 5 down to 1 in reverse order.<br>
Write a for loop to calculate the sum of numbers from 1 to 10 and print the total.<br>
Use a for loop to iterate over a list of fruits and print each fruit.<br>
Write a nested for loop to create a multiplication table for numbers 1 to 3, printing the product for each pair.<br>
Output<br>
1<br>
2<br>
3<br>
4<br>
5<br>
5<br>
4<br>
3<br>
2<br>
1<br>
The sum of numbers from 1 to 10 is: 55<br>
apple<br>
mango<br>
blueberry<br>
1 * 1 = 1<br>
1 * 2 = 2<br>
1 * 3 = 3<br>
2 * 1 = 2<br>
2 * 2 = 4<br>
2 * 3 = 6<br>
3 * 1 = 3<br>
3 * 2 = 6<br>
3 * 3 = 9<br>

<img src="Images/loop.png" alt="Output Screenshot" width="300">

FUNCTION AND SCOPE

basic_function.py<br>
Write a function greet that prints "Kuzuzangpo la!" and call it.<br>
Modify greet to accept a name parameter and greet that person.<br>
Write a function square that returns the square of a given number.<br>
Create a function is_even that returns True if a number is even, False otherwise.<br>
Write a function print_numbers that prints numbers from 1 to n inclusive.<br>
Output<br>
Kuzuzangpo la!<br>
Hello, Deolkar!<br>
25<br>
True<br>
False<br>
1<br>
2<br>
3<br>
4<br>
5<br>

<img src="Images/basic.png" alt="Output Screenshot" width="200"> <br>

parameters_and_returns.py<br>
Write a function greet_with_default that takes a name parameter with default "Guest" and prints a greeting.<br>
Define a function calculate_rectangle_area that calculates and returns the area from width and height.<br>
Write a function print_info that accepts any number of keyword arguments and prints their keys and values.<br>
Create a function min_max that takes a list and returns the minimum and maximum values.<br>
Define a function safe_divide that returns the division of two numbers, or an error message if divisor is zero.<br>
Output<br>
Hello, Guest!<br>
Hello, Rinzin!<br>
The area of the rectangle is: 54<br>
name: Deolkar<br>
age: 18<br>
city: pling<br>
Min: 1, Max: 11<br>
5.0<br>
Cannot divide by zero<br>

<img src="Images/parameter.png" alt="Output Screenshot" width="300"> <br>

recursion.py<br>
Write a recursive function factorial to compute the factorial of a number.<br>
Create a recursive function fibonacci to compute the nth Fibonacci number.<br>
Output<br>
120<br>
13<br>

<img src="Images/recursion.png" alt="Output Screenshot" width="100"> <br>

scope.py<br>
Demonstrate local vs global variables by defining a global variable x, a local x in a function, and printing both.<br>
Modify a global variable inside a function using the global keyword; increment a counter.<br>
Write nested functions that demonstrate use of nonlocal keyword with variable x.<br>
Local x: 20<br>
Global x: 10<br>
Count: 1<br>
Count: 2<br>
Final count: 2<br>
Inner x: inner<br>
Outer x: inner<br>

<img src="Images/scope.png" alt="Output Screenshot" width="200"> <br>

FILE OPERATORS

binary_files.py<br>
Write a function create_binary_file that writes a series of bytes to a binary file; call with 'binary_sample.bin'.<br>
Define a function read_binary_file that reads and prints the contents of a binary file; call with 'binary_sample.bin'.<br>
Write a function append_to_binary_file that appends bytes to an existing binary file; call to append bytes to 'binary_sample.bin', then read and print the file.<br>
Output<br>
Binary file created successfully.<br>
Binary content: b'\x00\x01\x02\x03\x04\x05'<br>
Bytes appended to binary file.<br>

<img src="Images/binary.png" alt="Output Screenshot" width="300"> <br>

file_management.py<br>
Write a function file_exists to check if a file exists; print results for 'sample.txt' and a nonexistent file.<br>
Define a function rename_file to rename a file; rename 'sample.txt' to 'renamed_sample.txt' and confirm it exists.<br>
Write a function delete_file to delete a given file, printing confirmation or nonexistence; delete 'binary_sample.bin'.<br>
Create a function create_directory to create a directory if not existing; create 'new_folder'.<br>
Write a function list_files to list all files in a given directory; list files in the current directory.<br>
Define a function copy_file to copy a file from a source to a destination; copy 'renamed_sample.txt' to 'new_folder/copied_sample.txt'.<br>
Write a function read_csv_file to read and print contents of a CSV file; first create a sample CSV with rows for "Name, Age, City" and read it.<br>
Output<br>
'sample.txt' exists: True<br>
'nonexistent.txt' exists: False<br>
File renamed successfully.<br>
'renamed_sample.txt' exists: True<br>
binary_sample.bin has been deleted.<br>
Directory 'new_folder' created successfully.<br>
Files in the current directory:<br>
new_folder<br>
renamed_sample.txt<br>
.DS_Store<br>
Icon<br>
Practical_1<br>
README.md<br>
.git<br>
Practical_2<br>
Practical_5<br>
Practical_4<br>
Practical_3<br>
first_programme.py<br>
File copied from renamed_sample.txt to new_folder/copied_sample.txt<br>
Contents of sample.csv:<br>
Name, Age, City<br>
Pema, 18, Bumthang<br>
Deolkar, 18, Paro<br>

text_files.py<br>
Write a function create_and_write_file that creates a new text file and writes three lines to it; call it with 'sample.txt'.<br>
Write a function read_and_print_file that reads and prints the content of a text file; call it with 'sample.txt'.<br>
Define a function append_to_file that appends a new line to an existing file; call it to append one line to 'sample.txt', then read and print the file.<br>
Write a function print_lines_with_numbers that reads a file line by line, printing each line prefixed by its line number; call it with 'sample.txt'.<br>
Create a function count_words that counts and returns the number of words in a file; call it with 'sample.txt' and print the word count.<br>
Output<br>
File create and written successfully.<br>
This is the first line.<br>
This is the second line.<br>
This is the third line.<br>
Line appended successfully.<br>
This is the first line.<br>
This is the second line.<br>
This is the third line.<br>
This is an appended line.<br>
1: This is the first line.<br>
2: This is the second line.<br>
3: This is the third line.<br>
4: This is an appended line.<br>
The file contains 20 words.<br>

<img src="Images/text_file.png" alt="Output Screenshot" width="200"> <br>