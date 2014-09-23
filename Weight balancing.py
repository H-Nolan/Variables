#Henry Nolan-Clutterbuck
#23/09/2014
#Weight balancing
weight=int(input("Please enter the weight in grams:"))
hundreds=weight//100
r1=weight%100
fifties = r1//50
r2 = r1%50
tens = r2//10
r3 = r2%10
fives = r3//5
r4 = r3%5
twos = r4//2
r5 = r4%2
ones = r5//1
r6 = r5%1
print("The weights needed are {0}x 100g, {1}x 50g, {2}x 10g, {3}x 5g, {4}x 2g, {5} x 1g".format(hundreds,fifties,tens,fives,twos,ones))
