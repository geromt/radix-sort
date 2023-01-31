
def sort(array: list[int]) -> list[int]:
    """Implementation of radixsort algorithm. All the numbers in array must be non-negative numbers
    
    :param array: list with the numbers that will be sorted
    :returns: a list with the integers of array sorted
    :raise ValueError: if at least one the integers in array is a negative number
    """
    if array == []:
        return []
    
    max_number_digit = 0
    for i in array:
        # Check that there are not negative numbers
        if i < 0:
            raise ValueError("All the integers must be non-negative numbers")
        
        # Check the max number of digits
        number_of_digits = get_number_of_digits(i)
        if max_number_digit < number_of_digits:
            max_number_digit = number_of_digits

    return _sort_aux([array], 0, max_number_digit)


def _sort_aux(array: list[list[int]], digit: int, number_of_iterations: int) -> list[int]:
    buckets = [[] for i in range(10)]

    for l in array:
        for i in l:
            b = get_digit(i, digit)
            buckets[get_digit(i, digit)].append(i)

    if digit+1 >=  number_of_iterations:
        return _orginize_buckets(buckets)
    else:
        return _sort_aux(buckets, digit+1, number_of_iterations)


def _orginize_buckets(buckets: list[list[int]]) -> list[int]:
    result = []
    for bucket in buckets:
        for i in bucket:
            result.append(i)
    
    return result


def get_digit(n: int, k: int) -> int:
    """Returns the k of n, beginning from the least significant digit, where the least significant 
    digit is the digit 0, the next of the left is the digit 1, and so on. If k is greater than the
    number of digits in n, then returns 0"""
    for i in range(k):
        n = n // 10

    return n % 10

def get_number_of_digits(n: int) -> int:
    # Case n is 0
    if n == 0:
        return 1

    # Case n is negative
    n = abs(n)

    count = 0
    while n != 0:
        n = n // 10
        count += 1

    return count

sort([3,1])