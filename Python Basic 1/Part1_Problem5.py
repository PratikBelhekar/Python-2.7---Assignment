#Pratik Sanjay Belhekar
#Part 1: Problem 5
#Python 2.7

msg = raw_input("Stego Message: ")
Msgkey = int(raw_input("Key: "))
print "Message:", msg[::Msgkey+1]