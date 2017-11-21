"""Using Python 3.6

Ans for 1st Program

Write a program that does – Loop through [1..100], if a number is divisible by 3, print “fizz”, divisible by 5 print “buzz”, divisible by 3 & 5, print “fizzbuzz”
"""

for i in range(1,100):
    if i%3==0:
        print(i,"fizz")
        if i%3 == 0 and i%5==0:
            print(i,"fizzbuzz")

            
    elif i%5==0:
        print(i,"buzz")
        if i%3 == 0 and i%5==0:
            print(i,"fizzbuzz")
