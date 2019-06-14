import ipaddress


def testing():
    r = ipaddress.ip_address('10.163.126.0').reverse_pointer[2:]
    return r


print(testing())
