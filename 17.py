from sys import argv
from os.path import exists
    # os.path is used because different opperating
    # systems (e.g., Mac, Windows, Linux) specify
    # files paths in different ways. "exists" is a
    # function that returns "TRUE" if the file paths
    # is valid (i.e., the file exists AND the user
    # has perimissions).

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

    #We could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
    #in_file is an object

    # One line: indata = open(from_file).read()
    # In this case you don't need in_file.close() at
    # the end. In fact, it will throw an error if you
    # don't remove it or comment it out.

    #Get the length of the string that you passed and returns that as a number.
print "The input is %d bytes long" % len(indata)

print "Does this file exist? %r" % exists(to_file)
print "Read, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

    # MY ADDITIONAL NOTES RE:TEXT - python does not actually write the file to disk until you execute "output.close()
    # For the most part, many changes to files in python do not go into effect until after the file is closed, so if your script edits, leaves open, and reads a file, it won't see the edits.
    #It can slow down your program. Too many things open, and thus more used space in the RAM, will impact performance.
    # theoretically, run in to limits of how many files you can have open.
out_file.close()
in_file.close()

    # This is said to be an important lesson because coping info from one files
    # and into another is a commmon task.
