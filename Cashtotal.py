#Henry Nolan-Clutterbuck
#18/09/2014
#Money division exercise

cashtotal= int(input("Please enter the total amount of money you would like converted:"))

twenty=cashtotal//20
remainder1=cashtotal%20

ten=remainder1//10
remainder2=remainder1%10

five=remainder2//5
remainder3=remainder2%5

two=remainder3//2
remainder4=remainder3%2
           
one=remainder4//1
endnumber=remainder4%1

print(" You would get: Twenty pound notes {0}, Ten pound notes {1}, Five pound notes {2}, Two pound coins {3}, One pound coins {4}!".format(twenty,ten,five,two,one))
