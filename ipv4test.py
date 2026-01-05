from ipv4 import IPv4
number1 = IPv4("255.255.255.255/24")

print(number1.cidr, number1.number)