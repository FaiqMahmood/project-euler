'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value number
'''
def multiples_of_3_or_5(number):
    sum = 0;
    for number in range(1,number+1):
        if (number % 3 == 0 or  number % 5 == 0):
            sum += number 
    return sum


print(test_1 := multiples_of_3_or_5(9))  
print(test_2 := multiples_of_3_or_5(49))
print(test_3 := multiples_of_3_or_5(1000))
print(test_4 := multiples_of_3_or_5(8456))
print(test_5 := multiples_of_3_or_5(19564))
