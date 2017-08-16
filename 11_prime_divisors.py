def main():
    number = input("Please enter a number:")
    number = int(number)
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime")
    else:
        print("Not prime")
main()
