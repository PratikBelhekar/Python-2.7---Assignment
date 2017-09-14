# Python-2.7---CSC 470 Assignment

Python Basic 1

  Problem 1 -
    Prompt the user to enter a radius and then calculate the area of the circle.  Print the area. The formula for the area of a circle is pi * radius * radius.  You can start your program with
  
  Problem 2 -
    Prompt the user for a starting value.  Then on the next 4 lines print that value to the nth power starting at 1 and increasing by 1.  Print it in a table like fashion
  
  Problem 3 -
    Prompt the user on a single line for 3 names.  Print those names on separate lines in reverse order.    You may want to use the help function to find the method you are looking for str types.
  
  Problem 4 -
    Initialize a dictionary that contains an emotion for the key and an ASCII emoticon for the value.  You can find a list of emoticons here: https://en.wikipedia.org/wiki/List_of_emoticons.  Prompt the user for an emotion and print the corresponding emoticon.  (Use a method to retrieve the emote as a key that doesn’t exist will throw an error if using the [] operation.  Use the help function to locate the necessary method.
  
  Problem 5 -
    Alice has created a steganography program that takes a message and a value and places garbage characters between each of the original characters.  Write a program that takes as input the hidden message and a key (a number value).  The key is how many characters between each character that was in the original message.  Output the original message.  (It may help to put the test message on one line in a file for testing.)

Python Basic 2

  Problem 1 -
      Frequency analysis is a common technique used in cryptanalysis and compression.  Write a function (or functions) that accepts a parameter and returns the count of each element.  The parameter must be a string or file location.  If a string just count the characters in the string and return a dictionary of the count.  If a file was desired, ask for the location of the file and read from the file returning a count of the characters in the file.  You should return a dictionary of the count.  If neither a file or direct is selected, simply return None.
    
  Problem 2 -
      Game worlds can be represented using a WxH grid.  These grids are represented internally by a 2D array (sometimes 1D for speed).  Write a world initializer function that receives a width and height and a default parameter that is initialized with a single space and return a 2D list with h number of rows and w number of spaces.  The default parameter must be one character.  Return None if default’s length is 2 or more or not a string type.  Return the 2D list, otherwise.
      
  Problem 3 -
      Write a program that generates addition problems randomly and displays them to the user.  The user then attempts to solve the problem.  Once the user has entered an incorrect solution print the number of correct solutions.  You’ll want to put:
      
  Problem 4 -
      The collatz sequence is an interesting sequence.
        It goes like this:
	      If a number, N, is divisible by 2 then divide it by 2.
	      If a number, N, is not divisible by 2 then multiply it by 3 and add 1.
	      Stop when the number, N, is 1.
      Write a function that accepts a number and prints the collatz sequence of that number.  The function may only accept a positive integer.  (I will be testing negative numbers so handle them gracefully)
      
OS Module -

  Write a command line application that takes a string and navigates the file system looking for either a file or directory with the name of the string that was passed.  The output should be the absolute path, (full path) to the directory or file.  The arguments are as follows:
    Root:  This is the root directory to start looking.  This is required.
    String:  This is the string to use to search for file or directory.  This is required.
    -f, --file: This will force the program to only list files.  This is optional.
    -d, --directory:  This will force the program to only list directories.  This is optional.
	  If neither –f or –d or their longnames are in the argument, then list both files and directories.
    -m, --last-modified:  The time the file/directory was last modified.  This is optional.  This will help you (http://effbot.org/zone/python-fileinfo.htm)
  The search string should be dynamic and allow *, ?, and ranges such as a-zA-Z.  You should print the results in a nicely laid format.  You can decide how you want to do this.
  
Create n Take Quiz -

  For this program you are to develop a small program that allows a user to develop a quiz that contains at least multiple choice questions, save it, and let’s other people take the quiz.  Therefore, you should have two modes which are creating a quiz and taking a quiz.  You can use any methods mentioned to save the quiz, its solutions, and its choices.  You should also store user data for anyone taking a quiz such as # of attempts, how many they got correct, and which problems they got wrong.
  


      
