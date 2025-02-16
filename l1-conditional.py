# if student is allowed for exam or not

#Take input for the student that he can attend the exam or not
medical_cause=input("did you have a medical cause Y or N: ")
#Take input of the attendance
atten = int(input("enter the attendance of the student: "))

#checking the user input predicting output accordingly

if medical_cause == 'Y': #checking the condition 1
  print ("You are allowed")
else:
  if atten>=75:  #checking the condition 2
    print ("Allowed")
  else:
    print ("Not allowed")
    
    
# electricity bill

# Take input of number of units consumed from the user
units = int(input(" Please enter Number of Units you Consumed : "))

# Check conditions of units consumed 
# Then calculate amount and tax accordingly
# tax for the units

# Check for units less than 50
if(units < 50):
    amount = units * 2.60 
    surcharge = 25 

# Check for units less than 100
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

# Check for units less than or equal to 200
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

# Check for all the cases other than mentioned 
# When units consumed are more than 200
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

# Calculate and Display the total electricity bill
# total amount = amount + surcharge
total = amount + surcharge
print("\nElectricity Bill = "  %total)

#customize your ride based on your choice

print("Select your ride: ")
print("1. Bike")
print("2. Car")
#take input of number 1 or 2
#select your ride
choice = int( input("Enter your choice: ") )
#User entering option 1 
if( choice == 1 ): #condition 1 outer if statement
  print( "what type of bike? " )
  print("1.Scooty\n")
  print("2.Scooter\n")

  #Condition for selecting the type of bike
  choice2=int(input("Enter you choice2: "))
  if choice2==1: #inner if statement
    print("you have selected scooty")
  else:
    print("you have selected scooter")

#User entering option 2
elif( choice == 2 ): #outer elif statement
  print( "what type of car?" )
  print("1.Sedan")
  print("2.XUV")
  choice3=int(input("enter your choice3: "))
  if choice3==1: #inner if statement
  #condition for selecting the type of car
    print("you have selected sedan")
  else:
    print("you have selected XUV")

else: #outer else statement
  print("Wrong choice!")
  
 #activity 3:
  
#input a digit, letter or special character
ch = input("Please Enter Your Own Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
  #check the alphabat
    print("The Given Character ", ch, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'): 
  #check the digit
    print("The Given Character ", ch, "is a Digit")
else: 
  #check the character other than character and digit
    print("The Given Character ", ch, "is a Special Character")
  


#Take input from user
print("Check your is between 10 to 20 years or not")
x = int(input("enter your age: "))


if x > 10: #condition 1
  print("Your age is more than 10 years")
  if x > 20: #nested condition
    print("And it is more than 20 as well")
  else:
    print("But it is less not more than 20")


#ACP check age

age = int(input("how old are you?:"))
if age >10:
    if age>=10 and age<=20:
        print("you are allowed in class age limit in between 10 and 20")
    else:
        print("you are not allowed in class")
else:
    print("you are too young for the class")





