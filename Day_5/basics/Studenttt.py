class Studentt:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    #def display(self):
        #print (f"Name: {self.name}, Grade:{self.grade}")

    #function that prints the values as print() 
    # only displays object representation
    def __str__(self):  
        return f"{self.name}   {self.grade}"

s1=Studentt("Anna","A")
#s1.display()
#s1.grade="B"
#print(s1.grade)

print(s1)