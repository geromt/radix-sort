
def sort(array: list[int]) -> list[int]:
    buckets = [[] for i in range(10)]
    flag_next_iter = False

    for i in array:
        if i < 0:
            raise ValueError("All the integers must be non-negative numbers")
        buckets[get_digit(i, 0)].append(i)
        if i > 9:
            flag_next_iter = True

    if flag_next_iter:
        return _sort_aux(buckets, 1)
    else:
        return _orginize_buckets(buckets)


def _sort_aux(array: list[list[int]], digit: int) -> list[int]:
    buckets = [[] for i in range(10)]
    flag_next_iter = False
    for l in array:
        for i in l:
            buckets[get_digit(i, digit)].append(i)
            if i > 10**(digit+1)-1:
                flag_next_iter = True

    if flag_next_iter:
        return _sort_aux(buckets, digit+1)
    else:
        return _orginize_buckets(buckets)


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