print "What file would you like to open?"
filename = raw_input("> ")

print "Opening the file %r for you..." % filename
review = open(filename)

print review.read()

target = open(filename, 'w')

print "\n"
print "I will now clear the file contents..."
target.truncate()

print "I will now close the file..."
target.close()

print "I will now reopen the file so we can add new text..."
freshfile = open(filename, 'w')

print "Let's write three new lines to the file. Begin entering text..."
line1 = raw_input("1> ")
line2 = raw_input("2> ")
line3 = raw_input("3> ")

print "\n I will now write to the file..."
freshfile.write ('{}\n{}\n{}\n' .format(line1,line2,line3))
freshfile.close()

reviewagain = open(filename)

print "Let's read the file to make sure everything is as it should be..."
print "---------------"
print reviewagain.read()
print "---------------"

print "I will now clean up behind us by closing the file..."
reviewagain.close()
print "The file is now closed, and this exercise is now complete!"


