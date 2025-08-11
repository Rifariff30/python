x = int(input("Enter a number: "))

if x > 0 and x < 10:
    print("The number is between 1 and 9.")

elif x < 0 or x > 100:
    print("The number is either negative or greater than 100.")
    
elif not x == 50:
    print("The number is not 50.")

else:
    print("The number is 50.")