print "What file do you want to open?"
filename = raw_input("> ")

print "Here's your file %r:" % filename
filename = open(filename)
print filename.read()
filename.close()

print "Type the filename again:"
file_3rdt = raw_input("> ")
txt_3rdt = open(file_3rdt, 'w')

print "Write something to the file:"

line1 = raw_input("> ")
line2 = raw_input("And theb > ")
line3 = raw_input("Last line > ")

txt_3rdt.write(line1)
txt_3rdt.write("\n")
txt_3rdt.write(line2)
txt_3rdt.write("\n")
txt_3rdt.write(line3)
txt_3rdt.write("\n")

print "Writting to file done."
print "Now closing."
txt_3rdt.close()

print "Open the file again to see what happened:"
file_4th = raw_input("> ")

text_4th = open(file_4th)
print text_4th.read()

