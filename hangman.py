import random
animal=['alligator','lion','panda','camel','pig','dog','cat','horse','sheep','hen','fox','cow','deer','giraffe','duck','snake']
word=random.choice(animal)
n=7
str1=""
print("word length is :",len(word))
while(n>0):
    alp=input("enter a letter")
    alp=alp.lower()
    if alp in word:
        print("present")
        for i in range(len(word)):
            if alp==word[i]:
                print(alp," is present at ",i+1)
        str1=str1+alp
    
    else:
        n=n-1
        print("not present\n .Only ",n,"chances remaining")
    if (str1==word):
        print("You won !!!!")
        break;
        
print(word)
