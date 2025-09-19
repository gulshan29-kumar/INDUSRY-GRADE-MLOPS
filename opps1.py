#initiate the class
class employee:
    #special method/ magic method /dunder method-constructor
    def __init__(self)->None:
        print("started executing attributes/data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("attributes and data have been initiated")
        
    def travel(self,destination):
        print("this travel function will called mannually")
        print(f"employee is now travelling to the {destination}")
           
 #creating the object or instance of the class
sam=employee()
#printing the attribuites
#print(sam.id)
#calling a method
print(sam.travel("kerala"))
print(type(sam))