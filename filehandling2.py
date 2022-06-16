file =open('h2.txt','r')
E=[]
upper=lower=space=special=sen=0
for line in file:
    sen=sen+1
    for word in line.split():
        space=space+1
        E.append(word)
for x in E:
    for y in x:
        if(y.isupper()):
            upper=upper+1
        elif(y.islower()):
            lower=lower+1
        else:
            special=special+1
print("Uppercase=",upper)
print("Lowercase=",lower)
print("Special=",special)
print("Words=",space)
print("No.of sentences:",sen)
