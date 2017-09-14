#Pratik Sanjay Belhekar
#Part 1: Problem 4
#Python 2.7

Dic = {'peek-a-boo': '(>_<) <(0o0)>' , 'Troubled': '(>_<)(>_<)>' , 'Cat':'(=_=)' , 'Wink':'(^_-)' , 'Amazing':'(@_@'}
emote = raw_input("Emote: ")

print Dic.get(emote)

#for k,v in Dic.items():
# if emote == k :
#  print v
