#Henry Nolan-Clutterbuck
#23/09/14
#Spot check 1

width = int(input("Please enter the width of the pool:"))
depth = int(input("Please enter the depth of the pool:"))
length = int(input("Please enter the length of the pool:"))

recvolume = (length*width*depth)

circleradius= width/2
circlearea=(3.14*(circleradius*circleradius))
halfcirclevolume=((circlearea/2)*depth)

poolvolume=recvolume+halfcirclevolume

print("The volume of the pool is {0}".format(poolvolume))





    
    
