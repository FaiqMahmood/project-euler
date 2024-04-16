def largest_prime_factor(number):
    largest_factor = 0
    for divisor in range(2, number + 1):
        while number % divisor == 0:
            largest_factor = divisor
            number //= divisor
    return largest_factor

# Example usage:
print(largest_prime_factor(7))    
print(largest_prime_factor(13195))

