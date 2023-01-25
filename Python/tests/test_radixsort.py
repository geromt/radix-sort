from tests.context import radixsort
import pytest
import random


class TestRadixSort:

    def test_get_digit_zero(self):
        assert radixsort.get_digit(0, 0) == 0

    def test_get_digit_one_digit(self):
        assert radixsort.get_digit(9, 0) == 9

    def test_get_digit_second_digit_zero(self):
        assert radixsort.get_digit(1, 1) == 0

    def test_get_digit_second_digit(self):
        assert radixsort.get_digit(37, 1) == 3

    def test_get_digit_third_digit(self):
        assert radixsort.get_digit(357, 2) == 3

    def test_get_digit_third_digit_zero(self):
        assert radixsort.get_digit(7, 2) == 0

    def test_sort_empty_list(self):
        assert radixsort.sort([]) == []

    def test_sort_one_item(self):
        assert radixsort.sort([1]) == [1]

    def test_sort_two_items(self):
        assert radixsort.sort([3, 1]) == [1,3]

    def test_sort_raise_valueerror(self):
        with pytest.raises(ValueError):
            radixsort.sort([1, -1, 2])

    def test_sort_ten_random_items(self):
        random.seed(100)
        l1 = [random.randint(0, 1000) for _ in range(10)]
        l2 = l1.copy()
        l2.sort()
        assert radixsort.sort(l1) == l2

    def test_sort_ten_items_sequence(self):
        random.seed(100)
        l1 = list(range(10))
        random.shuffle(l1)
        l2 = l1.copy()
        l2.sort()
        assert radixsort.sort(l1) == l2

    def test_sort_one_thousand_random_items(self):
        random.seed(100)
        l1 = [random.randint(0, 1000) for _ in range(1000)]
        l2 = l1.copy()
        l2.sort()
        assert radixsort.sort(l1) == l2

    def test_sort_one_thousand_items_sequence(self):
        random.seed(100)
        l1 = list(range(1000))
        random.shuffle(l1)
        l2 = l1.copy()
        l2.sort()
        assert radixsort.sort(l1) == l2
