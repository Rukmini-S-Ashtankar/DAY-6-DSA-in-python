# Reverse each word in a string
name = "Hello World!"
newname = " "                    
N = len(name)       
for i in range(N-1,-1,-3):         #if we put -5 in last postion, it will return !We (will print last char then count and last fifth)
    newname += name[i]
print(newname)