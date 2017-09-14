# Pratik Sanjay Belhekar
# Part 1 : Problem 3
# python 2.7

from random import randint

count = 0

while True:
    x = randint(1, 100)
    y = randint(1, 100)


    ans = int(raw_input(str(x)+ ' + ' +str(y)+ ' = '))

    if ans == (x + y):
        print "Correct!"
        count += 1
    else:
        print "Correct Solutions :", +count

        break