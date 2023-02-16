x=1
marks=59
grades=4567
#if statement
if x>0:
    print("The number is positive")
    print(4+10)
#if.. else statement
if marks>=60:
    print("You have passed")
else:
    print("You have failed")
#if... elif.. else
if grades<=29 and grades>=0:
    print("You have failed")
elif grades<=49 and grades>=30:
    print("You have passed ")
elif grades<=79 and grades >=50:
    print("You have credit")
elif grades<=100 and grades>=80:
    print("You have distinction")
else:
    print("Wrong input")
