def divisors():
    number = input("Please enter a number:")
    number = int(number)
    for i in range(2, number + 1):
        if number % i == 0:
            print(i)

divisors()
