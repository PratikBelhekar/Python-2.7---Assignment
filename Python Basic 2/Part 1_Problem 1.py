# Pratik Sanjay Belhekar
# Part 1 : Problem 1
# python 2.7

choice = raw_input("File or Direct: ")

def file_count(filename):
    f_handle = open(filename, "r")
    f_dict = {}
    text = f_handle.read()
    for char in text:
        if f_dict.has_key(char):
            f_dict[char] += 1
        else:
            f_dict[char] = 1
    print f_dict


def direct_count(direct):
    d_dict = {}
    for char in direct:
        if d_dict.has_key(char):
            d_dict[char] += 1
        else:
            d_dict[char] = 1
    print d_dict

if choice.lower() == "file":
    fileName = raw_input("File name: ")
    file_count(fileName)
elif choice.lower() == "direct":
    direct = raw_input("Text: ")
    direct_count(direct)
else:
    print "None"


