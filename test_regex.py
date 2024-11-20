import pytest
import re
from regex import check_email

def test_check_email():
    assert check_email("hello@world.com") == 'Valid email'

def test_check_email_no_dot_com():
    assert check_email("hello@world") == 'Invalid email'

def test_check_email_no_at():
    assert check_email("helloworld.com") == 'Invalid email'

def test_check_email_no_dot():
    assert check_email("hello@worldcom") == 'Invalid email'

if __name__ == "__main__":
    pytest.main()