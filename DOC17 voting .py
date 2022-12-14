# Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting to be 18. )


def voting(a):
    if a>=18:
        print("eligible for voting")
    else:
        print("not eligible for vote")
voting(int(input("enter your age")))        