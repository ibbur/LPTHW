from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (control-C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write('{}\n{}\n{}\n'.format(line1, line2, line3))

print "And finally, we close it."
target.close()

print "Let's open and take a look."
review = raw_input("> ")

review_txt = open(review)
print review_txt.read()

print "\n"
print "Now closing the file to clean up behind ourselves."
review_txt.close()