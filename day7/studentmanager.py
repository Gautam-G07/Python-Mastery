class student:
    students=[]
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
        self.students.append(marks)
    def display(self):
        print("Name:",self.name,"Age:",self.age,"Marks:",self.marks,"\n")
    @classmethod
    def highest(cls):
        high=0
        for i in cls.students:
            if i>high:
                high=i
        print("Highest no is",high)
                
    @classmethod
    def average(cls):
        sum=0
        for i in cls.students:
            sum=sum+i
        avg=sum/len(cls.students)
        print("the average is",avg)
s1=student("Gautam",20,99)
s2=student("Shruti",18,97)


s1.display()
s2.display()
student.average()
student.highest()