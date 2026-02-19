print("Select your ride:")
print("1.Bike")
print("2.car")
choice= int(input("Enter your choice:"))
if(choice==1) :
    print("What type of bike?")
    print("1.sctooty/n")
    print("2.scooter/n")
    choice2 = int(input("Enter your choice2:"))
    if choice2 == 1 :
     print("you have selected scooty" )
    else:
     print("you have selected scooter")   
elif (choice==2):
    print("What type of car?")
    print("1.Sedan")
    print("2.Xuv")    
    choice3 = int(input("Enter your choice three:"))
    if( choice3 ==1):
     print("you have selected sedan")
    else:
     print("you have selected Xuv")
else:
    print("Wrong choice!")