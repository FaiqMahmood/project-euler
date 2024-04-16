def multiples_of_3_or_5(number):
    total_sum = 0
    '''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below the provided parameter value number
    '''
    for num in range(1, number + 1):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num 
    return total_sum

print(multiples_of_3_or_5(9))  
print(multiples_of_3_or_5(49))
print(multiples_of_3_or_5(1000))
print(multiples_of_3_or_5(8456))
print(multiples_of_3_or_5(19564))

