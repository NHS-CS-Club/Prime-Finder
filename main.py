print("Enter a range!")
number_one = int(input("First number (smaller): "))
number_two = int(input("Second number (larger): "))


while number_two <= number_one:
    print("Please enter a second number larger than the first!")
    number_two = int(input("Second number (larger): "))

primeNums = []
primes = 0
test_number = number_two
while test_number >= number_one:  
    
    value = test_number - 1
    while value > 1:    
        if test_number % value == 0:
            value = 0
        value -= 15
    if value == 1:
        primeNums.append(test_number)
        primes +=1
    test_number -=1

print("There are " + str(primes) +" prime numbers.")

printPrimes = (input("Do you want to view the primes? ('Y' or 'N'):"))

if printPrimes == "N" or printPrimes == "n":
    print("Okay, bye!")
if printPrimes == "Y" or printPrimes == "y":
    print(primeNums)
