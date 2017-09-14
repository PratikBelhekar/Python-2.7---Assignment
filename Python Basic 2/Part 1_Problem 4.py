# Pratik Sanjay Belhekar
# Part 1 : Problem 4
# python 2.7

val = int(raw_input("Enter the Value: "))

def collatz(num):
    lst= []
    lst.append(num)
    while num != 1:
        if num % 2 == 0:
            num = num/2
            lst.append(num)
        else:
            num = (num*3)+1
            lst.append(num)
    print lst

if val > 0 :
    collatz(val)
else:
	print "Please Enter a Positive Integer greater than 0"

