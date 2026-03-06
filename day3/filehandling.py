with open("Data.txt",'w') as file:
    for i in range(3):
        x=input('Write name')
        file.write(x+'\n')
print("Saved names are")
with open("Data.txt",'r') as file:
    for i in range(3):
        content=file.read()
        print(content)