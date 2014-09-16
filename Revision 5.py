#Henry Nolan-Clutterbuck
#16/09/2014
#Revision exercise 5

heightF = float(input("Please input the height of the fridge in metres: "))
widthF = float(input("Please enter the width of the fridge in metres: "))
depthF = float(input("What is the depth of your fridge in metres: "))
volumeF= (depthF*widthF*heightF)
print("The volume of your fridge is {0}m^3!".format(volumeF))

heightL = float(input("What is the height of the lift? must be larger than fridge: "))
widthL = float(input("What is the width of the lift? must be larger than fridge: "))
depthL= float(input("What is the depth of the lift? must be larger than fridge: "))
volumeL = (depthL*widthL*heightL)
print("The volume of your lift is {0}m^3".format(volumeL))
spaceinlift=(volumeL-volumeF)
print("The space left in your lift is {0}m^3".format(spaceinlift))

              
