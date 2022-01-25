'''
Print Primes
Don't use the input function
1. Create a function named is_prime that receives a value and returns True
if the number is a prime and False otherwise
2. Create a function named get_primes that receives a value
3. Store that value passed to get_primes in the variable max_number
3. get_primes() will find all primes from 2 to max_number, using is_prime(),
and store them in a list named list_of_primes
5. Return list_of_primes from get_primes() and print each prime number
on separate lines

Note: This is a modified version of the program given in the tutorial
All I did was change max_num_to_check to 100 instead of an input
'''

# 1. create is_prime function
def is_prime(num):
    # This for loop cycles through primes from 2 to
    # the value to check
    for i in range(2, num):
        # If any division has no remainder we know it
        # isn't a prime number
        if (num % i) == 0:
            return False
    # If the modulus is never 0, it is a prime number
    return True

# 2.3. create get_primes function that takes in max_number
def get_primes(max_number):
    # Create a list to hold primes
    list_of_primes = []
    # This for loop cycles through primes from 2 to
    # the maximum value requested
    for num1 in range(2, max_number):
        # 3. Uses is_prime to check each number up to the
        # max_number and adds the values to list of primes
        if is_prime(num1):
            # This adds the number that is a prime
            # to the list of primes
            list_of_primes.append(num1)
    # returns the entire list of primes
    return list_of_primes

# max number is 100, not using input
max_number = int(100)
# creates a list from running the get_primes function
# that will run the check from 2 to 100
list_of_primes = get_primes(max_number)

# Runs a loop that will print out all of the prime values
# from the list_of_primes list
for prime in list_of_primes:
    print(prime)