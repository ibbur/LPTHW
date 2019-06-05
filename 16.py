from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (control-C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
    # The file is opened and made writable. The 'w' string also truncates...
    # the file making the origianl truncate line below unessesary.
    # Files are automatically opened in read mode. So, the 'w' argument is...
    # nessesary for writing to the file.
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
    # Truncate is redundant here. The 'w' string above does this in addition to
    # making the file writable.
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
