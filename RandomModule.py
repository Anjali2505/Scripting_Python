#This module implements pseudo-random number generators for various distributions.
import random

#random.randrange(start, stop, step)
#start: Optional. An integer specifying at which position to start. default:0
#stop:  Required. An integer specifying at which position to end.
#step:  Optional. An integer specifying the incrementation. default:1
print(random.randrange(0,50, 5)) #generate no more than or equal to 0 , less than 50 , with 5 step count
#print(random.randrange(23.2)) #error

#randint(start, end)
#A random integer in range [start, end] including the end points.
print(random.randint(0,20))
#print(random.randint(1.23, 9.34)) #error

#randint vs randrange
#Use randint() when you want to generate a random number from an inclusive range.
#Use randrange() when you want to generate a random number within a range by specifying the increment. It produces a random number from an exclusive range.