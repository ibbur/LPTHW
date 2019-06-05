#Get and load the argv module
from sys import argv

# Hold the arguments I pass to my Python script, unpack the two variables, and assign it to all the variables on the left in order
script, filename = argv

# Use the text entered after the file name is specified and use the open command to load the file. The file is being "opened", but not the contents at this point. Open makes something classed a "file object."
txt = open(filename)

# Print the text and subtitute the repr function for the the filename variable
print "Here's your file %r:" % filename
# Print the text file by opening it using the read command/function/method
print txt.read()

# Print the text
print "Type the filename again:"
# Create an argument form input entered through the keyboard while the script is running
file_again = raw_input("> ")

# Creat a varialbe called txt_again and make it equal to loading the previously lines input to the file_agian variable
txt_again = open(file_again)

# Using the varaible of txt_again print the contents to the screen using the read command/function/method
print txt_again.read()


# The difference between %s and %r is that %s uses the str function and %r uses the repr function. 