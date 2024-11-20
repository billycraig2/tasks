import pytest
from ip_address import ip_type

def test_ip_type_ipv4():
    ips = ["127.0.0.1", "192.168.1.1", "255.255.255.255", "0.0.0.0"]
    ipv4s, ipv6s = ip_type(ips)
    assert ipv4s == ips
    assert ipv6s == []

def test_ip_type_ipv6():
    ips = ["2001:db8:3333:4444:5555:6666:1.2.3.4", "c006:96ab:65c4:78ab:b75d:c8ae:bd7c:1912"]
    ipv4s, ipv6s = ip_type(ips)
    assert ipv4s == []
    assert ipv6s == ips

def test_ip_type_mixed():
    ips = ["127.0.0.1", "2001:db8:3333:4444:5555:6666:1.2.3.4", "192.168.1.1", "c006:96ab:65c4:78ab:b75d:c8ae:bd7c:1912"]
    ipv4s, ipv6s = ip_type(ips)
    assert ipv4s == ["127.0.0.1", "192.168.1.1"]
    assert ipv6s == ["2001:db8:3333:4444:5555:6666:1.2.3.4", "c006:96ab:65c4:78ab:b75d:c8ae:bd7c:1912"]

def test_ip_type_invalid():
    ips = ["300.300.300.300", "123.1.123.532", "invalid_ip", "gibberish"]
    ipv4s, ipv6s = ip_type(ips)
    assert ipv4s == []
    assert ipv6s == []

def test_ip_type_empty():
    ips = []
    ipv4s, ipv6s = ip_type(ips)
    assert ipv4s == []
    assert ipv6s == []

if __name__ == "__main__":
    pytest.main()