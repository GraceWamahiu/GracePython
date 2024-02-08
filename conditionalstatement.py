temperature = 13

if temperature > 25:
    print("It is hot")
else:
    print("It is cold")
print(temperature)

# A Program that returns the largest number among three numbers
num1 = 100
num2 = 50
num3 = 25
if num1 > num2 and num1 > num3:
    print(num1, "Is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 7

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# A program that checks whether a number is prime or not
number = 12
if number == 1:
    print(number, "is not a prime number")
elif number > 1:
    # check for factors
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
            print(i, "times", number // i, "is", number)
            break
    else:
        print(number, "is a prime number")
