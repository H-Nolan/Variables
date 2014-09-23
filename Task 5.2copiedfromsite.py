def input_number(min, max):1,20
while True:
        n = input("Please enter a number between {} and {}:".format(min, max))
        n = int(n)
        if (min <= n <= max):
        return n
        else:
            print("Bzzt! Wrong.")
