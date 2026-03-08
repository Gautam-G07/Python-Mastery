import csv
def add():
    with open("day4/marks.csv","a",newline='')as file:
        writer=csv.writer(file)
        name=input("Enter name")
        age=input("Enter age")
        marks=input("Enter marks")
        writer.writerow([name,age,marks])
        print("Written into file")

def highest():
    with open("day4/marks.csv","r",newline='')as file:
        high=0
        read=csv.reader(file)
        for i in read:
            if len(i)<3:
                continue
            try:
                if int(i[2])>high:
                    high=int(i[2])
            except ValueError:
                continue
        print("the highest no is",high)
def average():
    with open("day4/marks.csv","r",newline='')as file:
        Total=0
        count=0
        read=csv.reader(file)
        for i in read:
            count=count+1
            if len(i)<3:
                continue
            try:
                Total=Total+int(i[2])
            except ValueError:
                continue
        if count>0:
            print("the average is",Total/count)
        else:
            print("no records found")
def show():
    with open("day4/marks.csv","r",newline='')as file:
        read=csv.reader(file)
        for i in read:
            print(i)


while True:
    print("1.Add a record \n2.Find Highest marks. \n3.find Average Marks \n4.Show all Students \n5.exit")
    choice=int(input("Enter choice"))
    if choice==1:
        add()
    elif choice==2:
        highest()
    elif choice==3:
        average()
    elif choice==4:
        show()
    elif choice==5:
        break
    else:
        print("invalid")
