
def sort(array):
    buckets = [[] for i in range(10)]
    for i in array:
        pass

def _sort_aux(list):
    pass


def get_digit(n: int, k: int) -> int:
    """Returns the k of n, beginning from the least significant digit, where the least significant 
    digit is the digit 0, the next of the left is the digit 1, and so on. If k is greater than the
    number of digits in n, then returns 0"""
    for i in range(k):
        n = n // 10

    return n % 10