cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#cars not driven is equated by subtracting cars from available drivers
cars_not_driven = cars - drivers
#modules defines cars driven by mirroring drivers - this is a seemingly redundant module
cars_driven = drivers
#This calculation is incorrect because drivers are not deducted from space in cars
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."