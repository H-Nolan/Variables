#Henry Nolan-Clutterbuck
#16/09/2014
#Exercise 2.3

heightininch =int(input("How tall are you in inches?: "))
weightinstone=int(input("What is your weight in stone?: "))
heightincm = heightininch*2.54
weightinkg = weightinstone*6.364
print("Your height converted to cm is: {0:.0f}".format(heightincm))
print("Your weight converted to kg is: {0:.0f}".format(weightinkg))
