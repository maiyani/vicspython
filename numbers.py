# simple program that allows user input 4 numbers and returns the smallest
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))
third = int(input("Enter a third number: "))
fourth = int(input("Enter a fourth number: "))

if first < second and first < third and first < fourth:
    print(" The smallest number is", first)
elif second < first and second < second and second < fourth:
    print(" The smallest number is", second)
elif third < second and third < third and third < fourth:
    print("The smallest number", third)
else :
    print(" THe smallest is", fourth)

