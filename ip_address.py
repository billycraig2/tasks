import re

# uses regex to print if email is valid
def ip_type(ips):
    # checks string of ips with regex
    ipv4s = list(filter(lambda ipv4: re.search(r"^((25[0-5]|(2[0-4]|1[1-9]|[1-9]|)[0-9])\.?\b){4}$", ipv4), ips))
    ipv6s = list(filter(lambda ipv6: re.search(r"\b(?:[0-9a-fA-F]{1,4}:){5}[0-9a-fA-F]{1,4}:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b|\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b", ipv6), ips))
    
    return ipv4s, ipv6s

ips = ["300.300.300.300",'127.0.255.250', '2001:db8:3333:4444:5555:6666:1.2.3.4', '123.1.123.532', '4.3.5.213', 'c006:96ab:65c4:78ab:b75d:c8ae:bd7c:1912', '04a5:a394:61db:2217:b6c0:2d7d:241.37.148.135']

print("Ipv4s: " + str(ip_type(ips)[0]))
print("Ipv6s: " + str(ip_type(ips)[1]))