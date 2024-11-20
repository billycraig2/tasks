import pytest
from letter_frequency import letter_frequency

def test_letter_frequency_empty():
    assert letter_frequency("") == {}

