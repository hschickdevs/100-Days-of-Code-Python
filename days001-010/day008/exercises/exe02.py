# Write your code below this line 👇
def prime_checker(number):
    if number == 1:
        print("It's not a prime number.")
    else:
        for div in range(2, number):
            if number % div == 0:
                print("It's not a prime number.")
                break
        else:
            print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
