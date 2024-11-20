import pytest
from sort import sort_list


def test_sort_list_single_element():
    assert sort_list([1]) == [1]

if __name__ == "__main__":
    pytest.main()