import pytest
from dicts import find_person

def test_find_person_tom():
    assert find_person("tom") == { "name": "Tom", "age": 10 }

def test_find_person_mark():
    assert find_person("mark") == { "name": "Mark", "age": 5 }

def test_find_person_pam():
    assert find_person("pam") == { "name": "Pam", "age": 7 }

def test_find_person_nick():
    assert find_person("nick") == { "name": "Nick", "age": 12 }

def test_find_person_not_found():
    assert find_person("john") == None

if __name__ == "__main__":
    pytest.main()