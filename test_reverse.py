# test_reverse.py
import pytest
from reverse import reverse_list

def test_reverse_list_empty():
    assert reverse_list([]) == []

def test_reverse_list_single_element():
    assert reverse_list([1]) == [1]

def test_reverse_list_multiple_elements():
    assert reverse_list([1, 2, 3, 4, 5, 6, 7]) == [7, 6, 5, 4, 3, 2, 1]

def test_reverse_list_even_number_of_elements():
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]

def test_reverse_list_strings():
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']

def test_reverse_list_mixed_types():
    assert reverse_list([1, 'two', 3.0]) == [3.0, 'two', 1]

if __name__ == "__main__":
    pytest.main()