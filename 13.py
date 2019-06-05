from sys import argv

script, first, second = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second

test =  raw_input("Did I do this right?")
print "%s" % (
    test)