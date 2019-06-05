from sys import argv

script, filename = argv

print 'Opening %r...' % filename

#open the file and make it writable
target = open(filename, 'w')
#clear the file contents
target.truncate()

print "The file is now clear and ready for new input."

line1 = raw_input("Line one: ")
line2 = raw_input("Line two: ")
line3 = raw_input("Line three: ")

target.write ('{}\n{}\n{}\n' .format(line1,line2, line3))

target.close()

print "File closed."

print "Now let's look at what we wrote..."
print "..."

review = open(filename)

print review.read()
print "..."

print "\n"
review.close()
print "Cleaning up after myself."