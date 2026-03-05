y=input("enter student name")
print("enter 3 subject marks")
l=[]
for i in range(3):
    x=int(input("enter marks"))
    l.append(x)
sum=0
for i in l:
    sum=sum+i
average=sum/3
print("Student:",y)
print("Marks:",l) 
print("Total:",sum)
print("Average:",average)       