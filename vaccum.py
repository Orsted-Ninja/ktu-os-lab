

print("\t\t**Welcome to Vaccum Cleaner World**")
print("The World has 2 rooms A & B \nThe 2 valid operations are clean and dirty indicated by 0 and 1")
status={"A":0,"B":0}
loc=input("Please enter location of Agent(A/B):")
status[loc]=int(input("Enter Current Status:"))
loc=input("Please enter location of Agent(A/B):")
status[loc]=int(input("Enter Current Status:"))
print("Initial Status:")
print(status)
pcost=0
def cost():
      
    global pcost
    
    
    if(status["A"]==1 and status["B"]==1):
        print("Checking Current Location A")
        print("A is found to be dirty.Performing SUCK Operation")
        print("A has been Cleaned.A is Clean\nMoving to B")
        print("Checking current location B.\mB is found to B is found to be dirty.Performing SUCK Operation\n")
        print("B has been Cleaned.B is Clean")
        pcost+=2
        
        status["A"]=0
        status["B"]=0
        
        
      
    elif(status["A"]==0 and status["B"]==1):
        print("Checking Current Location A")
        print("A is Clean\nMoving to B")
        print("Checking current location B.\nB is found to be dirty.Performing SUCK Operation\n")
        print("B has been Cleaned.B is Clean")
        pcost+=1
        status["B"]=0
        
    
    elif(status["A"]==1 and status["B"]==0):
        print("Checking current location A.\nA is found to be dirty.Performing SUCK Operation\n")
        print("A has been Cleaned.A is Clean.\nMoving to B")

        print("Checking Current Location B")
        print("B is Clean\n")
        pcost+=1
        status["A"]=0
        
        
    elif(status["A"]==0 and status["B"]==0):
        print("Checking Current Location A")
        print("A is Clean\nMoving to B")
        print("Checking Current Location B")
        print("B is Clean\n")

 
cost()
print("Goal 'A'=0,'B'=0 achieved Task completed Successfully.Rooms A and B are clean\n")
print("Performance cost:",pcost)