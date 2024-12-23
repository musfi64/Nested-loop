m=str(input("enter a word"))
c=str(input("Enter a character"))
i=0
count=0
while(i<len(m)):
    if m[i]==c:
        count=count+1
    i=i+1
print(c,count)