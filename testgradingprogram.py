test_score = int(input("Please enter your test score: "))
if test_score >= 40 and test_score <=49:
    print("E grade")
elif test_score >= 50 and test_score <=59:
    print("D grade")
elif test_score >= 60 and test_score <=69:
    print("C grade")
elif test_score > 70 and test_score <=79:
    print("B grade")
elif test_score > 80:
    print("A grade")
else:
    print("Fail")
