# -*- coding: utf-8 -*-
cars=100#赋值语句 there are 100 cars.
space_in_a_car=4.0#there are four seats per  car. 
drivers=30#there are 30 drivers.
passengers=90#there are 90 passengers.
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car		
average_passengers_per_car=passengers/cars_driven

print"There are",cars,"cars available."
print"There are only ",drivers,"drivers available."
print"There will be ",cars_not_driven,"empty cars today."
print"We can transport",carpool_capacity,"pepple today."
print" We have",passengers,"to carpool today ."
print "we need to put about",average_passengers_per_car,"in each carpool."
