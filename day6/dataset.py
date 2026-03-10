class dataset:
    def __init__(self,L):
        self.L=L
    def average(self):
        total=0
        n=0
        for i in self.L:
            total=total+i
            n=n+1
        average=total/n
        print("average is",average)

    def maximum(self):
        maxi=self.L[0]
        for i in self.L:
            if i>maxi:
                maxi=i
        print("maximum element is ",maxi)
    def mini(self):
        mini=self.L[0]
        for i in self.L:
            if i<mini:
                mini=i
        print("minimum element is ",mini)
 
obj1=dataset([1,2,3,4])
obj1.average()
obj1.maximum()
obj1.mini()