my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
CM_PER_INCH = 2.540 #centimeters
K_PER_POUND = 0.453592 #Kilos

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s my_eyes and %s my_hair." % (my_eyes, my_hair)
print "His my_teeth are usually %r depending on the coffee." % my_teeth

#this  line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)

print 'WTF %r' % CM_PER_INCH