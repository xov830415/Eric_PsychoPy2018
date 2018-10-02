# change codes order ,add variables, but the output is the same as the LPTHW ex6
# Tried another output format

x = "There are %d types of people." % 10
B = "binary"
D_T = "don't"
y = "Those who know %s and those who %s." % (B, D_T)
z = "I said : '%r'." %x
a = "I also said : '%s'." %y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %s."

w = "This is the left side of..."
e = "a string with a right side."

print(x)
print(y)
print(z)
print(a)
print(joke_evaluation %hilarious)
print(w+e)


#Another output format
#print(x,y,z,a,joke_evaluation %hilarious,w+e)


