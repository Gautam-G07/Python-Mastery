Contacts={}
try:
    with open("contacts.txt",'r') as file:
        for i in file:
            data = i.strip().split(',')
            name = data[0]
            phone = data[1]
            Contacts[name]=phone
except FileNotFoundError:
    pass
def add():
    name=input("Enter name")
    phone=input("enter no")
    Contacts[name]=phone
def view():
    for key,Value in Contacts.items():
        print(key,":",Value)


 
def search():
    x=input("enter name to search")
    if x in Contacts:
        print(x,Contacts[x])
        
    else:
        print("key not found") 

def delete():
    x=input("enter name to delete")
    if x in Contacts:
       Contacts.pop(x)
            
    else:
            print("key not found")
while True:
    print("1.Add contact\n2.View Contact \n3.Search Contact \n4.Delete Contact \n5.Exit")
    choice=int(input("enter choice"))
    if choice==1:
        add()
    elif choice==2:
        view()
    elif choice==5:
        with open("contacts.txt","w") as file:
            for key,Value in Contacts.items():
                file.write(key+',')
                file.write(Value+'\n')
        break
    elif choice==3:
        search()
    elif choice==4:
        delete()
    else:
        print("Invalid")                                